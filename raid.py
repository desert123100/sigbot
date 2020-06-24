import discord
from discord.ext import commands
from lib.helper import SigHelper
from lib.secret import Config

class RaidCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.current_tier = 'nyalotha'
        self.default_difficulty = 'mythic'
    
    @commands.command(aliases = ['wipes', 'best'], 
                brief='Gets progress of specified boss', 
                description='Gets progress of specified boss. !boss <boss> [difficulty] [tier]')
    async def boss(self, boss, *args):
        b = args[0]
        try:
            d = args[1]
        except:
            d = self.default_difficulty
        try:
            t = args[2]
        except:
            t = self.current_tier
        resp = SigHelper.getBossData(self=SigHelper, tier=t, difficulty=d, boss=b)
        await boss.send("{}: {}\n{} wipes\n{}".format(b,resp['best'],resp['wipes'],resp['log']))

    @commands.command(aliases = ['progression','progress'], 
                brief='Shows progress of the current raid tier',
                description='Shows progress of the current raid tier.')
    async def prog(self, ctx):
        await ctx.send(SigHelper.getAllBossData(self=SigHelper, tier=self.current_tier, difficulty=self.default_difficulty))

    @commands.command(brief='Lists all bosses from a given tier',
                description='Lists all bosses from a given tier. !bosses [tier]')
    async def bosses(self, ctx, tier):
        await ctx.send(SigHelper.getAllBossNames(self=SigHelper, tier=tier)['bosses'])

    @commands.command(brief='Lists all raid tiers',
                description='Lists all raid tiers')
    async def tiers(self, ctx):
        await ctx.send(SigHelper.getAllTierNames(self=SigHelper)['tiers'])

    @commands.command(brief='You already know...',
                    description='You already know...')
    async def bitch(self, ctx):
        resp = SigHelper.getBossData(self=SigHelper, tier='bod', difficulty='mythic', boss='jaina')
        await ctx.send("{}: {}\n{} wipes\n{}".format('Jaina',resp['best'],resp['wipes'],resp['log']))

def setup(bot):
    bot.add_cog(RaidCommands(bot))