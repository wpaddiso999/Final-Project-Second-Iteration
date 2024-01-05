from fastapi import FastAPI
from googleapiclient.discovery import build
from pprint import pprint
import requests
from google.cloud import translate
from fastapi import FastAPI, HTTPException
from googleapiclient.discovery import build
# Import necessary libraries
from googletrans import Translator
from googleapiclient.discovery import build
from fastapi import HTTPException

app = FastAPI()

API_KEY = "AIzaSyB9lomWP02z3mjqFrnwXz1F3hrj7J8SJGE"


@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}

@app.get("/video")
def get_video(url: str):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    video_id = url.split("v=")[1]
    video_response = youtube.videos().list(
        part="snippet, statistics",
        id=video_id
    ).execute()

    title = video_response['items'][0]['snippet']['title']
    description = video_response['items'][0]['snippet']['description']
    category_id = video_response['items'][0]['snippet']['categoryId']
    view_count = video_response['items'][0]['statistics']['viewCount']

    category_response = youtube.videoCategories().list(
        part="snippet",
        id=category_id,
    ).execute()

    category = category_response['items'][0]['snippet']['title']

    return {
        "url": url,
        "title": title,
        "description": description,
        "view_count": view_count,
        "category": category,
    }

def youtube_search(query, max_results=10):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    search_response = youtube.search().list(
        q=query,
        type="video",
        part="id",
        maxResults=max_results
    ).execute()

    video_ids = [item['id']['videoId'] for item in search_response.get('items', [])]
    return video_ids

@app.get("/moviereviews_reviews/")
def get_youtube_reviews(movie_name: str):
   
    video_ids = youtube_search(movie_name)
    
    if not video_ids:
        raise HTTPException(status_code=404, detail=f"No videos found for the movie: {movie_name}")

    youtube = build("youtube", "v3", developerKey=API_KEY)

    reviews = []
    for video_id in video_ids:
        video_response = youtube.videos().list(
            part="snippet",
            id=video_id
        ).execute()

        video_info = video_response.get("items", [])
        if not video_info:
            continue

        title = video_info[0]["snippet"]["title"]
        description = video_info[0]["snippet"]["description"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        reviews.append({
            "title": title,
            "description": description,
            "video_url": video_url
        })

    return {"movie_name": movie_name, "reviews": reviews}


def extract_video_id(youtube_url: str) -> str:
    
    video_id = youtube_url.split("v=")[1]
    return video_id

def get_movie_description(video_id: str):
    youtube = build("youtube", "v3", developerKey=API_KEY)

    video_response = youtube.videos().list(
        part="snippet",
        id=video_id
    ).execute()

    video_info = video_response.get("items", [])

    if not video_info:
        raise HTTPException(status_code=404, detail=f"No information found for the video with ID: {video_id}")

    description = video_info[0]["snippet"]["description"]

    return {"video_id": video_id, "description": description}

@app.get("/video_description/")
def get_video_description_endpoint(video_id: str):
    return get_movie_description(video_id)


def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text


def youtube_search(movie_name):
   
    API_KEY = 'AIzaSyB9lomWP02z3mjqFrnwXz1F3hrj7J8SJGE'
    youtube = build("youtube", "v3", developerKey=API_KEY)

    # Perform the search
    search_response = youtube.search().list(
        q=movie_name,
        part="id",
        type="video",
        maxResults=5  # You can adjust the number of results as needed
    ).execute()

    
    video_ids = [item["id"]["videoId"] for item in search_response.get("items", [])]

    return video_ids


@app.get("/translate_moviereviews_reviews/")
def translate_and_get_youtube_reviews(movie_name: str, target_language: str):
   
    translated_movie_name = translate_text(movie_name, target_language)

   
    video_ids = youtube_search(translated_movie_name)

    if not video_ids:
        raise HTTPException(status_code=404, detail=f"No videos found for the movie: {translated_movie_name}")

    youtube = build("youtube", "v3", developerKey=API_KEY)

    reviews = []
    for video_id in video_ids:
        video_response = youtube.videos().list(
            part="snippet",
            id=video_id
        ).execute()

        video_info = video_response.get("items", [])
        if not video_info:
            continue

        title = translate_text(video_info[0]["snippet"]["title"], target_language)
        description = translate_text(video_info[0]["snippet"]["description"], target_language)
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        reviews.append({
            "title": title,
            "description": description,
            "video_url": video_url
        })

    return {"movie_name": translated_movie_name, "reviews": reviews}
