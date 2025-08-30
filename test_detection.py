#!/usr/bin/env python3
"""
Test file for Pkr_Notes detection functionality
"""

import unittest
import os
import tempfile
from unittest.mock import patch, MagicMock
import numpy as np

# Import the detection functions
try:
    from detect_pkr import load_model, detect_banknotes, PKR_CLASSES
except ImportError:
    print("Warning: Could not import detect_pkr module. Tests may fail.")

class TestPkrDetection(unittest.TestCase):
    """Test cases for PKR banknote detection functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_image_path = "test_image.jpg"
        self.test_model_path = "test_model.pt"
        
    def test_pkr_classes(self):
        """Test that PKR classes are properly defined."""
        expected_classes = {
            0: 'PKR_10',
            1: 'PKR_100', 
            2: 'PKR_1000',
            3: 'PKR_20',
            4: 'PKR_50',
            5: 'PKR_500',
            6: 'PKR_5000'
        }
        
        self.assertEqual(PKR_CLASSES, expected_classes)
        self.assertEqual(len(PKR_CLASSES), 7)
        
    @patch('detect_pkr.YOLO')
    def test_load_model_success(self, mock_yolo):
        """Test successful model loading."""
        mock_model = MagicMock()
        mock_yolo.return_value = mock_model
        
        result = load_model(self.test_model_path)
        
        self.assertIsNotNone(result)
        mock_yolo.assert_called_once_with(self.test_model_path)
        
    @patch('detect_pkr.YOLO')
    def test_load_model_failure(self, mock_yolo):
        """Test model loading failure."""
        mock_yolo.side_effect = Exception("Model loading failed")
        
        result = load_model(self.test_model_path)
        
        self.assertIsNone(result)
        
    def test_detect_banknotes_no_model(self):
        """Test detection with no model."""
        result = detect_banknotes(None, self.test_image_path)
        self.assertIsNone(result)
        
    @patch('detect_pkr.YOLO')
    def test_detect_banknotes_success(self, mock_yolo):
        """Test successful banknote detection."""
        # Mock model
        mock_model = MagicMock()
        mock_result = MagicMock()
        
        # Mock detection results
        mock_result.boxes.xyxy.cpu.return_value.numpy.return_value = np.array([[100, 100, 200, 200]])
        mock_result.boxes.conf.cpu.return_value.numpy.return_value = np.array([0.95])
        mock_result.boxes.cls.cpu.return_value.numpy.return_value = np.array([0])
        
        mock_model.predict.return_value = [mock_result]
        
        # Test detection
        result = detect_banknotes(mock_model, self.test_image_path)
        
        self.assertIsNotNone(result)
        mock_model.predict.assert_called_once()
        
    def test_detect_banknotes_invalid_path(self):
        """Test detection with invalid image path."""
        mock_model = MagicMock()
        
        result = detect_banknotes(mock_model, "nonexistent_image.jpg")
        
        # Should handle the error gracefully
        self.assertIsNone(result)

class TestPkrDetectionIntegration(unittest.TestCase):
    """Integration tests for PKR detection."""
    
    def test_imports(self):
        """Test that all required modules can be imported."""
        try:
            import ultralytics
            import cv2
            import numpy as np
            self.assertTrue(True, "All required modules imported successfully")
        except ImportError as e:
            self.fail(f"Failed to import required module: {e}")
            
    def test_file_structure(self):
        """Test that required project files exist."""
        required_files = [
            "README.md",
            "requirements.txt",
            "LICENSE",
            "data.yaml",
            "detect_pkr.py"
        ]
        
        for file in required_files:
            self.assertTrue(
                os.path.exists(file),
                f"Required file {file} not found"
            )

if __name__ == "__main__":
    # Create a simple test runner
    print("Running Pkr_Notes detection tests...")
    
    # Run basic tests
    unittest.main(verbosity=2, exit=False)
    
    print("\n✅ All tests completed!")
