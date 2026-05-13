import json
import os
import webbrowser

import pyttsx3
import pyaudio
import requests
from vosk import Model, KaldiRecognizer


MODEL_PATH = "model"


def speak(text):
    print("Assistant:", text)

    engine = pyttsx3.init()
    engine.setProperty("rate", 220)
    engine.say(text)
    engine.runAndWait()


def clean_text(text):
    words = text.split()

    filtered = []
    for w in words:
        if w not in ["the", "a", "an"]:
            filtered.append(w)

    return " ".join(filtered)


def listen(model):
    p = pyaudio.PyAudio()

    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=48000,
        input=True,
        frames_per_buffer=8192
    )

    recognizer = KaldiRecognizer(model, 48000)

    print("Listening...")
    stream.start_stream()

    text = ""

    while True:
        data = stream.read(4096, exception_on_overflow=False)

        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())

            # print("Raw result:", result)

            text = result.get("text", "")
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

    text = clean_text(text.lower().strip())

    print("You said:", text)

    return text


def get_word_info(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            return None, None

        data = response.json()

        meaning = data[0]["meanings"][0]["definitions"][0]["definition"]

        example = None

        for meaning_block in data[0]["meanings"]:
            for definition in meaning_block["definitions"]:
                if "example" in definition:
                    example = definition["example"]
                    break

        return meaning, example

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None, None


def main():
    if not os.path.exists(MODEL_PATH):
        print("Folder 'model' not found.")
        return

    model = Model(MODEL_PATH)

    last_word = ""
    last_meaning = ""
    last_example = ""

    speak("Hi, how can I help you?")

    while True:
        command = listen(model)

        if command.startswith("find "):
            word = command.replace("find ", "").strip()

            meaning, example = get_word_info(word)

            if meaning is None:
                speak("Word not found.")
                continue

            last_word = word
            last_meaning = meaning
            last_example = example

            speak(f"I found the word {word}")
            speak(meaning)

        elif command == "meaning":
            if last_meaning:
                speak(last_meaning)
            else:
                speak("No word selected.")

        elif command == "example":
            if last_example:
                speak(last_example)
            else:
                speak("No example found.")

        elif command == "link":
            if last_word:

                url = f"https://dictionary.cambridge.org/dictionary/english/{last_word}"

                speak("Opening browser.")
                webbrowser.open(url)

            else:
                speak("No word selected.")

        elif command in ["exit", "quit", "goodbye", "stop"]:
            speak("Goodbye.")
            break

        else:
            speak("Command not recognized.")


if __name__ == "__main__":
    main()
