from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import List

# Initializing the API App Engine
app = FastAPI(title="DecodeLabs Project 2: Backend API")

# Simulated Data Persistence Layer (In-Memory Database)
users_db = [
    {"id": 1, "name": "Martina Plantijn", "email": "martina@example.com"},
    {"id": 2, "name": "Alex Mercer", "email": "alex@example.com"}
]

# --- DATA VALIDATION MODELS ---
# Using Pydantic to validate input data (Key Requirement)
class UserCreate(BaseModel):
    name: str
    email: EmailStr  # Automatically rejects invalid email formats

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

# --- RESTFUL ENDPOINTS ---

# 1. GET /users (Resource Retrieval)
# Standard: Safe, Idempotent, returns nouns as resources
@app.get("/users", response_model=List[UserResponse], status_code=status.HTTP_200_OK)
def get_all_users():
    return users_db

# 2. GET /users/{id} (Specific Retrieval & Error Handling)
# Handles 404 validation gracefully as an intentional learning opportunity
@app.get("/users/{id}", response_model=UserResponse)
def get_user_by_id(id: int):
    for user in users_db:
        if user["id"] == id:
            return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"User with ID {id} does not exist."
    )

# 3. POST /users (Resource Creation)
# Standard: Unsafe, Non-idempotent, handles incoming user data streams
@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_input: UserCreate):
    # Auto-increment the ID based on the last user in our list
    new_id = users_db[-1]["id"] + 1 if users_db else 1
    
    new_user = {
        "id": new_id,
        "name": user_input.name,
        "email": user_input.email
    }
    
    users_db.append(new_user)
    return new_user

