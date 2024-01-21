# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

RUN apt update && apt install -y libsndfile1 ffmpeg 
# RUN apt install -y curl
# RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - &&\
#     apt-get install -y nodejs

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
RUN rm -rf /app/ui
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 3000 8000

# Command to run on container start
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
