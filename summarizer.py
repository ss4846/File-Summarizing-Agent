import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

my_api_key = os.environ.get('GENAI_API_KEY')

genai.configure(api_key=my_api_key)

model = "gemini-2.5-flash"

llm = genai.GenerativeModel(model)

def summarize_text(text):
    prompt = f"""
    You are an expert document summarizer.
    Read the text and generate:

    1. A short summary (50-100 words)
    2. A detailed summary (200-300 words)
    3. Key takeaways (5-10 bullet points)

    Text:
    {text}
    """
    response = llm.generate_content(prompt)

    with open('summary.txt', 'w', encoding='utf-8') as f:
        f.write(response.text)

    return response.text