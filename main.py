import discord
from datetime import datetime as dt
import pytz
from discord.ext import commands, tasks
from discord.utils import get
import random
import os.path
import pickle
import Database
from discord_slash import SlashCommand, SlashContext, SlashCommandOptionType
import requests

Fucking = True
random.seed()
Prefix = "M!"
TOKEN = pickle.load(open("Token.p", "rb"))
src = "Mittwoch/"
intents = discord.Intents().all()
client = commands.Bot(command_prefix=Prefix,
                      description="Verkündet den wichtigsten Tag.",
                      intents=intents)  # , help_command=PrettyHelp(no_category="Interactions"))

slash = SlashCommand(client, sync_commands=True)

SlashOption = [
    {
        "name": f"channel",
        "description": f"Dein neuer Mittwoch Channel",
        "required": True,
        "type": 7
    }

]
List = []
for guild in client.guilds:
    List.append(guild.id)


@client.event
async def on_ready():
    for Guild in client.guilds:
        Database.AddEntry(Guild.id)

    print("Done")


@client.event
async def on_message(message):
    if Fucking:
        if "fucking" in message.content.lower():
            await message.reply("Die Stadt ?")


@client.command(pass_context=True)  # , description=Description, name=self.command, aliases=self.aliases)
async def Channel(ctx):
    Chan = client.get_channel(Database.getMitChan(ctx.guild.id))
    await ctx.send(
        f"Der aktuelle Mittwoch Channel ist: {Chan.mention}. \n Du kannst ihn ändern mit {Prefix}SetChannel #[Neuer "
        f"Channel].")


@client.command(pass_context=True)  # , description=Description, name=self.command, aliases=self.aliases)
async def SetChannel(ctx, channel: discord.TextChannel):
    Database.UpdateMitChan(ctx.guild.id, channel.id)
    Chan = client.get_channel(Database.getMitChan(ctx.guild.id))
    await ctx.send(f"Der neue Mittwoch Channel ist: {Chan.mention}.")


@slash.slash(guild_ids=[701051127612964964])
async def Channel(ctx):
    Chan = client.get_channel(Database.getMitChan(ctx.guild.id))
    await ctx.send(
        f"Der aktuelle Mittwoch Channel ist: {Chan.mention}. \n Du kannst ihn ändern mit /SetChannel.")


@slash.slash(guild_ids=[701051127612964964], options=SlashOption)  # ,aliases=self.aliases)
async def SetChannel(ctx: SlashContext, channel):
    Database.UpdateMitChan(ctx.guild.id, channel.id)
    Chan = client.get_channel(Database.getMitChan(ctx.guild.id))
    await ctx.send(f"Der neue Mittwoch Channel ist: {Chan.mention}.")


@tasks.loop(minutes=10)
async def Mittwoch_check():
    await client.wait_until_ready()
    print("Looking for Wednesday")
    for guilds in client.guilds:
        if dt.now(tz=pytz.timezone("Europe/Amsterdam")).weekday() == 2:
            print("Ahh yes meine Kerle")
            if dt.now(tz=pytz.timezone("Europe/Amsterdam")).strftime("%e.%m.%y") != Database.getLast(guilds.id):
                print("Zeit für ein nices Meme")
                MitChanID = Database.getMitChan(guilds.id)
                if MitChanID is not None:
                    channel = client.get_channel(MitChanID)
                else:
                    await guilds.owner.send("Grüß dich Mein Kerl. Leider konnte ich die frohe Botschaft des "
                                            "Mittwoches nicht verkünden, da ich nicht weiß wo ich das machen sollte. "
                                            "Du kannst dass ändern mit dem Befehl M/MitChan oder einem Schrägstrich "
                                            "Befehl.\n Mit freundlichen Grüßen Der Mittwochbot.")
                    continue
                await client.change_presence(
                    activity=discord.Activity(type=discord.ActivityType.watching, name="lustige Mittwoch Memes"))
                await channel.send(content="@everyone ES IST Mittwoch meine Kerle",
                                   file=discord.File(f"Mittwoch/Mittwoch{str(Database.rando())}.png"))
                Database.UpdateLastTime(guilds.id, dt.now(tz=pytz.timezone("Europe/Amsterdam")).strftime("%e.%m.%y"))
        else:
            await client.change_presence(activity=discord.Game(name="das ewige Wartespiel"))


Mittwoch_check.start()
client.run(TOKEN)
