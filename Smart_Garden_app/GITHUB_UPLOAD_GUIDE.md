# 📤 GitHub Upload Guide - What Files to Upload

## ✅ FILES TO UPLOAD (Essential Files)

### Core Application Files
- ✅ `app.py` - Main application file
- ✅ `config.py` - Configuration (no API keys, loads from .env)
- ✅ `requirements.txt` - Python dependencies

### Utils Directory (All Files)
- ✅ `utils/__init__.py`
- ✅ `utils/data_manager.py`
- ✅ `utils/weather_service.py`
- ✅ `utils/plant_service.py`
- ✅ `utils/gemini_service.py`
- ✅ `utils/groq_service.py`
- ✅ `utils/huggingface_service.py`

### Documentation Files
- ✅ `README.md` - Main documentation
- ✅ `SETUP_GUIDE.md` - Setup instructions
- ✅ `PROJECT_SUMMARY.md` - Project overview
- ✅ `GITHUB_SETUP.md` - Security setup guide
- ✅ `QUICK_FIX.md` - Quick fix instructions
- ✅ `ENV_TEMPLATE.txt` - Environment variables template

### Configuration Files
- ✅ `.gitignore` - Git ignore rules (IMPORTANT!)

---

## ❌ FILES TO NEVER UPLOAD (Already in .gitignore)

### Sensitive Data (NEVER UPLOAD!)
- ❌ `.env` - Contains your API keys (CRITICAL - Never upload!)
- ❌ `data/user_profile.json` - User personal data
- ❌ `plants_database.json` - Plant data (user's plants)
- ❌ `chat_history.json` - Chat history
- ❌ `plant_images/` - User uploaded images

### Cache & Temporary Files
- ❌ `__pycache__/` - Python cache files (may contain compiled code with keys)
- ❌ `*.pyc`, `*.pyo` - Compiled Python files

### Old/Unused Files
- ❌ `Smart_Garden_app.ipynb` - Empty notebook file

---

## 🚀 Quick Upload Checklist

### Before Uploading:
1. ✅ Create `.env` file locally (copy from `ENV_TEMPLATE.txt`)
2. ✅ Add your API keys to `.env` file
3. ✅ Verify `.env` is in `.gitignore` (it should be)
4. ✅ Remove `__pycache__` from git if already tracked

### Files to Commit:
```
✅ app.py
✅ config.py
✅ requirements.txt
✅ .gitignore
✅ utils/ (entire folder)
✅ README.md
✅ SETUP_GUIDE.md
✅ PROJECT_SUMMARY.md
✅ GITHUB_SETUP.md
✅ QUICK_FIX.md
✅ ENV_TEMPLATE.txt
```

### Files NOT to Commit (Auto-ignored by .gitignore):
```
❌ .env
❌ __pycache__/
❌ data/user_profile.json
❌ plants_database.json
❌ chat_history.json
❌ plant_images/
❌ Smart_Garden_app.ipynb
```

---

## 📝 Git Commands to Upload

### If starting fresh:
```bash
# Initialize git (if not already done)
git init

# Add all files (gitignore will automatically exclude sensitive files)
git add .

# Check what will be uploaded (verify no .env or __pycache__)
git status

# Commit
git commit -m "Initial commit: Smart Garden App"

# Add remote repository
git remote add origin https://github.com/yourusername/your-repo-name.git

# Push to GitHub
git push -u origin main
```

### If __pycache__ is already tracked:
```bash
# Remove from git (but keep local files)
git rm -r --cached __pycache__

# Commit the removal
git commit -m "Remove __pycache__ for security"

# Push
git push
```

---

## ✅ Verification Before Push

Run this to verify no secrets will be uploaded:
```bash
# Check for API keys in code (should return nothing)
grep -r "gsk_\|AIza\|hf_" --include="*.py" .

# Check git status (should NOT show .env or __pycache__)
git status
```

---

## 🎯 Summary

**Upload:** All `.py` files, `.md` files, `.txt` template, `.gitignore`, `requirements.txt`

**Don't Upload:** `.env`, `__pycache__/`, data files, user images

**Your `.gitignore` is already configured correctly - Git will automatically exclude sensitive files!**

