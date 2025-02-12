from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings

# ✅ Import routers correctly (AFTER FastAPI is initialized)
from routes.chat import router as chat_router
from routes.health import router as health_router

app = FastAPI(title="ChatBot API", version="1.0.0")

# ✅ CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Root Route (Fix "Not Found" Issue)
@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI ChatBot!"}

# ✅ Include Modular Routes AFTER defining FastAPI app
app.include_router(health_router, prefix="/api")
app.include_router(chat_router, prefix="/api")
