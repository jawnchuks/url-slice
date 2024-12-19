from pydantic import BaseModel

class URLBase(BaseModel):
    original_url: str

class URLCreate(URLBase):
    pass

class URLResponse(URLBase):
    short_url: str

    class Config:
        orm_mode = True
