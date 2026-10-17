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
# File: interfaces/topology_interface.py
# Author: Gabriel Moraes
# Date: October 2026

from abc import ABC, abstractmethod
from typing import Dict, List, Any

class TopologyExtractor(ABC):
    """Interface for extracting topology information."""
    
    @abstractmethod
    def extract_junctions(self, parsed_data: Any) -> Dict[str, Any]:
        """Extract junction information from parsed data."""
        pass
    
    @abstractmethod
    def extract_edges(self, parsed_data: Any) -> Dict[str, Any]:
        """Extract edge information from parsed data."""
        pass
    
    @abstractmethod
    def extract_connections(self, parsed_data: Any) -> List[Any]:
        """Extract connection information from parsed data."""
        pass

class TopologyQuerier(ABC):
    """Interface for querying topology information."""
    
    @abstractmethod
    def get_downstream_edges(self, edge_id: str, edges: Dict[str, Any], junctions: Dict[str, Any]) -> List[str]:
        """Get edges that are directly downstream of the given edge."""
        pass
    
    @abstractmethod
    def get_upstream_edges(self, edge_id: str, edges: Dict[str, Any], junctions: Dict[str, Any]) -> List[str]:
        """Get edges that are directly upstream of the given edge."""
        pass

class TopologyReporter(ABC):
    """Interface for reporting topology information."""
    
    @abstractmethod
    def print_topology_summary(self, edges: Dict[str, Any], junctions: Dict[str, Any], connections: List[Any]):
        """Print a summary of the extracted topology."""
        pass