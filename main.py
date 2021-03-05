import discord
import time
from discord.ext import commands, tasks
import random
import os
import os.path
import pickle
from collections import defaultdict


def NullVoid():
    return False


random.seed()
Prefix = "M!"
#  Lasties = defaultdict(NullVoid)
#  Channels = defaultdict(NullVoid)
#  Lasties = {}
#  """""
Channels = {776823258385088552: 803731340154503250, 701051127612964964: 806312041697509426}
#  """""
#  Channels[701051127612964964] = 806312041697509426  # Test Channel

#  Lasties[776823258385088552] = False  # 803731340154503250  # Ghost Cave
#  Lasties[701051127612964964] = False  # Test Channel
#  """""
pickle.dump(Channels, open("Channels.p", "wb"))
#  pickle.dump(Lasties, open("Lasties.p", "wb"))
#  """""
Channels = pickle.load(open("Channels.p", "rb"))
Lasties = pickle.load(open("Lasties.p", "rb"))
TOKEN = pickle.load(open("Token.p", "rb"))
print(Lasties)
src = "Mittwoch/"
client = commands.Bot(command_prefix=Prefix, description="Extrem wichtiger Bot für extrem wichtige Sachen!")

for files in os.walk(src):
    file_count = len(files)


@client.event
async def on_ready():
    for guilds in client.guilds:
        try:
            print(f"Connected to {guilds.name}({guilds.id}) der Mittwochschannel ist: {Channels[guilds.id]}")
            pickle.dump(Lasties, open("Lasties.p", "wb"))
        except:
            pass


@client.event
async def on_guild_join(guild):
    return



@client.command()
@commands.has_permissions(administrator=True)
async def Mittwoch_Channel(ctx):
    try:
        Mit_chl = client.get_channel(Channels[ctx.author.guild.id])
        print(ctx.author.guild.id)
        await ctx.send(f"Der Mittwochschannel ist{Mit_chl.mention} \n"
                   f"Wenn du ihn ändern möchtest schreib: {Prefix}Mittwoch_Change #(Channel)")
    except:
        pass


@client.command()
@commands.has_permissions(administrator=True)
async def Mittwoch_Change(ctx):
    try:
        Channels[ctx.author.guild.id] = ctx.message.channel_mentions[0].id
        Mit_chl = client.get_channel(Channels[ctx.author.guild.id])
        await ctx.send(f"Der neue Mittwochschannel ist{Mit_chl.mention}")
        pickle.dump(Channels, open("Channels.p", "wb"))
    except:
        pass


@client.command()
async def cmd(ctx, channel: discord.TextChannel):
    await ctx.send(f"Here's your mentioned channel ID: {channel.id}")


@tasks.loop(hours=2)
async def Channel_Check():
    for guilds in client.guilds:
        print(f"{guilds.name} == {guilds.id}")
        pickle.dump(Channels, open("Channels.p", "rb"))


@tasks.loop(minutes=5)
async def Mittwoch_check():
    await client.wait_until_ready()
    global Channels
    global Lasties
    activity = discord.Game(name="Professionel am Existieren.")
    for guilds in client.guilds:
        try:
            print("checking...")
            Lasties = pickle.load(open("Lasties.p", "rb"))
            activity = discord.Game(name="Professionel am Existieren.")
            print(f"der letzte Mittwoch war am :{Lasties[guilds.id]}")
            print(1)
            if time.strftime("%A") == "Wednesday" and Lasties[guilds.id] != time.strftime("%W,%Y"):
                try:
                    activity = discord.Game(name="mit seinem Penis.", type=3)
                    channel = client.get_channel(Channels[guilds.id])
                    print(f"{guilds.name}")
                except Exception as e:
                    print(e)
                try:
                    await channel.send(content="@everyone ES IST Mittwoch meine Kerle",
                                   file=discord.File(f"Mittwoch/Mittwoch{random.randint(1, file_count)}.png"))
                    print(guilds.name, Lasties[guilds.id])
                    Lasties[guilds.id] = time.strftime("%W,%Y")
                    print(time.strftime("%W,%Y"))
                    print(Lasties[guilds.id])
                    pickle.dump(Lasties, open("Lasties.p", "wb"))
                except AttributeError:
                    pass
            elif time.strftime("%A") != "Wednesday":
                "Kein Mittwoch"
                pickle.dump(Lasties, open("Lasties.p", "wb"))
            print(f"Es wurde auf dem Server {guilds.name}({guilds.id}) am {Lasties[guilds.id]} Gemittwocht")
        except Exception as e:
            print(e)
    await client.change_presence(activity=activity)


Channel_Check.start()
Mittwoch_check.start()
client.run(TOKEN)
