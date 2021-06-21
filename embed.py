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


async def random_gif(tag: str = ""):
    ghiphy_url = (
        f"https://api.giphy.com/v1/gifs/random?api_key={Giphy_api}&tag={tag}&rating=g"
    )
    async with aiohttp.ClientSession() as session:
        async with session.get(ghiphy_url) as response:
            if response.status == 200:
                js = await response.json()
                return js["data"]


@bot.command()
async def random(ctx, tag: str = ""):
    data = await random_gif(tag)
    await ctx.send(data["images"]["downsized"]["url"])


@bot.command()
async def gifembed(ctx, tag: str = ""):
    data = await random_gif(tag)
    embed = discord.Embed()
    embed.set_image(url=data["images"]["downsized"]["url"])
    description = f"@{ctx.author.name} requested this {tag if tag!='' else 'random'}"
    color = discord.Color.purple()
    embed.description = description
    embed.color = color
    embed.title = data["title"]
    embed.url = data["url"]
    embed.set_thumbnail(url=data["images"]["fixed_height_small_still"]["url"])
    embed.add_field(name="Embed URL", value=data["embed_url"], inline=True)
    embed.add_field(name="Bitly URL", value=data["bitly_url"], inline=True)
    embed.set_footer(
        icon_url="https://eu.ui-avatars.com/api/name=G&background=40ff00",
        text="rating G",
    )
    await ctx.send(embed=embed)


bot.run(TOKEN)
