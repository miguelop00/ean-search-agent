# Agente de IA para búsqueda de productos mediante número EAN

Este proyecto presenta un asistente de búsqueda de productos mediante números EAN (European Article Number). En él se ha querido reflejar la capacidad para diseñar y programar soluciones de inteligencia artificial, haciendo uso de frameworks como LlamaIndex y modelos generativos tales como gpt-3.5-turbo. Además, fuera de los requisitos del proyecto, se ha implementado un bot en Telegram para que la comunicación con el agente sea cuanto más sencilla y humana.

## Uso del agente

Para empezar a utilizar el agente, se deben seguir los siguientes pasos:
1. Clonar el respositorio de Github:
   ```bash
   git clone https://github.com/miguelop00/ean-search-agent.git
   ```
2. Crear y activar un entorno virtual, para instalar los requerimientos del proyecto:
   ```bash
   pip install -r requirements.txt
   ```
3. En el directorio de trabajo (ean-search-agent), crear un archivo .env en el cual se incluirán los campos de configuración de OpenAI y de Telegram:
   ```python
   #.env
   OPENAI_API_KEY = ''
   TELEGRAM_TOKEN = ''
   ```
   Para conseguir el token de Telegram, la manera más sencilla es utilizando "Botfather". Al crear un bot, él mismo dará los pasos a seguir y creará un bot totalmente operativo con su respectivo token.
4. Ejecutar el agente: `python -m app.main`
5. En un nuevo terminal, ejecutar el bot de telegram: `python -m telegram_bot.bot`

Una vez el agente está en funcionamiento, se le podrá mandar un mensaje mediante Telegram, o en su defecto a través de una máquina local (localhost:8000) usando FastAPI. Como se especifica en los requisitos del proyecto, el agente devolverá una respuesta concisa respecto a la búsqueda, así como 3 archivos: ean.json, blocks.json y descriptive_blocks.html.

- ean.json: Muestra información de producto, atendiendo a los campos que incluye la API de UPCItemDB. Campos como título, descripción, categorías, etc.
- blocks.json: Bloques descriptivos generados por IA a partir de la información recibida en el archivo anterior. Estos bloques son más creativos, buscando un anuncio del producto o su venta.
- descriptive_blocks.html: Archivo HTML creado por IA a partir de la información de los bloques descriptivos.


## Ejemplos de uso
*El agente se ha construido en inglés en este caso, ya que los datos de UPCItemDB también se reciben en inglés

Los 2 ejemplos que muestro en este documento han sido llevados a cabo utilizando 2 números EAN diferentes:
- 0050036399302: Altavoz JBL Go 4
- 0791109269602: Apple MacBook Pro

En este primer ejemplo, se muestra como tras mandar como mensaje el numero EAN del producto, el agente devuelve una respuesta concisa en relación a la búsqueda, así como los 3 archivos requeridos por el proyecto. También se le pregunta sobre un tema distinto a la búsqueda de productos, a lo que responde de forma correcta y concisa.
<br><br>
<div align="center">
  <figure>
     <img src="https://github.com/user-attachments/assets/28c780d1-3f79-4a3c-aab9-26a0ee2765b5" alt="movil jbl" width="250"/>
  </figure>
</div>
<br><br><br>

Si echamos un vistazo a los archivos generados, podremos ver que incluyen toda la información disponible en la base de datos UPCItem. Cabe destacar que, si algún campo se ha dejado en blanco se debe a que no se incluye en dicha base de datos, como se puede observar en el campo "Category". Quizás en un futuro se podría implementar una nueva herramienta que genere mediante IA los campos restantes si alguno queda vacío.

<br>

*ean.json*

