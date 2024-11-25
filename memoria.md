# Memoria del proyecto

## Objetivos
En este proyecto se pretende construir un buscador de productos mediante número EAN, utilizando para ello algún modelo de inteligencia artificial. La solución debe incluir campos como el nombre del producto, 
descripción de este, imágenes si las hubiera, etc.Además, se deben crear varios bloques descriptivos generados por inteligencia artificial, los cuales den una descripción del producto de una manera más enfocada al marketing. 
Dichos bloques descriptivos serán utilizados más tarde para generar un HTML, el cual incluya también imágenes del producto si las hubiera.

## Propuesta
Para cumplir con los objetivos del proyecto, se han tomado varias decisiones en cuanto a arquitectura de la solución, que permitirán un desarrollo rápido y una mejor experiencia para el usuario.

### 1. Base de datos EAN
Para el buen desarrollo de este proyecto, es fundamental obtener buenos datos y de forma sencilla desde el primer momento, y es por ello que la base de datos es un pilar muy importante. Existen varias APIs que funcionarían, pero se
ha decidido utilizar UPCItemDB, por su sencillez y coste 0 para pequeñas cantidades de consultas. Quizás una mejora futura a añadir sería cambiar el tipo de base de datos utilizada, pero para la primera versión del proyecto, 
esta nos daba todos los campos necesarios para trabajar.
<br>

### 2. LlamaIndex
Debido a mi reciente experiencia utilizando agentes de IA y LlamaIndex, este será el framework que se va a utilizar para implementar la solución.

El agente incluye varias herramientas (funciones), que tendrá que usar para crear los archivos que necesita el proecto. Dichas funciones son:
- search_product: Se encarga de conectar con la API de UPCItemDB, tomando un numero EAN como input. A partir de la información obtenida se crea el archivo 'ean.json'. Este archivo no es creado mediante IA, porque de él dependen los demás
archivos que se crearán más tarde. Los campos que incluye son:
  ```json
  {
    "Title": ,
    "Description": ,
    "Category": ,
    "Images": ,
    "Brand": ,
    "Attributes": {
        "dimension": ,
        "weight": 
    }
  }
  ```

- descriptive_blocks: Lee los datos del archivo 'ean.json', y genera mediante IA 3 bloques descriptivos a partir de la información disponible. Dichos bloques también se guardan en un archivo 'blocks.json'.
Este es un ejemplo de dichos bloques:
  ```json
  {
    "Compact Powerhouse": "Experience music on-the-go with the JBL GO4 portable Bluetooth speaker. Ultra-portable, waterproof, and dustproof design for outdoor adventures. Multi-speaker connection for an immersive sound experience. Rechargeable battery with up to 7 hours of playtime.",
    "Seamless Connectivity": "Connect multiple devices effortlessly with Auracast technology. Use the JBL Portable APP for customized settings. Bluetooth 5.3 for seamless wireless connectivity up to 800 ft. Enjoy crystal-clear sound quality in a compact size.",
    "Stylish & Durable": "Available in multiple trendy colors, the JBL GO4 is a stylish accessory for any occasion. Water-resistant and built to last, this speaker is perfect for both indoor and outdoor use. Compact yet powerful sound performance."
  }
  ```

- create_HTML: crea un archivo HTML enfocado a vender el producto o darle un enfoque más comercial. Esto lo consigue utilizando también un modelo de IA dentro de la herramienta, en este caso un modelo que nos permita la mayor
creatividad posible.
<br>

### 3. Modelos de IA
Si hablamos de agentes de IA, que utilicen herramientas o llamadas externas, existen varios modelos de código abierto que podrían funcionar bien, aunque por el momento, OpenAI sigue siendo la opción a elegir si se quiere construir un agente
totalmente fiable. Es por ello que en este proyecto se utilizará en su mayoría el modelo `gpt-3.5-turbo`, salvo en ciertas ocasiones que requieran una mayor creatividad o desempeño, en los que se utilizará `gpt-4`. Todo ello haciendo
uso de la librería de LlamaIndex `llama-index-llms-openai`






