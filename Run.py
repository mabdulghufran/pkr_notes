from ultralytics import YOLO
model=YOLO('best04.pt')

model.predict(source=0 , imgsz=640 , conf=0.4 ,show=True)
#model.predict(source="1.jpeg" , imgsz=640 , conf=0.4 ,save=True)