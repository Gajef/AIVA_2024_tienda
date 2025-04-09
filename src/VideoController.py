from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
import cv2
import torch
import time
import pandas as pd
import os

class VideoController:
    def __init__(self):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = YOLO("yolo11x.pt").to(self.device)
        self.tracker = DeepSort(max_age=30)
        self.target_class = 0

    def count_people_frontal(self, video_path: str):
        FRAME_WIDTH = 384
        FRAME_HEIGHT = 288
        line_x = FRAME_WIDTH // 2

        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        output_filename = os.path.basename(video_path)
        output_path = os.path.join(r"C:\Users\josem\PycharmProjects\AIVA_2024_tienda\Videos\Procesado",
                                   f"procesado_{output_filename}.avi")
        out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'MJPG'), fps, (FRAME_WIDTH, FRAME_HEIGHT))

        count_right, count_left = set(), set()
        track_memory = {}
        frame_counter = 0
        unique_ids = set()
        people_by_frame = []

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
                cy = int((t + b) / 2)

                # Dibujo
                cv2.rectangle(frame, (int(l), int(t)), (int(r), int(b)), (0, 255, 0), 1)
                cv2.putText(frame, f'ID: {track_id}', (int(l), int(t) - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
                cv2.circle(frame, (cx, cy), 4, (0, 255, 255), -1)

                prev_cx = track_memory.get(track_id, None)
                if prev_cx is not None:
                    if prev_cx < line_x and cx >= line_x:
                        count_right.add(track_id)
                    elif prev_cx > line_x and cx <= line_x:
                        count_left.add(track_id)

                track_memory[track_id] = cx
                unique_ids.add(track_id)

            # Métricas y línea
            cv2.line(frame, (line_x, 0), (line_x, FRAME_HEIGHT), (0, 0, 255), 2)
            cv2.putText(frame, f'Left to Right: {len(count_right)}', (10, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            cv2.putText(frame, f'Right to Left: {len(count_left)}', (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            people_by_frame.append((frame_counter, len(count_left.union(count_right))))
            frame_counter += 1
            out.write(frame)

        cap.release()
        out.release()

        print(f"➡️ Video procesado: {output_path}")
        return people_by_frame, output_path

    def count_people_lateral(self, video_path: str):
        FRAME_WIDTH = 384
        FRAME_HEIGHT = 288
        line_y = 2 * FRAME_HEIGHT // 3  # Línea horizontal baja (parte inferior del frame)

        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        output_filename = os.path.basename(video_path)
        output_path = os.path.join(r"C:\Users\josem\PycharmProjects\AIVA_2024_tienda\Videos\Procesado",
                                   f"procesado_lateral_{output_filename}.avi")
        out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'MJPG'), fps, (FRAME_WIDTH, FRAME_HEIGHT))

        count_down, count_up = set(), set()
        track_memory = {}
        frame_counter = 0
        unique_ids = set()
        people_by_frame = []

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
                cx = int((l + r) // 2)
                cy = int((t + b) // 2)

                # Dibujo
                cv2.rectangle(frame, (int(l), int(t)), (int(r), int(b)), (0, 255, 0), 1)
                cv2.putText(frame, f'ID: {track_id}', (int(l), int(t) - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
                cv2.circle(frame, (cx, cy), 4, (0, 255, 255), -1)

                prev_cy = track_memory.get(track_id, None)
                if prev_cy is not None:
                    if prev_cy < line_y and cy >= line_y:
                        count_down.add(track_id)
                    elif prev_cy > line_y and cy <= line_y:
                        count_up.add(track_id)

                track_memory[track_id] = cy
                unique_ids.add(track_id)

            # Métricas y línea horizontal baja
            cv2.line(frame, (0, line_y), (FRAME_WIDTH, line_y), (0, 0, 255), 2)
            cv2.putText(frame, f'Up to Down: {len(count_down)}', (10, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            cv2.putText(frame, f'Down to Up: {len(count_up)}', (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            people_by_frame.append((frame_counter, len(count_up.union(count_down))))
            frame_counter += 1
            out.write(frame)

        cap.release()
        out.release()

        print(f"➡️ Video procesado: {output_path}")
        return people_by_frame, output_path

    def delete_videos(self, videos_path):
        for path in videos_path:
            try:
                os.remove(path)
                print(f"✅ Eliminado: {path}")
            except FileNotFoundError:
                print(f"⚠️ No se encontró: {path}")
            except PermissionError:
                print(f"❌ Sin permisos para: {path}")
            except Exception as e:
                print(f"❌ Error con {path}: {e}")
        return "Eliminados"