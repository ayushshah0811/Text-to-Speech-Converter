# Text-to-Speech Program (Python + pyttsx3)

A simple and interactive Python-based **Text-to-Speech (TTS)** program using the `pyttsx3` library.
The script allows users to:

* Choose from a filtered list of high-quality system voices
* Adjust speed and volume
* Convert any typed text into speech
* Run multiple conversions in a single session

This project works **offline** and supports **macOS system voices**.

---

## 🚀 Features

* 🎤 List available system voices
* 🎚️ Adjust TTS settings (speed, volume, voice)
* 🗣️ Filter voices using custom `ALLOWED_IDS`
* ⏩ Choose interactive voice selection
* 🔊 Convert any user-input text to speech
* 🔁 Loop until the user exits

---

## 📦 Requirements

Make sure you have Python installed.

Install pyttsx3:

```bash
pip install pyttsx3
```

---

## 📁 Project Structure

```
.
├── tts.py  # Your TTS program
└── README.md
```

---

## 🧠 How It Works

### 1. **Setup Engine**

Initializes the pyttsx3 engine:

```python
engine = pyttsx3.init()
```

### 2. **Adjust Settings**

Updates speed, volume, and voice:

```python
adjust_tts_settings(engine, speed=100, volume=1.0, voice_id=None)
```

### 3. **List Voices**

Fetches all system voices:

```python
voices = engine.getProperty('voices')
```

### 4. **Filter Voices**

Only keep selected voice IDs:

```python
ALLOWED_IDS = [
    "com.apple.voice.compact.en-US.Samantha",
    "com.apple.voice.compact.en-GB.Daniel",
    "com.apple.voice.compact.en-IN.Rishi",
    "com.apple.voice.compact.hi-IN.Lekha",
    "com.apple.voice.compact.ta-IN.Vani"
]
```

### 5. **Speak Text**

Converts text to speech:

```python
speak_text(engine, text)
```

---

## ▶️ Run the Program

In terminal:

```bash
python3 tts.py
```

You'll see:

* List of available filtered voices
* Option to pick a voice
* Input box to type text
* Real-time speech output

---

## 📝 Example Interaction

```
Welcome to the Text-to-Speech Program!
Here are the available voices:
Voice 0:
  Name: Samantha
  ID: com.apple.voice.compact.en-US.Samantha

Voice 1:
  Name: Daniel
  ID: com.apple.voice.compact.en-GB.Daniel
...
Type the number of the voice you want to use:
```

---

## 🛠️ Technologies Used

* Python 3
* pyttsx3 (offline TTS library)
* macOS system voices

---

## 📜 License

This project is licensed under the **MIT License**.
You can freely use, modify, and distribute it.

---

## 🤝 Contributions

Feel free to fork the repo and submit a pull request!

---

## ⭐ Author

**Ayush Shah**

---
