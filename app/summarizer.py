import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text: str, style: str = "brief") -> str:
    """
    Summarize input text using OpenAI GPT API.
    
    Parameters:
        text (str): Text to summarize
        style (str): "brief", "detailed", "bullet"
    
    Returns:
        str: Summarized text
    """
    style_prompts = {
        "brief": "Summarize the following text briefly:",
        "detailed": "Summarize the following text in detail:",
        "bullet": "Summarize the following text in bullet points:"
    }
    
    if style not in style_prompts:
        style = "brief"
    
    prompt = f"{style_prompts[style]}\n\n{text}"
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5
        )
        summary = response.choices[0].message.content.strip()
        return summary
    except Exception as e:
        return f"Error: {str(e)}"

