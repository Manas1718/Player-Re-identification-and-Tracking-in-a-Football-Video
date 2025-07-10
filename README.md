# Player-Re-identification-and-Tracking-in-a-Football-Video
This project demonstrates real-time player detection, tracking, and re-identification in a 15-second football video. It uses a custom-trained YOLO object detection model and DeepSORT tracker to ensure that players who go out of frame and reappear are consistently assigned the same identity.

### ⚙️ Setup Instructions
1. Clone the repository
```bash
git clone https://github.com/Manas1718/Player-Re-identification-and-Tracking-in-a-Football-Video.git
cd Player-Re-identification-and-Tracking-in-a-Football-Video
```

2. Install dependencies
```bash
pip install ultralytics opencv-python deep_sort_realtime
```

3. Download the trained YOLO model `best.pt` from the following Google Drive link and place it in the root folder:
[Download best.pt](https://drive.google.com/file/d/1-5fOSHOSB9UXyP_enOoZNAMScrePVcMD/view)

4. Place your `15sec_input_720p.mp4` video in the same folder.

5. Make sure `best.pt` is not tracked by Git:
   - Add this to `.gitignore`:
     ```
     best.pt
     ```
   - If it was already committed:
     ```bash
     git rm --cached best.pt
     git commit -m "Ignore best.pt in .gitignore"
     ```

6. Run the script
```bash
python main.py
```

7. Output: Annotated video saved as `output_tracked.mp4`

### 📦 Dependencies
- Python >= 3.8
- OpenCV
- Ultralytics YOLOv8
- DeepSORT (via deep_sort_realtime)

---

