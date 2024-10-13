import streamlit as st
import requests

# Streamlit app for frontend
st.title("アヤメの花の分類")
st.write("アヤメの花の測定値を入力してください:")

# Input fields for flower measurements
sepal_length = st.number_input("がく片の長さ（cm）", min_value=0.0, step=0.1)
sepal_width = st.number_input("がく片の幅（cm）", min_value=0.0, step=0.1)
petal_length = st.number_input("花びらの長さ（cm）", min_value=0.0, step=0.1)
petal_width = st.number_input("花びらの幅（cm）", min_value=0.0, step=0.1)

if st.button("分類"):
    # Make a request to the FastAPI backend
    response = requests.post(
        "http://localhost:8000/predict",
        json={
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width,
        },
    )
    result = response.json()
    if result['prediction'] == 0:
        st.write("予測されたクラスは: セトーサ")
    elif result['prediction'] == 1:
        st.write("予測されたクラスは: ヴァーシカラー")
    elif result['prediction'] == 2:
        st.write("予測されたクラスは: ヴァージニカ")
