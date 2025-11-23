# 🚀 Streamlit Cloud Setup Guide

## ⚠️ Important: Environment Variables on Streamlit Cloud

**Streamlit Cloud does NOT use `.env` files!** You must set environment variables in the Streamlit Cloud dashboard.

---

## 📋 Step-by-Step Setup

### Step 1: Deploy Your App to Streamlit Cloud

1. Push your code to GitHub (make sure `.env` is NOT committed)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app"
4. Connect your GitHub repository
5. Select your branch (usually `main`)
6. Set main file path: `app.py`

### Step 2: Set Environment Variables

**In the Streamlit Cloud dashboard:**

1. Click on your app
2. Click **"⚙️ Settings"** (gear icon in top right)
3. Scroll down to **"Secrets"** section
4. Click **"Edit secrets"** or **"Add secrets"**

### Step 3: Add Your API Keys

**Copy and paste this format into the secrets editor:**

```toml
OPENWEATHER_API_KEY = "your_openweather_api_key_here"
GEMINI_API_KEY = "your_gemini_api_key_here"
GROQ_API_KEY = "your_groq_api_key_here"
PERENUAL_API_KEY = "your_perenual_api_key_here"
HUGGINGFACE_API_KEY = "your_huggingface_api_key_here"
DEFAULT_LOCATION = "Sialkot,PK"
```

**Important Notes:**
- Use **quotes** around values in TOML format
- NO spaces around `=`
- One key per line
- Replace `your_xxx_api_key_here` with your actual keys

### Step 4: Save and Redeploy

1. Click **"Save"**
2. Streamlit Cloud will automatically redeploy
3. Wait for deployment to complete (usually 1-2 minutes)

---

## 🔑 Where to Get API Keys

### 1. OpenWeatherMap API Key
- **URL:** https://openweathermap.org/api
- **Free tier:** 1,000 calls/day
- **Format:** `99fe79fbdcc1796003cced4d01e1b3c7`

### 2. Google Gemini API Key
- **URL:** https://makersuite.google.com/app/apikey
- **Free tier:** 15 requests/minute
- **Format:** Starts with `AIza...`

### 3. Groq API Key
- **URL:** https://console.groq.com/
- **Free tier:** Generous free tier
- **Format:** Starts with `gsk_...`

### 4. Hugging Face API Key (Optional)
- **URL:** https://huggingface.co/settings/tokens
- **Free tier:** Available
- **Format:** Starts with `hf_...`
- **Note:** If not set, plant identification features will use fallback methods

### 5. Perenual API Key (Optional)
- **URL:** https://perenual.com/docs/api
- **Free tier:** Limited
- **Note:** Optional - app works without it

---

## ✅ Verification Checklist

After setting secrets, verify:

- [ ] All API keys are set in Streamlit Cloud secrets
- [ ] App redeploys successfully
- [ ] No errors in Streamlit Cloud logs
- [ ] Weather data loads correctly
- [ ] Chatbot responds to messages
- [ ] Location detection works (or can be set manually)

---

## 🐛 Troubleshooting

### Issue: "API key not found" errors

**Solution:**
1. Check that secrets are saved in Streamlit Cloud dashboard
2. Verify key names match exactly (case-sensitive)
3. Make sure you clicked "Save" after editing secrets
4. Wait for app to redeploy (check deployment status)

### Issue: Chatbot not responding

**Solution:**
1. Verify `GROQ_API_KEY` is set in secrets
2. Check Streamlit Cloud logs for API errors
3. Test Groq API key locally first

### Issue: Weather showing wrong location

**Solution:**
1. Location is auto-detected from IP address
2. If wrong, go to "📍 Location & Nurseries" page
3. Click "🔍 Detect Location" to re-detect
4. Or manually enter your city and country
5. Click "💾 Save Location"

### Issue: Location detection not working

**Solution:**
1. IP-based detection may not work on Streamlit Cloud servers
2. Manually set your location:
   - Go to "📍 Location & Nurseries" page
   - Enter your city and country manually
   - Click "💾 Save Location"

---

## 📝 Example Secrets Configuration

Here's what your secrets should look like in Streamlit Cloud:



---

## 🔒 Security Notes

- ✅ Secrets in Streamlit Cloud are encrypted
- ✅ Secrets are NOT visible in your code
- ✅ Secrets are NOT in your GitHub repository
- ✅ Only you (and collaborators you add) can see secrets

---

## 🎯 Quick Reference

| Setting | Location | Format |
|---------|----------|--------|
| Streamlit Cloud Secrets | Dashboard → Settings → Secrets | TOML format |
| Local Development | `.env` file | KEY=VALUE format |
| GitHub | ❌ Never commit | Use `.gitignore` |

---

## 📞 Need Help?

If you encounter issues:

1. Check Streamlit Cloud logs (click "Manage app" → "Logs")
2. Verify all required API keys are set
3. Test API keys locally first
4. Check API key formats match examples above

**Your app should now work perfectly on Streamlit Cloud! 🎉**

