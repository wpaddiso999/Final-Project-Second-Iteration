from fastapi import FastAPI
from googleapiclient.discovery import build
from pprint import pprint
import requests
from google.cloud import translate

app = FastAPI()
TARGET_LANGUAGE = "zh"  # Chinese
API_KEY = "AIzaSyB9lomWP02z3mjqFrnwXz1F3hrj7J8SJGE"
OMDB_API_KEY = "your_omdb_api_key"  # Replace with your OMDB API key
PROJECT_ID = "your_project_id"  # Replace with your Google Cloud project ID

@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}
