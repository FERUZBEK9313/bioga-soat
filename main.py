import asyncio, aiocron, datetime
from telethon import TelegramClient, events, sync, functions, types
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import date

api_id = 26352272
api_hash = "f9389f867486717ae6670f5db8bbdc75"
client = TelegramClient('session_name', api_id, api_hash)

client.start()

@aiocron.crontab('*/1 * * * *')
async def set_clock():
    day = date.today().strftime("%d")
    hour = datetime.datetime.today().strftime("%H")
    minut = datetime.datetime.today().strftime("%M")
    today = f"</> F E R U Z B E K </>  ⏰ {datetime.datetime.today().strftime('%H:%M')} ⏰"
    text = f"🎄 Yangi Yilga 📆 {31-int(day)} kun ⏰ {24-int(hour)} soat ⏳ {59-int(minut)} daqiqa qoldi! 🥳"
    async with client:
        await client(UpdateProfileRequest(about=text))
        await client(UpdateProfileRequest(first_name=today))

@client.on(events.NewMessage(pattern=".clock"))
async def clock(event):
    await event.edit("Soat muvaffaqiyatli ornatildi")

client.loop.run_forever()
client.run_until_disconnected()