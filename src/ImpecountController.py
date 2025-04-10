import argparse
from SFTPController import SFTPController
from VideoController import VideoController
from CsvGeneratorController import CsvGeneratorController
from EmailController import EmailController
from datetime import datetime, timedelta, time
import time


class ImpecountController:
    def __init__(self):
        self._arguments = self._parse_args()
        self._test_mode = self._arguments.test_mode
        self.sftp = SFTPController()
        self.video_processor = VideoController()
        self.csv_generator = CsvGeneratorController()
        self.email = EmailController(self._arguments.email)

    def run_daily_pipeline(self):
        print("[1] Obteniendo videos del servidor...")
        videos_path = self.sftp.retrieve_last_videos()
        '''
        print("[2] Procesando video frontal...")
        people_by_frame, processed_video_path = self.video_processor.count_people_frontal(videos_path[0])
        videos_path.append(processed_video_path)'''

        print("[2.1] Procesando video lateral...")
        people_by_frame, processed_video_path = self.video_processor.count_people_lateral(videos_path[1])
        videos_path.append(processed_video_path)

        print("[3] Generando CSV...")
        csv_path = self.csv_generator.generate_csv(people_by_frame)

        # Obtener la fecha del día anterior
        ayer = (datetime.now() - timedelta(days=1)).strftime("%d/%m/%Y")

        print("[4] Enviando email...")
        status = self.email.send_email(
            subject="Informe diario de afluencia",
            body=f"Analítica del día {ayer}",
            attachment_path=csv_path
        )

        if status == "OK":
            print("📩 Envío del informe completado con éxito.")
        else:
            print("⚠️ Hubo un problema al enviar el informe por email.")


        #self.video_processor.delete_videos(videos_path)
        return "✅ Proceso completo"

    def run(self):
        while True:
            now_time = datetime.now()
            if self._test_mode:
                retrieve_hour = now_time + timedelta(minutes=3)
            else:
                retrieve_hour = time(hour=23, minute=0, second=0)
            if now_time.hour == retrieve_hour.hour and now_time.minute == retrieve_hour.minute:
                self.run_daily_pipeline()
                time.sleep(60)
            else:
                time.sleep(30)

    def _parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--email", dest="email", type=str, help="Receiver email", required=True)
        parser.add_argument("--test", action="store_true", dest="test", help="Activate Test mode")
        args = parser.parse_args()
        return args