#!/usr/bin/env python3
"""
Simple example of using Pkr_Notes for banknote detection
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from detect_pkr import load_model, detect_banknotes

def main():
    """Simple example of PKR banknote detection."""
    print("🏦 Pkr_Notes - Simple Detection Example")
    print("=" * 50)
    
    # Check for available models
    available_models = [f for f in os.listdir(".") if f.endswith(".pt")]
    
    if not available_models:
        print("❌ No trained models found!")
        print("Please ensure you have trained models (.pt files) in the current directory.")
        return
    
    print(f"📁 Found {len(available_models)} model(s):")
    for model in available_models:
        print(f"  - {model}")
    
    # Use the first available model
    model_path = available_models[0]
    print(f"\n🔧 Using model: {model_path}")
    
    # Load the model
    model = load_model(model_path)
    if model is None:
        return
    
    # Check for test images
    test_dir = "test/images"
    if os.path.exists(test_dir):
        print(f"\n📸 Found test directory: {test_dir}")
        print("Running detection on test images...")
        
        # Run detection on test images
        detect_banknotes(model, test_dir, conf=0.25, save_results=True)
        
        print("\n✅ Detection completed! Check the 'runs/detect/predict' folder for results.")
    else:
        print(f"\n📸 Test directory not found: {test_dir}")
        print("You can test with your own images using:")
        print(f"python detect_pkr.py --model {model_path} --image path/to/your/image.jpg")
    
    print("\n🎉 Example completed successfully!")

if __name__ == "__main__":
    main()
