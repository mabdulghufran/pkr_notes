#!/usr/bin/env python3
"""
Pkr_Notes Detection Script

A simple script to detect Pakistani Rupee banknotes using trained YOLOv8 models.
"""

import argparse
import os
from pathlib import Path
from ultralytics import YOLO
import cv2
import numpy as np

# PKR denominations mapping
PKR_CLASSES = {
    0: 'PKR_10',
    1: 'PKR_100', 
    2: 'PKR_1000',
    3: 'PKR_20',
    4: 'PKR_50',
    5: 'PKR_500',
    6: 'PKR_5000'
}

def load_model(model_path):
    """Load the YOLOv8 model from the specified path."""
    try:
        model = YOLO(model_path)
        print(f"✅ Model loaded successfully: {model_path}")
        return model
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return None

def detect_banknotes(model, image_path, conf_threshold=0.25, save_results=True):
    """Detect PKR banknotes in the given image."""
    try:
        # Perform prediction
        results = model.predict(
            source=image_path,
            conf=conf_threshold,
            save=save_results,
            show=False
        )
        
        # Process results
        for result in results:
            if result.boxes is not None:
                boxes = result.boxes.xyxy.cpu().numpy()
                confidences = result.boxes.conf.cpu().numpy()
                class_ids = result.boxes.cls.cpu().numpy().astype(int)
                
                print(f"\n🔍 Detection Results for {image_path}:")
                print("-" * 50)
                
                if len(boxes) == 0:
                    print("No banknotes detected.")
                    continue
                
                for i, (box, conf, class_id) in enumerate(zip(boxes, confidences, class_ids)):
                    class_name = PKR_CLASSES.get(class_id, f"Unknown_{class_id}")
                    x1, y1, x2, y2 = box
                    
                    print(f"Banknote {i+1}: {class_name}")
                    print(f"  Confidence: {conf:.3f}")
                    print(f"  Bounding Box: ({x1:.1f}, {y1:.1f}) to ({x2:.1f}, {y2:.1f})")
                    print()
                
                print(f"Total banknotes detected: {len(boxes)}")
                
        return results
        
    except Exception as e:
        print(f"❌ Error during detection: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Detect PKR banknotes using YOLOv8")
    parser.add_argument("--model", type=str, default="best.pt", 
                       help="Path to the trained model (.pt file)")
    parser.add_argument("--image", type=str, required=True,
                       help="Path to the image file or directory")
    parser.add_argument("--conf", type=float, default=0.25,
                       help="Confidence threshold (default: 0.25)")
    parser.add_argument("--save", action="store_true", default=True,
                       help="Save detection results")
    
    args = parser.parse_args()
    
    # Check if model exists
    if not os.path.exists(args.model):
        print(f"❌ Model file not found: {args.model}")
        print("Available models:")
        for file in os.listdir("."):
            if file.endswith(".pt"):
                print(f"  - {file}")
        return
    
    # Load model
    model = load_model(args.model)
    if model is None:
        return
    
    # Check if image path exists
    if not os.path.exists(args.image):
        print(f"❌ Image path not found: {args.image}")
        return
    
    # Process image or directory
    if os.path.isfile(args.image):
        # Single image
        detect_banknotes(model, args.image, args.conf, args.save)
    elif os.path.isdir(args.image):
        # Directory of images
        image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
        image_files = []
        
        for ext in image_extensions:
            image_files.extend(Path(args.image).glob(f"*{ext}"))
            image_files.extend(Path(args.image).glob(f"*{ext.upper()}"))
        
        if not image_files:
            print(f"❌ No image files found in directory: {args.image}")
            return
        
        print(f"📁 Processing {len(image_files)} images...")
        for image_file in image_files:
            detect_banknotes(model, str(image_file), args.conf, args.save)
    else:
        print(f"❌ Invalid path: {args.image}")

if __name__ == "__main__":
    main()
