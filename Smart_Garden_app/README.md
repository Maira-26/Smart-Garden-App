# 🌱 Smart Garden App

A comprehensive AI-powered plant care application that helps you manage your garden using weather data, AI plant identification, and smart care reminders - **all without physical sensors!**

## ✨ Features

### 📊 Garden Dashboard
- **Real-time Weather Display**: Current weather conditions for your location (default: Sialkot, Pakistan)
- **Smart Plant Status Cards**: Each plant shows:
  - Watering status (Needs Water / Happy)
  - Sun exposure estimate based on weather + placement
  - Care recommendations
- **Intelligent Alerts**:
  - 🌧️ Rain alerts for outdoor plants
  - ⚠️ Storm warnings (thunderstorm, hail)
  - ☀️ Heat alerts when temperature exceeds 35°C

### 🌱 Add a Plant
- **AI Plant Identification**: Upload a photo and let Google Gemini identify your plant
- **Manual Entry**: Add plants manually with all care details
- **Smart Configuration**: Set placement (Open Roof, Balcony, Indoor Window) and sun preferences

### 🤖 AI Botanist Chat
- **Plant Care Q&A**: Ask questions about plant care
- **Health Diagnosis**: Upload photos for AI-powered health analysis
- **Contextual Advice**: AI considers your weather and plant list

## 🧠 Smart Features (No Sensors Required!)

### 1. Virtual Sun Sensor
- Uses OpenWeatherMap API for cloud cover and sunrise/sunset times
- Combines with user input (placement + sun preference) to estimate actual sun exposure
- Provides recommendations based on temperature and sun intensity

### 2. Smart Water Reminder
- **Weather-Aware**: Adjusts watering schedule based on:
  - Recent rainfall (resets timer)
  - Expected rain (pauses notifications)
  - High temperature >35°C (increases frequency)
- **Plant-Specific**: Each plant has its own watering interval

### 3. Shelter Alerts
- Monitors weather forecasts for severe conditions
- Alerts users to move outdoor plants indoors before storms
- Provides time estimates (e.g., "Rain in 2 hours")

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Python web framework)
- **AI/ML**: Google Gemini API (for plant identification and chat)
- **Weather Data**: OpenWeatherMap API (free tier)
- **Plant Database**: Perenual API (free tier)
- **Storage**: JSON files (lightweight, can upgrade to SQLite)

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- API keys for:
  - Google Gemini API
  - OpenWeatherMap API
  - Perenual API (optional, has fallback)

### Step 1: Clone/Download the Project

```bash
cd Smart_Garden_app
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure API Keys

1. Copy the example environment file:
```bash
copy .env.example .env
```

2. Edit `.env` and add your API keys:

```env
# OpenWeatherMap API Key (Get free key at https://openweathermap.org/api)
OPENWEATHER_API_KEY=your_openweather_api_key_here

# Google Gemini API Key (Get free key at https://makersuite.google.com/app/apikey)
GEMINI_API_KEY=your_gemini_api_key_here

# Perenual API Key (Optional - Get at https://perenual.com/docs/api)
PERENUAL_API_KEY=your_perenual_api_key_here

# Default Location
DEFAULT_LOCATION=Sialkot,PK
```

### Step 4: Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 🔑 Getting API Keys (Free Tiers)

### 1. OpenWeatherMap API
- Visit: https://openweathermap.org/api
- Sign up for free account
- Get API key from dashboard
- Free tier: 1,000 calls/day (more than enough!)

### 2. Google Gemini API
- Visit: https://makersuite.google.com/app/apikey
- Sign in with Google account
- Create new API key
- Free tier: Generous limits for personal use

### 3. Perenual API (Optional)
- Visit: https://perenual.com/docs/api
- Sign up for free account
- Get API key
- Free tier: 30 calls/day

## 📁 Project Structure

```
Smart_Garden_app/
├── app.py                      # Main Streamlit application
├── config.py                   # Configuration and environment variables
├── requirements.txt            # Python dependencies
├── .env.example               # Example environment file
├── README.md                   # This file
├── utils/
│   ├── weather_service.py     # OpenWeatherMap API integration
│   ├── plant_service.py        # Plant data and care logic
│   ├── gemini_service.py       # Google Gemini AI integration
│   └── data_manager.py         # Data storage (JSON files)
├── plant_images/               # Uploaded plant photos (auto-created)
├── plants_database.json        # Plant data storage (auto-created)
└── chat_history.json          # Chat history (auto-created)
```

## 🎯 Usage Guide

### Adding Your First Plant

1. Go to **"🌱 Add a Plant"** page
2. Upload a clear photo of your plant (optional but recommended)
3. Click **"🔍 Identify with AI"** to auto-fill plant details
4. Complete the form:
   - Select placement (Open Roof, Balcony, or Indoor Window)
   - Choose sun exposure preference
   - Set watering interval (days)
5. Click **"✅ Add Plant to Garden"**

### Monitoring Your Garden

1. Go to **"📊 Garden Dashboard"**
2. View weather conditions for your location
3. Check each plant's status:
   - Green badge = Happy, no action needed
   - Blue badge = Needs water soon
   - Red badge = Needs water today
4. Read alerts for rain, storms, or heat
5. Click **"💧 Mark Watered"** after watering

### Getting Plant Care Advice

1. Go to **"🤖 AI Botanist"** page
2. Type your question (e.g., "Why are leaves yellow?")
3. Optionally upload a photo for health diagnosis
4. Get AI-powered advice based on your plants and weather

## 🔧 Customization

### Change Default Location

Edit `.env` file:
```env
DEFAULT_LOCATION=YourCity,CountryCode
```

Or edit `config.py`:
```python
DEFAULT_CITY = "YourCity"
DEFAULT_COUNTRY = "CountryCode"
```

### Adjust Watering Check Time

Edit `config.py`:
```python
WATERING_CHECK_TIME = "08:00"  # Daily check time
```

## 🐛 Troubleshooting

### API Key Errors
- Ensure `.env` file exists and contains valid API keys
- Check that API keys are not expired
- Verify API key format (no extra spaces)

### Weather Data Not Loading
- Check internet connection
- Verify OpenWeatherMap API key is valid
- Check if city name is correct in config

### Plant Identification Not Working
- Ensure Gemini API key is configured
- Check image quality (clear, well-lit photos work best)
- Verify API quota hasn't been exceeded

### Data Not Saving
- Check file permissions in project directory
- Ensure `plants_database.json` and `chat_history.json` can be created
- Check disk space

## 🚀 Future Enhancements

- [ ] SQLite database for better data management
- [ ] Email/SMS notifications for alerts
- [ ] Plant growth tracking with photos over time
- [ ] Integration with smart home devices
- [ ] Mobile app version
- [ ] Multi-user support
- [ ] Plant care calendar
- [ ] Fertilizer reminders

## 📝 License

This project is open source and available for personal and educational use.

## 🙏 Credits

- **OpenWeatherMap** for weather data
- **Google Gemini** for AI capabilities
- **Perenual** for plant database
- **Streamlit** for the amazing framework

## 📧 Support

For issues or questions, please check the troubleshooting section or create an issue in the repository.

---

**Built with ❤️ for plant lovers everywhere! 🌱**

