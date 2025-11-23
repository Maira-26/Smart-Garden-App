# 🚀 Quick Setup Guide

## Step-by-Step Installation

### 1. Install Python Dependencies

Open terminal/command prompt in the project directory and run:

```bash
pip install -r requirements.txt
```

### 2. Get Your API Keys

#### OpenWeatherMap API (Required)
1. Go to https://openweathermap.org/api
2. Click "Sign Up" (free account)
3. After signup, go to "API Keys" section
4. Copy your API key
5. Free tier: 1,000 calls/day (perfect for this app!)

#### Google Gemini API (Required)
1. Go to https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key
5. Free tier: Generous limits for personal use

#### Perenual API (Optional - Has Fallback)
1. Go to https://perenual.com/docs/api
2. Sign up for free account
3. Get API key from dashboard
4. Free tier: 30 calls/day

### 3. Configure Environment Variables

1. **Copy the example file:**
   ```bash
   # Windows
   copy .env.example .env
   
   # Mac/Linux
   cp .env.example .env
   ```

2. **Open `.env` file in a text editor** and add your keys:
   ```env
   OPENWEATHER_API_KEY=your_actual_key_here
   GEMINI_API_KEY=your_actual_key_here
   PERENUAL_API_KEY=your_actual_key_here
   DEFAULT_LOCATION=Sialkot,PK
   ```

   **Important:** Replace `your_actual_key_here` with your real API keys!

### 4. Run the Application

```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

## ✅ Verification Checklist

- [ ] Python 3.8+ installed
- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file created with API keys
- [ ] OpenWeatherMap API key added
- [ ] Gemini API key added
- [ ] App runs without errors (`streamlit run app.py`)

## 🐛 Common Issues

### "Module not found" error
**Solution:** Make sure you installed dependencies:
```bash
pip install -r requirements.txt
```

### "API key not found" error
**Solution:** 
- Check that `.env` file exists in project root
- Verify API keys are correct (no extra spaces)
- Make sure keys are on separate lines

### Weather data not loading
**Solution:**
- Check internet connection
- Verify OpenWeatherMap API key is valid
- Check API quota hasn't been exceeded

### Plant identification not working
**Solution:**
- Verify Gemini API key is correct
- Check image quality (clear photos work best)
- Ensure API quota available

## 🎯 First Steps After Setup

1. **Add Your First Plant:**
   - Go to "🌱 Add a Plant" page
   - Upload a photo or add manually
   - Fill in plant details

2. **Check Dashboard:**
   - View weather for your location
   - See plant status and alerts

3. **Try AI Botanist:**
   - Ask questions about plant care
   - Upload photos for health diagnosis

## 📞 Need Help?

- Check the main `README.md` for detailed documentation
- Review error messages in terminal/console
- Verify all API keys are correct
- Ensure Python version is 3.8 or higher

---

**Happy Gardening! 🌱**

