import discord
from discord import Webhook, SyncWebhook
import aiohttp
import requests

#work on webhook integration
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('poopy'):
        await message.channel.send('STINKY')
        print(f'poopy has been registered')

webhook = SyncWebhook.from_url('https://discord.com/api/webhooks/[https://discord.com/api/webhooks/1055251923822968833/go13kfcvXVA2n0jhiRgaXDqvGOu_4KaYsJvWMr-fiNbviDGpVp8A_yAgX4KOETr51OqS]')
webhook.send(content="Hello World")



client.run('MTAzMzQ1OTkyODI0Mjg2MDEyMw.GImUKN.BTuVKWzzSqMp32nWXdrTvnPzYeksN43zWinVOY')