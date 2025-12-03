import joblib

# Load the trained pipeline
model = joblib.load("text_emotion.pkl")

def predict_emotion(text: str):
    return model.predict([text])[0]
