import requests
import json
# set the apikey and limit
import Database as DB

tenorApikey = "E43EM9PO00HC"
import discord
from datetime import datetime as dt
# import pytz
from discord.ext import commands, tasks
import discord.utils
from discord.utils import get
import random
# import os.path
import pickle
# import Database
# from discord_slash import SlashCommand, SlashContext
# import os
# import asyncio
# import EmbedsGen

TOKEN = pickle.load(open("Token.p", "rb"))
AwesomePlaylistUrl = "https://open.spotify.com/playlist/48zKTHYlstmgrRZSbRPIaY?si=097fa6be533d4f8e"
ReplyDict = {1: "Aller Anfang ist schwer.",
             2: "Doppelt Gemoppelt hält besser",
             3: "Aller guten Dinge sind 3.",
             4: "4 me!",
             5: "High Five",
             6: ";)",

             10: "Zehn zahme Ziegen ziehen Zehn Zuckerzuber zum Zoo!"
             }
ReplyPicDict = {69: "69.gif",
                420: "420.gif"}
WordDict = {}
CountList = ["naja", "tho", "lol", "fdp", "nice", "fuck", "ahhh", "hurensohn", "arcane", "genshin impact", "kino"]
Fucking = False
random.seed()
Prefix = "LMAO!"
src = "xD/"
intents = discord.Intents().all()
client = commands.Bot(command_prefix=Prefix, description="Verkündet den wichtigsten Tag.", intents=intents)
# slash = SlashCommand(client, sync_commands=True)
Vahlo = client.get_user(563044022835347492)
VahloID = 563044022835347492
SlashOption = [
    {
        "name": f"channel",
        "description": f"Dein neuer Mittwoch Channel",
        "required": True,
        "type": 7
    }
]
List = []
EckeDerSchandeID = 826069082984939590
EckeDerSchande = client.get_channel(EckeDerSchandeID)
QuantiID = 293443718319570964  # 318299815786053633
Quanti = client.get_user(QuantiID)
Troll = False
for guild in client.guilds:
    List.append(guild.id)
OptionDict = {
    "Fucking": False,
    "Troll": []
}
Settings = {}
ServerDict = {"ServerID": OptionDict}
OmoriList = [704975440963698768, 293443718319570964, 508365874223251457]
Reminders = {508365874223251457: [6, "CWIMI ABEND"],
             508365874223251457: [3, "CWIMI ABEND"]}
search_term = "omori"

def getRandoTenorGif(searchTerm):
    r = requests.get(
        "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (searchTerm, tenorApikey, 420))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_8gifs = json.loads(r.content)
        # json.dump(r.content, "Testerino.json")
        #json.dump(top_8gifs, open("Testerino.json", "w"), indent=True)
        return top_8gifs["results"][DB.randoMod(100)]["media"][0]["mediumgif"]["url"]
    else:
        return None

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(message.mentions)
    for ReminderUser, Reminder in Reminders.items():
        for mention in message.mentions:
            print(mention.id, ReminderUser, Reminder)
            if mention.id == ReminderUser and Reminder[0] == dt.now().weekday():
                print("Haha")
                await message.reply(Reminder[1])


@client.command
async def addReminder(ctx, day, reminder):
    Reminders[ctx.guild.id] = [day, reminder]
    DB.addReminder(ctx.message.mentions[0].id, day, reminder)
    await ctx.send("Reminder added, ma dear. And ATM probably broken")
    
client.run(TOKEN)