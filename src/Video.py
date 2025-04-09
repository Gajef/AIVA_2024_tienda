import cv2

class Video:
    def __init__(self, video_path: str):
        self.id = video_path.split("/")[-1]
        self.frames = self._load_frames(video_path)

    def _load_frames(self, path):
        cap = cv2.VideoCapture(path)
        frames = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)
        cap.release()
        return frames

    def getId(self):
        return self.id

    def getFrames(self):
        return self.frames
