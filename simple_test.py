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
# File: simple_test.py
# Author: Gabriel Moraes
# Date: October 2026

#!/usr/bin/env python3
"""
Simple test script to verify that the refactored topology analyzer can be imported.
"""

def test_imports():
    """Test that we can import the refactored modules."""
    try:
        from infrastructure.topology_analyzer import TopologyAnalyzer
        print("✓ TopologyAnalyzer imported successfully")
        
        from interfaces.parser_interface import FileParser
        print("✓ FileParser interface imported successfully")
        
        from interfaces.topology_interface import TopologyExtractor, TopologyQuerier, TopologyReporter
        print("✓ Topology interfaces imported successfully")
        
        from infrastructure.parsers.xml_parser import XMLParser
        print("✓ XMLParser imported successfully")
        
        from infrastructure.topology.topology_extractor import TopologyExtractorImpl
        print("✓ TopologyExtractorImpl imported successfully")
        
        from infrastructure.topology.topology_querier import TopologyQuerierImpl
        print("✓ TopologyQuerierImpl imported successfully")
        
        from infrastructure.topology.topology_reporter import TopologyReporterImpl
        print("✓ TopologyReporterImpl imported successfully")
        
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False

def test_class_structure():
    """Test basic class structure."""
    try:
        from infrastructure.topology_analyzer import TopologyAnalyzer
        
        # Check that the class can be instantiated
        analyzer = TopologyAnalyzer()
        print("✓ TopologyAnalyzer can be instantiated")
        
        # Check that expected methods exist
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
    except Exception as e:
        print(f"✗ Class structure test failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing refactored TopologyAnalyzer structure...\n")
    
    tests = [
        test_imports,
        test_class_structure
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"Passed {passed}/{len(tests)} test groups")
    
    if passed == len(tests):
        print("🎉 All tests passed!")
    else:
        print("❌ Some tests failed!")