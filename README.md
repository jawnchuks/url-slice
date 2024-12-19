# URL Slice Application

Welcome to the URL Slice Application! This project is a fast, reliable, and easy-to-use service for creating shortened URLs. It is built using **Python**, **FastAPI**, and comes with an interactive API documentation powered by **Swagger**.

---

## Features

- **Create Short URLs**: Quickly generate a shortened URL from a long URL.
- **Redirect**: Automatically redirect users to the original URL when the short link is accessed.
- **Custom Aliases**: Optionally create custom short links for easy memorization.
- **Interactive API Documentation**: Built-in Swagger UI for testing and exploring the API.
- **Lightweight and Scalable**: Built with FastAPI, optimized for performance and scalability.

---

## Tech Stack

- **Python**: Programming language used for development.
- **FastAPI**: Framework for building the API.
- **SQLite**: Default database for storing URL mappings (easily replaceable).
- **Uvicorn**: ASGI server for running the application.

---

## Installation

### Prerequisites
- Python 3.9 or later
- pip (Python package installer)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/jawnchuks/url-shortener.git
   cd url-shortener
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Access the application:
   - API Documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc Documentation: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Usage

### Endpoints

#### 1. Create a Short URL
**POST** `/shorten`

- **Request Body**:
  ```json
  {
    "long_url": "https://example.com",
    "custom_alias": "example"  # Optional
  }
  ```
- **Response**:
  ```json
  {
    "short_url": "http://127.0.0.1:8000/example"
  }
  ```

#### 2. Redirect to Original URL
**GET** `/{short_url}`

- Access a short URL, and it will redirect to the original URL.

#### 3. List All Short URLs (for Admin)
**GET** `/urls`

- **Response**:
  ```json
  [
    {
      "long_url": "https://example.com",
      "short_url": "http://127.0.0.1:8000/example",
      "created_at": "2024-01-01T00:00:00"
    }
  ]
  ```

---

## Project Structure
```
url-shortener/
├── app/
│   ├── main.py          # Application entry point
│   ├── models.py        # Database models
│   ├── routes.py        # API endpoints
│   ├── schemas.py       # Pydantic schemas
│   ├── database.py      # Database connection setup
├── tests/               # Unit and integration tests
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed explanation.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Contact

For any inquiries or issues, please contact:
- **GitHub**: [jawnchuks](https://github.com/jawnchuks)
- **Email**: jawnchuks@gmail.com
