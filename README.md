# Hashtag Generator from Images

This is a simple Flask application that generates hashtags based on the content of an uploaded image. The application leverages OpenAI's API to analyze the image and return a list of relevant hashtags.

## Features
- Upload an image and get 30 hashtags based on the content of the image.
- Uses OpenAI's GPT model for image processing and hashtag generation.
- Simple web interface for image uploads.

## Installation

### Prerequisites
- Python 3.x
- pip (Python package manager)
- OpenAI API key

### Steps to Set Up

1. **Clone the repository**:
    ```bash
    git clone https://github.com/sashakukhtyk/ai-hashtag-generator.git
    cd hashtag-generator
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root of your project and add your OpenAI API key:
    ```bash
    OPENAI_KEY=your_openai_api_key
    ```

5. **Run the application**:
    ```bash
    python app.py
    ```

6. Open your browser and navigate to `http://localhost:5556/` to use the app.

## Usage

1. On the homepage, you can upload an image file.
2. Once the image is uploaded, the app will generate 30 hashtags based on the image content.
3. The hashtags will be displayed on the page, along with a base64 preview of the image.

## File Structure

- `app.py`: Main Flask application.
- `templates/index.html`: HTML template for the frontend.
- `static/style.css`: CSS stylesheet for the frontend.
- `.env`: File to store environment variables such as the OpenAI API key (not included in the repository).
- `requirements.txt`: Python dependencies required to run the app.

## License

This project is licensed under the MIT License 
