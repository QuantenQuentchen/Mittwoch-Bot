import random
import time
import discord
import Database
from PIL import Image, ImageSequence
from PIL import ImageFont
from PIL import ImageDraw
from io import BytesIO
from imgur_python import Imgur
import requests

OmoriDict = {
    704975440963698768: "Aubrey",
    293443718319570964: "Kel",
    508365874223251457: "Omowiiiiii"
}

AddingDict = {
    "Aubrey": [" das E-Girl turned Bully", " und Dianas Emotionen", " Queen of HEAD-BOONK"],
    "Kel": [" der Grund für Maxis Halsschmerzen", " die Hyperaktive Sportlegende", " ADHS für Emos"],
    "Omowiiiiii": [" absolute Legende.", " SexGott", " der mit den besten Lines ", " Depression Pog "]
}

FunnyFact = [
    "Diego stammt ursprünglich aus dem altgriechischen und hebräischen. Der Name Diego leitet sich von dem hebräischen Namen Jakobus den Älteren ab, der im mittelalterlichen Spanisch als Sant Yago beziehungsweise Santiago bezeichnet wurde. Somit ist Diego die spanische Form von Jakob.",
    "Leute die Diego heißen haben eine 100% höhere Chance das man sie mit der besten Insel aller Zeiten verwechselt im Vergleich mit Leute die Dave, Dietmar oder Kevin heißen.",
    "Der männliche Vorname Diego hat mehrere Bedeutungen. Diego kann als der Lehrende, der Betrüger, der vor Gott schützende oder der Fersenhalter übersetzt werden.",
    "Bekannte Persönlichkeiten mit dem Namen Diego: \n-Diego bekannt aus Ice Age (ja das ist der Film mit Valentin)\n -Diego Ramos bekannt als Schauspieler und besitzer des spanischten Namens in ganz Argentinien. \n -Und natürlich Diego Garcia das einzige Opfer des 2004 Tsunamis in Indonesien aus Diego Garcia.",
    "Der englische Wikipedia Eintrag ist 4.577 Fach so lang wie der deutsche. Außerdem kommt im englischen Artikel das Wort diego 208 aber das wort garcia nur 206 mal vor. Wer wohl Diego Diego ist ?",
    "Diego Garcia ist gegenstand mehrerer UN Resulotionen und eines aktiven Streites zwischen dem United Kingdom, der USA und der UN. UN LMAO",
    "Es gibt 18,437 Leute in der USA die Diego heißen und 1,066,520 die Garcia heißen. Das Glück Diego Garcia zu heißen haben allerdings nur 59 Leute in den USA.",
    "Eine Depression ist eine weit verbreitete psychische Störung, die durch Traurigkeit, Interesselosigkeit und Verlust an Genussfähigkeit, Schuldgefühle und geringes Selbstwertgefühl, Schlafstörungen, Appetitlosigkeit, Müdigkeit und Konzentrationsschwächen gekennzeichnet sein kann.",
]

