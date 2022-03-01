import random
import time
import discord
import Database

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
    MittwochEmbed = discord.embeds.Embed(title= "Mittwoch Mutterficker")
    MittwochEmbed.set_image()

def genLeaveEmbed():
    LeaveEmbed = discord.embeds.Embed(title= "Pain")
    LeaveEmbed.set_image(url=Database.getRandoTenorGif("Depression"))
    return LeaveEmbed