from pydantic import BaseModel
from typing import Optional
from enum import Enum

class Note(BaseModel):
    id: Optional[int] = None
    title: str
    content: str

class ChatMode(str, Enum):
    teacher = "teacher"
    concise = "concise"
    creative = "creative"

class ChatRequest(BaseModel):
    message: str
    mode: ChatMode = ChatMode.concise