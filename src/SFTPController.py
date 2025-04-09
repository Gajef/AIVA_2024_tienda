import paramiko
import os

class SFTPController:
    def __init__(self):
        self.host = "212.128.3.86"
        self.port = 22
        self.username = "alumno_redes"
        self.password = "TomateVolador"
        self.remote_base_path = "videos_cc"
        self.local_base_path = "Videos"
        self.subdirs = ["frontal", "lateral"]

    def _connect(self):
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        return sftp

    def retrieve_last_videos(self):
        sftp = self._connect()
        downloaded_paths = []

        for subdir in self.subdirs:
            remote_dir = f"{self.remote_base_path}/{subdir}"
            local_dir = os.path.join(self.local_base_path, subdir)
            os.makedirs(local_dir, exist_ok=True)

            files = sftp.listdir(remote_dir)
            if not files:
                print(f"No hay archivos en {remote_dir}")
                continue

            files = sorted(files, reverse=True)
            latest_file = files[0]

            remote_path = os.path.join(remote_dir, latest_file)
            local_path = os.path.join(local_dir, latest_file)

            print(f"Descargando {remote_path} → {local_path}")
            sftp.get(remote_path, local_path)
            downloaded_paths.append(local_path)

        sftp.close()
        return downloaded_paths
