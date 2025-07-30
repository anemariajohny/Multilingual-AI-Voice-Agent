def detect_emotion(text):
    happy_keywords = ["अच्छा", "खुश", "शानदार", "great", "happy", "awesome"]
    sad_keywords = ["दुखी", "बुरा", "निराश", "sad", "bad", "upset"]

    text = text.lower()

    for word in happy_keywords:
        if word in text:
            return "happy"
    for word in sad_keywords:
        if word in text:
            return "sad"

    return "neutral"

