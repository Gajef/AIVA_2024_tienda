class Video:
    def __init__(self, video_path: str):
        self._path = video_path

    def getPath(self):
        return self._path
