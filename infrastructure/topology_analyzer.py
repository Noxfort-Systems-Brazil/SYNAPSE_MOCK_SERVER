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
# File: infrastructure/topology_analyzer.py
# Author: Gabriel Moraes
# Date: October 2026

"""
Topology Analyzer for SUMO .net.xml files.

This module analyzes SUMO network files to extract topological information
about the road network, including edges, connections, and junctions.
"""

import os
from typing import Dict, List
from interfaces.parser_interface import FileParser
from interfaces.topology_interface import TopologyExtractor, TopologyQuerier, TopologyReporter
from infrastructure.parsers.xml_parser import XMLParser
from infrastructure.topology.topology_extractor import TopologyExtractorImpl, EdgeInfo, JunctionInfo, ConnectionInfo
from infrastructure.topology.topology_querier import TopologyQuerierImpl
from infrastructure.topology.topology_reporter import TopologyReporterImpl

class TopologyAnalyzer:
    """
    Analyzes SUMO .net.xml files to extract network topology.
    
    Extracts information about:
    - Edges (roads) and their properties
    - Lanes within edges
    - Connections between lanes
    - Junctions and their connecting edges
    """
    
    def __init__(self, 
                 parser: FileParser = None,
                 extractor: TopologyExtractor = None,
                 querier: TopologyQuerier = None,
                 reporter: TopologyReporter = None):
        # Dependencies with default implementations
        self.parser = parser or XMLParser()
        self.extractor = extractor or TopologyExtractorImpl()
        self.querier = querier or TopologyQuerierImpl()
        self.reporter = reporter or TopologyReporterImpl()
        
        # Data storage
        self.edges: Dict[str, EdgeInfo] = {}
        self.junctions: Dict[str, JunctionInfo] = {}
        self.connections: List[ConnectionInfo] = []
        
    def analyze_file(self, file_path: str) -> bool:
        """
        Analyze a SUMO .net.xml or .net.xml.gz file.
        
        Args:
            file_path: Path to the network file
            
        Returns:
            True if analysis was successful, False otherwise
        """
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return False
            
        try:
            # Parse the file using injected parser
            parsed_data = self.parser.parse_file(file_path)
            
            # Extract topology information
            self.junctions = self.extractor.extract_junctions(parsed_data)
            self.edges = self.extractor.extract_edges(parsed_data)
            self.connections = self.extractor.extract_connections(parsed_data)
            
            # Build junction connectivity
            self._build_junction_connectivity()
            
            return True
        except Exception as e:
            print(f"Error analyzing network file: {e}")
            return False
    
    def _build_junction_connectivity(self):
        """Build connectivity information for junctions."""
        # For each edge, add it to the appropriate junction's incoming/outgoing sets
        for edge_id, edge_info in self.edges.items():
            from_node = edge_info.from_node
            to_node = edge_info.to_node
            
            # Add to outgoing edges of from_node
            if from_node and from_node in self.junctions:
                self.junctions[from_node].out_edges.add(edge_id)
            
            # Add to incoming edges of to_node
            if to_node and to_node in self.junctions:
                self.junctions[to_node].inc_edges.add(edge_id)
    
    def get_downstream_edges(self, edge_id: str) -> List[str]:
        """
        Get edges that are directly downstream (connected after) of the given edge.
        
        Args:
            edge_id: ID of the edge to find downstream connections for
            
        Returns:
            List of downstream edge IDs
        """
        return self.querier.get_downstream_edges(edge_id, self.edges, self.junctions)
    
    def get_upstream_edges(self, edge_id: str) -> List[str]:
        """
        Get edges that are directly upstream (connected before) of the given edge.
        
        Args:
            edge_id: ID of the edge to find upstream connections for
            
        Returns:
            List of upstream edge IDs
        """
        return self.querier.get_upstream_edges(edge_id, self.edges, self.junctions)
    
    def get_connected_edges(self, edge_id: str) -> Dict[str, List[str]]:
        """
        Get all connected edges (both upstream and downstream).
        
        Args:
            edge_id: ID of the edge to find connections for
            
        Returns:
            Dictionary with 'upstream' and 'downstream' keys containing lists of edge IDs
        """
        return {
            'upstream': self.get_upstream_edges(edge_id),
            'downstream': self.get_downstream_edges(edge_id)
        }
    
    def print_topology_summary(self):
        """Print a summary of the extracted topology."""
        self.reporter.print_topology_summary(self.edges, self.junctions, self.connections)
