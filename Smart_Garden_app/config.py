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
DEFAULT_COUNTRY_CODE = "PK"

# Country name to code mapping (common countries)
COUNTRY_CODE_MAP = {
    "pakistan": "PK", "pk": "PK",
    "united states": "US", "usa": "US", "us": "US",
    "united kingdom": "GB", "uk": "GB", "britain": "GB",
    "india": "IN", "in": "IN",
    "canada": "CA", "ca": "CA",
    "australia": "AU", "au": "AU",
    "germany": "DE", "de": "DE",
    "france": "FR", "fr": "FR",
    "spain": "ES", "es": "ES",
    "italy": "IT", "it": "IT",
    "china": "CN", "cn": "CN",
    "japan": "JP", "jp": "JP",
    "south korea": "KR", "kr": "KR",
    "brazil": "BR", "br": "BR",
    "mexico": "MX", "mx": "MX",
    "russia": "RU", "ru": "RU",
    "turkey": "TR", "tr": "TR",
    "saudi arabia": "SA", "sa": "SA",
    "uae": "AE", "united arab emirates": "AE", "ae": "AE",
    "bangladesh": "BD", "bd": "BD",
    "sri lanka": "LK", "lk": "LK",
    "nepal": "NP", "np": "NP",
    "afghanistan": "AF", "af": "AF",
    "iran": "IR", "ir": "IR",
    "iraq": "IQ", "iq": "IQ",
}

def get_country_code(country_name_or_code):
    """
    Convert country name to ISO country code
    Returns 2-letter country code (e.g., "PK", "US")
    """
    if not country_name_or_code:
        return DEFAULT_COUNTRY_CODE
    
    # If already a 2-letter code, return as-is
    country_str = str(country_name_or_code).strip()
    if len(country_str) == 2 and country_str.isalpha():
        return country_str.upper()
    
    # Try to find in mapping (case-insensitive)
    country_lower = country_str.lower()
    if country_lower in COUNTRY_CODE_MAP:
        return COUNTRY_CODE_MAP[country_lower]
    
    # If not found, return default
    print(f"⚠️ Country code not found for '{country_name_or_code}', using default: {DEFAULT_COUNTRY_CODE}")
    return DEFAULT_COUNTRY_CODE

def get_secret_value(st_secrets, key_variations):
    """
    Try to get a secret value using multiple key name variations and formats
    Supports both direct and nested formats in Streamlit secrets
    """
    # Try direct format first (most common on Streamlit Cloud)
    for key in key_variations:
        try:
            if key in st_secrets:
                value = st_secrets[key]
                if value and str(value).strip():
                    return str(value).strip()
        except (KeyError, AttributeError, TypeError):
            continue
    
    # Try nested format: st.secrets["api"]["key"]
    try:
        if "api" in st_secrets:
            api_secrets = st_secrets["api"]
            for key in key_variations:
                # Try exact key
                if key in api_secrets:
                    value = api_secrets[key]
                    if value and str(value).strip():
                        return str(value).strip()
                # Try lowercase key
                key_lower = key.lower()
                if key_lower in api_secrets:
                    value = api_secrets[key_lower]
                    if value and str(value).strip():
                        return str(value).strip()
                # Try without _API_KEY suffix
                key_short = key.replace("_API_KEY", "").replace("_KEY", "").lower()
                if key_short in api_secrets:
                    value = api_secrets[key_short]
                    if value and str(value).strip():
                        return str(value).strip()
    except (KeyError, AttributeError, TypeError):
        pass
    
    return None

