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
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        image = request.files["image"]
        image.save("tmp.png")

        image_base64 = encode_image("tmp.png")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f'Bearer {os.getenv("OPENAI_KEY")}',
        }

        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "system",
                    "content": """You are a hashtag generation model. 
                    When you get an image as input, your response 
                    should always contain exactly 
                    30 hashtags separated by commas.""",
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": """Provide the hashtags 
                            for this image:""",
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"""data:image/jpeg;base64,
                                           {image_base64}"""
                            },
                        },
                    ],
                },
            ],
            "max_tokens": 300,
        }

        response = requests.post(
            "https://api.openai.com/v1/chat/completions", 
            headers=headers, 
            json=payload
        )

        hashtags = (
            response.json()
            .get("choices")[0]
            .get("message")
            .get("content")
            .split(",")
        )

        return render_template(
            "index.html", 
            hashtags=hashtags, 
            image_base64=image_base64
        )

    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5556)