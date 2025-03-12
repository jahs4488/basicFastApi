# FastAPI Project

Este es un proyecto básico usando **FastAPI** para crear una API RESTful. Este README proporciona instrucciones para configurar y ejecutar el proyecto en tu máquina local usando JWT.

## Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes programas:

- **Python 3+**
- **pip** (gestor de paquetes de Python)

## Instalación

1. Clona el repositorio:

   ```
   git clone https://github.com/tu-usuario/tu-proyecto-fastapi.git
   cd tu-proyecto-fastapi
   ```

2. Crea un entorno virtual (opcional, pero recomendado):

    ```
    python3 -m venv env
    source env/bin/activate  # En macOS/Linux
    env\Scripts\activate     # En Windows
    ```

3. Instala las dependencias:
    - Para probar la API necesitarás un servidor web local. Uvicorn es un servidor web de interfaz de puerta de enlace de servidor asíncrono (ASGI) para Python. Instala uvicorn
    ```
    pip3 install uvicorn
    ```

    - Para actualizar todas las dependencias listadas en requirements.txt, usa:
    ```
    pip3 install --upgrade -r requirements.txt
    ```
    - Si no tienes un requirements.txt, puedes generarlo con:
    ```
    pip3 freeze > requirements.txt
    ```
    - Luego, ejecuta el comando para instalar todos los paquetes.
    ```
    pip install -r requirements.txt
    ```

4. Ejecuta el servidor:

    ```
    uvicorn main:app --reload
    ```

    Si presenta problemas con pip intenta con:
    ```
    python -m uvicorn main:app --reload
    ```
    Esto garantizará que el proyecto se ejecute con la misma versión de Python y que las dependencias estén instaladas correctamente.


# Documentación Interactiva

* FastAPI proporciona documentación interactiva automáticamente. Puedes acceder a ella en:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

Estas páginas te permiten probar los endpoints directamente desde el navegador.