import time
import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")


@bot.event
async def on_ready():
    print("目前登入身份：", bot.user)


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.event
# 當有訊息時
async def on_message(message):
    # 排除自己的訊息，避免陷入無限循環
    if message.author == bot.user:
        return
    # 如果以「說」開頭
    if message.content.startswith("Start"):
        await message.channel.send("K")
        while 1:
            now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if now_time[11:19:1] == "22:20:40":
                await message.channel.send("謝謝大哥")
            time.sleep(1)


if __name__ == "__main__":
    bot.run(TOKEN)
