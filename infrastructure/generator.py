# Synapse Mock Server is an open-source test harness and telemetry simulator for the Synapse HFT protocol.
#
# SPDX-FileCopyrightText: 2026 Gabriel Moraes - Noxfort Systems
# SPDX-License-Identifier: Apache-2.0
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
# File: infrastructure/generator.py
# Author: Gabriel Moraes
# Date: October 2026

import time
import random
from interfaces import IDataGenerator

# Imports from existing proto folder
from proto import synapse_hft_pb2

class RandomTrafficGenerator(IDataGenerator):
    """Generates fake traffic data with oscillating occupancy and speed using a random walk for realism."""
    
    def __init__(self, edge_ids=None):
        self.edge_ids = []
        self.current_states = {}
        self.set_edges(edge_ids or ["edge_1", "edge_2", "edge_3", "junction_north", "junction_south"])
        
    def set_edges(self, edge_ids):
        """Dynamically update the edges and initialize their states."""
        self.edge_ids = edge_ids
        self.current_states = {eid: self._get_initial_state() for eid in edge_ids}

    def _get_initial_state(self):
        """Helper to create a starting point for an edge."""
        return {
            "occupancy": random.uniform(0.1, 0.5),
            "mean_speed": random.uniform(40.0, 60.0),
            "queue_length": random.randint(0, 5),
            "density": random.uniform(10.0, 15.0)
        }

    def _update_state(self, eid):
        """Applies a small random variation to the current state of an edge."""
        state = self.current_states[eid]
        
        # Random walk deltas
        state["occupancy"] = max(0.01, min(0.95, state["occupancy"] + random.uniform(-0.05, 0.05)))
        state["mean_speed"] = max(5.0, min(120.0, state["mean_speed"] + random.uniform(-2.0, 2.0)))
        state["queue_length"] = max(0, min(50, state["queue_length"] + random.randint(-1, 1)))
        state["density"] = max(1.0, min(100.0, state["density"] + random.uniform(-1.0, 1.0)))
        
        return state.copy()

    def generate_frame(self, sequence_id: int):
        """Generates a single TrafficFrame message with smooth transitions."""
        edges_data = {}
        for eid in self.edge_ids:
            if eid not in self.current_states:
                self.current_states[eid] = self._get_initial_state()
            
            edges_data[eid] = self._update_state(eid)
            
        return {
            "timestamp": time.time(),
            "sequence_id": sequence_id,
            "edges": edges_data
        }
