# STEP 1: Install dependencies
!pip install ultralytics opencv-python deep_sort_realtime

# STEP 2: Upload video and model
from google.colab import files
print("Upload your video (15sec_input_720p.mp4) and model (best.pt)")
uploaded = files.upload()

# STEP 3: Load YOLO model and DeepSORT tracker
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
import cv2

model = YOLO("best.pt")  # Custom trained YOLO model
tracker = DeepSort(max_age=30)

# STEP 4: Open input video and prepare output
input_video = "15sec_input_720p.mp4"
cap = cv2.VideoCapture(input_video)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output_tracked.mp4", fourcc, fps, (width, height))

# STEP 5: Run detection + tracking
while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]
    detections = []

    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        if label == "player":  # Change this if your label differs
            detections.append(([x1, y1, x2 - x1, y2 - y1], conf, None))

    tracks = tracker.update_tracks(detections, frame=frame)

    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        x1, y1, x2, y2 = map(int, track.to_ltrb())
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f'ID {track_id}', (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()

# STEP 6: Download output
files.download("output_tracked.mp4")
