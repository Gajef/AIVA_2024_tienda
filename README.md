# AIVA_2024: Sistema de conteo de personas en un centro comercial, frente a un local concreto

Este proyecto tiene como objetivo proporcionar una solución automatizada para el conteo de personas que pasan frente a la tienda de nuestro cliente, utilizando las grabaciones de video obtenidas de dos cámaras de vigilancia del centro comercial en el que se encuentra dicho local: una frontal y otra lateral.

El sistema se diseña para procesar los videos de cada jornada por la noche, extrayendo información relevante sobre el flujo de personas a lo largo del día. Mediante técnicas de visión artificial, identificaremos y contaremos los transeúntes en las grabaciones, generando un informe con los datos desglosados por hora y de ese día en agregado. Finalmente, estos resultados se enviarán automáticamente al dueño mediante un correo electrónico con un archivo CSV adjunto que contendrá dicha información.


# IMPECOUNT – Afluencia de Personas con Visión por Computador

Este proyecto desarrollado en Python utiliza visión por computador para contar personas que pasan frente a una tienda, usando vídeos de dos cámaras: una **frontal** y otra **lateral**. El sistema descarga los vídeos automáticamente desde un servidor SFTP, los procesa usando un modelo YOLO con seguimiento DeepSort, genera un informe `.csv` con la analítica por hora y lo envía por email.

---

## 📦 Requisitos del sistema

- **Python 3.10 o superior**
- Tarjeta **GPU (opcional pero recomendado)** para usar YOLO con CUDA

### 🔧 Bibliotecas necesarias

Puedes instalar todas las dependencias con:

```bash
pip install -r requirements.txt
```

Si no tienes el archivo `requirements.txt`, aquí tienes las principales dependencias manualmente:

```bash
pip install ultralytics
pip install opencv-python
pip install deep_sort_realtime
pip install pandas
pip install paramiko
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

## 📁 Estructura del proyecto

```
AIVA_2024_tienda/
│
├── main.py                       # Punto de entrada
├── ImpecountController.py       # Controlador principal del flujo
├── SFTPController.py            # Gestión de conexión y descarga desde servidor
├── VideoController.py           # Procesamiento y conteo con YOLO + DeepSort
├── CsvGeneratorController.py    # Generación de CSV con resultados
├── EmailController.py           # Envío de correo con el informe
├── Videos/                      # Carpeta con vídeos descargados y procesados
│   ├── frontal/
│   ├── lateral/
│   └── Procesado/                 
└── README.md
```

