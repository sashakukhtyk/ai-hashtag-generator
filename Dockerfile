FROM python:3.12.2

WORKDIR /ai_hashtag

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

WORKDIR /ai_hashtag/flask_hashtag_generator

CMD ["python3", "app.py"]