import whisper

def transcribe_audio(audio_path):
    model = whisper.load_model("base")  # Loading Whisper ASR model
    result = model.transcribe(audio_path)
    return result["text"]

if __name__ == "__main__":
    audio_file = "sample.wav"  # Providing an audio file path
    print("Transcription:", transcribe_audio(audio_file))
