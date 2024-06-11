from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model.train(data="dataset.yaml", epochs=50, imgsz=1080)
model.export()
