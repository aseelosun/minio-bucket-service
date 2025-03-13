import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_bucket():
    response = client.post("/buckets?bucket_name=test-bucket")
    assert response.status_code == 200
    assert "message" in response.json()

def test_list_buckets():
    response = client.get("/buckets")
    assert response.status_code == 200
    assert isinstance(response.json()["buckets"], list)
