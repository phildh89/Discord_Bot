import discord
from discord.ext import commands

class Commands(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
    
    #Events
    @commands.Cog.listener()
    async def on_ready():
        print('Bot is ready.')

    #Commands
    @commands.command()
    async def ping(ctx):
        await ctx.send('Example Message')


    @commands.command()
    async def clear(ctx, amount=5):
        if amount > 0 and amount < 11:
            await ctx.channel.purge(limit=amount)
        else:
            await ctx.send("I can only delete 1 to 10 messages at a time!")


def setup(bot):
    bot.add_cog(commands(bot))

