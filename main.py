import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv
import random
from asyncore import read

# Variables
BOT_NAME = "Text File To Discord Chat Bot"
load_dotenv('token.env')
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

# Verify The Bot is Logged in
@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

# The Main Chat Features of the bot.
@bot.event
async def on_message(message):
    message.content = message.content.lower()

    # Reply back to the user who used command
    if message.content.startswith(f'!hello'):
        await message.reply('SUP HOMIE!', mention_author=True)

    if message.content.startswith(f'!knockknock'):
        await message.channel.send('I Hate Knock Knock Jokes!')

    # Sends DM to person who issues command.
    if message.content.startswith(f'!help'):
        await message.author.send("Hello, I am sending you a direct message!")

    # Reply Back with a random message from file
    if message.content.startswith(f'!chat'):
        with open("text.txt", "r") as f:
            chat = (f.readlines())
        await message.channel.send(random.choice(chat))
      
  
    if message.content.startswith(f'!vibin'):
      await message.channel.send('https://www.youtube.com/watch?v=FCb3rblTEds&t=136s')


bot.run(DISCORD_TOKEN)
