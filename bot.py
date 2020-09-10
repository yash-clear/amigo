
import discord
import requests
import joke_api
import os

from dotenv import load_dotenv
URL = 'https://official-joke-api.appspot.com/random_joke'
load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

from discord.ext import commands
#GUILD='CodingClub-Development'
client = commands.Bot(command_prefix="!")


@client.command(pass_context=True)
async def DM(ctx, user: discord.User, *, message=None):
    message = message or "This Message is sent via DM"
    await user.send_message(user, message)


@client.command(help="it will print whatever u write")
async def print(ctx, *args):
	response = ""

	for arg in args:
		response = response + " " + arg

	await ctx.channel.send(response)



@client.command(help="ensuring the working of client",brief="Prints pong back to the channel.")
async def ping(ctx):
	await ctx.channel.send("pong")
	

@client.command(help="say hello to amigo")
async def hello(ctx):
	await ctx.channel.send("Hello, I hope you brought a pizza for me")



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!joke'):
        joke = joke_api.get_joke()
        print(joke)

        if joke == False:
            await message.channel.send("Couldn't get joke from API. Try again later.")
        else:
            await message.channel.send(joke['setup'] + '\n' + joke['punchline'] )
    await client.process_commands(message)

'''       
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to Coding Club IIT Jammu Discord server.')
    await logs.print(f'{member.mention} joined Server!')
'''
client.run(DISCORD_TOKEN)