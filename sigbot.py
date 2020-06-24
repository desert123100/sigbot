import discord
from discord.ext import commands
from lib.secret import Config

def get_prefix(bot, message):
    prefixes = ['!', '>']
    if not message.guild:
        return '?'
    return commands.when_mentioned_or(*prefixes)(bot, message)

initial_extensions = ['raid']

bot = commands.Bot(command_prefix=get_prefix, description='SIGBOT', case_insensitive = True)

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    game = discord.Game("!help | www.sigkillguild.com")  
    await bot.change_presence(activity=game)

bot.run(Config.DISCORD_TOKEN, bot=True)
