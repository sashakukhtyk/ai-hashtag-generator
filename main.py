"""
This is the main logic of the programm

"""
import os
import base64
import requests
from dotenv import load_dotenv


# Load .env file with OpenAI API key
load_dotenv()


def encode_image(image_path):
    """
    This function takes path to the image and return a base64 version
    of it
    
    Args:
        image_path (str): path to the image

    Returns:
        str: base64
    """
    with open(image_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')
    

image_base64 = encode_image('images/test_image01.jpeg')

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.getenv("OPENAI_KEY")}'
}