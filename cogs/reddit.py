import discord
from discord.ext import commands
import praw
import random

client_id = "ImvhhDV83C8hVg"
client_secret = "2qlN_fcI6KQjW296cB53DJhLVnA"
user_agent = "pull_posts"
username = "kingofthemilkyway"
password = "hailtotheking"

class reddit1(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def reddit(self, ctx, subredd):
        red = praw.Reddit(client_id = client_id,
                        client_secret= client_secret,
                        user_agent= user_agent,
                        username= username,
                        password= password)
        subred = red.subreddit(subredd)
        hot = subred.hot(limit = 10)
        lst = []
        for i in hot:
            L =(i.url)
            lst.append(L)
        z = random.choice(lst)

        await ctx.send(z)


def setup(client):
    client.add_cog(reddit1(client))