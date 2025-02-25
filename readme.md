# API de Google Analytics 4 (GA4)

Este proyecto es una API construida con Flask que interactúa con la API de Google Analytics 4 (GA4) para obtener y procesar datos de informes.

## Requisitos

- Python 3.10 o superior
- Flask
- pandas
- google-auth
- google-analytics-data

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/api_GA4.git
    cd api_GA4
    ```

2. Crea un entorno virtual y actívalo:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # En Windows
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Configuración

1. Obtén las credenciales de servicio de Google Cloud y guarda el archivo JSON en una ubicación segura.
2. Asegúrate de que el archivo JSON de credenciales esté disponible y que su contenido se pueda cargar en una variable.

## Uso

### Ejecutar la aplicación

Para ejecutar la aplicación Flask, usa el siguiente comando:
```bash
python main.py