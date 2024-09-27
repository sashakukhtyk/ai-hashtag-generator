"""
This is Flask app that help to generate hashtags from images
"""
import os 
import base64

import requests
from dotenv import load_dotenv
from flask import Flask, request, render_template, jsonify


load_dotenv()

app = Flask(__name__)


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
    
    
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        pass
    return render_template('index.html')