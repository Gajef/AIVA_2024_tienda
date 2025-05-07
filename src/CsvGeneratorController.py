import os
import pandas as pd
from datetime import datetime, timedelta

from CsvFile import CsvFile

class CsvGeneratorController:
    def __init__(self):
        pass

    def generate_csv(self, inference_data, video_filename="informe"):
        # Crear carpeta de salida si no existe
        output_dir = os.path.join("Videos", "Procesado")
        os.makedirs(output_dir, exist_ok=True)

        # Calcular horas estimadas
        start_time = datetime.strptime("08:00:00", "%H:%M:%S")
        timestamps = [
            start_time + timedelta(seconds=frame / 25)
            for frame, _ in inference_data
        ]
        personas = [count for _, count in inference_data]

        # Crear DataFrame por hora estimada
        df_horas = pd.DataFrame({
            "Hora estimada": [t.strftime("%H:%M:%S") for t in timestamps],
            "Personas acumuladas": personas
        }).groupby("Hora estimada").median()

        df_horas = df_horas.reset_index()

        df_horas['Personas acumuladas'] = df_horas['Personas acumuladas'].round().astype(int)

        # Guardar como CSV
        output_path = os.path.join(output_dir, f"{video_filename}_informe_por_hora.csv")
        df_horas.to_csv(output_path, index=False)

        generated_csv = CsvFile(output_path)

        print(f"📄 CSV generado en: {generated_csv.getPath()}")
        return generated_csv
