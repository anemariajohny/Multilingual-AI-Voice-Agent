from speech_input import get_hindi_input
from voice_output import speak_hindi

def hindi_bot():
    while True:
        user_input = get_hindi_input()

        if user_input is None:
            continue

        # Very simple rule-based logic
        if "समय" in user_input:
            response = "अभी समय है दोपहर के तीन बजकर पंद्रह मिनट"
        elif "कैसे हो" in user_input or "कैसी हो":
            response = "मैं अच्छा हूँ, धन्यवाद!"
        elif "बंद" in user_input or "बाय" in user_input:
            response = "अलविदा! फिर मिलेंगे।"
            speak_hindi(response)
            break
        else:
            response = "माफ़ कीजिए, मैं वह नहीं समझ पाया।"

        speak_hindi(response)

# Run the bot
hindi_bot()
