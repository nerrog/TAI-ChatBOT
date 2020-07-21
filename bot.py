import pya3rt
import discord

TOKEN = 'Discord Token Here'
client = discord.Client()


def send_message(message):
    apikey = "A3RT TalkAPI Token Here"
    client = pya3rt.TalkClient(apikey)
    reply_message = client.talk(message)
    return reply_message['results'][0]['reply']

@client.event
async def on_ready():

    print('( ᐛ👐) パァ')
    activity = discord.Activity(name='tai-chat', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)

@client.event
async def on_message(message_disco):

    if message_disco.author.bot:
        return

    if message_disco.channel.name == "tai-chat":
        message = message_disco.content
        reply   = send_message(message)
        await message_disco.channel.send(reply)
client.run(TOKEN)
