import os
import pandas as pd
from datetime import datetime, timedelta

class CsvGeneratorController:
    def __init__(self):
        pass

    def generate_csv(self, inference_data, video_filename="informe"):
        # Crear carpeta de salida si no existe
        output_dir = os.path.join("Videos", "Procesado")
        os.makedirs(output_dir, exist_ok=True)

        # Crear DataFrame por frame
        df_frames = pd.DataFrame(inference_data, columns=["Frame", "Personas acumuladas"])

        # Crear DataFrame por hora estimada
        start_time = datetime.strptime("08:00:00", "%H:%M:%S")
        timestamps = [
            start_time + timedelta(seconds=frame / 25)
            for frame, _ in inference_data
        ]
        personas = [count for _, count in inference_data]
        df_horas = pd.DataFrame({
            "Hora estimada": [t.strftime("%H:%M:%S") for t in timestamps],
            "Personas acumuladas": personas
        })

        # Guardar en Excel con dos hojas
        output_path = os.path.join(output_dir, f"{video_filename}_informe.xlsx")
        with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
            df_frames.to_excel(writer, index=False, sheet_name="Por Frame")
            df_horas.to_excel(writer, index=False, sheet_name="Por Hora")

        print(f"📄 CSV generado en: {output_path}")
        return output_path
