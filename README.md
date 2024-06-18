# Cognitive vision using drone

The project demonstrates usage of drone for the real-time detection and classification of objects in street traffic in a video stream using YOLO model.

## Installation
- Download repository
```
git clone https://github.com/mklimek001/cogni-drone-traffic.git
cd cogni-drone-traffic
```
- Create venv
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
- Make sure you have `ffmpeg` installed.
- Download the model [Model link](https://drive.google.com/file/d/1W-uRGyMSBUd0T6GIvDAQjXQJkxF-QUJn/view?usp=sharing)
- Unzip it in the repository main folder

# How to run
1. Update `src` in `yt.py` with the desired Youtube video URL.
2. Run 
```
python py/youtube/yt.py
```

For more details and documentation on YOLO, refer to the [Ultralytics YOLO documentation](https://docs.ultralytics.com/).


