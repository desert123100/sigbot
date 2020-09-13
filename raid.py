import discord
from discord.ext import commands
from lib.helper import SigHelper
from lib.secret import Config

class RaidCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.current_tier = 'nathria'
        self.default_difficulty = 'mythic'
    
    @commands.command(aliases = ['wipes', 'best'], 
                brief='Gets progress of specified boss', 
                description='Gets progress of specified boss. !boss [boss?]-[difficulty?]-[tier?]')
    async def boss(self, ctx, *args):
        try:
            b = args[0]
        except:
            _b = SigHelper.getCurrentBoss(self=SigHelper, tier=self.current_tier)
            b = _b['boss']
            d = _b['difficulty']
        try:
            if not d:
                d = args[1]
        except:
            d = self.default_difficulty
        try:
            t = args[2]
        except:
            t = self.current_tier
        resp = SigHelper.getBossData(self=SigHelper, tier=t, difficulty=d, boss=b)
        await ctx.send("{}:\n{}: {}\n{} wipes\n{}".format(d,b,resp['best'],resp['wipes'],resp['log']))

    @commands.command(aliases = ['progression','progress'], 
                brief='Shows progress of the current raid tier',
                description='Shows progress of the current raid tier. !tier [difficulty?]-[tier?]')
    async def prog(self, ctx, *args):
        try:
            difficulty = args[0]
        except:
            difficulty = self.default_difficulty
        try:
            tier = args[1]
        except:
            tier = self.current_tier
        await ctx.send(SigHelper.getAllBossData(self=SigHelper, tier=tier, difficulty=difficulty))

    @commands.command(brief='Lists all bosses from a given tier',
                description='Lists all bosses from a given tier. !bosses [tier?]')
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