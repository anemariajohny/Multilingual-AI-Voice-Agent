def check_emergency(text):
    emergency_keywords = [
        "help", "emergency", "save", "accident", "danger",
        "मदद", "आपातकाल", "खतरा", "बचाओ", "अटैक"
    ]

    text = text.lower()
    for word in emergency_keywords:
        if word in text:
            return True
    return False

