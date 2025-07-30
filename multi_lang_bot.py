from speech_input import get_hindi_input
from voice_output import speak_hindi
from langdetect import detect
from emotion_module import detect_emotion
from lead_followup_module import handle_lead_conversation
from emergency_module import check_emergency

def multi_lang_bot():
    while True:
        user_input = get_hindi_input()

        if user_input is None:
            continue

        # 🔴 Emergency check before anything else
        if check_emergency(user_input):
            speak_hindi("आपातकालीन स्थिति पाई गई है। कृपया शांत रहें। हम मदद के लिए कार्रवाई कर रहे हैं।")
            continue

        try:
            detected_lang = detect(user_input)
        except:
            speak_hindi("भाषा पहचानने में समस्या हुई।")
            continue

        # 🧠 Detect emotion
        emotion = detect_emotion(user_input)

        # 🇮🇳 Hindi logic
        if detected_lang == 'hi':
            if "समय" in user_input:
                response = "अभी समय है तीन बजकर तीस मिनट"
            elif "कैसे हो" in user_input:
                if emotion == "happy":
                    response = "आप खुश हैं, यह सुनकर अच्छा लगा!"
                elif emotion == "sad":
                    response = "अगर आप दुखी हैं, तो मैं सुन रहा हूँ। क्या मैं कुछ मदद कर सकता हूँ?"
                else:
                    response = "मैं ठीक हूँ, धन्यवाद!"
            elif "बंद" in user_input:
                response = "अलविदा!"
                speak_hindi(response)
                break
            else:
                response = handle_lead_conversation(user_input)

            speak_hindi(response)

        # 🇺🇸 English logic
        elif detected_lang == 'en':
            if "time" in user_input.lower():
                response = "The current time is 3:30 PM."
            elif "how are you" in user_input.lower():
                if emotion == "happy":
                    response = "You sound happy — that's awesome!"
                elif emotion == "sad":
                    response = "I'm here for you if you're feeling down."
                else:
                    response = "I'm doing great, thank you!"
            elif "bye" in user_input.lower():
                response = "Goodbye!"
                speak_hindi(response)
                break
            else:
                response = handle_lead_conversation(user_input)

            speak_hindi(response)

        # 🌐 Unrecognized language
        else:
            speak_hindi("यह भाषा समर्थित नहीं है।")

# 🔁 Run the bot loop
multi_lang_bot()



