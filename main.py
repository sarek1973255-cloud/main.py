from telethon import TelegramClient
import asyncio

API_ID = 123456
API_HASH = "YOUR_API_HASH"
SESSION_NAME = "session"

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def main():
    await client.start()
    print("✅ LOGIN SUCCESSFUL")

    me = await client.get_me()
    print("User:", me.username)

asyncio.run(main())