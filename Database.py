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
import json

tenorApikey = "E43EM9PO00HC"
src = "Mittwoch/"

Creds = pickle.load(open("Credentials.p", "rb"))
con = psycopg2.connect(database=Creds[0], user=Creds[1], password=Creds[2], host=Creds[3], port=Creds[4])
cur = con.cursor()


def createTable():
    cur.execute(f"CREATE TABLE WordCounter"
                f"("
                f"UserID BIGINT,"
                f"Countable TEXT,"
                f"Counter BIGINT"
                f");")
    con.commit()


def createOptionTable():
    cur.execute(f"CREATE TABLE Option"
                f"("
                f"ServerID BIGINT,"
                f"Option TEXT,"
                f"Toggle BOOL,"
                f"Number BIGINT,"
                f"Targets ARRAY"
                f");")
    con.commit()


def getBoolOption(ServerID, Option):
    BoolOptionQuery = "SELECT Toggle FROM Option WHERE ServerID = %s AND Option = %s;"
    BoolOptionData = (ServerID, Option)

    try:
        cur.execute(BoolOptionQuery, BoolOptionData)
        try:
            return cur.fetchall()[0]
        except IndexError:
            return cur.fetchall()
    except Exception as e:
        print(f"getBoolOption({ServerID}, {Option}) raised {e}")


def toggleBoolOption(ServerID, Option, Toggle):
    BoolOptionUpdateRequest = "UPDATE Option SET Toggle = %s WHERE ServerID = %s AND Option = %s;"
    BoolOptionUpdateData = (Toggle, ServerID, Option)

    try:
        cur.execute(BoolOptionUpdateRequest, BoolOptionUpdateData)
        con.commit()
    except Exception as e:
        print(f"toggleBoolOption({ServerID}, {Option}, {Toggle}) raised {e}")


def getCount(UserID, Countable):
    CountRequest = "SELECT Counter FROM WordCounter WHERE UserID = %s AND Countable = %s;"
    CountData = (UserID, Countable)
    CheckUserQuery = "SELECT EXISTS(SELECT 1 FROM WordCounter WHERE UserID = %s AND Countable = %s);"
    CheckUserData = (UserID, Countable)
    InsertAll = "INSERT INTO WordCounter (UserID, Countable, Counter) VALUES (%s, %s, %s);"

    cur.execute(CheckUserQuery, CheckUserData)
    if cur.fetchall()[0][0]:
        cur.execute(CountRequest, CountData)
        return cur.fetchall()[0][0]
    else:
        cur.execute(InsertAll, (UserID, Countable, 0))
        con.commit()
        cur.execute(CountRequest, CountData)
        return cur.fetchall()[0][0]


def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di


def getAllCount(UserID):
    CountRequest = "SELECT Counter, Countable FROM WordCounter WHERE UserID = %s;"
    CountData = (UserID,)
    CheckUserQuery = "SELECT EXISTS(SELECT 1 FROM WordCounter WHERE UserID = %s);"
    CheckUserData = (UserID,)

    cur.execute(CheckUserQuery, CheckUserData)
    if cur.fetchall()[0][0]:
        cur.execute(CountRequest, CountData)
        return dict(sorted(dict(cur.fetchall()).items(), reverse=True))
    else:
        return None


def UpdateCount(UserID, Countable, Count):
    UpdateRequest = "UPDATE WordCounter SET Counter = %s WHERE UserID = %s AND Countable = %s;"
    UpdateData = (Count, UserID, Countable)
    try:
        cur.execute(UpdateRequest, UpdateData)
        con.commit()
        return True
    except Exception:
        return False


def getLast(ServerID):
    try:
        cur.execute(f"SELECT LastTime FROM main WHERE ServerID IN({ServerID})")
        try:
            return cur.fetchall()[0][0]  # .replace(" ","")
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


def getAll():
    cur.execute(f"SELECT * FROM main")
    try:
        return cur.fetchall()
    except IndexError:
        return cur.fetchall()


def deleteAll():
    cur.execute(f"DELETE FROM main")


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
    cur.execute(f"SELECT EXISTS(SELECT 1 FROM main WHERE ServerID = {ServerID})")
    if not cur.fetchall()[0][0]:
        cur.execute(f"INSERT INTO main (ServerID, WedChan, LastTime) VALUES ({ServerID}, NULL, NULL);")
        con.commit()
        return True


def rando():
    file_count = 35
    for files in os.walk(src):
        file_count = len(files)
    GET = requests.get(
        f"https://www.random.org/integers/?num=1&min=1&max={file_count}&col=1&base=10&format=plain&rnd=new")
    return GET.text.split("\n")[0]


def randoMod(MaxNum):
    file_count = MaxNum
    for files in os.walk(src):
        file_count = len(files)
    GET = requests.get(
        f"https://www.random.org/integers/?num=1&min=0&max={file_count}&col=1&base=10&format=plain&rnd=new")
    return int(GET.text.split("\n")[0])


def getRandoTenorGif(searchTerm):
    r = requests.get(
        "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (searchTerm, tenorApikey, 50))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_8gifs = json.loads(r.content)
        json.dump(json.loads(r.content), open("Testerino.json", "w"))
        RandoNum = randoMod(49)
        RandoNum = random.randint(0, 49)
        print(RandoNum)
        try:
            return top_8gifs["results"][RandoNum]["media"][0]["mediumgif"]["url"]
        except IndexError:
            try:
                return top_8gifs["results"][RandoNum]["media"][0]["smallgif"]["url"]
            except IndexError:
                try:
                    return top_8gifs["results"][RandoNum]["media"][0]["tinygif"]["url"]
                except IndexError:
                    return top_8gifs["results"][RandoNum]["media"][0]["nanogif"]["url"]

    else:
        return None


def getSettings(guildID):
    pass

if __name__ == "__main__":
    # print(getLast(776823258385088552))
    # print(bool(dt.now(tz=pytz.timezone("Europe/Amsterdam")).strftime("%e.%m.%y") != getLast(776823258385088552)))
    pass
