# 🔐 Create Your .env File - Step by Step

## ⚠️ IMPORTANT: You MUST create a `.env` file for the app to work!

All API keys have been removed from the code for security. You need to create a `.env` file with your actual API keys.

---

## 📝 Step-by-Step Instructions

### Step 1: Create the .env File

**Option A: Using ENV_TEMPLATE.txt (Easiest)**
1. Open `ENV_TEMPLATE.txt` in your project folder
2. Copy ALL the content
3. Create a NEW file named exactly `.env` (just `.env`, nothing else)
4. Paste the content
5. Replace `your_xxx_api_key_here` with your actual API keys

**Option B: Create Manually**
1. Create a new file in your project root
2. Name it exactly `.env` (make sure it starts with a dot!)
3. Copy and paste this content:

```env
# Smart Garden App - API Keys
# IMPORTANT: This file is gitignored and will NOT be uploaded to GitHub

OPENWEATHER_API_KEY=your_openweather_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
GROQ_API_KEY=your_groq_api_key_here
PERENUAL_API_KEY=your_perenual_api_key_here
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
DEFAULT_LOCATION=Sialkot,PK
```

### Step 2: Add Your Actual API Keys

Replace the placeholders with your real API keys:

```env
OPENWEATHER_API_KEY=weather_key
GEMINI_API_KEY=gemini_key
GROQ_API_KEY=grk_key
PERENUAL_API_KEY=
HUGGINGFACE_API_KEY=
DEFAULT_LOCATION=Sialkot,PK
```

**⚠️ Important Rules:**
- NO quotes around values
- NO spaces around the `=` sign
- One key per line
- Save the file

### Step 3: Verify .env is Gitignored

Check that `.env` is in your `.gitignore` file (it should already be there):

```bash
# Check if .env is ignored
cat .gitignore | grep .env
```

You should see `.env` in the output.

### Step 4: Test Your Setup

Run the app to verify it works:

```bash
streamlit run app.py
```

If you see errors about missing API keys, double-check your `.env` file:
- File is named exactly `.env` (not `.env.txt` or `env.txt`)
- No quotes around values
- No spaces around `=`
- Keys are on separate lines

---

## 🔒 Security Checklist

Before pushing to GitHub, verify:

- ✅ `.env` file exists locally (with your keys)
- ✅ `.env` is in `.gitignore` (already done)
- ✅ No API keys in `config.py` (already done)
- ✅ No API keys in any `.py` files (already done)
- ✅ `__pycache__/` is in `.gitignore` (already done)

---

## 📋 All API Keys Required

Your `.env` file needs these keys:

1. **OPENWEATHER_API_KEY** - Weather data
   - Get free key: https://openweathermap.org/api

2. **GEMINI_API_KEY** - Plant identification & health analysis
   - Get free key: https://makersuite.google.com/app/apikey
   - Format: Starts with `AIza...`

3. **GROQ_API_KEY** - Fast AI chat responses
   - Get free key: https://console.groq.com/
   - Format: Starts with `gsk_...`

4. **HUGGINGFACE_API_KEY** - Backup plant identification (Optional)
   - Get free key: https://huggingface.co/settings/tokens
   - Format: Starts with `hf_...`

5. **PERENUAL_API_KEY** - Plant database (Optional)
   - Get key: https://perenual.com/docs/api

---

## ✅ Verification Commands

Before pushing to GitHub, run these to verify no secrets are exposed:

```bash
# Check for API keys in Python files (should return nothing)
grep -r "gsk_\|AIza\|99fe79fbdcc1796003cced4d01e1b3c7" --include="*.py" .

# Check git status (should NOT show .env)
git status

# Verify .env is ignored
git check-ignore .env
# Should output: .env
```

---

## 🎯 Summary

1. ✅ Create `.env` file (copy from `ENV_TEMPLATE.txt`)
2. ✅ Add your actual API keys
3. ✅ Verify `.env` is gitignored
4. ✅ Test the app works
5. ✅ Push to GitHub (`.env` will NOT be uploaded)

**Your API keys are now secure! 🔐**

