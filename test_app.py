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
    
def test_translate_and_get_youtube_reviews():
    # Replace 'your_movie_name' and 'your_target_language' with actual values
    movie_name = "your_movie_name"
    target_language = "your_target_language"

    response = client.get(f"/translate_moviereviews_reviews/?movie_name={movie_name}&target_language={target_language}")

    assert response.status_code == 200
    assert "movie_name" in response.json()
    assert "reviews" in response.json()

    # Add more specific assertions based on the expected response structure
    for review in response.json()["reviews"]:
        assert "title" in review
        assert "description" in review
        assert "video_url" in review
