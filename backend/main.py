from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend (http://localhost:5173) to access the backend (http://127.0.0.1:8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to ["http://localhost:5173"] for better security
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def read_root():
    return {"message": "Welcome to NemNatur API"}

@app.get("/products")
def get_products():
    return [
        {"name": "Mærk Naturen", "description": "Experience nature through senses"},
        {"name": "Hulebyggeri", "description": "Build shelters in the woods"},
    ]
