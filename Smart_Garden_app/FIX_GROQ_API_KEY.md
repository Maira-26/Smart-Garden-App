# 🔧 Fix: Groq API Key Not Configured

## ⚠️ Error Message
```
🌱 I'm here to help with your plant care questions! However, the Groq API key is not configured. 
Please set your GROQ_API_KEY in Streamlit Cloud secrets (Settings → Secrets) to enable AI chat responses.
```

---

## ✅ Solution: Add Groq API Key to Streamlit Cloud

### Step 1: Get Your Groq API Key

1. **Go to Groq Console:**
   - Visit: https://console.groq.com/
   - Sign in (or create account if needed)

2. **Create API Key:**
   - Click on **"API Keys"** in the left menu
   - Click **"Create API Key"** button
   - Copy your API key (starts with `gsk_...`)
   - ⚠️ **Save it immediately** - you won't see it again!

---

### Step 2: Add Key to Streamlit Cloud

1. **Go to Streamlit Cloud:**
   - Visit: https://share.streamlit.io
   - Sign in with your GitHub account

2. **Open Your App:**
   - Click on your **Smart Garden App**

3. **Open Settings:**
   - Click the **⚙️ Settings** button (gear icon in top right corner)

4. **Go to Secrets:**
   - Scroll down to find **"Secrets"** section
   - Click **"Edit secrets"** or **"Add secrets"** button

5. **Add Your API Key:**
   - In the secrets editor, add this line:
   
   ```toml
   GROQ_API_KEY = "gsk_your_actual_key_here"
   ```
   
   **Important:**
   - Replace `gsk_your_actual_key_here` with your actual Groq API key
   - Keep the quotes around the key
   - Use TOML format (shown above)

6. **If You Have Other Keys:**
   - Add all your API keys in the same secrets file:
   
   ```toml
   OPENWEATHER_API_KEY = "your_openweather_key"
   GEMINI_API_KEY = "your_gemini_key"
   GROQ_API_KEY = "gsk_your_groq_key"
   HUGGINGFACE_API_KEY = "your_huggingface_key"
   PERENUAL_API_KEY = "your_perenual_key"
   DEFAULT_LOCATION = "Sialkot,PK"
   ```

7. **Save:**
   - Click **"Save"** button at the bottom
   - Streamlit Cloud will automatically redeploy your app

8. **Wait for Redeploy:**
   - Wait 1-2 minutes for deployment to complete
   - Check the deployment status (should show "Running")

---

### Step 3: Test Your App

1. **Open Your App:**
   - Go to your app URL (e.g., `https://your-app-name.streamlit.app`)

2. **Test Chatbot:**
   - Go to "🤖 AI Botanist" page
   - Type a question like: "How do I water my plants?"
   - The chatbot should now respond!

---

## 🎯 Quick Visual Guide

```
Streamlit Cloud Dashboard
    ↓
Click Your App
    ↓
Click ⚙️ Settings (top right)
    ↓
Scroll to "Secrets" section
    ↓
Click "Edit secrets"
    ↓
Add: GROQ_API_KEY = "gsk_your_key_here"
    ↓
Click "Save"
    ↓
Wait 1-2 minutes for redeploy
    ↓
✅ Done! Chatbot should work now
```

---

## 🔑 Where to Get Groq API Key

1. **Visit:** https://console.groq.com/
2. **Sign in** (or create free account)
3. **Go to:** API Keys section
4. **Click:** "Create API Key"
5. **Copy** the key (starts with `gsk_`)

**Free Tier:** Groq offers generous free tier - perfect for your app!

---

## ⚠️ Common Mistakes

### ❌ Wrong Format:
```toml
GROQ_API_KEY = gsk_abc123  # Missing quotes
```

### ✅ Correct Format:
```toml
GROQ_API_KEY = "gsk_abc123"  # With quotes
```

---

## 🐛 Still Not Working?

### Check These:

1. **API Key Format:**
   - Should start with `gsk_`
   - Should be in quotes: `"gsk_..."`
   - No extra spaces

2. **Saved Correctly:**
   - Make sure you clicked "Save" button
   - Check that key appears in secrets list

3. **Redeployed:**
   - Wait 1-2 minutes after saving
   - Check deployment status shows "Running"

4. **Test Locally First:**
   - Add key to your local `.env` file
   - Test with: `streamlit run app.py`
   - If it works locally, the key is correct

5. **Check Logs:**
   - In Streamlit Cloud, click "Manage app"
   - Click "Logs" tab
   - Look for any error messages

---

## 📝 Example Secrets File

Here's what your complete secrets file should look like:

```toml
# Required for Weather
OPENWEATHER_API_KEY = "9c7"

# Required for Chatbot
GROQ_API_KEY = "g"

# Optional - for Plant Health Analysis
GEMINI_API_KEY = "A"

# Optional - for Plant Identification
HUGGINGFACE_API_KEY = "h"

# Optional - for Plant Database
PERENUAL_API_KEY = ""

# Default Location
DEFAULT_LOCATION = "Sialkot,PK"
```

**Replace all values with your actual API keys!**

---

## ✅ Success Checklist

After adding the key:

- [ ] Groq API key added to Streamlit Cloud secrets
- [ ] Key is in correct format (with quotes)
- [ ] Clicked "Save" button
- [ ] App redeployed successfully
- [ ] Chatbot responds to questions
- [ ] No error messages in app

---

## 🎉 That's It!

Once you add the `GROQ_API_KEY` to Streamlit Cloud secrets and save, your chatbot will work perfectly!

**Need help?** Check Streamlit Cloud logs if you see any errors.

