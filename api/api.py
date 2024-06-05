from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import FileResponse
from fastapi.exceptions import RequestValidationError
from exceptions import custom_validation_exception_handler
from tts import generate_audio
from models import TTS_Model
import os

app = FastAPI()

app.add_exception_handler(RequestValidationError, custom_validation_exception_handler)

async def delete_file(file_path: str):
    os.remove(file_path)

@app.post("/api/tts")
async def create_audio(content: TTS_Model, background_tasks: BackgroundTasks):
    now = await generate_audio(content.text, content.lang, content.slow)
    file_path = f"{now}.mp3"
    background_tasks.add_task(delete_file, file_path)
    return FileResponse(file_path)
