from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

app = Client(
    name = "botstatus_teletips",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_string = os.environ["SESSION_STRING"]
)
TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]

async def main_teletips():
    async with app:
            while True:
                print("Checking...")
                xxx_teletips = "ā³ | **Real-Time Bot Status**"
                for bot in BOT_LIST:
                    try:
                        yyy_teletips = await app.send_message(bot, "/start")
                        aaa = yyy_teletips.id
                        await asyncio.sleep(10)
                        zzz_teletips = app.get_chat_history(bot, limit = 1)
                        async for ccc in zzz_teletips:
                            bbb = ccc.id
                        if aaa == bbb:
                            xxx_teletips += f"\n\nš¤  @{bot}\n        ā **Down** ā"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"šØ **Beep! Beep!! @{bot} is down** ā")
                                except Exception:
                                    pass
                            await app.read_chat_history(bot)
                        else:
                            xxx_teletips += f"\n\nš¤  @{bot}\n        ā **Alive** ā"
                            await app.read_chat_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y - %I:%M %p")
                xxx_teletips += f"\n\n**Last checked on: {last_update} [{TIME_ZONE}]**\n\n__Refreshes automatically...__"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_teletips)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(100)
                        
app.run(main_teletips())
