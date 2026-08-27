# test_thrivebridge.py
"""
Tests for ThriveBridge module.
"""

import unittest
from thrivebridge import ThriveBridge

class TestThriveBridge(unittest.TestCase):
    """Test cases for ThriveBridge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ThriveBridge()
        self.assertIsInstance(instance, ThriveBridge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ThriveBridge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
