import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "28619498"))
    API_HASH = os.environ.get("API_HASH", "1260dfef465c35e76def4fb3d414d08f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5913937604:AAGGUgwGj1rMUoGe7-Xp6rsFym5qhuiEtjI") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "") 
    OWNER_ID = os.environ.get("OWNER_ID", "6239765334")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://clone2:clone2@cluster0.ctv0ysf.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_Files')
    SESSION = os.environ.get("SESSION", "BQC5xVZXj8CR6BGfe7iUSeQ3rizpgc_A-MeKEFRLqo1OjFRgzUOJAz0PBL3tWaz9AbbUxxBh0tHgE-cE167AWx1WrelP1jIkOY0YWfRNPPnXLVvKBxazDoFjMkrfaSXGN8SIjEU4NH3gB3WRQClIzQ2VNi2761Xa1JtGXSJXW4JKq5djM6-6TltcxABU9JgJiI3rS9QYTw8QRE4l-19Z-st6tHTuYxc7tggs0yqSMKMke-rnHdyywbYDXwv6-OqlM1V-xup3oJtF4zCgPO5w8ea7ehNqyT-oin_SQ2WXB9XjFfs6xgqnIkvkbCkpcd5KSqU7w7-UeU-8aEIwksd4Y7SCAAAAAXPrQ1YA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001817174604"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "autowadegbot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
