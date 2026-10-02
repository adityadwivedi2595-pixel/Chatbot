from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import chat, documents, search, voice, image, health

app = FastAPI(title="Multimodal AI Personal Assistant", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For MVP only; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat.router, prefix="/api/chat", tags=["Chat"])
app.include_router(documents.router, prefix="/api/documents", tags=["Documents"])
app.include_router(search.router, prefix="/api/search", tags=["Search"])
app.include_router(voice.router, prefix="/api/voice", tags=["Voice"])
app.include_router(image.router, prefix="/api/image", tags=["Image"])
app.include_router(health.router, prefix="/api/health", tags=["Health"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Multimodal AI Personal Assistant API"}
