import discord
from discord.ext import commands
from lib.secret import Config
import lib.mail
import asyncio


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

async def status_task():
        bodies = lib.mail.main()
        if bodies == None:
            print('no messages')
            return
        channel = bot.get_channel(550318783810764810)
        for body in bodies['apps']:
            await channel.send(body)
            print('New Recruit')

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    game = discord.Game("!help | www.sigkillguild.com")  
    await bot.change_presence(activity=game)
    while True:
        await status_task()
        await asyncio.sleep(3600)

bot.run(Config.DISCORD_TOKEN, bot=True)
