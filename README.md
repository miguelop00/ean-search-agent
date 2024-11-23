# Agente de IA para búsqueda de productos mediante número EAN

Este proyecto presenta un asistente de búsqueda de productos mediante números EAN (European Article Number). En él se ha querido reflejar la capacidad para diseñar y programar soluciones de inteligencia artificial, haciendo uso de frameworks como LlamaIndex y modelos generativos tales como gpt-3.5-turbo. Además, fuera de los requisitos del proyecto, se ha implementado un bot en Telegram para que la comunicación con el agente sea cuanto más sencilla y humana.

### Uso del agente

Para empezar a utilizar el agente, se deben seguir los siguientes pasos:
1. Crear y activar un entorno virtual, para instalar los requerimientos del proyecto:
`pip install -r requirements.txt`
2. En el directorio de trabajo (ean-search-agent), crear un archivo .env en el cual se incluirán los campos de configuración de OpenAI y de Telegram:
   ```python
   #.env
   OPENAI_API_KEY = ''
   TELEGRAM_TOKEN = ''
   ```
3. Ejecutar el agente: `python -m app.main`
4. En un nuevo terminal, ejecutar el bot de telegram: `python -m telegram_bot.bot`

Una vez el agente está en funcionamiento, se le podrá mandar un mensaje mediante Telegram, o en su defecto a través de una máquina local (localhost:8000) usando FastAPI. Como se especifica en los requisitos del proyecto, el agente devolverá una respuesta concisa respecto a la búsqueda, así como 3 archivos: ean.json, blocks.json y descriptive_blocks.html.


