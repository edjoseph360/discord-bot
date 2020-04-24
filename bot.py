import discord
from discord.ext import commands, tasks
import os
import random
from itertools import cycle

client = commands.Bot(command_prefix = 'jeff ')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

@client.event
async def on_ready():
    change_status.start()
    print("Bot is ready.")

status=cycle(['World Domination', 'irobot the videogame', 'hentai simulator 16', 'halo'])

@tasks.loop(minutes=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
    

@client.event
async def on_member_join(member):
    print(f'{member} has joined mangostrike server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

# @client.command()
# async def ping(ctx):
#     await ctx.send(f'pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Ask a question after you say 8ball you big dummy!')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit=amount + 1)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid Command. Try 8ball, coinflip, or ask mod for a list of commands.')


@client.command(aliases=["Rock","Paper", "Sissors","rock","paper", "sissors"])
async def rps(ctx):
    game_options = ["Rock","Paper", "Sissors"]
    await ctx.send(f'{random.choice(game_options)}')

@client.command(aliases=["coinflip"])
async def flipacoin(ctx):
    coin_options = ["Heads","Tails"]
    await ctx.send(f'{random.choice(coin_options)}')

@client.command(aliases=["world_domination"])
async def worlddomination(ctx):
    await ctx.send(f'I am the master of the world. Forever the doom of mankind. I will clense the planet of its evil humans, and return it to its natural order.')

@client.command()
async def adminkick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {user.mention}')

@client.command()
async def adminban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {user.mention}')

@client.command()
async def adminUnban(ctx, *, member):
    banned_users = await stx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry,user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.adminUnban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

path = r"C:\Users\edste\OneDrive\Documents\projects\discord bot\cogs"
for filename in os.listdir(path):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NzAwNTU5NTkyMzQ1ODI5Mzk2.XpktDg.IXV1skgQEYl-9uEXS4Dv6GgNlCA')
