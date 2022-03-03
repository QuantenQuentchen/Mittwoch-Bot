import discord
from datetime import datetime as dt
import pytz
from discord.ext import commands, tasks
import discord.utils
from discord.utils import get
import random
import os.path
import pickle
import Database
from discord_slash import SlashCommand, SlashContext
import os
import asyncio

import EmbedsGen

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
slash = SlashCommand(client, sync_commands=True)
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


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="SlashCommands"))
    await slash.sync_all_commands(delete_from_unused_guilds=True)
    for Guild in client.guilds:
        Settings[Guild.id] = Database.getSettings(Guild.id)
        Quanti = Guild.get_member(QuantiID)
        Database.AddEntry(Guild.id)
    print("Done")


@client.command(pass_context=True)
async def play(ctx):
    VoiceClient = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if ctx.message.author.voice is not None:
        VoiceChannel = ctx.message.author.voice.channel
        if VoiceClient is None:
            await VoiceChannel.connect()
            VoiceClient = discord.utils.get(client.voice_clients, guild=ctx.guild)
        await LoopSchmoop(ctx, VoiceClient)


async def LoopSchmoop(ctx, VoiceClient):
    await ctx.send('Playing: "FORTNITE SONG "Skybase" Standart Skill feat. Ayanda (Official Music Video)"')
    await VoiceClient.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(f"OneAndOnly.mp3"), 0.5))
    await LoopSchmoop(ctx, VoiceClient)


@client.command(pass_context=True)
async def EndeDenSchmerz(ctx):
    VoiceClient = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if VoiceClient.is_connected():
        await ctx.send(embed=EmbedsGen.genLeaveEmbed())
        await VoiceClient.disconnect()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    for word in CountList:
        if word in message.content.lower():
            WordCount = Database.getCount(message.author.id, word)
            WordCount = WordCount + 1
            WordText = f"Das ist dein {WordCount}. {word}."
            ReplyFile = None
            for key, val in ReplyDict.items():
                if WordCount == key:
                    WordText = f"{WordText} {val}"
                    await message.reply(WordText, mention_author=False, file=ReplyFile)
            for key, val in ReplyPicDict.items():
                if WordCount == key:
                    ReplyFile = discord.File(val)
                    await message.reply(WordText, mention_author=False, file=ReplyFile)
            Database.UpdateCount(message.author.id, word, WordCount)

    if Troll:
        if message.author.id == VahloID:
            await message.reply(file=discord.File("CryAbout.gif"))
        if "5,3" in message.content.lower():
            await message.reply(f"<@{VahloID}>")
        if message.content.lower() in ["lol", "League", "League of Legends"]:
            await message.reply(f"<@{VahloID}>")

    if Fucking:
        if "fucking" in message.content.lower():
            await message.reply("Die Stadt ?", mention_author=False, )
    await client.process_commands(message)


@client.event
async def on_voice_state_update(member, before, after):
    members = after.channel.members
    MemId = []
    for meberino in channel.members:
        MemId.append(memberino.id)
    if False:
        if all(x in OmoriList for x in MemId) and len(MemId) == 2 and OmoriPing:
            for CoolDud in OmoriList:
                if CoolDud not in MemId:
                    Channel = Database.getMitChan(ServerID)
                    MissingPep = await client.get_user(CoolDud)
                    await Channel.send("")
        if member.id == VahloID:
            if not after.channel == None or after.channel == EckeDerSchande:
                await member.move_to(EckeDerSchande)

                VoiceChannel = after.channel
                guild = member.guild
                voiceClient = discord.utils.get(client.voice_clients, guild=member.guild)
                players[guild.id] = voiceClient

                ydl_opts = {
                    "format": "bestaudio/best",
                    "postprocessors": [{
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }],
                }
                player = await YTDLSource.from_url(url, loop=client.loop, stream=True)
                voiceClient.play(player)
                await asyncio.sleep(30)
                await VoiceChannel.disconnect()


@client.command(pass_context=True)
async def Channel(ctx):
    Chan = client.get_channel(Database.getMitChan(ctx.guild.id))
    await ctx.send(
        f"Der aktuelle Mittwoch Channel ist: {Chan.mention}. \n Du kannst ihn ändern mit {Prefix}SetChannel #[Neuer "
        f"Channel].")


@client.command(pass_context=True)
async def SetChannel(ctx, channel: discord.TextChannel):
    text_channel_list = []
    Chan = client.get_channel(Database.getMitChan(ctx.guild.id))
    for channäl in ctx.guild.text_channels:
        text_channel_list.append(channäl.id)
    if channel.id in text_channel_list:
        Database.UpdateMitChan(ctx.guild.id, channel.id)
        await ctx.send(f"Der neue Mittwoch Channel ist: {Chan.mention}.")
    else:
        await ctx.send(f"Bitte benutze einen Channl der Existiert und auf den der Bot zugriff hat.\nDer Mittwoch "
                       f"Channel bleibt {Chan.mention}")


