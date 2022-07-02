# 導入Discord.py
import discord
import asyncio
import os
import time

# client是我們與Discord連結的橋樑
client = discord.Client()

# 調用event函式庫
@client.event
# 當機器人完成啟動時
async def on_ready():
    print("目前登入身份：", client.user)


async def thank_aniki(message):
    if message.author == client.user:
        return
    while 1:
        await asyncio.sleep(1)
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(now_time)
        if now_time[11:19:1] == "16:30:20":
            await message.channel.send("謝謝大哥")
            await asyncio.sleep(86400 - 1)

async def sumimasan(message):
    if message.author == client.user:
        return
    if message.content.startswith("對不起"):
        await message.channel.send("對不起")



@client.event
# 當有訊息時
async def on_message(message):
    sorry = asyncio.create_task(sumimasan(message)) 
    aniki = asyncio.create_task(thank_aniki(message)) 
    await sorry
    await aniki
    


TOKEN = os.getenv("DISCORD_TOKEN")
client.run(
    TOKEN
    # "OTg3MTk4OTA2NDM1Nzc2NjEz.GewQ7v.ZdA21gHyfe5BdSzwtVlLwH-Jtxl_EbG0evGOHs"
)  # TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
