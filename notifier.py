import os
import urllib.parse
import asyncio
import logging
from dotenv import load_dotenv

# Conditionally import httpx or curl_cffi based on OS, matching mainmob.py behavior
if os.name == "nt":
    import httpx
else:
    from curl_cffi import requests

import aiohttp

load_dotenv(override=True)

logger = logging.getLogger("Notifier")
logger.setLevel(logging.ERROR)

def get_bot_token(bot_name):
    """Retrieve bot token from environment variables."""
    token = os.environ.get(bot_name)
    if not token:
        logger.error(f"Telegram bot token for {bot_name} not found in .env")
    return token

async def async_send_telegram(url):
    """Send an async GET request to the given Telegram API URL."""
    try:
        header = {
            "accept-language": "en-US,en;q=0.9",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "accept-encoding": "gzip, deflate",
            "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; ASUS_X00TD Build/OPM1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.78 Mobile Safari/537.36"
        }
        
        async with aiohttp.ClientSession(headers=header) as session:
            async with session.get(url, proxy="", timeout=15, ssl=False) as resp:
                response = await resp.text()
                if "Bad Request" in response:
                    logger.error(f"{url}\r\n{response}")
                print(response)
    except Exception as e:
        logger.error(f"Error in async_send_telegram: {e}")

def myasyncsend(telegramurl):
    """Synchronous wrapper to run the async telegram function."""
    try:
        asyncio.run(async_send_telegram(telegramurl))
    except Exception as e:
        logger.error(f"Failed to run async_send_telegram: {e}")

def send_message(bot_name, chat_id, text, parse_mode="HTML", disable_notification=False, disable_web_page_preview=False):
    """Helper to format and send a Telegram message via the async wrapper."""
    token = get_bot_token(bot_name)
    if not token:
        return
        
    url = f"https://api.telegram.org/{token}/sendMessage?chat_id={chat_id}&text={urllib.parse.quote(text)}"
    if parse_mode:
        url += f"&parse_mode={parse_mode}"
    if disable_notification:
        url += "&disable_notification=1"
    if disable_web_page_preview:
        url += "&disable_web_page_preview=1"
        
    myasyncsend(url)
