# Agente de IA para búsqueda de productos mediante número EAN

Este proyecto presenta un asistente de búsqueda de productos mediante números EAN (European Article Number). En él se ha querido reflejar la capacidad para diseñar y programar soluciones de inteligencia artificial, haciendo uso de frameworks como LlamaIndex y modelos generativos tales como gpt-3.5-turbo. Además, fuera de los requisitos del proyecto, se ha implementado un bot en Telegram para que la comunicación con el agente sea cuanto más sencilla y humana.

## Uso del agente

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

- ean.json: Muestra información de producto, atendiendo a los campos que incluye la API de UPCItemDB. Campos como título, descripción, categorías, etc.
- blocks.json: Bloques descriptivos generados por IA a partir de la información recibida en el archivo anterior. Estos bloques son más creativos, buscando un anuncio del producto o su venta.
- descriptive_blocks.html: Archivo HTML creado por IA a partir de la información de los bloques descriptivos.


## Ejemplos de uso
*El agente se ha construido en inglés en este caso, ya que los datos de UPCItemDB también se reciben en inglés

Los 2 ejemplos que muestro en este documento han sido llevados a cabo utilizando 2 números EAN diferentes:
- 0050036399302: Altavoz JBL Go 4
- 0791109269602: Apple MacBook Pro

En este primer ejemplo, se muestra como tras mandar como mensaje el numero EAN del producto, el agente devuelve una respuesta concisa en relación a la búsqueda, así como los 3 archivos requeridos por el proyecto:
<br><br>
<div align="center">
  <figure>
     <img src="https://github.com/user-attachments/assets/28c780d1-3f79-4a3c-aab9-26a0ee2765b5" alt="movil jbl" width="250"/>
  </figure>
</div>
<br><br><br>

Si echamos un vistazo a los archivos generados, podremos ver que incluyen toda la información disponible en la base de datos UPCItem. Cabe destacar que, si algún campo se ha dejado en blanco se debe a que no se incluye en dicha base de datos, como se puede observar en el campo "Category". Quizás en un futuro se podría implementar una nueva herramienta que genere mediante IA los campos restantes si alguno queda vacío.
<br><br>
<div align="center">
  <figure>
     <img src="https://github.com/user-attachments/assets/2ba92044-e40f-4440-b81b-c8068126a523" alt="ean jbl" width="400"/>
     <br>
     <img src="https://github.com/user-attachments/assets/ca6ce798-7618-43ac-88ad-681950ddd245" alt="blocks jbl" width="400"/>
  </figure>
</div>
<br><br><br>

Tras haber generado los bloques descriptivos, el agente crea el último archivo restante en HTML. En este caso se muestran 2 capturas, una referente al EAN 0050036399302: Altavoz JBL Go 4, y la segunda al 0791109269602: Apple MacBook Pro. En estas capturas podemos ver que el LLM muestra cierta creatividad en cuanto al display de los bloques, aunque requerirá de un estudio humano para su despliegue, ya que en alguna ocasión puede generar bloques de texto-imagen muy diferentes en tamaño y forma.

<br><br>
<div align="center">
  <figure>
     <img src="https://github.com/user-attachments/assets/4782478a-60fb-4737-bfa4-7e86d99d7245" alt="html jbl" width="400"/>
     <img src="https://github.com/user-attachments/assets/af9772d7-6416-47f6-b4cc-582a63e071e5" alt="html mac" width="420"/>
  </figure>
</div>
<br><br><br>

