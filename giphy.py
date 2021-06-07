import discord
from discord.client import Client
from discord.flags import Intents
from dotenv import load_dotenv
import os
import aiohttp
from discord.ext import commands
import random as rnd
from discord.ext import commands

chucknorris_random_api = "https://api.chucknorris.io/jokes/random"
chucknorris_search_api = "https://api.chucknorris.io/jokes/search?query="

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
Giphy_api = os.getenv("GIPHY_API")

bot = commands.Bot(command_prefix="!")

@bot.command()
async def random(ctx):
    ghiphy_url =f'https://api.giphy.com/v1/gifs/random?api_key={Giphy_api}&tag=&rating=g'
    async with aiohttp.ClientSession() as session:
        async with session.get(ghiphy_url) as response:
            if response.status == 200:
                js = await response.json()
                await ctx.send (js ["data"]["images"]["original"]["url"])
    return

@bot.command()
async def search(ctx,search_term):
    async with aiohttp.ClientSession() as session:
        async with session.get(chucknorris_search_api+search_term) as response:
            if response.status == 200:
                js = await response.json()
                await ctx.send (rnd.choice(js["result"])["value"])
    return


bot.run(TOKEN)
