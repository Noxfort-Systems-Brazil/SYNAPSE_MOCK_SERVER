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
# File: interfaces.py
# Author: Gabriel Moraes
# Date: October 2026

from abc import ABC, abstractmethod
from typing import Iterator

class IDataGenerator(ABC):
    """Interface for generating traffic data frames."""
    
    @abstractmethod
    def generate_frame(self, sequence_id: int) -> any:
        """Generates a single TrafficFrame."""
        pass

class ISynapseClient(ABC):
    """Interface for gRPC client communication with Carina."""
    
    @abstractmethod
    def connect(self, address: str):
        """Connects to the gRPC server."""
        pass
    
    @abstractmethod
    def system_control(self, action: str) -> bool:
        """Sends a SystemControl command (e.g., START, STOP)."""
        pass
    
    @abstractmethod
    def load_scenario(self, map_file_path: str) -> bool:
        """Loads a scenario from a map file."""
        pass
    
    @abstractmethod
    def stream_traffic(self, generator: IDataGenerator, on_frame_sent=None):
        """
        Starts streaming traffic data.
        on_frame_sent: optional callback(seq_id, frame)
        """
        pass
    
    @abstractmethod
    def stop_streaming(self):
        """Stops the streaming process."""
        pass
