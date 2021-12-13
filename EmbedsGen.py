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


def genOmoriPing(Targets: list, inits: list):
    WishString = f""
    BroString = f""
    SingularNeed = "braucht"
    PluralNeed = "brauchen"
    if len(inits) == 1:
        SoloIn = inits[0]
        print(len(AddingDict[OmoriDict[SoloIn.id]])-1)
        WishString = WishString + f"{SoloIn.mention} als:\n{OmoriDict[SoloIn.id]},{AddingDict[OmoriDict[SoloIn.id]][Database.randoMod(len(AddingDict[OmoriDict[SoloIn.id]]))-1]} \n"
    else:
        for idx, Init in enumerate(inits):
            WishString = WishString + f"{Init.mention} als:\n{OmoriDict[Init.id]},{AddingDict[OmoriDict[Init.id]][Database.randoMod(len(AddingDict[OmoriDict[Init.id]]))-1]}\n"
            if idx == 0:
                WishString = WishString + "und"
    if len(Targets) == 1:
        Target = inits[0]
        BroString = BroString + f"{Target.mention} als:\n{OmoriDict[Target.id]},{AddingDict[OmoriDict[Target.id]][Database.randoMod(len(AddingDict[OmoriDict[Target.id]]))-1]}\n"
    else:
        for idx, Target in enumerate(Targets):
            BroString = BroString + f"{Target.mention} als:\n{OmoriDict[Target.id]},{AddingDict[OmoriDict[Target.id]][Database.randoMod(len(AddingDict[OmoriDict[Target.id]]))-1]}\n"
            if idx == 0:
                BroString = BroString + "und"
    if len(inits) >= 2:
        NeedStr = PluralNeed
    else:
        NeedStr = SingularNeed
    PingString = f"{WishString} {NeedStr} {BroString} \n "
    OmoriEmbed = discord.embeds.Embed(title="Omori ping")
    OmoriEmbed.add_field(name = "Depressionen machen einfach mehr Spaß zusammen", value=PingString)
    if len(Targets) == 1:
        OmoriEmbed.set_image(url=Database.getRandoTenorGif(OmoriDict[Targets[0].id]))
    else:
        OmoriEmbed.set_image(url=Database.getRandoTenorGif("Omori"))
    return OmoriEmbed
