from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
import cv2
import torch
import time
import pandas as pd
import os

class ProcessVideoController:
    def __init__(self):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = YOLO("yolo11x.pt")
        self.model.to(self.device)
        self.tracker = DeepSort(max_age=30)
        self.target_class = 0

    def count_people(self, video_path: str):
        FRAME_WIDTH = 384
        FRAME_HEIGHT = 288
        line_x = FRAME_WIDTH // 2

        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        out = cv2.VideoWriter(f"procesado_{os.path.basename(video_path)}.avi",
                              cv2.VideoWriter_fourcc(*'MJPG'), fps, (FRAME_WIDTH, FRAME_HEIGHT))

        count_right, count_left = set(), set()
        track_memory, tracking_log = {}, []
        frame_counter = 0
        start_time = time.time()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))
            results = self.model(frame, classes=[self.target_class], device=self.device)[0]

            detections = []
            for box in results.boxes:
                if int(box.cls[0]) != self.target_class:
                    continue
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf[0])
                detections.append(([x1, y1, x2 - x1, y2 - y1], conf, 'person'))

            tracks = self.tracker.update_tracks(detections, frame=frame)

            for track in tracks:
                if not track.is_confirmed():
                    continue
                track_id = track.track_id
                l, t, r, b = track.to_ltrb()
                cx = int((l + r) / 2)
                prev_cx = track_memory.get(track_id, None)

                if prev_cx is not None:
                    if prev_cx < line_x and cx >= line_x:
                        count_right.add(track_id)
                    elif prev_cx > line_x and cx <= line_x:
                        count_left.add(track_id)

                track_memory[track_id] = cx
                tracking_log.append({"frame": frame_counter, "track_id": track_id, "cx": cx})

            frame_counter += 1
            out.write(frame)

        cap.release()
        out.release()

        df = pd.DataFrame(tracking_log)
        csv_path = f"tracking_{os.path.basename(video_path)}.csv"
        df.to_csv(csv_path, index=False)

        info = f"Left to Right: {len(count_right)} | Right to Left: {len(count_left)}"
        print(info)
        return info, csv_path
