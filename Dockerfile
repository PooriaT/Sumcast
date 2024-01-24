FROM python:3.10-slim-buster

RUN apt update && apt install -y libsndfile1 ffmpeg 
# RUN apt install -y curl
# RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - &&\
#     apt-get install -y nodejs

WORKDIR /app

COPY . /app
RUN rm -rf /app/ui
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
