# app/Dockerfile

FROM python:3.7.9


WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    ffmpeg \
    libsm6 \
    libxext6 \
    software-properties-common \
    nano \
    git \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip --no-cache-dir

COPY ai-service/ .

RUN pip install -r requirements.txt

EXPOSE 7001