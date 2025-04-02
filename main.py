import os
from scripts.elevenlabs_tts import generate_speech
from scripts.did_avatar import generate_avatar_animation

# Use local files (or upload to a server for public access)
AVATAR_IMAGE_PATH = "assets/avatar.jpg"
AUDIO_FILE_PATH = "assets/output.mp3"

# Convert local file paths to public URLs (Upload manually or use an API)
AVATAR_IMAGE_URL = "D:\AIA Task\assets\avtar.jpg"  
AUDIO_FILE_URL = "D:\AIA Task\assets\output.mp3"  

if __name__ == "__main__":
    # Step 1: Generate Speech
    text = "Hello! Welcome to the AI Avatar demo."
    speech_path = generate_speech(text)

    # Step 2: Generate Avatar Animation
    if speech_path:
        generate_avatar_animation(AVATAR_IMAGE_URL, AUDIO_FILE_URL)