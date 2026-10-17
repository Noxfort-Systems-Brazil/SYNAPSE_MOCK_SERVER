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
# File: infrastructure/realistic_generator.py
# Author: Gabriel Moraes
# Date: October 2026

import time
import math
import random
from datetime import datetime
from interfaces import IDataGenerator

# Imports from existing proto folder
from proto import synapse_hft_pb2

class RealisticTrafficGenerator(IDataGenerator):
    """Generates realistic traffic data based on time-of-day patterns and edge characteristics."""
    
    def __init__(self, edge_ids=None):
        self.edge_ids = []
        self.edge_profiles = {}  # Store profile info for each edge
        self.base_timestamp = time.time()
        self.set_edges(edge_ids or ["edge_1", "edge_2", "edge_3", "junction_north", "junction_south"])
        
    def set_edges(self, edge_ids):
        """Dynamically update the edges and initialize their profiles."""
        self.edge_ids = edge_ids
        self.edge_profiles = {}
        for eid in edge_ids:
            self.edge_profiles[eid] = self._create_edge_profile(eid)
            
    def _create_edge_profile(self, edge_id):
        """Create a completely random traffic profile for an edge."""
        return {
            "type": "random",
            "base_speed": random.uniform(20.0, 100.0),
            "capacity": random.randint(500, 2500),
            "length_factor": random.uniform(0.2, 1.0)
        }
    
    def _get_time_of_day_factor(self):
        """Calculate traffic pattern factor based on time of day (0.0 to 1.0)."""
        # Get current hour (0-23) in local time
        current_hour = datetime.now().hour
        
        # Model typical traffic patterns:
        # - Low traffic at night (2-5 AM)
        # - Morning rush hour (7-9 AM)
        # - Midday moderate traffic (10 AM - 3 PM)
        # - Evening rush hour (4-7 PM)
        # - Night traffic (8 PM - 1 AM)
        
        if 2 <= current_hour <= 5:
            # Night minimum
            return 0.2
        elif 6 <= current_hour <= 8:
            # Morning ramp-up
            return 0.2 + (current_hour - 6) * 0.2
        elif 9 <= current_hour <= 11:
            # Morning peak
            return 0.8 - (current_hour - 9) * 0.1
        elif 12 <= current_hour <= 15:
            # Midday
            return 0.5 + 0.1 * math.sin((current_hour - 12) * math.pi / 3)
        elif 16 <= current_hour <= 19:
            # Evening peak
            return 0.6 + 0.4 * math.sin((current_hour - 16) * math.pi / 3)
        else:
            # Night ramp-down or low night traffic
            return 0.4 - 0.2 * math.cos((current_hour - 20) * math.pi / 4)
    
    def _calculate_traffic_state(self, profile, time_factor, edge_id="default", noise_factor=0.1):
        """Calculate traffic state that changes every 1 minute and spans from free flow to severe congestion."""
        
        # Calculate the current 1-minute block
        minute_block = int(time.time() / 60)
        
        # Deterministically seed based on the minute and the edge
        # This guarantees the state holds for 1 minute for each edge, then jumps to a new state
        seed_string = f"{minute_block}_{edge_id}"
        random.seed(seed_string)
        
        # We define 4 critical scenarios:
        # 0: Via Livre (Free Flow)
        # 1: Tráfego Moderado (Moderate Traffic)
        # 2: Congestionamento Leve (Light Congestion)
        # 3: Congestionamento Severo (Severe Congestion)
        scenario = random.randint(0, 3)
        
        if scenario == 0:
            # Via Livre
            base_occupancy = random.uniform(0.0, 0.2)
            base_speed = random.uniform(70.0, 120.0)
            base_density = random.uniform(0.0, 20.0)
            base_queue = random.randint(0, 5)
        elif scenario == 1:
            # Moderado
            base_occupancy = random.uniform(0.3, 0.5)
            base_speed = random.uniform(40.0, 60.0)
            base_density = random.uniform(30.0, 50.0)
            base_queue = random.randint(10, 20)
        elif scenario == 2:
            # Congestionamento Leve
            base_occupancy = random.uniform(0.6, 0.8)
            base_speed = random.uniform(20.0, 35.0)
            base_density = random.uniform(60.0, 90.0)
            base_queue = random.randint(30, 60)
        else:
            # Congestionamento Severo
            base_occupancy = random.uniform(0.85, 1.0)
            base_speed = random.uniform(2.0, 8.0)  # Média em torno de 5 km/h
            base_density = random.uniform(100.0, 150.0)
            base_queue = random.randint(80, 150)
            
        # Restore random seed to avoid side effects
        random.seed()
        
        # Add a tiny bit of jitter so values don't completely freeze during the minute
        occupancy = max(0.0, min(1.0, base_occupancy + random.uniform(-0.02, 0.02)))
        mean_speed = max(0.0, min(130.0, base_speed + random.uniform(-2.0, 2.0)))
        density = max(0.0, base_density + random.uniform(-2.0, 2.0))
        queue_length = max(0, base_queue + random.randint(-1, 1))
        
        return {
            "occupancy": occupancy,
            "mean_speed": mean_speed,
            "queue_length": queue_length,
            "density": density
        }
    
    def generate_frame(self, sequence_id: int):
        """Generates a single TrafficFrame message with realistic patterns."""
        # Get time-based factor for this frame
        time_factor = self._get_time_of_day_factor()
        
        edges_data = {}
        for eid in self.edge_ids:
            if eid not in self.edge_profiles:
                self.edge_profiles[eid] = self._create_edge_profile(eid)
                
            profile = self.edge_profiles[eid]
            edges_data[eid] = self._calculate_traffic_state(profile, time_factor, edge_id=eid)
            
        return {
            "timestamp": time.time(),
            "sequence_id": sequence_id,
            "edges": edges_data
        }