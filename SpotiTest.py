import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import discord
from discord.ext import commands
import youtube_dl
import os
import pickle
import discord.utils

# discord.opus.load_opus()
TOKEN = pickle.load(open("Token.p", "rb"))
intents = discord.Intents().all()
client = commands.Bot(command_prefix="M!", intents=intents)
VoiceClients = {}
Queues = {}


def FicktEuch(List, id):
    for Item in List:
        print(Item)
        print(Item.guild.id)
        if Item.guild.id == id:
            return Item


def getGuildQue(GuildID):
    try:
        GuildQue = Queues[GuildID]
        if GuildQue is not None:
            return GuildQue
    except KeyError:
        Queues[GuildID] = Queueü(GuildID)
        return Queues[GuildID]


@client.event
async def on_ready():
    print("AHHHHHHHH!!!")
    for guild in client.guilds:
        VoiceClients[guild.id] = None


@client.command()
async def play(ctx, url: str):
    VoiceClient = discord.utils.get(client.voice_clients, guild=ctx.guild)
    VoiceChannel = ctx.message.author.voice.channel
    if VoiceClient is None:
        await VoiceChannel.connect()
        VoiceClient = discord.utils.get(client.voice_clients, guild=ctx.guild)
        VoiceClients[ctx.guild.id] = VoiceClient
    elif VoiceClient.channel != VoiceChannel and VoiceChannel.is_connected():
        await ctx.send("You're in the wrong Channel mate!")
        return
    GuildQue = getGuildQue(ctx.guild.id)
    if VoiceClient.is_playing():
        await ctx.send("Adding to Queueueueueue!!")
        GuildQue.addTrack(Track(None, None, None, url))
    else:
        GuildQue.addTrack(Track(None, None, None, url))
        GuildQue.start()
        await ctx.send("Playing UwU")


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def Queue(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    await ctx.send(Queues[voice.channel.id])


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


@client.command()
async def skip(ctx):
    GuildQue = getGuildQue(ctx.guild)
    GuildQue.skip()


class Track:
    def __init__(self, Type, Length, Metadata, Url, Done=False):
        self.Type = Type
        self.Length = Length
        self.Metadata = Metadata
        self.Url = Url
        self.Done = Done


class Queueü:
    def __init__(self, GuildID, VoiceClient=None, Loop=False):
        self.Qüüü = []
        self.GuildID = GuildID
        self.SkipFlag = False
        self.ydl_opts = {
            "outtmpl": f"/{self.GuildID}.mp3",
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        self.VoiceClient = VoiceClient
        self.Loop = Loop

    def play(self, Track):
        print(client.voice_clients[0].guild.id)
        self.VoiceClient = FicktEuch(client.voice_clients, self.GuildID)
        if self.VoiceClient is not None:
            with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
                try:
                    os.remove(f"{self.GuildID}.mp3")
                except FileNotFoundError:
                    pass
                ydl.download([Track.Url])
        self.VoiceClient.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(f"{self.GuildID}.mp3"), 0.5))

    def start(self):
        i = 0
        while i < len(self.Qüüü) or self.SkipFlag:
            CurrentTrack = self.Qüüü[i]
            if CurrentTrack.Done:
                continue
            if not self.SkipFlag:
                self.play(CurrentTrack)
            CurrentTrack.Done = True
            self.SkipFlag = False
            i = i + 1

    def skip(self):
        self.SkipFlag = True
        self.VoiceClient = discord.utils.get(client.voice_clients, guild__id=self.GuildID)
        self.VoiceClient.stop()
        self.SkipFlag = True
        self.start()

    def addTrack(self, Track: Track, pos=None):
        if pos is None:
            self.Qüüü.append(Track)
        else:
            self.Qüüü.insert(pos - 1, Track)


client.run(TOKEN)
# If you wish to securely hide your token, you can do so in a .env file.
# 1. Create a .env in the same directory as your Python scripts
# 2. In the .env file format your variables like this: VARIABLE_NAME=your_token_here
# 3. At the top of the Python script, import os
# 4. In Python, you can read a .env file using this syntax:
# token = os.getenv(VARIABLE_NAME)
"""

PlaylistList = []
ClientID = "3bd576c93ab843e7b39205c9a2b3ef01"
ClientSecret = "e6b86e71bd1b48adb096eae64c77daf2"

AwesomePlaylistUrl = "https://open.spotify.com/playlist/6TCCCUBd0eE7xmACdHwAve?si=2b356fe0304a4d36"
"https://open.spotify.com/playlist/48zKTHYlstmgrRZSbRPIaY?si=097fa6be533d4f8e"

SpotifyClient = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(client_id=ClientID, client_secret=ClientSecret))

AwesomePlaylist = SpotifyClient.playlist(AwesomePlaylistUrl)
print(AwesomePlaylist)
for Item in AwesomePlaylist["tracks"]["items"]:
    PlaylistList.append(Item["track"]["uri"])

SpotifyClient.start_playback(PlaylistList[2])

"""
