import discord

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

client.run('MTAzMzQ1OTkyODI0Mjg2MDEyMw.GWIRYu.FUmpKS5cQXkuzpJMg5FhSGvvY-3Ef8JU1Kw1LQ')