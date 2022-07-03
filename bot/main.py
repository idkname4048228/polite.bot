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
    global times
    times = 0


async def thank_aniki(message, message_times):
    if message_times > 1:
        return
    while 1:
        await asyncio.sleep(1)
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(now_time, times)
        if now_time[11:19:1] == "14:00:00":
            await message.channel.send("謝謝大哥")
            await asyncio.sleep(86400 - 1)


async def sumimasan(message):
    if (
        message.content.startswith("對不起")
        or message.content.startswith("sorry")
        or message.content.startswith("我很抱歉")
    ):
        await message.channel.send("對不起")
    elif message.content.startswith("time"):
        await message.channel.send(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


@client.event
# 當有訊息時
async def on_message(message):
    global times
    if message.author == client.user:
        return
    if times <= 1:
        times += 1
    sorry = asyncio.create_task(sumimasan(message))
    aniki = asyncio.create_task(thank_aniki(message, times))
    await sorry
    await aniki


TOKEN = os.getenv("DISCORD_TOKEN")
client.run(
    TOKEN
)  # TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
