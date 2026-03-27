import os
import google.generativeai as genai
from dotenv import load_dotenv
import json
import re

load_dotenv()

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    print("WARNING: GEMINI_API_KEY not found in environment variables.")

def predict_with_gemini(text: str):
    """
    Uses Google Gemini to verify if the news is real or fake.
    """
    if not api_key:
        return {
            "result": "Configuration Error",
            "confidence": 0,
            "justification": "Gemini API Key is missing. Please set GEMINI_API_KEY in your .env file."
        }
    
    # Try multiple model variants from the discovered available models list
    model_names = ['gemini-2.0-flash', 'gemini-flash-latest', 'gemini-1.5-flash', 'gemini-pro-latest']
    
    last_error = ""
    for name in model_names:
        try:
            print(f"DEBUG: Attempting to use model: {name}")
            model = genai.GenerativeModel(name)
            
            prompt = f"""
            Analyze the following news text and determine if it is likely to be 'Real' or 'Fake/Misleading'.
            Provide your response in the following JSON format:
            {{
                "result": "Real News" or "Fake News",
                "confidence": 0.0 to 1.0 (float),
                "justification": "A brief 1-2 sentence explanation of why you reached this conclusion based on your knowledge."
            }}
            
            News Text: {text}
            """
            
            response = model.generate_content(prompt)
            
            # Clean the response text to find JSON
            match = re.search(r'\{.*\}', response.text, re.DOTALL)
            if match:
                result_data = json.loads(match.group())
                return result_data
            else:
                return {
                    "result": "Error",
                    "confidence": 0,
                    "justification": "Failed to parse AI response. Raw output: " + response.text[:100]
                }
        except Exception as e:
            last_error = str(e)
            print(f"DEBUG: Error with {name}: {last_error}")
            continue
            
    return {
        "result": "API Error",
        "confidence": 0,
        "justification": f"Failed to connect to Gemini API with all models. Last error: {last_error}"
    }
