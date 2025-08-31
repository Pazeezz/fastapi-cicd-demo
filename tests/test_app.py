from fastapi.testclient import TestClient
from app.main import app
c = TestClient(app)

def test_root():
    r = c.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Hello, UOK students 2025 !"}
