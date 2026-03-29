
from fastapi import FastAPI
from backend.orchestrator.pipeline import run_pipeline

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Enterprise AI Content System Running"}

@app.post("/generate")
def generate(topic: str, audience: str):
    return run_pipeline(topic, audience)
