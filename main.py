import discord
import time
from datetime import datetime as dt
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
    776823258385088552: 803731340154503250,  # GhostCave
    701051127612964964: 806312041697509426  # Test Nils
}
src = "Mittwoch/"
client = commands.Bot(command_prefix=Prefix, description="Extrem wichtiger Bot für extrem wichtige Sachen!")
Delemiter = ";:;"
role_name = "Mittwoch⠀Boii"

for files in os.walk(src):
    file_count = len(files)

"""
async def DisSafe(Object):
    channel = client.get_channel(821116383713951756)
    Returnstring = ""
    if Object is not await DisLoad():
        for Guilds, Data in Object.items():
            Returnstring = Returnstring + str(Guilds) + Delemiter + str(Data["Channels"]) + Delemiter + str(
                Data["Lasties"]) + "\n"
        await channel.send(content=Returnstring)


async def DisLoad():
    ReturnObject = {}
    channel = client.get_channel(821116383713951756)
    messages = await channel.history(limit=200).flatten()
    for message in messages:
        if message.author == client.user:
            try:
                for Data in message.content.split("\n"):
                    Datachunk = Data.split(Delemiter)
                    ReturnObject[int(Datachunk[0])] = {"Channels": int(Datachunk[1]), "Lasties": Datachunk[2]}
                return ReturnObject
            except Exception as e:
                print(e)
"""


@client.event
async def on_ready():
    global role
    for guilds in client.guilds:
        check_for_duplicate = get(guilds.roles, name=role_name)
        if check_for_duplicate is None:
            role = await guilds.create_role(name=role_name)
    print("Done")


"""""
@client.command()
@commands.has_permissions(administrator=True)
async def Mittwoch_Channel(ctx):
    global Data
    try:
        Mit_chl = client.get_channel(Data[ctx.author.guild.id]['Channels'])
        print(ctx.author.guild.id)
        await ctx.send(f"Der Mittwochschannel ist{Mit_chl.mention} \n"
                       f"Wenn du ihn ändern möchtest schreib: {Prefix}Mittwoch_Change #(Channel)")
    except Exception as e:
        print(e)


@client.command()
@commands.has_permissions(administrator=True)
async def Mittwoch_Change(ctx):
    global Data
    try:
        Channels[ctx.author.guild.id] = ctx.message.channel_mentions[0].id
        Mit_chl = client.get_channel(Data[ctx.author.guild.id]['Channels'])
        await ctx.send(f"Der neue Mittwochschannel ist{Mit_chl.mention}")
        await DisSafe(Data)
    except Exception as e:
        print(e)
"""""


@tasks.loop(minutes=60)
async def Mittwoch_check():
    await client.wait_until_ready()
    for guilds in client.guilds:
        Botmember = get(guilds.members, id=client.user.id)
        role = get(guilds.roles, name=role_name)
        if time.strftime("%A") == "Wednesday":
            if role in member.roles:
                channel = client.get_channel(Channels[guilds.id])
                await client.change_presence(
                    activity=discord.Activity(type=discord.ActivityType.watching, name="lustige Mittwoch Memes"))
                await channel.send(content="@everyone ES IST Mittwoch meine Kerle",
                                   file=discord.File(f"Mittwoch/Mittwoch{random.randint(1, file_count)}.png"))
                await Botmember.add_roles(role, reason="Weil es Mittwoch ist.")
        else:
            await client.change_presence(activity=discord.Game(name="das ewige Wartespiel"))
            await Botmember.remove_roles(role, reason="Es ist nicht mehr Mittwoch")


Mittwoch_check.start()
client.run(TOKEN)
