from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run as app_run

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def home():
    return "Welcome to the Reddit Sentiment Analysis API"


if __name__ == "__main__":
    app_run(app, host="0.0.0.0", port=8000)
