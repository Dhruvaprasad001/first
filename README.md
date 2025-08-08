# Blog Application

## Overview

This is a FastAPI-based blog application that provides user authentication, blog post creation, and management functionalities.

## Features

- User Registration and Authentication
- Create, Read, Update, and Delete (CRUD) Blog Posts
- Secure Password Hashing
- JWT-based Authentication
- SQLAlchemy ORM for Database Interactions

## Prerequisites

- Python 3.8+
- pip (Python Package Manager)

## Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
cd first
```

2. Create a virtual environment:

```bash
python -m venv blog-env
```

3. Activate the virtual environment:

- On Windows:

```bash
blog-env\Scripts\activate
```

- On macOS/Linux:

```bash
source blog-env/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI server:

```bash
uvicorn blog.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`

## API Documentation

Once the server is running, you can access:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Project Structure

```
first/
├── blog/
│   ├── __init__.py
│   ├── main.py           # FastAPI application setup
│   ├── database.py       # Database configuration
│   ├── model.py          # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   ├── oauth2.py         # Authentication logic
│   ├── token.py          # JWT token generation
│   ├── hashing.py        # Password hashing
│   ├── repository/       # Data access layer
│   │   ├── blog.py
│   │   └── user.py
│   └── routers/          # API route handlers
│       ├── authentication.py
│       ├── blog.py
│       └── user.py
├── blog-env/             # Virtual environment
└── requirements.txt      # Project dependencies
```

## Dependencies

- FastAPI
- Uvicorn
- Pydantic
- SQLAlchemy
- Passlib (Password hashing)
- Bcrypt
- Python-jose (JWT)
- Python-multipart

## Authentication

The application uses JWT (JSON Web Tokens) for user authentication. Users must register and then login to obtain an access token for protected routes.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

[Specify your license here]

## Contact

[Your Name/Contact Information]
