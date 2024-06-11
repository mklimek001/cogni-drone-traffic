from ultralytics import YOLO

model = YOLO('../../runs_1920_e200/detect/train/weights/last.pt')
results = model.predict('../mini_test', imgsz=1920)

for result in results:
	result.show(labels=False)
	result.show(labels=True)
