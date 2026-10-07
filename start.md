# Flipkart Scraper Engine V2

Welcome to the new unified Flipkart Scraper Engine. This document provides a quick overview of how the new architecture works and how to run it effectively.

## 🌟 What's New?
Previously, this project relied on 16+ separate Python files (e.g. `pages_1.py`, `appliances_M.py`, `pages_AC.py`), all running duplicate logic. This consumed massive amounts of memory, caused blocking issues, and was very hard to maintain.

**The new architecture:**
1. **Unified Engine**: `scraper_engine.py` is the only script you need to run. It handles all multithreading, scheduling, and garbage collection in one place.
2. **Centralized Config**: All of the individual URLs and scraping target files have been moved into `config.json`. You no longer need to edit Python code to add or remove tracking links!
3. **Environment Variables**: Hardcoded Telegram API keys have been removed from the code for better security and easier maintenance. They are now managed in the `.env` file.

---

## 🚀 How to Run the Scraper

The engine dynamically loads your scraping tasks from `config.json` and dispatches them efficiently. 

### Option 1: Run EVERYTHING (Recommended for Heroku)
To start tracking every single link across all categories, simply run the engine with no arguments:
```bash
python3 scraper_engine.py
```
*Note: This is how the `Procfile` is currently configured to run your app on Heroku. It will automatically load all tasks in parallel using the `ThreadPoolExecutor`.*

### Option 2: Run a Specific Group
If you want to test or run a specific subset of links (just like running a single old `pages_X.py` script), you can pass the group name as an argument.

**Mobile & Tech Categories:**
```bash
python3 scraper_engine.py M9_hkmeg78/
python3 scraper_engine.py Mextraspl_hkmeg78/
python3 scraper_engine.py m7_hkpk78/
python3 scraper_engine.py m8_hkpk78/
```

**Web & Appliances Categories:**
```bash
python3 scraper_engine.py W9_hkmeg78/
python3 scraper_engine.py Wextraspl_hkmeg78/
python3 scraper_engine.py W_appliences_HKPK/
python3 scraper_engine.py M_appliences_HKPK/
```

**Location/Special Categories:**
```bash
python3 scraper_engine.py hk1_spl1/
python3 scraper_engine.py hk1_spl2/
python3 scraper_engine.py hk3_p6/
python3 scraper_engine.py mukta/
python3 scraper_engine.py mukta1/
python3 scraper_engine.py krnar/
python3 scraper_engine.py krnar1/
python3 scraper_engine.py guj/
```

---

## 🔧 Managing Telegram Bots
You no longer need to search through Python files to change a Telegram Bot token!

Open the `.env` file in the root folder, and you will see your keys defined here:
```ini
TELEGRAM_BOT_BIS="bot5595946728:AAE04_hy37h-SNUAKgC9nrUOjr-c-513Tm8"
TELEGRAM_BOT_MAIN="bot630455540:AAHtnLN2YFEzDpiVWeZBInQ_nlsPCpFzNEI"
TELEGRAM_BOT_ALT="bot1311880981:AAG9eM_c62lH5ITjMp_OzR7Klp40e3urnjA"
TELEGRAM_BOT_BLOCK="bot923259452:AAG1tBRBM7PIIYUL1g789IP4tBMgsI8uOJg"
```
If a bot ever gets banned or needs to be replaced, just change the token in this file, and the entire engine will instantly adapt.

---

## 📝 Adding New Tracking Links
To add new URLs to track:
1. Open `config.json`.
2. Find the group you want to add the link to.
3. Add a new block in the array. For example:
```json
{
    "filename": "W_appliences_HKPK/My_New_File.txt",
    "force": 1,
    "notassured": false,
    "url": "https://www.flipkart.com/...",
    "source_script": "manual_entry"
}
```
4. Save the file and restart the engine. No Python code needs to be modified!

---

## 🖥️ Web UI Dashboard
Instead of manually editing the `config.json` file or using CLI scripts, you can use the built-in premium Web Dashboard to easily add new tracking links!

**To start the Web Dashboard:**
```bash
python3 web_ui.py
```
Then, open your web browser and navigate to: **http://localhost:5050**
