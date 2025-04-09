import paramiko
import os

class SFTPController:
    def __init__(self):
        self.host = "212.128.3.86"
        self.port = 22
        self.username = "alumno_redes"
        self.password = "TomateVolador"
        self.remote_path = "videos_cc"

    def _connect(self):
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        return sftp

    def retrieve_last_video(self):
        sftp = self._connect()
        files = sftp.listdir(self.remote_path)
        files = sorted(files, reverse=True)
        latest = files[0]
        local_path = os.path.join("Videos", latest)
        sftp.get(os.path.join(self.remote_path, latest), local_path)
        sftp.close()
        return local_path
