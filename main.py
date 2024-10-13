# main.py
from fastapi import FastAPI
from app.model import InputData
from app.predict import make_prediction

# FastAPIのインスタンスを作成
app = FastAPI()

# 予測エンドポイント
@app.post("/predict")
async def predict(data: InputData):
    return make_prediction(data)