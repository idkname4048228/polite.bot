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
    while 1:
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if now_time[11:19:1] == "19:15:40":
            await message.channel.send("謝謝大哥")
        await time.sleep(86400 - 1)


@client.event
# 當有訊息時
async def on_message(message):
    # 排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    thank_aniki(message)
    # 如果以「說」開頭
    if message.content.startswith("對不起"):
        await message.channel.send("對不起")


TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)  # TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
