# Synapse Mock Server is an open-source test harness and telemetry simulator for the Synapse HFT protocol.
# Copyright (C) 2026 Gabriel Moraes - Noxfort Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# File: infrastructure/grpc_client.py
# Author: Gabriel Moraes
# Date: 2026-10-10

import grpc
import os
import time
import hashlib
import random
from typing import Iterator

from interfaces import ISynapseClient, IDataGenerator

# Imports from existing proto folder
from proto import synapse_hft_pb2
from proto import synapse_hft_pb2_grpc

class GRPCClient(ISynapseClient):
    """Concrete implementation of gRPC client for HFTLink service."""
    
    def __init__(self):
        self.channel = None
        self.stub = None
        self.is_streaming = False
        
    def connect(self, address: str):
        self.channel = grpc.insecure_channel(address)
        self.stub = synapse_hft_pb2_grpc.HFTLinkStub(self.channel)
        
    def system_control(self, action: str) -> bool:
        if not self.stub:
            return False
            
        action_enum = getattr(synapse_hft_pb2.ControlCommand, action.upper(), None)
        if action_enum is None:
            print(f"Unknown control action: {action}")
            return False
            
        request = synapse_hft_pb2.ControlCommand(action=action_enum)
        try:
            response = self.stub.SystemControl(request)
            return response.success
        except Exception as e:
            print(f"Error in SystemControl ({action}): {e}")
            return False
            
    def load_scenario(self, map_file_path: str) -> bool:
        if not os.path.exists(map_file_path):
            return False
            
        with open(map_file_path, "rb") as f:
            content = f.read()
            
        map_hash = hashlib.sha256(content).hexdigest()
        
        peak_schedule_json = ""
        peak_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "peak_schedule.json")
        if os.path.exists(peak_file_path):
            try:
                with open(peak_file_path, "r", encoding="utf-8") as f:
                    peak_schedule_json = f.read()
            except Exception as e:
                print(f"Error reading peak schedule: {e}")
        
        request = synapse_hft_pb2.ScenarioDefinition(
            map_hash=map_hash,
            map_file_content=content,
            map_file_name=os.path.basename(map_file_path),
            peak_schedule_json=peak_schedule_json
        )
        
        try:
            response = self.stub.LoadScenario(request)
            return response.accepted
        except Exception as e:
            print(f"Error loading scenario: {e}")
            return False
            
    def stream_traffic(self, generator: IDataGenerator, on_frame_sent=None):
        self.is_streaming = True
        
        def request_iterator():
            seq_id = 0
            while self.is_streaming:
                data = generator.generate_frame(seq_id)
                
                # Convert dict to TrafficFrame message
                frame = synapse_hft_pb2.TrafficFrame(
                    timestamp=data["timestamp"],
                    sequence_id=data["sequence_id"]
                )
                
                for eid, estate in data["edges"].items():
                    frame.edges[eid].occupancy = estate["occupancy"]
                    frame.edges[eid].mean_speed = estate["mean_speed"]
                    frame.edges[eid].queue_length = estate["queue_length"]
                    frame.edges[eid].density = estate["density"]
                
                yield frame
                if on_frame_sent:
                    on_frame_sent(seq_id, frame)
                seq_id += 1
                # Frequency: 50ms to 100ms
                time.sleep(random.uniform(0.050, 0.100))
                
        try:
            # StreamTraffic is a client-streaming RPC (stream TrafficFrame returns SystemState)
            self.stub.StreamTraffic(request_iterator())
        except Exception as e:
            print(f"Streaming error: {e}")
            self.is_streaming = False
            
    def stop_streaming(self):
        self.is_streaming = False
        if self.channel:
            # We don't necessarily close the channel here, just stop the loop
            pass
