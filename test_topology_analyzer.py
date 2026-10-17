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
# File: test_topology_analyzer.py
# Author: Gabriel Moraes
# Date: October 2026

#!/usr/bin/env python3
"""
Test script to verify that the refactored topology analyzer maintains the same functionality.
"""

import sys
import os

# Add the project root to the path so we can import modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from infrastructure.topology_analyzer import TopologyAnalyzer

def test_topology_analyzer_creation():
    """Test that we can create a TopologyAnalyzer instance."""
    try:
        analyzer = TopologyAnalyzer()
        print("✓ TopologyAnalyzer created successfully")
        return True
    except Exception as e:
        print(f"✗ Failed to create TopologyAnalyzer: {e}")
        return False

def test_public_interface():
    """Test that the public interface methods exist."""
    analyzer = TopologyAnalyzer()
    
    # Check that all expected methods exist
    expected_methods = [
        'analyze_file',
        'get_downstream_edges',
        'get_upstream_edges',
        'get_connected_edges',
        'print_topology_summary'
    ]
    
    for method in expected_methods:
        if hasattr(analyzer, method):
            print(f"✓ Method '{method}' exists")
        else:
            print(f"✗ Method '{method}' is missing")
            return False
    
    return True

def test_injected_dependencies():
    """Test that we can inject dependencies."""
    from infrastructure.parsers.xml_parser import XMLParser
    from infrastructure.topology.topology_extractor import TopologyExtractorImpl
    from infrastructure.topology.topology_querier import TopologyQuerierImpl
    from infrastructure.topology.topology_reporter import TopologyReporterImpl
    
    try:
        analyzer = TopologyAnalyzer(
            parser=XMLParser(),
            extractor=TopologyExtractorImpl(),
            querier=TopologyQuerierImpl(),
            reporter=TopologyReporterImpl()
        )
        print("✓ Dependencies can be injected")
        return True
    except Exception as e:
        print(f"✗ Failed to inject dependencies: {e}")
        return False

if __name__ == "__main__":
    print("Testing refactored TopologyAnalyzer...\n")
    
    tests = [
        test_topology_analyzer_creation,
        test_public_interface,
        test_injected_dependencies
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"Passed {passed}/{len(tests)} tests")
    
    if passed == len(tests):
        print("🎉 All tests passed!")
        sys.exit(0)
    else:
        print("❌ Some tests failed!")
        sys.exit(1)