import pytest
from fastapi.testclient import TestClient
from your_fastapi_module import app  # replace with the actual module name

# Create a test client using the FastAPI app
client = TestClient(app)

def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_get_video():
    # Replace 'your_youtube_video_url' with an actual YouTube video URL
    response = client.get("/video?url=your_youtube_video_url")
    assert response.status_code == 200
    # Add more assertions based on the expected response structure

def test_get_youtube_reviews():
    # Replace 'your_movie_name' with an actual movie name
    response = client.get("/moviereviews_reviews/?movie_name=your_movie_name")
    assert response.status_code == 200
    # Add more assertions based on the expected response structure

def test_get_movie_description_endpoint(mock_get_movie_description):
    response = client.get("/movie_description/?movie_name=your_movie_name")

    assert response.status_code == 200
    assert response.json() == {
        "movie_name": "your_movie_name",
        "description": "Movie Description"
    }
