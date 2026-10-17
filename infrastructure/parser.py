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
# File: infrastructure/parser.py
# Author: Gabriel Moraes
# Date: October 2026

import xml.etree.ElementTree as ET
import gzip
import os

def extract_edge_ids(file_path):
    """
    Extracts edge IDs from a SUMO .net.xml file.
    Supports both plain .xml and .gz compressed files.
    Filters out internal edges (starting with ':').
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Map file not found: {file_path}")

    is_gz = file_path.endswith('.gz')
    
    try:
        if is_gz:
            with gzip.open(file_path, 'rb') as f:
                tree = ET.parse(f)
        else:
            tree = ET.parse(file_path)
            
        root = tree.getroot()
        
        edge_ids = []
        for edge in root.findall('edge'):
            edge_id = edge.get('id')
            if edge_id and not edge_id.startswith(':'):
                edge_ids.append(edge_id)
                
        return edge_ids
    except Exception as e:
        print(f"Error parsing map XML: {e}")
        return []
