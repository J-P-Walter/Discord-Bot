from discord.ext import commands
import configparser
import os
from mongoengine import *

connect('discord', host='localhost', username='root', password='root', authentication_source='admin')

bot = commands.Bot(command_prefix='!')

for filename in os.listdir('./cogs'):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

config = configparser.ConfigParser()
config.read('tokens.cfg')
token = config.get('TOKEN', 'token')
bot.run(token)