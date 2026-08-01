# Helpdesk Ticket System API

A REST API for managing IT support tickets built with Python and FastAPI.

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication
- bcrypt password hashing

## Features

- User registration and login with JWT authentication
- Create, read, update and close support tickets
- Role based access (admin and user)
- Secure password hashing with bcrypt
- PostgreSQL database with SQLAlchemy ORM

## Project Structure

helpdesk-ticket-system/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── auth.py
├── requirements.txt
├── .env
└── routers/
├── users.py
└── tickets.py


## Setup and Installation

1. Clone the repository

git clone https://github.com/Sufyan240403/helpdesk-ticket-system.git


2. Create virtual environment

python -m venv venv
venv\Scripts\activate


3. Install dependencies

pip install -r requirements.txt


4. Create .env file with your values

DATABASE_URL=postgresql://postgres:yourpassword@localhost/helpdesk_db
SECRET_KEY=yoursecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30


5. Run the application

uvicorn main:app --reload


## API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /auth/register | Register new user |
| POST | /auth/login | Login and get JWT token |

### Tickets
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /tickets | Get all tickets |
| GET | /tickets/{id} | Get one ticket |
| POST | /tickets | Create ticket |
| PUT | /tickets/{id} | Update ticket |
| PATCH | /tickets/{id}/close | Close ticket |
| DELETE | /tickets/{id} | Delete ticket |

## API Documentation

Once running visit:

http://127.0.0.1:8000/docs


## Built By

Sufyan Mahmood