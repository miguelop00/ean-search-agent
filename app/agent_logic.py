from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool
from llama_index.core.agent import FunctionCallingAgentWorker, AgentRunner
import nest_asyncio
import requests
import json
import os
from dotenv import load_dotenv
nest_asyncio.apply()


load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')


agent_prompt = """
    You work as a product search engine. The client will send you a question that should include the EAN reference number of a product, for example: 0458379287465. Use the tools available to process 
    the search in an efficient and trustful way.
    
    To consider your job finished, you will have to do 3 tasks with the provided EAN number:
    1. Search the product: use search_product() to retrieve information about the product by calling an external API.
    2. Create marketing descriptive blocks: use descriptive_blocks() to generate creative information about the product.
    3. From the data aquired at previous stages, create a HTML file, showing the descriptive blocks in a creative way.

    If the query includes an EAN number, you should communicate with the client to say that something went wrong with the query, or to present it's success. A good response would be:
    'The search for the product with the EAN number 0850036393302 was successful. The product is the Samsung Galaxy S23 in Black. For more detailed information, 
    please refer to the structured data and descriptive blocks files.'

    If the query doesn't include a number, then try to help the client in the best way possible, without going out of scope of your duties (EAN numbers search).
    """


def search_product(ean_number):
    """This function takes as input an EAN number 13 characters long, and calls an external API to process the product search. Be aware that, if the number starts with one
    or more zeros (0), they should stay. So if the message includes 0053426546357, the input of the function should be 0053426546357"""

    # UPCitemDB API 
    api_url = f"https://api.upcitemdb.com/prod/trial/lookup?upc={ean_number}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_KEY"
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        product_info = response.json()

        data = {
            "Title": product_info['items'][0]['title'],
            "Description": product_info['items'][0]['description'],
            "Category": product_info['items'][0]['category'],
            "Images": product_info['items'][0]['images'],
            "Brand": product_info['items'][0]['brand'],
            "Attributes": {
                "dimension": product_info['items'][0]['dimension'],
                "weight": product_info['items'][0]['weight']
            }
        }

        with open('docs\\ean.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        return data
    else:
        print(f"Error: {response.status_code}, {response.text}")


def descriptive_blocks():
    """This function takes data from the ean.json document and creates descriptive blocks about the product, in a more marketing-like way."""
    
    with open('docs\\ean.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    prompt = f"""
    You are a creative product marketer. Given the following product data, generate descriptive blocks with a creative title and description for each block:

    Product Data:
    Title: {data.get('Title')}
    Description: {data.get('Description')}
    Brand: {data.get('Brand')}
    Attributes: {data.get('Attributes')}

    Each block should have:
    1. A creative title (less than 10 words).
    2. A descriptive paragraph about the product, highlighting its features and benefits. No more than 40 words.
    
    Create 3 blocks. Create them in a Python dictionary format, using the title as key and the description as item.
    """
    llm = OpenAI(api_key=OPENAI_API_KEY, model="gpt-3.5-turbo", temperature=0.7,)
    response = llm.complete(prompt)
    response_data = json.loads(response.text)
    with open('docs\\blocks.json', 'w', encoding='utf-8') as file:
        json.dump(response_data, file, ensure_ascii=False, indent=4)
    return response


def create_HTML(descriptive_blocks, images:list):
    """This function creates an HTML file using as an input the descriptive blocks information in dictionary format and the images retrieved from the product search in a list format."""

    prompt = f"""
    I want to create an HTML layout for displaying product or service information in a marketing-focused style. 
    It should have sections for a title, description, and image, presented in an alternating layout for visual variety.

    Each block should contain:
    - A title (H2), coming from {descriptive_blocks}.
    - A description (paragraph), coming from {descriptive_blocks} respectively.
    - An image (on either the left or right side, alternating per section), coming from {images}. If there are not enough images, change the format of the HTML in accordance.
    
    The design should be modern and creative, with:
    - Rounded corners for images.
    - Drop shadows around each block.
    - Modern and creative fonts, that give a clean vision of the product.
    - A modern layout that adjusts for the vertical mobile devices.
    - Images must fit in the layout and not be truncated. Re-size them if needed.

    Please generate the HTML and CSS for this design.

    Be aware that this response will go directly to a HTML file, so only include the code in your response, there's no need of interaction with the user.
    """

    llm = OpenAI(api_key=OPENAI_API_KEY, model="gpt-4o", temperature=0.7)
    response = llm.complete(prompt)
    clean_response = response.text.replace("```html", "").replace("```", "").strip()
    with open('docs\\descriptive_blocks.html', 'w', encoding='utf-8') as file:
        file.write(clean_response)
    return response


def send_message_to_telegram(message:str, user_id:str):

    bot_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        'chat_id': user_id,
        'text': message
    }

    response = requests.post(bot_url, data=data)
    if response.status_code != 200:
        print(f"Error al enviar mensaje a Telegram: {response.status_code}, {response.text}")


def send_files_to_telegram(path:str, user_id:str):

    bot_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument"

    file_paths = [
        os.path.join(path, 'ean.json'),
        os.path.join(path, 'blocks.json'),
        os.path.join(path, 'descriptive_blocks.html')
    ]

    for file_path in file_paths:
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write("")
    
    file1 = open(file_paths[0], 'rb')
    file2 = open(file_paths[1], 'rb')
    file3 = open(file_paths[2], 'rb')

    data = {'chat_id': user_id}

    response1 = requests.post(bot_url, data=data, files={'document': file1})

    response2 = requests.post(bot_url, data=data, files={'document': file2})

    response3 = requests.post(bot_url, data=data, files={'document': file3})
    
    file1.close()
    file2.close()
    file3.close()



async def run_agent_logic(message, user_id):
    search_product_tool = FunctionTool.from_defaults(fn=search_product)
    descriptive_blocks_tool = FunctionTool.from_defaults(fn=descriptive_blocks)
    create_HTML_tool = FunctionTool.from_defaults(fn=create_HTML)

    llm = OpenAI(api_key=OPENAI_API_KEY, model="gpt-3.5-turbo", temperature=0.1)
    agent_worker = FunctionCallingAgentWorker.from_tools(
        tools=[search_product_tool, descriptive_blocks_tool, create_HTML_tool], 
        system_prompt=agent_prompt,
        llm=llm, 
        verbose=True,
    )

    agent = AgentRunner(agent_worker)

    response = agent.chat(message)

    send_message_to_telegram(response, user_id)
    send_files_to_telegram('docs',user_id=user_id)