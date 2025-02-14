# Voice Chatbot  

This project is a voice-based chatbot that leverages speech recognition, natural language understanding (NLU), and text-to-speech (TTS) to process and respond to user queries. It is built using FastAPI, Whisper ASR, DialoGPT, and Google Cloud Text-to-Speech.  

## Features  
- Speech Recognition: Uses OpenAI's Whisper ASR to convert audio input into text.  
- Natural Language Processing: Employs Facebook BlenderBot for chatbot responses.  
- Text-to-Speech: Converts chatbot responses back to speech using Google Cloud TTS.  
- FastAPI Backend: Handles audio file uploads and response generation.  

## File Structure  
- `asr.py` – Transcribes speech to text using Whisper.  
- `nlu.py` – Processes text input and generates responses using BlenderBot.  
- `tts.py` – Converts chatbot responses to speech using Google Cloud TTS.  
- `main.py` – FastAPI server to handle audio input and response processing.  
- `script.py` – Sends recorded audio to the FastAPI backend.  
- `Dockerfile` – Docker configuration for containerizing the application.  

## How It Works  
1. User Uploads Audio: FastAPI receives the voice input.  
2. Speech-to-Text (STT): Whisper ASR converts audio to text.  
3. Chatbot Response: BlenderBot processes the text and generates a response.  
4. Text-to-Speech (TTS): Google Cloud TTS converts the response back to audio.  
5. Response is Sent: The user receives the chatbot’s spoken response.  

## Running the Project  
1. Install dependencies:  
   ```bash
   pip install fastapi uvicorn openai transformers google-cloud-texttospeech
   ```
2. Run the FastAPI server:  
   ```bash
   python main.py
   ```
3. Use `script.py` to send an audio file for processing.  

## Future Improvements  
- Support for real-time voice interaction.  
- Integration with multiple NLU models for enhanced chatbot capabilities.  
- Deployment on cloud platforms for scalability.  
