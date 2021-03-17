import discord
import time
from discord.ext import commands, tasks
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
DATA = {}
src = "Mittwoch/"
client = commands.Bot(command_prefix=Prefix, description="Extrem wichtiger Bot für extrem wichtige Sachen!")
Delemiter = ";:;"

for files in os.walk(src):
    file_count = len(files)


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


@client.event
async def on_ready():
    for guilds in client.guilds:
        global Data
        Data = await DisLoad()
        #  global Data
        try:
            print(f"Connected to {guilds.name}({guilds.id}) der Mittwochschannel ist: {Data[guilds.id]['Channels']}")
            await DisSafe(Data)
        except Exception as e:
            print(e)


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


@tasks.loop(hours=2)
async def Channel_Check():
    global Data
    for guilds in client.guilds:
        print(f"{guilds.name} == {guilds.id}")
        await DisSafe(Data)


@tasks.loop(minutes=60)
async def Mittwoch_check():
    await client.wait_until_ready()
    global Data
    global Channels
    global Lasties
    activity = discord.Game(name="Professionel am Existieren.")
    for guilds in client.guilds:
        try:
            print("checking...")
            Data = await DisLoad()
            activity = discord.Game(name="Professionel am Existieren.")
            print(f"der letzte Mittwoch war am :{Data[guilds.id]['Lasties']}")
            if time.strftime("%A") == "Wednesday" and Data[guilds.id]['Lasties'] != time.strftime("%W,%Y"):
                try:
                    activity = discord.Game(name="mit seinem Penis.", type=3)
                    channel = client.get_channel(Data[guilds.id]['Channels'])
                    print(f"{guilds.name}")
                except Exception as e:
                    print(e)
                try:
                    await channel.send(content="@everyone ES IST Mittwoch meine Kerle",
                                       file=discord.File(f"Mittwoch/Mittwoch{random.randint(1, file_count)}.png"))
                    print(guilds.name, Data[guilds.id]['Lasties'])
                    Data[guilds.id]['Lasties'] = time.strftime("%W,%Y")
                    print(time.strftime("%W,%Y"))
                    print(Data[guilds.id]['Lasties'])
                    await DisSafe(Data)
                except AttributeError:
                    pass
            elif time.strftime("%A") != "Wednesday":
                "Kein Mittwoch"
                await DisSafe(Data)
            print(f"Es wurde auf dem Server {guilds.name}({guilds.id}) am {Data[guilds.id]['Lasties']} Gemittwocht")
        except Exception as e:
            print(e)
    await client.change_presence(activity=activity)


Channel_Check.start()
Mittwoch_check.start()
client.run(TOKEN)
