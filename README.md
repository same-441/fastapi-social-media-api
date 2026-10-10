# Social Media REST API

A REST API for a simple social media platform, built with FastAPI and PostgreSQL. Users can register, log in with JWT tokens, create and manage posts, and vote on posts.

Built as a practice project to learn production-style backend development with FastAPI.

## Features

- **User registration** with password hashing (Argon2)
- **JWT authentication** using OAuth2 password flow
- **Posts CRUD**: create, read, update and delete posts
- **Ownership checks**: only the author can edit or delete a post
- **Voting**: like or unlike a post, with protection against double votes
- **Search and pagination** on the post list (`search`, `Limit`, `skip`)
- **Vote counts** returned with every post via SQL join and aggregation
- **Database migrations** managed with Alembic
- **Interactive API docs** with Swagger UI

## Tech stack

Python · FastAPI · PostgreSQL · SQLAlchemy 2 (ORM) · Alembic · Pydantic v2 · python-jose (JWT) · passlib / Argon2

## Data model

| Table | Columns | Notes |
| --- | --- | --- |
| `users` | id, email, password, phone_number, created_at | Email is unique; password stored as hash |
| `posts` | id, title, content, published, created_at, owner_id | `owner_id` → `users.id`, cascade on delete |
| `votes` | user_id, post_id | Composite primary key: one vote per user per post |

## API endpoints

| Method | Endpoint | Auth | Description |
| --- | --- | --- | --- |
| `POST` | `/users/` | – | Register a new user |
| `GET` | `/users/{id}` | – | Get a user's public profile |
| `POST` | `/login` | – | Log in and receive a JWT access token |
| `GET` | `/posts/` | ✔ | List posts with vote counts (`?search=&Limit=&skip=`) |
| `GET` | `/posts/{id}` | ✔ | Get one post with its vote count |
| `POST` | `/posts/` | ✔ | Create a post |
| `PUT` | `/posts/{id}` | ✔ | Update your own post |
| `DELETE` | `/posts/{id}` | ✔ | Delete your own post |
| `POST` | `/vote/` | ✔ | Vote (`dir: 1`) or remove a vote (`dir: 0`) |

Endpoints marked ✔ need the header `Authorization: Bearer <token>`.

## Getting started

**1. Install dependencies** (Python 3.11+)

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
```

**2. Configure the environment**

Create a PostgreSQL database, then copy `.env.example` to `.env` and fill in your values. Generate a secret key with:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

**3. Create the tables**

```bash
alembic upgrade head
```

**4. Start the API**

```bash
uvicorn app.main:app --reload
```

Open **http://localhost:8000/docs** to try the API. Register a user, click **Authorize** and log in, then use the protected endpoints.

## Project structure

```
├── app/
│   ├── main.py        # App setup, CORS, routers
│   ├── config.py      # Settings loaded from .env
│   ├── database.py    # SQLAlchemy engine and session
│   ├── models.py      # Database tables
│   ├── schemas.py     # Request and response models
│   ├── oauth2.py      # JWT creation and validation
│   ├── utils.py       # Password hashing
│   └── routers/       # auth, users, posts, votes
├── alembic/           # Database migrations
├── alembic.ini
├── .env.example
└── requirements.txt
```

## Author

**Sammer** – M.Sc. Automotive Software Engineering, TU Chemnitz
