import speech_recognition as sr
import sounddevice as sd
import soundfile as sf

def record_audio(filename="temp.wav", duration=5, fs=44100):
    print("🎤 Recording for", duration, "seconds...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    sf.write(filename, recording, fs)
    print("✅ Recording saved to", filename)

def get_hindi_input():
    record_audio()
    recognizer = sr.Recognizer()
    with sr.AudioFile("temp.wav") as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data, language="hi-IN")
        print("🗣️ You said (Hindi):", text)
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return ""
    except sr.RequestError as e:
        print("⚠️ Could not request results; {0}".format(e))
        return ""
