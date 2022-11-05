from fastapi.testclient import TestClient
from src.app.app import app


class TestPictureInvert:
    client = TestClient(app)
