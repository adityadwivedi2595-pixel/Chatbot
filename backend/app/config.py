import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    LLM_API_KEY = os.getenv("LLM_API_KEY")
    SEARCH_API_KEY = os.getenv("SEARCH_API_KEY")
    EMBEDDING_API_KEY = os.getenv("EMBEDDING_API_KEY")
    TTS_API_KEY = os.getenv("TTS_API_KEY")
    STT_API_KEY = os.getenv("STT_API_KEY")

settings = Settings()
