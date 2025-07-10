### 🧠 Approach & Methodology
- A custom-trained YOLO model (`best.pt`) is used to detect players.
- DeepSORT is used for real-time tracking and re-identification.
- Bounding box IoU and appearance embeddings ensure players retain consistent IDs.

### 🔬 Techniques Tried
- **Naive IoU tracking:** Replaced due to ID mismatch.
- **DeepSORT:** Successful in maintaining player identity during occlusion and re-entry.
- **Confidence thresholding:** Filtered out false positives effectively.

### ⚠️ Challenges Encountered
- Maintaining player identity during full occlusion or frame exit was difficult with basic tracking.
- Required tuning `max_age` in DeepSORT to preserve IDs when players temporarily leave the frame.
- Class label filtering was needed due to multi-class detection capability of YOLO.

---

### ✅ Final Output
- Players entering, leaving, and re-entering the frame are assigned consistent IDs.
- `output_tracked.mp4` serves as a visual demonstration of successful re-identification.
