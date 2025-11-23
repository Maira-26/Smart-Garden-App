"""
Configuration file for Smart Garden App
Loads environment variables from Streamlit secrets (Cloud) or .env file (Local)
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

# Default Settings
DEFAULT_LOCATION = os.getenv("DEFAULT_LOCATION", "Sialkot,PK")
DEFAULT_CITY = "Sialkot"
DEFAULT_COUNTRY = "Pakistan"

def load_api_keys():
    """
    Load API keys from Streamlit secrets and set them as environment variables
    This ensures all services can access them via os.getenv()
    Call this function after Streamlit is initialized (in app.py)
    """
    try:
        import streamlit as st
        
        # Load keys from Streamlit secrets and set as environment variables
        if hasattr(st, 'secrets'):
            # OpenWeather API
            if "OPENWEATHER_API_KEY" in st.secrets:
                os.environ["OPENWEATHER_API_KEY"] = st.secrets["OPENWEATHER_API_KEY"]
            
            # Gemini API
            if "GEMINI_API_KEY" in st.secrets:
                os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
            
            # Groq API
            if "GROQ_API_KEY" in st.secrets:
                os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
            
            # Hugging Face API
            if "HUGGINGFACE_API_KEY" in st.secrets:
                os.environ["HUGGINGFACE_API_KEY"] = st.secrets["HUGGINGFACE_API_KEY"]
            
            # Perenual API (if you use it)
            if "PERENUAL_API_KEY" in st.secrets:
                os.environ["PERENUAL_API_KEY"] = st.secrets["PERENUAL_API_KEY"]
            
            print("✅ API keys loaded from Streamlit secrets")
            return True
    except Exception as e:
        print(f"⚠️ Could not load from Streamlit secrets: {e}")
    
    # Fallback: keys might already be in environment from .env file
    if os.getenv("OPENWEATHER_API_KEY"):
        print("✅ Using API keys from environment variables (.env file)")
        return True
    
    print("❌ No API keys found in secrets or environment")
    return False

# Helper functions to get API keys (for services to use)
def get_openweather_key():
    """Get OpenWeather API key from environment"""
    return os.getenv("OPENWEATHER_API_KEY", "")

def get_groq_key():
    """Get Groq API key from environment"""
    return os.getenv("GROQ_API_KEY", "")

def get_gemini_key():
    """Get Gemini API key from environment"""
    return os.getenv("GEMINI_API_KEY", "")

def get_huggingface_key():
    """Get Hugging Face API key from environment"""
    return os.getenv("HUGGINGFACE_API_KEY", "")

def get_perenual_key():
    """Get Perenual API key from environment"""
    return os.getenv("PERENUAL_API_KEY", "")

# API Endpoints
OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5"
PERENUAL_BASE_URL = "https://perenual.com/api"

# Data Storage
PLANTS_DB_FILE = "plants_database.json"
CHAT_HISTORY_FILE = "chat_history.json"

# App Settings
WATERING_CHECK_TIME = "08:00"  # Daily check time
MAX_PLANTS = 50  # Maximum number of plants user can add