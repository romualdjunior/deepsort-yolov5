# syntax=docker/dockerfile:1
FROM python:3.8
WORKDIR /deepsort-yolov5
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y
COPY ./requirements.txt /deepsort-yolov5/requirements.txt
RUN  pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run","app.py","--server.port","8080"]
EXPOSE 8080