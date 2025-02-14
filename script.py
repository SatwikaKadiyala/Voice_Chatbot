import requests

# Server URL (Make sure your FastAPI server is running)
url = "http://127.0.0.1:8050/chat/"

# Path to your audio file
file_path = "C:/Users/DELL/Desktop/Voice Chatbot/sample.wav"

# Open the file and send the request
with open(file_path, "rb") as file:
    files = {"audio": file}
    headers = {"Jenkins-Crumb": "your-crumb-value-here"}  # Add if required, otherwise remove

    # Sending POST request
    response = requests.post(url, files=files, headers=headers)

    # Print server response
    print(response.text)
