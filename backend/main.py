from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings


from routes.chat import router as chat_router
from routes.health import router as health_router

app = FastAPI(title="ChatBot API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI ChatBot!"}

app.include_router(health_router, prefix="/api")
app.include_router(chat_router, prefix="/api")
