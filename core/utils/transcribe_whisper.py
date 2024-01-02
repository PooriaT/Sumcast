from pydub import AudioSegment
import math
import os
import whisper

BASE_CHUNK_PATH = "core/storage/audio/chunks/"
DURATION = 10 * 60

def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    return model.transcribe(audio_path)

def transcribe_large_audio_with_whisper(audio_path):
    audio = AudioSegment.from_file(audio_path)
    total_length = len(audio)
    num_parts = math.ceil(total_length / (DURATION * 1000))
    os.makedirs(BASE_CHUNK_PATH, exist_ok=True)

    texts = []
    for i in range(num_parts):
        texts.append(transcribe_audio_chunk(audio, i))
    whole_text = ' '.join(texts)
    os.remove(audio_path)
    return whole_text


def transcribe_audio_chunk(audio, index):
    start_time = index * DURATION * 1000
    end_time = (index + 1) * DURATION * 1000
    chunk_audio = audio[start_time:end_time]
    output_path = os.path.join(BASE_CHUNK_PATH, f"part_{index+1}.mp3")
    chunk_audio.export(output_path, format="mp3")
    text = transcribe_audio(output_path)
    os.remove(output_path)
    return text["text"]
