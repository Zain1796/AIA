import requests
import os
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = os.getenv("VOICE_ID")

def generate_speech(text, output_path="assets/output.mp3"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {"xi-api-key": ELEVENLABS_API_KEY, "Content-Type": "application/json"}
    data = {"text": text, "voice_settings": {"stability": 0.5, "similarity_boost": 0.8}}

    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Speech saved to {output_path}")
        return output_path
    else:
        print("❌ Error generating speech:", response.text)
        return None

if __name__ == "__main__":
    generate_speech("Investing in AIA is more than financial—it’s an intellectual and strategic play in the future of human-AI interaction.")
