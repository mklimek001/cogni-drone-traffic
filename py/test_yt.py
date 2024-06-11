from ultralytics import YOLO

src = "https://youtu.be/1fiF7B6VkCk"

model = YOLO('runs_1920/detect/train/weights/best.pt')
results = model.predict(src, stream=True, imgsz=1920)

for result in results:
	result.show(labels=False)
