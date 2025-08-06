from fastapi import FastAPI
from pydantic import BaseModel
from agents import manager_agent

app = FastAPI()

class UserInput(BaseModel):
    input_text: str
    documents_path: str = None

@app.post("/process")
def process_input(data: UserInput):
    response = manager_agent.decide_and_execute(data.input_text, data.documents_path)
    return response
