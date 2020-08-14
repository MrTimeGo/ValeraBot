import discord
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command()
async def Igor(ctx):
    print('Пидор!')

bot.run(settings['token'])