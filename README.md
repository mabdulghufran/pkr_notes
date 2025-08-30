# Pkr_Notes - Pakistani Rupee Banknote Detection

A YOLOv8-based object detection system for identifying and classifying Pakistani Rupee (PKR) banknotes. This project uses computer vision to detect 7 different denominations of PKR banknotes.

## 🏦 Supported Banknote Denominations

- **PKR_10** - 10 Rupees
- **PKR_20** - 20 Rupees  
- **PKR_50** - 50 Rupees
- **PKR_100** - 100 Rupees
- **PKR_500** - 500 Rupees
- **PKR_1000** - 1000 Rupees
- **PKR_5000** - 5000 Rupees

## 🚀 Features

- **YOLOv8 Architecture**: State-of-the-art object detection using Ultralytics YOLOv8
- **Multi-class Detection**: Detects 7 different PKR banknote denominations
- **High Accuracy**: Trained on a comprehensive dataset with multiple training iterations
- **Real-time Detection**: Fast inference for real-world applications
- **Multiple Models**: Various trained models with different hyperparameters

## 📁 Project Structure

```
Pkr_Notes/
├── data.yaml                 # Dataset configuration
├── train/                    # Training images and labels
├── valid/                    # Validation images and labels  
├── test/                     # Test images and labels
├── runs/                     # Training outputs and results
│   ├── detect/
│   │   ├── train/           # Training run 1
│   │   ├── train2/          # Training run 2
│   │   ├── train3/          # Training run 3
│   │   ├── train4/          # Training run 4
│   │   ├── train5/          # Training run 5
│   │   └── predict/         # Prediction results
├── best.pt                   # Best model weights
├── best02.pt                # Alternative model weights
├── best03.pt                # Alternative model weights
├── best04.pt                # Alternative model weights
├── best05.pt                # Alternative model weights
├── yolov8n.pt               # Base YOLOv8 nano model
└── Pkr_notes.ipynb          # Training and evaluation notebook
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- CUDA-compatible GPU (recommended)
- Git

### Setup
1. Clone the repository:
```bash
git clone https://github.com/mabdulghufran/pkr_notes.git
cd Pkr_Notes
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install Ultralytics:
```bash
pip install ultralytics==8.0.20
```

## 📊 Dataset

The dataset contains:
- **Training**: 1,542 images
- **Validation**: 242 images  
- **Testing**: 140 images

Each image is annotated with bounding boxes and class labels for the 7 PKR denominations.

## 🎯 Training

The project includes multiple training runs with different hyperparameters:

- **Run 1**: 10 epochs, batch=16, workers=8
- **Run 2**: 10 epochs, batch=32, workers=16  
- **Run 3**: 10 epochs, batch=10, workers=5
- **Run 4**: 10 epochs, batch=64, workers=4, mask_ratio=2
- **Run 5**: 8 epochs, batch=19, workers=9, mask_ratio=6, patience=25

## 🔍 Usage

### Training
```python
from ultralytics import YOLO

# Load model
model = YOLO('yolov8n.pt')

# Train model
model.train(data='data.yaml', epochs=10, imgsz=640, batch=16)
```

### Inference
```python
# Load trained model
model = YOLO('runs/detect/train3/weights/best.pt')

# Predict on images
results = model.predict('path/to/image.jpg', conf=0.25)
```

### Validation
```python
# Validate model
model.val(data='data.yaml')
```

## 📈 Results

The models achieve high accuracy in detecting PKR banknotes across different denominations. Training metrics and confusion matrices are available in the respective training run directories.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Ultralytics](https://github.com/ultralytics/ultralytics) for YOLOv8 implementation
- [Roboflow](https://roboflow.com/) for dataset management
- The computer vision community for continuous improvements

## 📞 Contact

For questions or support, please open an issue on GitHub.

---

**Note**: This project is designed for educational and research purposes. Please ensure compliance with local regulations when using this system for financial applications.

