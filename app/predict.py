from app.model import InputData
from app.train import train_model

# 予測モデルの初期化（初回のみトレーニング）
clf = train_model()

def make_prediction(data: InputData):
    input_data = [[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]]
    prediction = clf.predict(input_data)
    return {"prediction": int(prediction[0])}
