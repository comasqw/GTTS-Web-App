from gtts import gTTS
from datetime import datetime


async def generate_audio(text, lang="en", slow=False):
    now = datetime.now().strftime("%d-%m-%Y_%H-%M-%S-%f")
    tts = gTTS(text=text, lang=lang, slow=slow)
    tts.save(f"{now}.mp3")

    return now
