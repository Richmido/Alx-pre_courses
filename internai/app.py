from fastapi import FastAPI, UploadFile, Form
from pydantic import BaseModel
from typing import List

app = FastAPI(title="InternAI")

MISSIONS = {
    1: {"title": "Développeur Python", "keywords": ["python", "flask", "docker"]},
    2: {"title": "Data Analyst", "keywords": ["sql", "analysis", "pandas"]},
}

class Candidate(BaseModel):
    id: int
    name: str
    mission_id: int
    score: float

candidates: List[Candidate] = []
_counter = 1

@app.post("/apply", response_model=Candidate)
async def apply(name: str = Form(...), mission_id: int = Form(...), cv: UploadFile = None):
    global _counter
    content = await cv.read()
    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        text = ""
    keywords = MISSIONS.get(mission_id, {}).get("keywords", [])
    hits = sum(1 for k in keywords if k.lower() in text.lower())
    score = (hits / len(keywords) * 100) if keywords else 0.0
    candidate = Candidate(id=_counter, name=name, mission_id=mission_id, score=score)
    candidates.append(candidate)
    _counter += 1
    return candidate

@app.get("/candidates", response_model=List[Candidate])
def list_candidates():
    return candidates
