context = {
    "name": None,
    "interested": None,
    "followup_done": False
}

def handle_lead_conversation(text):
    response = ""

    if "नाम" in text or "name" in text:
        context["name"] = extract_name(text)
        response = f"{context['name']} जी, आपका स्वागत है।"
    
    elif "रुचि" in text or "interested" in text or "want" in text:
        context["interested"] = True
        response = "यह सुनकर अच्छा लगा कि आप हमारी सेवा में रुचि रखते हैं। क्या हम आगे बात करें?"

    elif "नहीं" in text or "not interested" in text:
        context["interested"] = False
        response = "ठीक है, धन्यवाद। अगर आपको ज़रूरत हो तो हमसे संपर्क करें।"

    elif "फॉलो अप" in text or "follow up" in text:
        if context["interested"]:
            response = f"{context['name']} जी, हम आपको एक डेमो शेड्यूल करने में मदद कर सकते हैं।"
            context["followup_done"] = True
        else:
            response = "आपकी रुचि नहीं है, इसलिए हम फॉलो अप नहीं करेंगे।"

    else:
        response = "क्या आप हमारी सेवा के बारे में कुछ पूछना चाहेंगे?"

    return response

def extract_name(text):
    words = text.split()
    for i, word in enumerate(words):
        if word.lower() in ["नाम", "name", "मैं", "my"]:
            if i + 1 < len(words):
                return words[i + 1]
    return "ग्राहक"
