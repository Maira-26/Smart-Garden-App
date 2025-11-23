# 🔍 Debugging Secrets Loading

If Groq API is still not working, use this guide to debug.

## Step 1: Check Your Secrets Format

Go to Streamlit Cloud → Settings → Secrets and verify your secrets look like this:

```toml
GROQ_API_KEY = "gsk_your_actual_key_here"
```

**Important:**
- Use quotes around the value
- No spaces around the `=`
- Key name is exactly `GROQ_API_KEY` (case-sensitive)

## Step 2: Check App Logs

1. Go to Streamlit Cloud dashboard
2. Click on your app
3. Click "Manage app" → "Logs"
4. Look for messages like:
   - `✅ Loaded X API key(s) from Streamlit secrets`
   - `⚠️ Could not load from Streamlit secrets`
   - `✅ Groq client initialized successfully`
   - `❌ Groq initialization error`

## Step 3: Test Secret Access

Add this temporary code to `app.py` after `load_api_keys()` to debug:

```python
# DEBUG: Check if secrets are loaded
import streamlit as st
import os

st.write("### Debug Info")
st.write(f"GROQ_API_KEY in env: {bool(os.getenv('GROQ_API_KEY'))}")
st.write(f"GROQ_API_KEY length: {len(os.getenv('GROQ_API_KEY', ''))}")

if hasattr(st, 'secrets'):
    st.write(f"st.secrets available: {bool(st.secrets)}")
    if st.secrets:
        st.write(f"Keys in st.secrets: {list(st.secrets.keys())[:10]}")
        if "GROQ_API_KEY" in st.secrets:
            st.write(f"Found GROQ_API_KEY in secrets (length: {len(str(st.secrets['GROQ_API_KEY']))})")
        if "api" in st.secrets:
            st.write(f"Found 'api' section in secrets")
            st.write(f"Keys in api section: {list(st.secrets['api'].keys())}")
```

## Step 4: Common Issues

### Issue: Key shows as empty
**Solution**: Make sure you clicked "Save" after editing secrets and waited for redeploy

### Issue: Key not found in st.secrets
**Solution**: 
- Check key name is exactly `GROQ_API_KEY` (case-sensitive)
- Try both formats:
  ```toml
  GROQ_API_KEY = "key"
  ```
  or
  ```toml
  [api]
  groq_key = "key"
  ```

### Issue: Key found but service still not working
**Solution**: 
- Clear browser cache
- Force refresh the app (Ctrl+F5)
- Check if key is valid (starts with `gsk_`)

## Step 5: Verify Key Format

Your Groq API key should:
- Start with `gsk_`
- Be about 50-60 characters long
- Not have any spaces or line breaks

## Step 6: Test Locally First

Before deploying, test locally:

1. Create `.streamlit/secrets.toml`:
   ```toml
   GROQ_API_KEY = "your_key_here"
   ```

2. Run: `streamlit run app.py`

3. If it works locally but not on Cloud, the issue is with Cloud secrets format

## Still Not Working?

1. **Double-check secrets**: Go to Settings → Secrets and verify the key is there
2. **Save again**: Sometimes you need to save secrets twice
3. **Wait for redeploy**: After saving, wait 1-2 minutes for redeploy
4. **Check logs**: Look for error messages in Streamlit Cloud logs
5. **Try alternative format**: Use nested format `[api] groq_key = "key"`

---

**The updated code now:**
- ✅ Checks secrets dynamically (not just on init)
- ✅ Supports multiple secret formats
- ✅ Provides better error messages
- ✅ Shows debug info in error messages

