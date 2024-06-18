from ultralytics import YOLO
from vidgear.gears import CamGear
import cv2

# set in yt quality (1080, 720, 480, ...)
res_h = 1080
res_w = round(res_h * 16/9)
print(res_w, res_h)

# intersection
# src = "http://youtu.be/ByED80IKdIU"
# roundabout
# src = "http://youtu.be/1fiF7B6VkCk"
# low video
# src = "http://youtu.be/7HaJArMDKgI"
# Kraków new footage
src = "http://youtu.be/jN5UWu-2cno"
# zoom & movement
src = "http://youtu.be/ULT1Sf_nbes"
# zoom & sharpen
src = "http://youtu.be/D2cRE3JT-0k"

save_images = False

model = YOLO('models/runs_1920/detect/train/weights/best.pt')
yolo_input_size = res_w
yt_stream_res   = f"{res_h}p"

stream = CamGear(
    source=src,
    stream_mode=True,
    logging=True,
    STREAM_RESOLUTION=yt_stream_res
).start()

labels = True

fid = 0
while True:
    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # run predictions
    results = model.predict(frame, stream=False, imgsz=yolo_input_size)
    frame = results[0].plot(labels=labels)
    
    if save_images:
        cv2.imwrite(f"frame{fid:05}.jpg", frame)
        fid += 1

    # Show output window
    cv2.imshow("Output", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    if key == ord("l"):
        labels ^= True # flip

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()