hotGarciaPics = [
    "https://p6.focus.de/img/fotos/id_3740167/diego-garcia.jpg?im=Resize%3D%28800%2C450%29&hash=2e9aaeb24bf109d34c4d74c3eab2960efe2ea54a8c5969f0a9433310ba160101",
    "https://live.staticflickr.com/7566/16142510460_59dedb067c_b.jpg",
    "https://cdn.britannica.com/06/164906-050-BD7ED10E/Diego-Garcia-Indian-Ocean-International-Space-Station.jpg",
    "https://www.borgenmagazine.com/wp-content/uploads/2016/10/Diego-Garcia-The-Poverty-of-a-Kidnapped-Nation.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/2/22/GEODSS_Diego_Garcia_2006-05-01.jpg",
    "https://www.travelbook.de/data/uploads/2020/05/bildschirmfoto-2020-05-15-um-10.33.17_1589532015.jpg",
    "https://static.wikia.nocookie.net/halo/images/f/f9/Diego_Garcia.jpg/revision/latest?cb=20110806172438&path/-prefix=de",
    "https://www.lowyinstitute.org/sites/default/files/6256855435_0645fa0fed_o.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/a/aa/Nasa_diego_garcia.jpg",
    "https://media-cdn.tripadvisor.com/media/photo-c/2560x500/05/3a/4f/8b/diego-garcia.jpg",
    "https://i1.wp.com/idsa.hu/wp-content/uploads/2020/12/diego-garcia.jpg?fit=1200%2C675",
    "https://media.defense.gov/2019/Feb/06/2002087298/-1/-1/0/190207-F-TG070-001.JPG",
    "https://www.heise.de/tp/imgs/89/2/6/0/9/3/8/4/Diego_Garcia_aerial_view_in_2013-fc15967241564773.jpeg",
    "https://upload.wikimedia.org/wikipedia/commons/8/8e/Diego_Garcia_%28satellite%29.jpg",
    "https://www.travelbook.de/data/uploads/2020/05/diego-garcia-c-corbis_1589374069.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/f/f4/Diegogarcia.jpg"
]


def genOmoriPing(Targets: list, inits: list):
    WishString = f""
    BroString = f""
    SingularNeed = "braucht"
    PluralNeed = "brauchen"
    if len(inits) == 1:
        SoloIn = inits[0]
        print(len(AddingDict[OmoriDict[SoloIn.id]]) - 1)
        WishString = WishString + f"{SoloIn.mention} als:\n{OmoriDict[SoloIn.id]},{AddingDict[OmoriDict[SoloIn.id]][Database.randoMod(len(AddingDict[OmoriDict[SoloIn.id]])) - 1]} \n"
    else:
        for idx, Init in enumerate(inits):
            WishString = WishString + f"{Init.mention} als:\n{OmoriDict[Init.id]},{AddingDict[OmoriDict[Init.id]][Database.randoMod(len(AddingDict[OmoriDict[Init.id]])) - 1]}\n"
            if idx == 0:
                WishString = WishString + "und\n"
    if len(Targets) == 1:
        Target = inits[0]
        BroString = BroString + f"{Target.mention} als:\n{OmoriDict[Target.id]},{AddingDict[OmoriDict[Target.id]][Database.randoMod(len(AddingDict[OmoriDict[Target.id]])) - 1]}\n"
    else:
        for idx, Target in enumerate(Targets):
            BroString = BroString + f"{Target.mention} als:\n{OmoriDict[Target.id]},{AddingDict[OmoriDict[Target.id]][Database.randoMod(len(AddingDict[OmoriDict[Target.id]])) - 1]}\n"
            if idx == 0:
                BroString = BroString + "und\n"
    if len(inits) >= 2:
        NeedStr = PluralNeed
    else:
        NeedStr = SingularNeed
    PingString = f"{WishString} {NeedStr}\n {BroString} \n "
    OmoriEmbed = discord.embeds.Embed(title="Omori ping")
    OmoriEmbed.add_field(name="Depressionen machen einfach mehr Spaß zusammen", value=PingString)
    if len(Targets) == 1:
        OmoriEmbed.set_image(url=Database.getRandoTenorGif(OmoriDict[Targets[0].id]))
    else:
        OmoriEmbed.set_image(url=Database.getRandoTenorGif("Omori"))
    return OmoriEmbed


i = 0


def genGarciaEmbed():
    global i
    GarciaNum = i  # random.randint(0, len(FunnyFact))
    i = i + 1
    returnEmbed = discord.embeds.Embed(title="Hier ist ein lustiger Fakt über Diego Garcia:")
    returnEmbed.add_field(value=FunnyFact[GarciaNum], name=f"Fakt:{GarciaNum + 1}/{len(FunnyFact)}")
    returnEmbed.set_image(url=hotGarciaPics[random.randint(0, len(hotGarciaPics))])
    if i == len(FunnyFact):
        i = 0
    return returnEmbed


