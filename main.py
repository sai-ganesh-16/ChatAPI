from fastapi import FastAPI, HTTPException
from typing import List
from models import Note, ChatRequest
from services import get_llm_response

app = FastAPI(title="Notes & AI Chat API")

# Storage Strategy: In-memory list
notes_db: List[Note] = []
chat_history: List[ChatRequest] = []  # Store chat history for retrieval

@app.post("/notes", response_model=Note)
async def create_note(note: Note):
    note.id = len(notes_db) + 1
    notes_db.append(note)
    return note

@app.get("/notes", response_model=List[Note])
async def get_notes():
    return notes_db

@app.post("/chat")
async def chat_with_ai(request: ChatRequest):
    try:
        if not request.message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        answer = get_llm_response(request.message, request.mode)
        chat_history.append(request)
        return {"mode": request.mode, "response": answer}
        chat_history.append({"response": answer})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/chat", response_model=List[ChatRequest])
async def get_chat_history():
    return chat_history