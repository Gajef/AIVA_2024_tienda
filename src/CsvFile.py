class CsvFile:
    def __init__(self, csv_path: str):
        self.id = csv_path.split("/")[-1]
        with open(csv_path, "r") as f:
            self.content = f.read()

    def getId(self):
        return self.id

    def getContent(self):
        return self.content
