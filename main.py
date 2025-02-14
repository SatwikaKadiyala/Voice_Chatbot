from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/chat/")
async def upload_audio(audio: UploadFile = File(...)):
    return {"filename": audio.filename}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8050)
