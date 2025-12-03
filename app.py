from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_emotion
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()   

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Input(BaseModel):
    text: str

@app.post("/predict")
def predict(data: Input):
    emotion = predict_emotion(data.text)
    return {"emotion": emotion}
