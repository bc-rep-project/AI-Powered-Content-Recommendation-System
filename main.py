import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to AI Content Recommendation API", "status": "online"}

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ai-powered-content-recommendation-frontend.vercel.app",
        "https://ai-powered-content-recommendation-frontend-kslis1lqp.vercel.app",
        "*"  # During development - remove in production
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add authentication endpoints
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class UserLogin(BaseModel):
    email: str
    password: str

@app.post("/auth/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        # Add your authentication logic here
        # This is a basic example - implement proper authentication!
        if form_data.username == "test@example.com" and form_data.password == "password":
            return {"access_token": "dummy_token", "token_type": "bearer"}
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/login")
async def login(user_data: UserLogin):
    try:
        # Add your login logic here
        return {"message": "Login successful"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/register")
async def register(user_data: UserLogin):
    try:
        # Add your registration logic here
        return {"message": "Registration successful"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 