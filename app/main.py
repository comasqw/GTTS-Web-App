from fastapi import FastAPI, Form, BackgroundTasks, Request
from fastapi.responses import FileResponse, JSONResponse
from exceptions import custom_validation_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi.templating import Jinja2Templates
from datetime import datetime
import os
import httpx

app = FastAPI()

templates = Jinja2Templates(directory="temp")


app.add_exception_handler(RequestValidationError, custom_validation_exception_handler)

async def delete_file(file_path: str):
    os.remove(file_path)

@app.get("/")
async def main_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit")
async def submit( background_tasks: BackgroundTasks,
            user_text=Form(..., max_length=500), language=Form(...), slow=Form(...)):

    requests_dct = {
        "text": user_text,
        "lang": language,
        "slow": slow
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post("http://127.0.0.1:8001/api/tts", json=requests_dct)
    except Exception as e:
        return JSONResponse(f"Couldn't send a request - {e}")


    if response.status_code == 200:

        filename = datetime.now().strftime("%d-%m-%Y_%H-%M-%S-%f")

        with open(f"{filename}.mp3", "wb") as audio:
            audio.write(response.content)

        background_tasks.add_task(delete_file, f"{filename}.mp3")
        return FileResponse(f"{filename}.mp3", filename=f"{filename}.mp3")
    else:
        return response.text