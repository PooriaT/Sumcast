import os
from dotenv import load_dotenv, find_dotenv
import google.generativeai as genai

load_dotenv(find_dotenv())

google_gemini_api_key = os.getenv("GOOGLE_GEMINI_API_KEY")

genai.configure(api_key=google_gemini_api_key)
model = genai.GenerativeModel('gemini-pro')

def summarizing(text_path, streaming):
    with open(text_path, "r", encoding="utf-8") as file:
        text = file.read()
    prompt = f"""
        Imagine you are a senior reviewer.
        Summarize the text and highlight the important parts. The text is as follows: \n
        {text}
    """
    response = model.generate_content(prompt, stream=streaming)

    return response
