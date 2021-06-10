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
import youtube_dl
import os
import asyncio
"""
import spotify
from spotify.oauth import Spo
"""
TOKEN = pickle.load(open("Token.p", "rb"))
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
ClientID = "3bd576c93ab843e7b39205c9a2b3ef01"
ClientSecret = "e6b86e71bd1b48adb096eae64c77daf2"

AwesomePlaylistUrl = "https://open.spotify.com/playlist/48zKTHYlstmgrRZSbRPIaY?si=097fa6be533d4f8e"
ReplyDict = {1: "Aller Anfang ist schwer.",
             3: "Aller guten Dinge sind 3.",
             }
ReplyPicDict = {69: "69.gif",
                420: "420.gif"}
WordDict = {}
CountList = ["naja", "tho", "lol", "fdp"]
Fucking = True
random.seed()
Prefix = "M!"
discord.voice_client
src = "Mittwoch/"
intents = discord.Intents().all()
client = commands.Bot(command_prefix=Prefix, description="Verkündet den wichtigsten Tag.", intents=intents)
slash = SlashCommand(client)  # , sync_commands=True)
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
VahloName = "*crying about it*"
Troll = False
for guild in client.guilds:
    List.append(guild.id)

"""


@client.event
async def on_ready():
    # await slash.sync_all_commands(delete_from_unused_guilds=False)
    # await discord_slash.manage_commands.add_slash_command(bot_id=client.user.id, bot_token=TOKEN, guild_id=None,
    #                                                      cmd_name="setchannel",
    #                                                      description="Ändere den Mittwoch-Channel",
    #                                                      options=SlashOption)
    EckeDerSchandeID = 826069082984939590
    EckeDerSchande = client.get_channel(EckeDerSchandeID)
    QuantiID = 293443718319570964  # 318299815786053633
    Quanti = client.get_user(QuantiID)
    print(type(Quanti))
    for Guild in client.guilds:
        Quanti = Guild.get_member(QuantiID)
        Database.AddEntry(Guild.id)
    # await Quanti.move_to(EckeDerSchande)
    for i in client.voice_clients:
        print(i)
    player = vc.create_ffmpeg_player('vuvuzela.mp3', after=lambda: print('done'))
    player.start()
    '''
    
    for guild in client.guilds:
        if guild.name == "ghost cave":
            for channel in guild.channels:
                if channel.id == 776889397479735317:
                    print("JA")
                    Finally = channel
                    async for message in Finally.history(limit=10):
                        if message.id == 776892471497326633:
                            reactionSchwarz = message.reactions[0]
                            await message.add_reaction(reactionSchwarz)
    
    '''

    print("Done")
"""


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    for word in CountList:
        if message.author.id == 293443718319570964:
            if word in message.content.lower():
                WordCount = Database.getCount(message.author.id, word)
                WordCount = WordCount + 1
                WordText = f"Das ist dein {WordCount}. {word}."
                ReplyFile = None
                for key, val in ReplyDict.items():
                    if WordCount == key:
                        WordText = f"{WordText} {val}"
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

""""
@client.event
async def on_voice_state_update(member, before, after):
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

            # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            # ydl.download([url])
            # for file in os.listdir("./"):
            # if file.endswith(".mp3"):
            # os.rename(file, "song.mp3")
            player = await YTDLSource.from_url(url, loop=client.loop, stream=True)
            voiceClient.play(player)
            await asyncio.sleep(30)
            await VoiceChannel.disconnect()
            """


@client.command(pass_context=True)  # , description=Description, name=self.command, aliases=self.aliases)
async def Channel(ctx):
    Chan = client.get_channel(Database.getMitChan(ctx.guild.id))
    await ctx.send(
        f"Der aktuelle Mittwoch Channel ist: {Chan.mention}. \n Du kannst ihn ändern mit {Prefix}SetChannel #[Neuer "
        f"Channel].")

"""
@client.event
async def on_member_update(before, after):
    if before.id == VahloID:
        print("Haha")
        if not after.nick == VahloName:
            await before.edit(nick=VahloName)
            await after.edit(nick=VahloName)
"""


@client.command(pass_context=True)  # , description=Description, name=self.command, aliases=self.aliases)
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

"""
@client.command(pass_context=True)
async def Test(ctx, url):
    VoiceChannel = ctx.message.author.voice.channel
    VoiceClient = await VoiceChannel.connect()
    print(ctx.voice_client.source)
    guild = ctx.message.guild
    voiceClient = discord.utils.get(client.voice_clients, guild=ctx.guild)
    players[guild.id] = voiceClient

    ydl_opts = {
        "outtmpl": f"/{ctx.guild.id}",
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("/"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    print(type(ctx.voice_client.source))
    Player = YTDLSource(VoiceClient.source, data=ydl_opts)
    print(Player)
    await voiceClient.play(Player.from_url(url))
    # player.start()
"""


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
                        # await guilds.owner.send("Grüß dich Mein Kerl. Leider konnte ich die frohe Botschaft des "
                        #                   "Mittwoches nicht verkünden, da ich nicht weiß wo ich das machen sollte. "
                        #                  "Du kannst dass ändern mit dem Befehl M/MitChan oder einem Schrägstrich "
                        #                 "Befehl.\n Mit freundlichen Grüßen Der Mittwochbot.")
                        continue
                    await client.change_presence(
                        activity=discord.Game(name="Amogus"))
                    await channel.send(content="@everyone Es ist Mittwoch meine Kerle",
                                       file=discord.File(f"Mittwoch/Mittwoch{str(Database.rando())}.png"))
                    Database.UpdateLastTime(guilds.id,
                                            dt.now(tz=pytz.timezone("Europe/Amsterdam")).strftime("%e.%m.%y"))
                except AttributeError:
                    pass
                    # Database.UpdateMitChan(guilds.id, 0)
        else:
            await client.change_presence(activity=discord.Game(name="Fortnait"))


Mittwoch_check.start()
client.run(TOKEN)
