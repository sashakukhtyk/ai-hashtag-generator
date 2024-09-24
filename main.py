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
    

# Call the image function and store it into the variable
image_base64 = encode_image('images/test_image01.jpeg')

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.getenv("OPENAI_KEY")}'
}

payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "system",
                    "content": """You are a hashtag generation model. 
                    When you get an image as input, your response 
                    should always contain exactly 
                    30 hashtags separated by commas."""
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": """Provide the hashtags 
                            for this image:"""
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"""data:image/jpeg;base64,
                                           {image_base64}"""
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 300
        }