# 🔐 Complete Secrets Setup Guide

## ✅ Supports Both Local & Streamlit Cloud!

Your app now supports **two methods** for API keys:

1. **Local Development:** `.streamlit/secrets.toml` file
2. **Streamlit Cloud:** Secrets in dashboard (automatic)

---

## 🏠 Local Development Setup

### Step 1: Create Secrets File

1. **Create `.streamlit` folder** (if it doesn't exist):
   ```bash
   mkdir .streamlit
   ```

2. **Create `secrets.toml` file:**
   - Copy `.streamlit/secrets.toml.template`
   - Rename to `secrets.toml`
   - Or create new file: `.streamlit/secrets.toml`

### Step 2: Add Your API Keys

**Open `.streamlit/secrets.toml` and add your keys:**

```toml
[api]
openweather_key = "your_openweather_api_key_here"
gemini_key = "your_gemini_api_key_here"
groq_key = "your_groq_api_key_here"
huggingface_key = "your_huggingface_api_key_here"
perenual_key = "your_perenual_api_key_here"
default_location = "Sialkot,PK"
```

**Or use alternative format (also works):**

```toml
OPENWEATHER_API_KEY = "your_openweather_api_key_here"
GEMINI_API_KEY = "your_gemini_api_key_here"
GROQ_API_KEY = "your_groq_api_key_here"
HUGGINGFACE_API_KEY = "your_huggingface_api_key_here"
PERENUAL_API_KEY = "your_perenual_api_key_here"
DEFAULT_LOCATION = "Sialkot,PK"
```

### Step 3: Verify It's Gitignored

**Check `.gitignore` includes:**
```
.streamlit/secrets.toml
```

✅ Already added! Your secrets file won't be uploaded to GitHub.

### Step 4: Test Locally

```bash
streamlit run app.py
```

Your app should now work with API keys from `secrets.toml`!

---

## ☁️ Streamlit Cloud Setup

### Step 1: Go to Streamlit Cloud Dashboard

1. Visit: https://share.streamlit.io
2. Click on your app
3. Click **⚙️ Settings** (gear icon)

### Step 2: Add Secrets

1. Scroll to **"Secrets"** section
2. Click **"Edit secrets"**

### Step 3: Add Your API Keys

**Use this format (TOML):**

```toml
[api]
openweather_key = "your_openweather_api_key_here"
gemini_key = "your_gemini_api_key_here"
groq_key = "your_groq_api_key_here"
huggingface_key = "your_huggingface_api_key_here"
perenual_key = "your_perenual_api_key_here"
default_location = "Sialkot,PK"
```

**Or use direct format (also works):**

```toml
OPENWEATHER_API_KEY = "your_openweather_api_key_here"
GEMINI_API_KEY = "your_gemini_api_key_here"
GROQ_API_KEY = "your_groq_api_key_here"
HUGGINGFACE_API_KEY = "your_huggingface_api_key_here"
PERENUAL_API_KEY = "your_perenual_api_key_here"
DEFAULT_LOCATION = "Sialkot,PK"
```

### Step 4: Save and Redeploy

1. Click **"Save"**
2. Wait 1-2 minutes for redeploy
3. ✅ Done!

---

## 🔄 How It Works

The app checks for API keys in this order:

1. **Streamlit Cloud:** `st.secrets` (automatically available)
2. **Local:** `.streamlit/secrets.toml` (via `st.secrets`)
3. **Fallback:** `.env` file (via `os.getenv()`)

**This means:**
- ✅ Works on Streamlit Cloud (uses dashboard secrets)
- ✅ Works locally (uses `secrets.toml`)
- ✅ Still supports `.env` file (backward compatible)

---

## 📋 Format Examples

### Format 1: Nested (Recommended)
```toml
[api]
openweather_key = "your_key"
groq_key = "your_key"
```

### Format 2: Direct (Also Works)
```toml
OPENWEATHER_API_KEY = "your_key"
GROQ_API_KEY = "your_key"
```

### Format 3: Mixed (Also Works)
```toml
[api]
openweather_key = "your_key"

GROQ_API_KEY = "your_key"
```

**All formats work!** The code handles both.

---

## ✅ Verification

### Local:
1. Create `.streamlit/secrets.toml`
2. Add your keys
3. Run: `streamlit run app.py`
4. Check if chatbot/weather works

### Streamlit Cloud:
1. Add secrets in dashboard
2. Save
3. Wait for redeploy
4. Test your app

---

## 🔒 Security Checklist

- [ ] `.streamlit/secrets.toml` is in `.gitignore` ✅
- [ ] `.env` is in `.gitignore` ✅
- [ ] No API keys in `config.py` ✅
- [ ] No API keys in any `.py` files ✅
- [ ] Secrets file not committed to GitHub ✅

---

## 🐛 Troubleshooting

### Issue: "API key not found" on Streamlit Cloud

**Solution:**
1. Check secrets are saved in dashboard
2. Verify format (use quotes, TOML format)
3. Wait for redeploy (1-2 minutes)
4. Check logs for errors

### Issue: "API key not found" locally

**Solution:**
1. Check `.streamlit/secrets.toml` exists
2. Verify file format (TOML syntax)
3. Check keys are correct
4. Restart Streamlit: `streamlit run app.py`

### Issue: Both formats not working

**Solution:**
- Use Format 1 (nested `[api]` section) - most reliable
- Make sure quotes are around values
- No spaces around `=`

---

## 📝 Quick Reference

| Location | File/Setting | Format |
|----------|-------------|--------|
| **Local** | `.streamlit/secrets.toml` | TOML |
| **Cloud** | Dashboard → Secrets | TOML |
| **Fallback** | `.env` | KEY=VALUE |

---

## 🎉 That's It!

Your app now supports:
- ✅ Local development with `secrets.toml`
- ✅ Streamlit Cloud with dashboard secrets
- ✅ Backward compatible with `.env` file

**No more authentication issues!** 🚀

