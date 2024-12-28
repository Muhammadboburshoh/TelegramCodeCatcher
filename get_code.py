from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
string_session = 'YOUR_STRING_SESSION'

client = TelegramClient(StringSession(string_session), api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    if event.is_private:  # Faqat shaxsiy xabarlar uchun
        if 'Telegram' in event.sender_id:  # Faqat Telegram'dan kelgan kodlar
            print("Keldi:", event.raw_text)  # Xabarni konsolga chiqarish
            # Xohlasangiz xabarni faylga ham yozishingiz mumkin
            # with open('codes.txt', 'a') as f:
            #     f.write(event.raw_text + '\n')

client.start()
client.run_until_disconnected()
