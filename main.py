from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS to allow communication from the frontend
origins = [
    "http://localhost",
    "http://localhost:8000", # If served by Uvicorn on another port
    "http://127.0.0.1:8000", # Common for local development
    "null" # For file:// access in some browsers during local testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/add")
async def add(a: float, b: float):
    return {"result": a + b}

@app.get("/sub")
async def subtract(a: float, b: float):
    return {"result": a - b}

@app.get("/mul")
async def multiply(a: float, b: float):
    return {"result": a * b}

@app.get("/div")
async def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
    return {"result": a / b}

from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
def home():
    return open("index.html").read()
