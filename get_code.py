from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession

# Telegram API ma'lumotlari
api_id = 'YOUR_API_ID'  # o'zingizning API ID'ni bu yerga yozing
api_hash = 'YOUR_API_HASH'  # o'zingizning API Hash'ni bu yerga yozing
string_session ='YOUR_STRING_SESSION'  # O'zingizning string session'ni bu yerga yozing

client = TelegramClient(StringSession(string_session), api_id, api_hash)

# Xabarni qayta ishlash
@client.on(events.NewMessage)
async def handler(event):
    if event.is_private:  # Faqat shaxsiy xabarlar uchun
        if event.sender_id == 777000:  # Faqat Telegram'dan kelgan kodlar (ID: 777000)
            print("Keldi:", event.raw_text)  # Xabarni konsolga chiqarish
            
            # Xohlasangiz xabarni faylga ham yozishingiz mumkin
            # with open('codes.txt', 'a') as f:
            #     f.write(event.raw_text + '\n')

# Clientni ishga tushirish
client.start()
client.run_until_disconnected()