def load_api_keys():
    """
    Load API keys from Streamlit secrets and set them as environment variables
    This ensures all services can access them via os.getenv()
    Call this function after Streamlit is initialized (in app.py)
    Supports multiple secret formats:
    - Direct: st.secrets["GROQ_API_KEY"]
    - Nested: st.secrets["api"]["groq_key"]
    """
    try:
        import streamlit as st
        
        # Load keys from Streamlit secrets and set as environment variables
        if hasattr(st, 'secrets') and st.secrets:
            keys_loaded = 0
            
            # OpenWeather API - try multiple key name variations
            openweather_key = get_secret_value(st.secrets, [
                "OPENWEATHER_API_KEY", "openweather_api_key", "OPENWEATHER_KEY", 
                "openweather_key", "OPENWEATHER", "openweather"
            ])
            if openweather_key:
                os.environ["OPENWEATHER_API_KEY"] = openweather_key
                keys_loaded += 1
            
            # Gemini API
            gemini_key = get_secret_value(st.secrets, [
                "GEMINI_API_KEY", "gemini_api_key", "GEMINI_KEY", 
                "gemini_key", "GEMINI", "gemini"
            ])
            if gemini_key:
                os.environ["GEMINI_API_KEY"] = gemini_key
                keys_loaded += 1
            
            # Groq API - try multiple key name variations
            groq_key = get_secret_value(st.secrets, [
                "GROQ_API_KEY", "groq_api_key", "GROQ_KEY", 
                "groq_key", "GROQ", "groq"
            ])
            if groq_key:
                os.environ["GROQ_API_KEY"] = groq_key
                keys_loaded += 1
            
            # Hugging Face API
            huggingface_key = get_secret_value(st.secrets, [
                "HUGGINGFACE_API_KEY", "huggingface_api_key", "HUGGINGFACE_KEY",
                "huggingface_key", "HUGGINGFACE", "huggingface"
            ])
            if huggingface_key:
                os.environ["HUGGINGFACE_API_KEY"] = huggingface_key
                keys_loaded += 1
            
            # Perenual API
            perenual_key = get_secret_value(st.secrets, [
                "PERENUAL_API_KEY", "perenual_api_key", "PERENUAL_KEY",
                "perenual_key", "PERENUAL", "perenual"
            ])
            if perenual_key:
                os.environ["PERENUAL_API_KEY"] = perenual_key
                keys_loaded += 1
            
            if keys_loaded > 0:
                print(f"✅ Loaded {keys_loaded} API key(s) from Streamlit secrets")
                return True
    except Exception as e:
        print(f"⚠️ Could not load from Streamlit secrets: {e}")
        import traceback
        traceback.print_exc()
    
    # Fallback: keys might already be in environment from .env file
    if os.getenv("OPENWEATHER_API_KEY") or os.getenv("GROQ_API_KEY"):
        print("✅ Using API keys from environment variables (.env file)")
        return True
    
    print("❌ No API keys found in secrets or environment")
    return False

# Helper functions to get API keys (for services to use)
def get_openweather_key():
    """Get OpenWeather API key from environment"""
    return os.getenv("OPENWEATHER_API_KEY", "")

def get_groq_key():
    """Get Groq API key from environment or secrets"""
    # First check environment (set by load_api_keys)
    key = os.getenv("GROQ_API_KEY", "")
    if key:
        return key
    
    # Fallback: Try to get directly from Streamlit secrets (in case load_api_keys wasn't called)
    try:
        import streamlit as st
        if hasattr(st, 'secrets') and st.secrets:
            # Try direct format
            if "GROQ_API_KEY" in st.secrets:
                key = st.secrets["GROQ_API_KEY"]
                if key:
                    os.environ["GROQ_API_KEY"] = str(key).strip()
                    return str(key).strip()
            
            # Try nested format
            if "api" in st.secrets:
                api_secrets = st.secrets["api"]
                for key_name in ["groq_key", "GROQ_KEY", "groq_api_key", "GROQ_API_KEY"]:
                    if key_name in api_secrets:
                        key = api_secrets[key_name]
                        if key:
                            os.environ["GROQ_API_KEY"] = str(key).strip()
                            return str(key).strip()
    except Exception as e:
        print(f"⚠️ Error checking Streamlit secrets for Groq key: {e}")
    
    return ""

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