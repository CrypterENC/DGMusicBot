import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv

from help_cog import help_cog
from music_cog import music_cog

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')  # Load environment variables from .env file

if TOKEN is None:
    raise ValueError("No DISCORD_TOKEN found in environment variables")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents)

# Remove the default help command
bot.remove_command('help')

async def main():
    async with bot:
        await bot.add_cog(help_cog(bot))
        await bot.add_cog(music_cog(bot))
        await bot.start(TOKEN)

asyncio.run(main())