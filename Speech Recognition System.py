import speech_recognition as sr

def transcribe_audio_file(filename):
    """Transcribes a short audio file to text."""
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    
    # Open the audio file
    try:
        with sr.AudioFile(filename) as source:
            print(f"Reading audio file: {filename}...")
            audio_data = recognizer.record(source)  # Read the entire audio file
            print("Audio captured.")
        
        # Convert the audio to text using the Google Web Speech API
        try:
            text = recognizer.recognize_google(audio_data)
            print("\nTranscription Result:")
            print(text)
        except sr.UnknownValueError:
            print("Sorry, could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not connect to Google API; {e}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def transcribe_microphone_input():
    """Captures audio from the microphone and transcribes it."""
    recognizer = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Speak something now...")
        # Optional: adjust for ambient noise for better accuracy
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("Audio captured. Transcribing...")

    # Convert speech to text
    try:
        text = recognizer.recognize_google(audio)
        print("\nTranscription Result:")
        print(text)
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not connect to Google API; {e}")


if __name__ == "__main__":
    # --- Option 1: Transcribe a local WAV file ---
    # Ensure you have a WAV file named "sample.wav" in the same directory
    transcribe_audio_file("sample.wav")

    # --- Option 2: Transcribe live microphone input ---
    transcribe_microphone_input()
