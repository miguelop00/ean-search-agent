# AI Agent for Product Search via EAN Number

This project introduces an assistant for product search using EANs (European Article Numbers). The goal is to showcase the ability to design and develop AI-based solutions using frameworks like LlamaIndex and generative models such as GPT-3.5-Turbo. Additionally, beyond the project's core requirements, a Telegram bot has been implemented to make communication with the agent as simple and user-friendly as possible.

## Using the Agent

To start using the agent, follow these steps:

1. Clone the GitHub repository:
   ```bash
   git clone https://github.com/miguelop00/ean-search-agent.git
   ```
2. Create and activate a virtual environment to install the project's dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. In the working directory (ean-search-agent), create a .env file to include the OpenAI and Telegram configuration fields:
   ```python
   #.env
   OPENAI_API_KEY = ''
   TELEGRAM_TOKEN = ''
   ```
   To obtain the Telegram token, the easiest way is through "Botfather." When you create a bot, it will guide you through the steps and provide a fully operational bot with its respective token.

4. Run the agent:
   ```bash
   python -m app.main
   ```

5. In a new terminal, run the Telegram bot:
   ```bash
   python -m telegram_bot.bot
   ```

Once the agent is running, you can send it messages via Telegram or alternatively through a local machine (localhost:8000) using FastAPI. As specified in the project requirements, the agent will provide a concise response related to the search, along with three files: ean.json, blocks.json, and descriptive_blocks.html.

- ean.json: Displays product information based on the fields provided by the UPCItemDB API, such as title, description, categories, etc.
- blocks.json: AI-generated descriptive blocks based on the data from the previous file. These blocks are more creative, aiming to advertise or market the product.
- descriptive_blocks.html: An HTML file created by AI using the information from the descriptive blocks.


## Usage examples
*El agente se ha construido en inglés en este caso, ya que los datos de UPCItemDB también se reciben en inglés

The two examples shown in this document were conducted using two different EANs:
- 0050036399302: JBL Go 4 Speaker
- 0791109269602: Apple MacBook Pro

In the first example, after sending the product's EAN as a message, the agent returns a concise response about the search along with the three files required by the project. It is also asked about a topic unrelated to product search, to which it responds correctly and concisely.
<br><br>
<div align="center">
  <figure>
     <img src="https://github.com/user-attachments/assets/28c780d1-3f79-4a3c-aab9-26a0ee2765b5" alt="movil jbl" width="250"/>
  </figure>
</div>
<br><br><br>

Examining the generated files reveals that they include all the information available in the UPCItemDB database. Note that if any fields are left blank, it is because they are not included in the database, as shown in the "Category" field. In the future, a tool could be implemented to generate missing fields using AI if any remain empty.

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

After generating the descriptive blocks, the agent creates the final HTML file. Below are two screenshots: one for EAN 0050036399302 (JBL Go 4 Speaker) and another for EAN 0791109269602 (Apple MacBook Pro). Both show that the LLM adds creativity to the display of the blocks, although some manual adjustments might be needed as the text-image blocks can vary in size and layout.

<br><br>
<div align="center">
  <figure>
     <img src="https://github.com/user-attachments/assets/4782478a-60fb-4737-bfa4-7e86d99d7245" alt="html jbl" width="350"/>
     <img src="https://github.com/user-attachments/assets/af9772d7-6416-47f6-b4cc-582a63e071e5" alt="html mac" width="368"/>
  </figure>
</div>
<br><br><br>
