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
# File: infrastructure/parsers/xml_parser.py
# Author: Gabriel Moraes
# Date: October 2026

import xml.etree.ElementTree as ET
import gzip
import os
from interfaces.parser_interface import FileParser

class XMLParser(FileParser):
    """Concrete implementation of FileParser for XML files."""
    
    def parse_file(self, file_path: str) -> ET.Element:
        """
        Parse a SUMO .net.xml or .net.xml.gz file.
        
        Args:
            file_path: Path to the network file
            
        Returns:
            Root element of the parsed XML tree
            
        Raises:
            FileNotFoundError: If file doesn't exist
            Exception: If parsing fails
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
            
        try:
            # Parse the XML file
            if file_path.endswith('.gz'):
                with gzip.open(file_path, 'rb') as f:
                    tree = ET.parse(f)
            else:
                tree = ET.parse(file_path)
                
            return tree.getroot()
        except Exception as e:
            raise Exception(f"Error parsing network file: {e}")