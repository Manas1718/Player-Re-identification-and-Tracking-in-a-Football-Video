# Player-Re-identification-and-Tracking-in-a-Football-Video
This project demonstrates real-time player detection, tracking, and re-identification in a 15-second football video. It uses a custom-trained YOLO object detection model and DeepSORT tracker to ensure that players who go out of frame and reappear are consistently assigned the same identity.

### ⚙️ Setup Instructions
1. Clone the repository
```bash
git clone https://github.com/Manas1718/player-tracking.git
cd player-tracking
```

2. Install dependencies
```bash
pip install ultralytics opencv-python deep_sort_realtime
```

3. Place your `best.pt` YOLO model and `15sec_input_720p.mp4` video in the root folder.

4. Run the script
```bash
python main.py
```

5. Output: Annotated video saved as `output_tracked.mp4`

### 📦 Dependencies
- Python >= 3.8
- OpenCV
- Ultralytics YOLOv8
- DeepSORT (via deep_sort_realtime)

---
