from gtts import gTTS
import playsound
import os

def speak_hindi(text):
    tts = gTTS(text=text, lang='hi')
    tts.save("output.mp3")
    playsound.playsound("output.mp3")
    os.remove("output.mp3")  # Optional: delete file after speaking

# Test the function
speak_hindi("नमस्ते! मैं आपकी सहायता के लिए तैयार हूँ।")




