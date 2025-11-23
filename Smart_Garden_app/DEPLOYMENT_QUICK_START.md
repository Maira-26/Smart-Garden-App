# 🚀 Quick Deployment Guide - Streamlit Cloud

## Prerequisites Checklist

Before deploying, ensure you have:

- [ ] GitHub account
- [ ] All API keys ready (see below)
- [ ] Code pushed to GitHub repository

## Step 1: Push to GitHub

1. **Initialize Git** (if not already done):
   ```bash
   cd Smart_Garden_app
   git init
   git add .
   git commit -m "Initial commit - Smart Garden App"
   ```

2. **Create GitHub Repository**:
   - Go to https://github.com/new
   - Create a new repository (e.g., `smart-garden-app`)
   - **DO NOT** initialize with README (if you already have one)

3. **Push to GitHub**:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/smart-garden-app.git
   git branch -M main
   git push -u origin main
   ```

## Step 2: Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud**:
   - Visit: https://share.streamlit.io
   - Sign in with your GitHub account

2. **Create New App**:
   - Click "New app"
   - Select your repository: `YOUR_USERNAME/smart-garden-app`
   - Select branch: `main`
   - **Main file path**: `app.py` ⚠️ **IMPORTANT: Use `app.py` not `Smart_Garden_app/app.py`**
   - Click "Deploy!"

## Step 3: Configure Secrets

**⚠️ CRITICAL: Set these in Streamlit Cloud Dashboard**

1. In your app dashboard, click **"⚙️ Settings"** (top right)
2. Scroll to **"Secrets"** section
3. Click **"Edit secrets"**
4. Paste this format (replace with your actual keys):

```toml
OPENWEATHER_API_KEY = "your_openweather_key_here"
GEMINI_API_KEY = "your_gemini_key_here"
GROQ_API_KEY = "your_groq_key_here"
HUGGINGFACE_API_KEY = "your_huggingface_key_here"
PERENUAL_API_KEY = "your_perenual_key_here"
DEFAULT_LOCATION = "Sialkot,PK"
```

5. Click **"Save"** - App will auto-redeploy

## Step 4: Verify Deployment

After deployment completes:

- [ ] App loads without errors
- [ ] Weather data displays correctly
- [ ] AI Botanist chat responds
- [ ] Can add plants successfully
- [ ] Location detection works (or can be set manually)

## 🔑 Getting API Keys

### OpenWeatherMap (Required)
- URL: https://openweathermap.org/api
- Free tier: 1,000 calls/day
- Get key from dashboard after signup

### Google Gemini (Required)
- URL: https://makersuite.google.com/app/apikey
- Free tier: Generous limits
- Sign in with Google account

### Groq (Required)
- URL: https://console.groq.com/
- Free tier: Available
- Create account and generate API key

### Hugging Face (Optional)
- URL: https://huggingface.co/settings/tokens
- Free tier: Available
- Used for plant identification

### Perenual (Optional)
- URL: https://perenual.com/docs/api
- Free tier: Limited
- App works without this

## 📁 Important File Structure

Your GitHub repository should have this structure:

```
smart-garden-app/
├── app.py                    # ⚠️ Main entry point
├── config.py
├── requirements.txt
├── .streamlit/
│   └── config.toml          # Streamlit configuration
├── utils/
│   ├── __init__.py
│   ├── data_manager.py
│   ├── weather_service.py
│   ├── plant_service.py
│   ├── gemini_service.py
│   ├── groq_service.py
│   └── huggingface_service.py
└── README.md
```

**⚠️ Note**: If your app is in a subdirectory, adjust the main file path in Streamlit Cloud settings.

## 🐛 Common Issues

### Issue: "ModuleNotFoundError"
**Solution**: Check that `requirements.txt` includes all dependencies and main file path is correct.

### Issue: "API key not found"
**Solution**: 
- Verify secrets are saved in Streamlit Cloud dashboard
- Check key names match exactly (case-sensitive)
- Wait for app to redeploy after saving secrets

### Issue: "App not found" or 404
**Solution**: 
- Verify main file path is `app.py` (or correct relative path)
- Check that app.py exists in the root of your repository branch

### Issue: Location detection not working
**Solution**: 
- IP-based detection may not work on Streamlit Cloud servers
- Users can manually set location in "📍 Location & Nurseries" page

## ✅ Success Checklist

After deployment, your app should:
- ✅ Load without errors
- ✅ Display weather information
- ✅ Allow adding plants
- ✅ Respond to AI Botanist questions
- ✅ Show garden dashboard with plant status

## 📞 Need Help?

1. Check Streamlit Cloud logs: Dashboard → "Manage app" → "Logs"
2. Verify all API keys are set correctly
3. Test API keys locally first
4. Review error messages in logs

---

**🎉 Your app is now live on Streamlit Cloud!**

Share your app URL: `https://YOUR_APP_NAME.streamlit.app`