def genMittwochEmbed():
    MittwochEmbed = discord.embeds.Embed(title="Mittwoch Mutterficker")
    MittwochEmbed.set_image()


def genLeaveEmbed():
    LeaveEmbed = discord.embeds.Embed(title="Pain")
    LeaveEmbed.set_image(url=Database.getRandoTenorGif("Depression"))
    return LeaveEmbed


def genCounterEmbed(member):
    CounterDicts = Database.getAllCount(member.id)
    Top3 = ""
    LongStr = ""
    for idx, (num, name) in enumerate(CounterDicts.items()):
        if idx <= 2:
            Top3 += f"{name.capitalize()}: {num}\n"
        LongStr += f"{name.capitalize()}: {num}\n"
    returnEmbed = discord.embeds.Embed(title="Dein ganz persönlicher Word-Counter", color=discord.Colour.gold())
    returnEmbed.add_field(name="Top 3:", value=Top3)
    returnEmbed.add_field(name="All:", value=LongStr)
    returnEmbed.set_footer(text=f"Made for {member.name}", icon_url=member.avatar_url)
    returnEmbed.set_thumbnail(url="https://cdn.mos.cms.futurecdn.net/LsBqeNKPFjosmaNcCGXcS7.jpeg")
    return returnEmbed


def genCounterImg(member):
    AvatarOffsetY = 0
    AvatarOffsetX = 0
    Top1OffY = 3
    Top1OffX = 3
    Top1Perc = 10
    Top2OffY = 6
    Top2OffX = 6
    Top2Perc = 12
    Top3OffY = 9
    Top3OffX = 9
    Top3Perc = 99
    #barImg = Image.open("Resources/Bar.jpeg")
    barBB = (200, 30)
    #100/
    """
   
    def ImgManipulation(input: Image, avatar: Image, Top3: dict, mainDic: dict):

        x, y = avatar.size
        AvatarOffset = (AvatarOffsetY, AvatarOffsetX, x, y)

        input.convert("RGB").save(inptStream, format="JPEG")
        inptStream.seek(0)
        inptImage = Image.open(intStream)
        
        avatar.convert("RGB").save(avtStream, format="JPEG")
        avtStream.seek(0)
        avtImage = Image.open(avtStream)
    
    """
    with open("Resources/Background.png", "rb") as f:
        background = Image.open(f)
        draw = ImageDraw.Draw(background)
        avatarReqResponse = requests.get(member.avatar_url)
        avatarImg = Image.open(BytesIO(avatarReqResponse.content))
        print(background.info)
        print(avatarImg.info)
        """
            Basic Drawing Stuff
        """

        """
            Still Image Editing
        """

        """
            Image Pasting
        """

        if str(member.avatar_url).split("?size")[0].endswith(".gif"):
            gifFrames = []
            x, y = avatarImg.size
            AvatarOffset = (AvatarOffsetY, AvatarOffsetX, x, y)
            Mask = None
            idx = 0
            frameStream = BytesIO()
            for frame in ImageSequence.Iterator(avatarImg):
                frame.convert("RGB").save(frameStream, format="JPEG")
                frameStream.seek(0)
                framePic = Image.open(frameStream)
                background.paste(framePic, box=AvatarOffset)
                Test = background
                """
                Gif Editing
                """
                print(Test)
                gifFrames.append(Test)
                del(Test)
                idx = idx + 1
            outputStream = BytesIO()
            print(gifFrames)
            gifFrames[0].save(outputStream, format="GIF", save_all=True, optimize=False,
                              duration=avatarImg.info["duration"], loop=True,
                              append_images=gifFrames[1:])
            outputStream.seek(0)
            return outputStream
        else:
            background.paste(avatarImg)
            avatarImg.paste(background)
            background.save("Test.jpg")
            avatarImg("wda.jpg")

        return background
