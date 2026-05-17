from fastapi.testclient import TestClient
from hello import app  # Import your FastAPI app

client = TestClient(app)

def test_root():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_greet():
    """Test greeting endpoint"""
    response = client.get("/greet/Alice")   
    assert response.status_code == 200
    assert response.json() == {"greeting": "Hello Alice!"}