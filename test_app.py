import json
from fastapi.testclient import TestClient
from your_fastapi_app_file_name import app  # Replace with the actual filename of your FastAPI app

client = TestClient(app)

def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_get_video():
    
    url = "https://www.youtube.com/watch?v=9lVB1-c69Sw"
    response = client.get(f"/video?url={url}")
    assert response.status_code == 200
    

def test_get_youtube_reviews():
    
    movie_name = "Harry Potter"
    response = client.get(f"/moviereviews_reviews/?movie_name={movie_name}")
    assert response.status_code == 200
   

def test_get_movie_description_endpoint():
   
    movie_name = "Harry Potter"
    response = client.get(f"/movie_description/?movie_name={movie_name}")
    assert response.status_code == 200
   

def test_translate_and_get_youtube_reviews():
   
    movie_name = "Harry Potter"
    target_language = "es"
    response = client.get(f"/translate_moviereviews_reviews/?movie_name={movie_name}&target_language={target_language}")
    assert response.status_code == 200
   
