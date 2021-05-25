import psycopg2
import pickle

Creds = pickle.load(open("Credentials.p", "rb"))
con = psycopg2.connect(database=Creds[0], user=Creds[1], password=Creds[2], host=Creds[3], port=Creds[4])
cur = con.cursor()


def getLast(ServerID):
    cur.execute(f"SELECT LastTime FROM main WHERE ServerID IN({ServerID})")
    try:
        return cur.fetchall()[0][0]
    except IndexError:
        return cur.fetchall()


def getMitChan(ServerID):
    cur.execute(f"SELECT WedChan FROM main WHERE ServerID IN({ServerID})")
    try:
        return cur.fetchall()[0][0]
    except IndexError:
        return cur.fetchall()


def UpdateMitChan(ServerID, MitChan):
    cur.execute(f"UPDATE main SET WedChan = {MitChan} WHERE ServerID = {ServerID}")
    con.commit()
    return True


def UpdateLastTime(ServerID, LastTime):
    cur.execute(f"UPDATE main SET LastTime = '{LastTime}' WHERE ServerID = {ServerID}")
    con.commit()
    return True


def AddEntry(ServerID):
    if not cur.execute(f"SELECT EXISTS(SELECT 1 FROM main WHERE ServerID = {ServerID})"):
        cur.execute(f"INSERT INTO main (ServerID, WedChan, LastTime) VALUES ({ServerID}, NULL, NULL);")
    con.commit()
    return True