```json
{
    "Title": "JBL - Go 4 Portable Bluetooth Speaker - Blue",
    "Description": "Listen to your music anywhere with this JBL GO4 ultra-portable Bluetooth speaker.FEATURES Fits into the palm of your hand Waterproof and dustproof design Multi-speaker connection by Auracast JBL Portable APPWHAT'S INCLUDED JBL GO4, USB Type C Cable, quick start guide, warranty cardDETAILS 3\"H x 3.7\"W x 1.7\"D Weight: 0.42 lbs. Rechargeable lithium ion battery Battery life: up to 7 hours Battery charge time: 3 hours Wireless: Bluetooth 5.3 Wireless range: up to 800 ft. Speaker side: 1.75-in. Water resistant up to 1 meter Manufacturer's 1-year limited warranty: For warranty information please click here Model no. JBLGO4BLUAM, JBLGO4WHTAM, JBLGO4PURAM, JBLGO4BLKAM, JBLGO4SQUADAM, JBLGO4REDAM Imported WARNING: This product may contain a chemical known to the state of California to cause cancer, birth defects or other reproductive harm. For more information go to www.P65Warnings.ca.gov. Gift Givers: This item ships in its original packaging. If intended as a gift, the packaging may reveal the contents. Size: One S",
    "Category": "",
    "Images": [
        "https://media.kohlsimg.com/is/image/kohls/7002490_Blue?wid=800&hei=800&op_sharpen=1",
        "https://images.thdstatic.com/productImages/3a93e032-1520-419e-9198-1450294591ab/svn/blue-jbl-portable-audio-video-jblgo4bluam-64_1000.jpg",
        "https://pisces.bbystatic.com/prescaled/500/500/image2/BestBuy_US/images/products/6583/6583088_sd.jpg",
        "https://target.scene7.com/is/image/Target/GUEST_90bb2abc-2e9b-46af-9f9f-a945bc61e2d9?wid=1000&hei=1000",
        "https://www.jbl.com/dw/image/v2/BFND_PRD/on/demandware.static/-/Sites-masterCatalog_Harman/default/dw3839dbd9/JBL_GO_4_HERO_BLUE_48170_x6.png?sw=1600&sh=1600&sm=fit",
        "https://snpi.dell.com/snp/bysku/images2/400/ad075175.jpg",
        "https://ss7.vzw.com/is/image/VerizonWireless/jblgo4bluam-iset?wid=700&hei=700&fmt=webp",
        "https://www.brandsmartusa.com/syndigo/images/product/detail/3d7467de-74ad-471f-9942-b948c3f00791.webp"
    ],
    "Brand": "JBL",
    "Attributes": {
        "dimension": "",
        "weight": "1 lbs"
    }
}
```
<br>

*blocks.json*

```json
{
    "Compact Powerhouse": "Experience music on-the-go with the JBL GO4 portable Bluetooth speaker. Ultra-portable, waterproof, and dustproof design for outdoor adventures.Multi-speaker connection for an immersive sound experience. Rechargeable battery with up to 7 hours of playtime.",
    "Seamless Connectivity": "Connect multiple devices effortlessly with Auracast technology. Use the JBL Portable APP for customized settings. Bluetooth 5.3 for seamless wireless connectivity up to 800 ft. Enjoy crystal-clear sound quality in a compact size.",
    "Stylish & Durable": "Available in multiple trendy colors, the JBL GO4 is a stylish accessory for any occasion. Water-resistant and built to last, this speaker is perfect for both indoor and outdoor use. Compact yet powerful sound performance."
}
```

<br><br>

Tras haber generado los bloques descriptivos, el agente crea el último archivo restante en HTML. En este caso se muestran 2 capturas, una referente al EAN 0050036399302: Altavoz JBL Go 4, y la segunda al 0791109269602: Apple MacBook Pro. En estas capturas podemos ver que el LLM muestra cierta creatividad en cuanto al display de los bloques, aunque requerirá de un estudio humano para su despliegue, ya que en alguna ocasión puede generar bloques de texto-imagen muy diferentes en tamaño y forma.

<br><br>
<div align="center">
  <figure>
     <img src="https://github.com/user-attachments/assets/4782478a-60fb-4737-bfa4-7e86d99d7245" alt="html jbl" width="350"/>
     <img src="https://github.com/user-attachments/assets/af9772d7-6416-47f6-b4cc-582a63e071e5" alt="html mac" width="368"/>
  </figure>
</div>
<br><br><br>

