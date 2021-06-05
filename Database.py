import discord
from datetime import datetime as dt
import pytz
from discord.ext import commands, tasks
from discord.utils import get
import random
import os.path
import pickle
from discord_slash import SlashCommand, SlashContext, SlashCommandOptionType
import requests
import psycopg2

src = "Mittwoch/"

Creds = pickle.load(open("Credentials.p", "rb"))
con = psycopg2.connect(database=Creds[0], user=Creds[1], password=Creds[2], host=Creds[3], port=Creds[4])
cur = con.cursor()


def getLast(ServerID):
    try:
        cur.execute(f"SELECT LastTime FROM main WHERE ServerID IN({ServerID})")
        try:
            return cur.fetchall()[0][0]#.replace(" ","")
        except IndexError or AttributeError:
            return cur.fetchall()
    except Exception:
        return False


def getMitChan(ServerID):
    try:
        cur.execute(f"SELECT WedChan FROM main WHERE ServerID IN({ServerID})")
        try:
            return cur.fetchall()[0][0]
        except IndexError:
            return cur.fetchall()
    except Exception:
        return False


def UpdateMitChan(ServerID, MitChan):
    try:
        cur.execute(f"UPDATE main SET WedChan = '{MitChan}' WHERE ServerID = {ServerID}")
        con.commit()
        return True
    except Exception:
        return False


def UpdateLastTime(ServerID, LastTime):
    try:
        cur.execute(f"UPDATE main SET LastTime = '{LastTime}' WHERE ServerID = {ServerID}")
        con.commit()
        return True
    except Exception:
        return False


def AddEntry(ServerID):
    if not cur.execute(f"SELECT EXISTS(SELECT 1 FROM main WHERE ServerID = {ServerID})"):
        cur.execute(f"INSERT INTO main (ServerID, WedChan, LastTime) VALUES ({ServerID}, NULL, NULL);")
    con.commit()
    return True


def rando():
    for files in os.walk(src):
        file_count = len(files)
    GET = requests.get(
        f"https://www.random.org/integers/?num=1&min=1&max=35&col=1&base=10&format=plain&rnd=new")
    return GET.text.split("\n")[0]


if __name__ == "__main__":
    print(getLast(776823258385088552))
    print(bool(dt.now(tz=pytz.timezone("Europe/Amsterdam")).strftime("%e.%m.%y") != getLast(776823258385088552)))
