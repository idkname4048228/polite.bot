# 導入Discord.py
import discord
import time

# client是我們與Discord連結的橋樑
client = discord.Client()

# 調用event函式庫
@client.event
# 當機器人完成啟動時
async def on_ready():
    print("目前登入身份：", client.user)


@client.event
# 當有訊息時
async def on_message(message):
    # 排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    # 如果以「說」開頭
    if message.content.startswith("Start"):
        await message.channel.send("K")
        while 1:
            now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            if now_time[11:19:1] == '22:20:40':
                await message.channel.send("謝謝大哥")
            time.sleep(1)


        # # 分割訊息成兩份
        # tmp = message.content.split(" ", 2)
        # # 如果分割後串列長度只有1
        # if len(tmp) == 1:
        #     await message.channel.send("你要我說什麼啦？")
        # else:
        #     await message.channel.send(tmp[1])


client.run(
    "OTg3MTk4OTA2NDM1Nzc2NjEz.GR0lWJ.ASeFLtOevEczxzF1QOILD-I1GuG73bsbaGKEMA"
)  # TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
