from pydantic import BaseModel, Field
from typing import Annotated
from enum import Enum

class Lang_Choise(str, Enum):
    en = "en"
    ru = "ru"

class TTS_Model(BaseModel):
    text: Annotated[str, Field(min_length=1, max_length=500)]
    lang: Lang_Choise = "en"
    slow: bool = False