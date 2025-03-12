# main.py
from datetime import timedelta
from http.client import HTTPException
from typing import List
from uuid import UUID, uuid4
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from auth import create_access_token, get_current_user, hash_password, verify_password
from models import Gender, Role, UpdateUser, User

app = FastAPI()
db: List[User] = [
 User(
 id=uuid4(),
 first_name="John",
 last_name="Doe",
 gender=Gender.male,
 roles=[Role.user],
 ),
 User(
 id=uuid4(),
 first_name="Jane",
 last_name="Doe",
 gender=Gender.female,
 roles=[Role.user],
 ),
 User(
 id=uuid4(),
 first_name="James",
 last_name="Gabriel",
 gender=Gender.male,
 roles=[Role.user],
 ),
 User(
 id=uuid4(),
 first_name="Eunit",
 last_name="Eunit",
 gender=Gender.male,
 roles=[Role.admin, Role.user],
 ),
]

# Simulación de usuarios en memoria (esto debería ser una base de datos)
fake_users_db = {
    "admin": {"username": "admin", "hashed_password": hash_password("1234")},
}

# Modelo de datos para el login
class LoginData(BaseModel):
    username: str
    password: str

# Endpoint de login
@app.post("/login")
def login(data: LoginData):
    user = fake_users_db.get(data.username)
    if not user or not verify_password(data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos")
    
    access_token = create_access_token(data={"sub": data.username}, expires_delta=timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}

# Endpoint protegido con JWT
@app.get("/users/me")
def read_users_me(current_user: dict = Depends(get_current_user)):
    return {"message": f"Bienvenido {current_user['username']}"}

@app.get("/")
async def root():
 return {"greeting":"Hello world"}

@app.get("/api/v1/users")
async def get_users():
 return db

@app.get("/api/v1/user/{id}")
async def get_users(id: UUID):
    for user in db:
        if user.id == id:
            return user
    raise HTTPException(
        status_code=404, detail=f"Get user failed, id {id} not found."
    )

@app.post("/api/v1/users")
async def create_user(user: User):
 db.append(user)
 return {"id": user.id}

@app.delete("/api/v1/users/{id}")
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404, detail=f"Delete user failed, id {id} not found."
    )

@app.put("/api/v1/users/{id}")
async def update_user(user_update: UpdateUser, id: UUID):
    for user in db:
        if user.id == id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.roles is not None:
                user.roles = user_update.roles
        return user.id
    raise HTTPException(status_code=404, detail=f"Could not find user with id: {id}")