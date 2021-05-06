import discord
import time
from datetime import datetime as dt
import pytz
from discord.ext import commands, tasks
from discord.utils import get
import random
import os
import os.path
import pickle
from collections import defaultdict
import dill


def NullVoid():
    return False

random.seed()
Prefix = "M!"
TOKEN = pickle.load(open("Token.p", "rb"))
Channel = {
    # 776823258385088552: 803731340154503250,  # GhostCave
    701051127612964964: 806312041697509426  # Test Nils
}
src = "Mittwoch/"
intents = discord.Intents().default()
intents.members = True
client = commands.Bot(command_prefix=Prefix, description="Extrem wichtiger Bot für extrem wichtige Sachen!",
                      intents=intents)
Delemiter = ";:;"
role_name = "Mittwoch⠀Boii"

for files in os.walk(src):
    file_count = len(files)


@client.event
async def on_ready():
    global role
    for guilds in client.guilds:
        check_for_duplicate = get(guilds.roles, name=role_name)
        if check_for_duplicate is None:
            role = await guilds.create_role(name=role_name)
    print("Done")


@tasks.loop(minutes=60)
async def Mittwoch_check():
    random.seed()
    await client.wait_until_ready()
    print("Looking for Wednesday")
    for guilds in client.guilds:
        Botmember = get(guilds.members, id=client.user.id)
        role = get(guilds.roles, name=role_name)
        if dt.now(tz=pytz.timezone("Europe/Amsterdam")).weekday() == 2:
            print("Ahh yes meine Kerle")
            if role not in Botmember.roles:
                print("Mittwoch war noch nicht Meine Kerle")
                channel = client.get_channel(Channel[guilds.id])
                await client.change_presence(
                    activity=discord.Activity(type=discord.ActivityType.watching, name="lustige Mittwoch Memes"))
                await channel.send(content="@everyone ES IST Mittwoch meine Kerle",
                                   file=discord.File(f"Mittwoch/Mittwoch{random.randint(1, file_count)}.png"))
                await Botmember.add_roles(role, reason="Weil es Mittwoch ist.")
        else:
            await client.change_presence(activity=discord.Game(name="das ewige Wartespiel"))
            await Botmember.remove_roles(role, reason="Es ist nicht mehr Mittwoch.")


Mittwoch_check.start()
client.run(TOKEN)