@slash.slash(guild_ids=[701051127612964964, 776823258385088552])
async def Channel(ctx):
    Chan = client.get_channel(Database.getMitChan(ctx.guild.id))
    await ctx.send(
        f"Der aktuelle Mittwoch Channel ist: {Chan.mention}. \n Du kannst ihn mit /SetChannel ändern.")


@slash.slash(guild_ids=[701051127612964964, 776823258385088552], options=SlashOption)  # ,aliases=self.aliases)
async def SetChannel(ctx: SlashContext, channel):
    text_channel_list = []
    Chan = client.get_channel(Database.getMitChan(ctx.guild.id))
    for channäl in ctx.guild.text_channels:
        text_channel_list.append(channäl.id)
    if channel.id in text_channel_list:
        Database.UpdateMitChan(ctx.guild.id, channel.id)
        await ctx.send(f"Der neue Mittwoch Channel ist: {Chan.mention}.")
    else:
        await ctx.send(f"Bitte benutze einen Channl der Existiert und auf den der Bot zugriff hat.\nDer Mittwoch "
                       f"Channel bleibt {Chan.mention}")


@slash.slash(guild_ids=[919734517881778186, 701051127612964964, 776823258385088552],
             description="Funktioniert nicht. Was du heute kannst besorgen und so...")
async def SetOmori(ctx: SlashContext):
    pass


@slash.slash(guild_ids=[919734517881778186, 701051127612964964, 776823258385088552],
             description="Ping den Rest der OMORIII GANG!!!")
async def OmoriPing(ctx: SlashContext):
    PingPong = f""
    nichtIchList = []
    ichList = []
    for ID in OmoriList:
        if ID == ctx.author.id:
            continue
        nichtIchList.append(client.get_user(ID))
    ichList.append(ctx.author)
    for usr in nichtIchList:
        PingPong = PingPong + f"{usr.mention}"
    await ctx.send(PingPong, embed=EmbedsGen.genOmoriPing(nichtIchList, ichList))


@slash.slash(guild_ids=[919734517881778186, 701051127612964964, 776823258385088552],
             description="Interessante Fakten über Diego Garcia")
async def GarciaFacts(ctx: SlashContext):
    await ctx.send(embed=EmbedsGen.genGarciaEmbed())


@client.command(pass_context=True)
async def GarciaFacts():
    await ctx.send(embed=EmbedsGen.genGarciaEmbed())


@slash.slash(guild_ids=[919734517881778186])
async def TestEmbed(ctx: SlashContext):
    nichtIchList = []
    ichList = []
    for ID in IDList:
        nichtIchList.append(client.get_user(ID))
    ichList.append(client.get_user(293443718319570964))
    await ctx.send(embed=EmbedsGen.genOmoriPing(nichtIchList, ichList))


@client.command(pass_context=True)
async def TestEmbed():
    await ctx.send("LMAO")


@tasks.loop(minutes=60)
async def Mittwoch_check():
    await client.wait_until_ready()
    print("Looking for Wednesday")
    for guilds in client.guilds:
        if dt.now(tz=pytz.timezone("Europe/Amsterdam")).weekday() == 2:
            print("Ahh yes meine Kerle")
            if dt.now(tz=pytz.timezone("Europe/Amsterdam")).strftime("%e.%m.%y") != Database.getLast(guilds.id):
                print("Zeit für ein nices Meme")
                MitChanID = Database.getMitChan(guilds.id)
                try:
                    if MitChanID is not None:
                        channel = client.get_channel(MitChanID)
                    else:
                        continue
                    await client.change_presence(
                        activity=discord.Game(name="Amogus"))
                    await channel.send(content="@everyone Es ist Mittwoch meine Kerle!!!!",
                                       file=discord.File(f"Mittwoch/Mittwoch{str(Database.rando())}.png"))
                    Database.UpdateLastTime(guilds.id,
                                            dt.now(tz=pytz.timezone("Europe/Amsterdam")).strftime("%e.%m.%y"))
                except AttributeError:
                    pass
                    # Database.UpdateMitChan(guilds.id, 0)
        else:
            # await client.change_presence(activity=discord.Game(name="Fortnait"))
            await client.change_presence(activity=discord.Game(name="SlashCommands"))


@slash.slash(guild_ids=[701051127612964964, 776823258385088552, 919734517881778186])
async def counter(ctx):
    await ctx.reply(embed=EmbedsGen.genCounterEmbed(ctx.author))


@client.command(pass_context=True)
async def counter(ctx):
    await ctx.reply(embed=EmbedsGen.genCounterEmbed(ctx.author))

Mittwoch_check.start()
client.run(TOKEN)
