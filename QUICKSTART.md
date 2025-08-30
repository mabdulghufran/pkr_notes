# 🚀 Quick Start Guide - Pkr_Notes

Get up and running with Pkr_Notes in just a few minutes!

## ⚡ Quick Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Pkr_Notes.git
cd Pkr_Notes
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Verify Installation
```bash
python -c "import ultralytics; print('✅ Ultralytics installed successfully!')"
```

## 🔍 Quick Detection Test

### Single Image Detection
```bash
python detect_pkr.py --model best.pt --image test/images/your_image.jpg
```

### Batch Detection
```bash
python detect_pkr.py --model best.pt --image test/images/ --conf 0.3
```

### Using Python Script
```python
from ultralytics import YOLO

# Load model
model = YOLO('best.pt')

# Detect banknotes
results = model.predict('your_image.jpg', conf=0.25)
```

## 📊 Quick Training

### 1. Prepare Your Data
Ensure your data is organized as:
```
data/
├── train/
│   ├── images/
│   └── labels/
├── valid/
│   ├── images/
│   └── labels/
└── test/
    ├── images/
    └── labels/
```

### 2. Update data.yaml
```yaml
train: data/train
val: data/valid
test: data/test
nc: 7
names: ['PKR_10', 'PKR_100', 'PKR_1000', 'PKR_20', 'PKR_50', 'PKR_500', 'PKR_5000']
```

### 3. Start Training
```python
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
model.train(data='data.yaml', epochs=10, imgsz=640)
```

## 🎯 Common Use Cases

### Real-time Detection
```python
# Webcam detection
results = model.predict(source=0, show=True, conf=0.25)
```

### Batch Processing
```python
# Process multiple images
results = model.predict('folder_with_images/', save=True, conf=0.3)
```

### Export Model
```python
# Export to different formats
model.export(format='onnx')  # ONNX format
model.export(format='tflite')  # TensorFlow Lite
```

## 🔧 Configuration Tips

### Confidence Threshold
- **High Precision**: `conf=0.5` (fewer false positives)
- **High Recall**: `conf=0.1` (catch more banknotes)
- **Balanced**: `conf=0.25` (recommended)

### Image Size
- **Fast**: `imgsz=320` (lower accuracy)
- **Balanced**: `imgsz=640` (recommended)
- **High Quality**: `imgsz=1280` (higher accuracy, slower)

### Batch Size
- **GPU Memory**: Adjust based on your hardware
- **Small GPU**: `batch=8`
- **Large GPU**: `batch=32` or higher

## 🚨 Troubleshooting

### Common Issues

#### 1. CUDA Out of Memory
```bash
# Reduce batch size
python detect_pkr.py --model best.pt --image image.jpg --batch 4
```

#### 2. Model Not Found
```bash
# Check available models
ls *.pt
```

#### 3. Import Errors
```bash
# Reinstall ultralytics
pip uninstall ultralytics
pip install ultralytics==8.0.20
```

### Performance Tips

#### 1. GPU Acceleration
```bash
# Check CUDA availability
python -c "import torch; print(torch.cuda.is_available())"
```

#### 2. Model Optimization
```python
# Use smaller model for speed
model = YOLO('yolov8n.pt')  # Fastest
model = YOLO('yolov8s.pt')  # Balanced
model = YOLO('yolov8m.pt')  # Most accurate
```

## 📚 Next Steps

### 1. Explore Examples
- Check `examples/` folder
- Run `python examples/simple_detection.py`

### 2. Customize Training
- Modify hyperparameters in training notebook
- Experiment with different model sizes
- Try data augmentation techniques

### 3. Deploy Your Model
- Export to production format
- Integrate with web/mobile apps
- Set up API endpoints

### 4. Contribute
- Report bugs via GitHub Issues
- Submit feature requests
- Contribute code via Pull Requests

## 🆘 Need Help?

- 📖 **Documentation**: Check `docs/` folder
- 🐛 **Issues**: GitHub Issues page
- 💬 **Discussions**: GitHub Discussions
- 📧 **Contact**: Open an issue for support

---

**Happy detecting! 🏦✨**

For detailed information, check the main [README.md](README.md) and [PROJECT_OVERVIEW.md](docs/PROJECT_OVERVIEW.md).
