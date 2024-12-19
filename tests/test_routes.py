import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal
from app.models import URL
from sqlalchemy.orm import sessionmaker


# Set up a test database
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# Dependency override for testing
def override_get_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[override_get_db] = override_get_db

client = TestClient(app)

@pytest.fixture
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_shorten_url(test_db):
    response = client.post("/shorten", json={"original_url": "https://example.com"})
    assert response.status_code == 200
    data = response.json()
    assert "short_url" in data

def test_redirect_url(test_db):
    # Create a test URL
    client.post("/shorten", json={"original_url": "https://example.com"})
    # Get the short URL
    short_url = client.post("/shorten", json={"original_url": "https://example.com"}).json()["short_url"]
    # Test the redirect
    response = client.get(f"/{short_url}")
    assert response.status_code == 200
    assert response.json()["original_url"] == "https://example.com"
