# AIVA_2024: IMPECOUNT - Sistema de conteo de personas en un centro comercial, frente a un local concreto

Este proyecto tiene como objetivo proporcionar una solución automatizada para el conteo de personas que pasan frente a la tienda de nuestro cliente, utilizando las grabaciones de video obtenidas de dos cámaras de vigilancia del centro comercial en el que se encuentra dicho local: una frontal y otra lateral.

El sistema se diseña para procesar los videos de cada jornada por la noche, extrayendo información relevante sobre el flujo de personas a lo largo del día. Mediante técnicas de visión artificial, identificaremos y contaremos las personas que pasan de las grabaciones, generando un informe con los datos desglosados por hora y de ese día en agregado. Finalmente, estos resultados se enviarán automáticamente al dueño mediante un correo electrónico con un archivo CSV adjunto que contendrá dicha información.

---

## 📦 Requisitos del sistema

- **Python 3.10 o superior**
- Tarjeta **GPU (opcional pero recomendado)** para usar YOLO con CUDA

### 🔧 Bibliotecas necesarias

Puedes instalar todas las dependencias con:

```bash
pip install -r requirements.txt
```

---

## 🔄 Clonar el repositorio

```bash
git clone https://github.com/Gajef/AIVA_2024_tienda.git
cd AIVA_2024_tienda
```

---

## 🚀 Cómo ejecutar el proyecto

Una vez tengas instaladas las dependencias y hayas clonado el proyecto, puedes ejecutar el sistema así:

```bash
python main.py --email tu_correo@ejemplo.com
```

---

## 🧪 Ejemplo de ejecución

```bash
python main.py --email usuario@ejemplo.com
```

Esto hará lo siguiente:

1. Se conecta al servidor SFTP.
2. Descarga el último vídeo de la cámara **frontal** y **lateral**.
3. Procesa el vídeo lateral (o frontal, si se descomenta).
4. Genera un `.csv` con las personas acumuladas por hora.
5. Envía el CSV por correo electrónico.
6. Elimina los vídeos locales.

---

## 🧪 Ejecución de tests

Para verificar que el sistema de detección funciona correctamente, se incluyen tests automatizados para vídeos con y sin personas.

Para ejecutarlos, simplemente se ejecuta en terminal:

```bash
python -m unittest test/TestVideoController.py
```

Esto ejecuta los siguientes tests:

- **test_video_with_people_detected**: Verifica que un vídeo con personas sea detectado correctamente.
- **test_video_without_people_detected**: Verifica que no se detecten personas en un vídeo vacío.

---

## 📁 Estructura del proyecto

```
AIVA_2024_tienda/
│
├── src/
│   ├── CsvFile.py                  # Clase axiliar para el tipo de objeto CSV
│   ├── CsvGeneratorController.py   # Controlador para generar CSVs con resultados
│   ├── EmailController.py          # Envío de correos con informes
│   ├── Impecount.py                # Clase que lanza el software
│   ├── ImpecountController.py      # Controlador general del proceso entero
│   ├── SFTPController.py           # Gestión de conexión y descarga desde servidor
│   ├── Video.py                    # Clase auxiliar para manejar vídeos
│   ├── VideoController.py          # Procesamiento de vídeo y detección con YOLO
│   ├── Videos/                     # Carpeta para guardar vídeos descargados
│
├── test/
│   ├── TestVideoController.py      # Tests para el módulo de vídeo
│   ├── Video con personas test.mp4 # Vídeo de prueba con personas
│   ├── Video test sin personas.mp4 # Vídeo de prueba sin personas
│   └── Videos/                     # Carpeta para posibles vídeos procesados
│
├── README.md                       # Documentación general del proyecto
└── requirements.txt                # Dependencias del proyecto

```

