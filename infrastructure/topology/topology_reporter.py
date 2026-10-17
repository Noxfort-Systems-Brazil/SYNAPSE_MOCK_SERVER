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
# File: infrastructure/topology/topology_reporter.py
# Author: Gabriel Moraes
# Date: October 2026

from typing import Dict, List, Any
from infrastructure.topology.topology_extractor import EdgeInfo, JunctionInfo, ConnectionInfo
from interfaces.topology_interface import TopologyReporter

class TopologyReporterImpl(TopologyReporter):
    """Concrete implementation of TopologyReporter for SUMO networks."""
    
    def print_topology_summary(self, edges: Dict[str, EdgeInfo], junctions: Dict[str, JunctionInfo], connections: List[ConnectionInfo]):
        """Print a summary of the extracted topology."""
        print(f"Network Topology Summary:")
        print(f"  Edges: {len(edges)}")
        print(f"  Junctions: {len(junctions)}")
        print(f"  Connections: {len(connections)}")
        
        # Print sample edges and their connections
        print(f"\nSample Edge Connections:")
        sample_count = 0
        for edge_id, edge_info in edges.items():
            if sample_count >= 5:
                break
                
            print(f"  {edge_id}:")
            print(f"    From: {edge_info.from_node}")
            print(f"    To: {edge_info.to_node}")
            sample_count += 1