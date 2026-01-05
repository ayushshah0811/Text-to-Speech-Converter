
import pyttsx3

def setup_tts_engine():
    engine = pyttsx3.init()
    return engine

def adjust_tts_settings(engine, speed=190, volume=1.0, voice_id=None):
    engine.setProperty('rate', speed)
    
    engine.setProperty('volume', volume)
    
    if voice_id:
        engine.setProperty('voice', voice_id)

def list_available_voices(engine):
    voices = engine.getProperty('voices')
    return voices

ALLOWED_IDS = [
    "com.apple.voice.compact.en-US.Samantha",
    "com.apple.voice.compact.en-GB.Daniel",
    "com.apple.voice.compact.en-IN.Rishi",
    "com.apple.voice.compact.hi-IN.Lekha",
    "com.apple.voice.compact.ta-IN.Vani"
]

def filter_by_ids(voices):
    return [v for v in voices if v.id in ALLOWED_IDS]

def show_voices(voices):
    for index, voice in enumerate(voices):
        print(f"Voice {index}:")
        print(f"  Name: {voice.name}")
        print(f"  ID: {voice.id}")
        print()

def speak_text(engine, text):
    engine.say(text)
    
    engine.runAndWait()

def main():
    engine = setup_tts_engine()
    
    while True:
        print("Welcome to the Text-to-Speech Program!")
        
        voices = list_available_voices(engine)

        filtered_voices = filter_by_ids(voices)

        print("Here are the available voices:")
        show_voices(filtered_voices)

        
        choice = input("Type the number of the voice you want to use, or just press Enter for the default voice: ")
        
        if choice.isdigit():
            index = int(choice)
            if 0 <= index < len(voices):
                voice_id = filtered_voices[index].id
                adjust_tts_settings(engine, voice_id=voice_id)
            else:
                print("Invalid choice. Using default voice.")
        else:
            print("Using default voice.")
        
        text = input("Type the text you want to hear: ")
        
        speak_text(engine, text)
        
        more = input("Do you want to convert more text? (yes/no): ").strip().lower()
        
        if more != 'yes':
            break
    
    print("Thanks for using the Text-to-Speech Program.")

if __name__ == "__main__":
    main()