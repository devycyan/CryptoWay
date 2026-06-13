# test_cryptoway.py
"""
Tests for CryptoWay module.
"""

import unittest
from cryptoway import CryptoWay

class TestCryptoWay(unittest.TestCase):
    """Test cases for CryptoWay class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoWay()
        self.assertIsInstance(instance, CryptoWay)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoWay()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
