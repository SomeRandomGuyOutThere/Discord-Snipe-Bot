import os
from dotenv import load_dotenv
import discord
from discord.ext import commands 

load_dotenv()

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")

@bot.command()
async def snipe(ctx):
    pass


@bot.event
async def on_message_delete(ctx):

    deleted_message = ctx.content

    print(deleted_message)

    await ctx.channel.send(f"Sniped out {ctx.author.name} ! \nMessage : {deleted_message}")

@bot.command(aliases=['leave'])
async def leaveg(ctx):

    await ctx.send("Good bye !")
    await ctx.guild.leave()

@bot.command(aliases=['createdby'])
async def info(ctx):
    await ctx.send("I was created by Wumble")  # it's my discord username 

if __name__ == '__main__':
    
    token = os.getenv('TOKEN')
    bot.run(token)
