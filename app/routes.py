import random
import string
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter()

# Helper function to generate short URLs
def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@router.post("/shorten", response_model=schemas.URLResponse)
def shorten_url(url: schemas.URLCreate, db: Session = Depends(database.get_db)):
    # Check if URL already exists
    existing_url = db.query(models.URL).filter(models.URL.original_url == url.original_url).first()
    if existing_url:
        return existing_url

    # Generate a new short URL
    short_url = generate_short_url()
    new_url = models.URL(original_url=url.original_url, short_url=short_url)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return new_url

@router.get("/{short_url}")
def redirect_url(short_url: str, db: Session = Depends(database.get_db)):
    url = db.query(models.URL).filter(models.URL.short_url == short_url).first()
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url.original_url)


