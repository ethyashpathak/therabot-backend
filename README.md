# Therabot API

A simple FastAPI service that predicts text emotion using a pre-trained model pipeline loaded from `text_emotion.pkl`.

## Project structure

- [app.py](app.py): FastAPI application defining the `/predict` endpoint.
- [model.py](model.py): Model loader and predictor exposing [`predict_emotion`](model.py).
- [text_emotion.pkl](text_emotion.pkl): Serialized scikit-learn pipeline with text preprocessing and classifier.
- [.gitignore](.gitignore): Typical Python, IDE, and data ignores.

## Installation

1. Create and activate a virtual environment (recommended).
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the API

Start the server with:
```sh
uvicorn app:app --reload
```

By default, it runs at:
- http://127.0.0.1:8000
- Interactive docs: http://127.0.0.1:8000/docs

## Usage

POST to `/predict` with JSON:
```json
{
  "text": "I am feeling great today!"
}
```

Response:
```json
{
  "emotion": "happy"
}
```

## Notes

- Ensure `text_emotion.pkl` is present in the project root, matching the loader in [model.py](model.py).
- The endpoint is defined in [app.py](app.py) and calls [`model.predict_emotion`](model.py).