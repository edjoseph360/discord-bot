import discord
from discord.ext import commands

class cog1(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    #events
    # @commands.Cog.listener()
    # async def on_ready(self):
    #     await self.client.change_presence(status=discord.Status.idle, activity=discord.Game('World domination'))
    #     print('Bot is online')

    #commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong! {round(self.client.latency * 1000)}ms')
        # await ctx.send("pong")
def setup(client):
    client.add_cog(cog1(client))