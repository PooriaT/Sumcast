import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence

# create a speech recognition object
r = sr.Recognizer()

def transcribe_audio(path):
    with sr.AudioFile(path) as source:
        audio_listened = r.record(source)
        text = r.recognize_google(audio_listened)
    return text


def get_large_audio_transcription_on_silence(path):
    sound = AudioSegment.from_file(path)  
    chunks = split_on_silence(
        sound,
        min_silence_len=400,
        silence_thresh= sound.dBFS - 14,
        keep_silence=100,
    )
    print("Number of chunks: ", len(chunks))

    folder_name = "core/data/audio/chunks"
    os.makedirs(folder_name, exist_ok=True)
    whole_text = ""

    for i, audio_chunk in enumerate(chunks, start=1):
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        try:
            text = transcribe_audio(chunk_filename)
            whole_text += text + " "
        except Exception as e:#sr.UnknownValueError as e:
            print("Error:", str(e))
    return whole_text

# if __name__ == '__main__':
#     path = "../data/audio/podcast.mp3"
#     print("\nFull text: \n", get_large_audio_transcription_on_silence(path))