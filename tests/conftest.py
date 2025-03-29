"""
Configuration file for pytest that sets up the testing environment.
This file is automatically recognized by pytest.
"""

import os
import sys
from pathlib import Path

# Add src directory to Python path for testing
src_path = Path(__file__).parent.parent / 'src'
sys.path.insert(0, str(src_path))