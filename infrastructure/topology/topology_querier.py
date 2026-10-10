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
# File: infrastructure/topology/topology_querier.py
# Author: Gabriel Moraes
# Date: 2026-10-10

from typing import Dict, List
from infrastructure.topology.topology_extractor import EdgeInfo, JunctionInfo
from interfaces.topology_interface import TopologyQuerier

class TopologyQuerierImpl(TopologyQuerier):
    """Concrete implementation of TopologyQuerier for SUMO networks."""
    
    def get_downstream_edges(self, edge_id: str, edges: Dict[str, EdgeInfo], junctions: Dict[str, JunctionInfo]) -> List[str]:
        """
        Get edges that are directly downstream (connected after) of the given edge.
        
        Args:
            edge_id: ID of the edge to find downstream connections for
            edges: Dictionary of all edges
            junctions: Dictionary of all junctions
            
        Returns:
            List of downstream edge IDs
        """
        if edge_id not in edges:
            return []
            
        edge = edges[edge_id]
        junction_id = edge.to_node
        
        if not junction_id or junction_id not in junctions:
            return []
            
        # Return outgoing edges of the junction this edge leads to
        return list(junctions[junction_id].out_edges)
    
    def get_upstream_edges(self, edge_id: str, edges: Dict[str, EdgeInfo], junctions: Dict[str, JunctionInfo]) -> List[str]:
        """
        Get edges that are directly upstream (connected before) of the given edge.
        
        Args:
            edge_id: ID of the edge to find upstream connections for
            edges: Dictionary of all edges
            junctions: Dictionary of all junctions
            
        Returns:
            List of upstream edge IDs
        """
        if edge_id not in edges:
            return []
            
        edge = edges[edge_id]
        junction_id = edge.from_node
        
        if not junction_id or junction_id not in junctions:
            return []
            
        # Return incoming edges of the junction this edge comes from
        return list(junctions[junction_id].inc_edges)