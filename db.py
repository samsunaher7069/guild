"""
db.py — MongoDB connection layer for FFGlory panel
"""
import os
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime, timezone

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME   = os.getenv("MONGO_DB",  "ffglory")

_client: AsyncIOMotorClient | None = None

def get_client() -> AsyncIOMotorClient:
    global _client
    if _client is None:
        _client = AsyncIOMotorClient(MONGO_URI)
    return _client

def get_db():
    return get_client()[DB_NAME]

# ── Collection helpers ──────────────────────────────────────────────────────
def users():         return get_db()["users"]
def groups():        return get_db()["groups"]
def transactions():  return get_db()["transactions"]
def activity_log():  return get_db()["activity_log"]
def coupons():       return get_db()["coupons"]
def inbox_messages():return get_db()["inbox_messages"]
def alerts():        return get_db()["alerts"]
def pricing_cfg():   return get_db()["pricing_config"]
def push_subs():     return get_db()["push_subscriptions"]
def notifications(): return get_db()["notifications"]

def now_utc() -> datetime:
    return datetime.now(timezone.utc)