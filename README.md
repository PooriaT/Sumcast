# podcast_summary

This app helps you to summarize a podcast content. 

# Sumcast

The Web app to summarize the podcast content

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/KprKj7lCiBU/0.jpg)](https://www.youtube.com/watch?v=KprKj7lCiBU)

## Descritpion

In this project, first we retrieve the related information of a specific podcast and related episode. Then, store the audio format of that episode. The audio file will be transcribe via OpenAI Whisper module. Finally, the extracted text of podcast content is fed into Google Gemini API to sumerize and highlight the whole content.

## Getting Started

### Prerequisite 

The project prerequisites are outlined below:

- Python 3.10 
- OpenAI Whisper
- Google I Generativelanguage (Gemini)
- libsndfile1 and ffmpeg packages on Linux

### Installation 

The project comprises a backend constructed with the FastAPI framework and a UI utilizing the Next.js framework. To install, follow the steps outlined below:

1. Clone the repository to your local machine and navigate to the directory.

```bash
git clone https://github.com/PooriaT/Sumcast.git
cd Sumcast
```

2. Set up the virtual environment and activate it. 

```bash
python -m venv venv
# On Linux
. venv/bin/activate
```

3. Setting up the necessary Python libraries using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

4. Install the following two packages on a Linux machine.

```bash 
apt install -y libsndfile1 ffmpeg 
```

5. Navigate to the UI folder and execute the command to install the Node packages.

```bash
cd ui 
nmp install 
```

6. Begin the development environment for the backend and frontend in separate terminals

In one terminal, navigate to the root directory and execute the following command:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload 
```

On another terminal, access the `ui` folder and then run:

(**Attention**: To test it locally, you need to change the base url in frontend to `http://localhost:8000/api`. You can find it in `ui/utils/fastApiCall.ts`.)

```bash
npm run dev
```

1. After that, navigate to `http://localhost:3000` to see the application in action.

### Deployment

To deploy the application, you'll need to build UI and run the FastAPI server, taking into account the number of workers you want to use. So, we have:

```bash
cd ui
npm run build
npm start
```

In the root direcotry:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --worker 4
```

### Docker

The Dockerfiles for both the backend and frontend are available. Follow the procedure below to build the images and run the containers:

To build the images:

```bash
docker build -t sumcast_backend .
```
```bash
cd ui 
docekr build -t sumcast_frontend .
```

To run the containers:

```bash
docker run -p 8000:8000 -name <name> sumcast_backend
```

```bash
docker run -p 3000:3000 -name <name> sumcast_frontend
```

## Test

To test the API, below command can be used:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"podcast_name": "startalk", "episode_name": "This is Your Brain on social media with anna lembke, MD"}' http://localhost:8000/api/summarize/
```

## Contribution

We welcome contributions from the community! If you have suggestions, bug reports, or would like to contribute code or documentation, please feel free to open an issue or submit a pull request on our GitHub repository.

## License