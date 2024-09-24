"""
This is the main logic of the programm

"""
import base64
import requests


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
    

