import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "2132402"))
    API_HASH = os.environ.get("API_HASH", "d8ae5b42da814105c8433a4a02767f6f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6749443346:AAF-hknYraHoZKjy62pWLRJv_nDxUWUsbd8") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "") 
    OWNER_ID = os.environ.get("OWNER_ID", "5911954612")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://wade2001:wade2001@cluster0.wkjofrl.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Telegram_files')
    SESSION = os.environ.get("SESSION", "BQC5xVZXj8CR6BGfe7iUSeQ3rizpgc_A-MeKEFRLqo1OjFRgzUOJAz0PBL3tWaz9AbbUxxBh0tHgE-cE167AWx1WrelP1jIkOY0YWfRNPPnXLVvKBxazDoFjMkrfaSXGN8SIjEU4NH3gB3WRQClIzQ2VNi2761Xa1JtGXSJXW4JKq5djM6-6TltcxABU9JgJiI3rS9QYTw8QRE4l-19Z-st6tHTuYxc7tggs0yqSMKMke-rnHdyywbYDXwv6-OqlM1V-xup3oJtF4zCgPO5w8ea7ehNqyT-oin_SQ2WXB9XjFfs6xgqnIkvkbCkpcd5KSqU7w7-UeU-8aEIwksd4Y7SCAAAAAXPrQ1YA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1002059242652"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "pdfforwardbot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
