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
# File: infrastructure/topology/topology_extractor.py
# Author: Gabriel Moraes
# Date: October 2026

import xml.etree.ElementTree as ET
from typing import Dict, List, Set, Any
from interfaces.topology_interface import TopologyExtractor

class EdgeInfo:
    """Information about a road edge."""
    def __init__(self, edge_id: str, from_node: str, to_node: str, 
                 priority: int = 0, length: float = 0.0, 
                 speed_limit: float = 13.89, n_lanes: int = 1):
        self.id = edge_id
        self.from_node = from_node
        self.to_node = to_node
        self.priority = priority
        self.length = length
        self.speed_limit = speed_limit
        self.n_lanes = n_lanes
        self.lanes = []

class LaneInfo:
    """Information about a lane."""
    def __init__(self, lane_id: str, index: int, speed_limit: float = 13.89, 
                 length: float = 0.0, width: float = 3.2):
        self.id = lane_id
        self.index = index
        self.speed_limit = speed_limit
        self.length = length
        self.width = width

class ConnectionInfo:
    """Information about a connection between lanes."""
    def __init__(self, from_lane: str, to_lane: str, direction: str = "",
                 tls: str = "", tl_link_index: int = -1):
        self.from_lane = from_lane
        self.to_lane = to_lane
        self.direction = direction
        self.tls = tls  # Traffic light system
        self.tl_link_index = tl_link_index

class JunctionInfo:
    """Information about a junction."""
    def __init__(self, node_id: str, node_type: str, x: float = 0.0, y: float = 0.0):
        self.id = node_id
        self.type = node_type
        self.x = x
        self.y = y
        self.inc_edges: Set[str] = set()  # Incoming edges
        self.out_edges: Set[str] = set()  # Outgoing edges

class TopologyExtractorImpl(TopologyExtractor):
    """Concrete implementation of TopologyExtractor for SUMO networks."""
    
    def extract_junctions(self, root: ET.Element) -> Dict[str, JunctionInfo]:
        """Extract junction information from XML."""
        junctions = {}
        for node_elem in root.findall('node'):
            node_id = node_elem.get('id')
            node_type = node_elem.get('type', 'priority')
            x = float(node_elem.get('x', 0.0))
            y = float(node_elem.get('y', 0.0))
            
            junctions[node_id] = JunctionInfo(node_id, node_type, x, y)
        
        return junctions
    
    def extract_edges(self, root: ET.Element) -> Dict[str, EdgeInfo]:
        """Extract edge information from XML."""
        edges = {}
        for edge_elem in root.findall('edge'):
            edge_id = edge_elem.get('id')
            
            # Skip internal edges (those starting with ':')
            if edge_id and edge_id.startswith(':'):
                continue
                
            if not edge_id:
                continue
                
            from_node = edge_elem.get('from')
            to_node = edge_elem.get('to')
            priority = int(edge_elem.get('priority', 0))
            
            # Create edge info
            edge_info = EdgeInfo(edge_id, from_node, to_node, priority)
            
            # Extract lane information
            for lane_elem in edge_elem.findall('lane'):
                lane_id = lane_elem.get('id')
                lane_index = int(lane_elem.get('index', 0))
                speed_limit = float(lane_elem.get('speed', 13.89))
                length = float(lane_elem.get('length', 0.0))
                width = float(lane_elem.get('width', 3.2))
                
                lane_info = LaneInfo(lane_id, lane_index, speed_limit, length, width)
                edge_info.lanes.append(lane_info)
            
            # Set edge properties based on lanes
            if edge_info.lanes:
                edge_info.n_lanes = len(edge_info.lanes)
                edge_info.length = edge_info.lanes[0].length
                edge_info.speed_limit = edge_info.lanes[0].speed_limit
            
            edges[edge_id] = edge_info
        
        return edges
    
    def extract_connections(self, root: ET.Element) -> List[ConnectionInfo]:
        """Extract connection information from XML."""
        connections = []
        for conn_elem in root.findall('connection'):
            from_lane = conn_elem.get('from')
            to_lane = conn_elem.get('to')
            direction = conn_elem.get('dir', '')
            tls = conn_elem.get('tl', '')
            tl_link_index = int(conn_elem.get('linkIndex', -1))
            
            # Validate connection
            if from_lane and to_lane:
                conn_info = ConnectionInfo(from_lane, to_lane, direction, tls, tl_link_index)
                connections.append(conn_info)
        
        return connections