init:
    $ imagewidth = config.screen_width
    $ imageheight = config.screen_height

    image ctc_blink:
        xalign 0.94
        yalign 0.92
        "assets/menu/CTC1.png"
        linear 0.25 zoom 1.1
        linear 0.25 zoom 1.0
        repeat

    image mm_bg_scroll:
        "assets/backgrounds/MM_BG_Lines.png"
        ypan 0
        linear 100 ypan 360
        repeat

    image willitblend:
        yalign 0.0
        xalign 0.475
        zoom 0.5
        "assets/menu/OCP_Logo2.png"
        additive 0.25

    image pressStart:
        alpha 0.0
        yalign 0.9
        xalign 0.5
        "assets/backgrounds/pressStart.png"
        ease 2.0 alpha 1.0
        ease 2.0 alpha 0.0
        repeat

    image mm_glitch:
        zoom 2.87
        "assets/backgrounds/glitch1.png"
        pause 0.05
        "assets/backgrounds/glitch2.png"
        pause 0.05
        "assets/backgrounds/glitch3.png"
        pause 0.05
        "assets/backgrounds/glitch4.png"
        pause 0.05
        "assets/backgrounds/glitch5.png"
        pause 0.05
        repeat

    image splashscreen_bg = LiveComposite((1920,1080),
                                (0,0), "mm_bg_scroll",
                                (0,0), "assets/backgrounds/MM_BG_Vignette.png",
                                (0,0), "assets/backgrounds/TemashawValleyLogo.png"
                                )

    image main_menu_bg = LiveComposite((1920,1080),
                                (0,0), "mm_bg_scroll",
                                (0,0), "assets/backgrounds/MM_BG_Vignette.png",
                                #(0,0), "willitblend"
                                )

    image Credits1 = LiveComposite((1920,1080),
                                (0,0), "main_menu_bg",
                                (0,0), "assets/menu/Credits1.png")

    image Credits2 = LiveComposite((1920,1080),
                                (0,0), "main_menu_bg",
                                (0,0), "assets/menu/Credits2.png")

    image Credits3 = LiveComposite((1920,1080),
                                (0,0), "main_menu_bg",
                                (0,0), "assets/menu/Credits3.png")

    image Credits4 = LiveComposite((1920,1080),
                                (0,0), "main_menu_bg",
                                (0,0), "assets/menu/Credits4.png")

    image Credits5 = LiveComposite((1920,1080),
                                (0,0), "main_menu_bg",
                                (0,0), "assets/menu/Credits5.png")

    image Credits6 = LiveComposite((1920,1080),
                                (0,0), "main_menu_bg",
                                (0,0), "assets/menu/Credits6.png")
    transform flip:
        xzoom -1

    transform menuFade:
        zoom 0.0
        linear 0.3 zoom 1.1
        linear 0.1 zoom 1.0


    image kitchendrang = LiveComposite((1920,1080),
                                (0,0), "kitchen",
                                (0,0), "assets/backgrounds/KitchenDrang1.png")

    image kitchenact3B = LiveComposite((1920,1080),
                                (0,0), "kitchen",
                                (0,0), "assets/backgrounds/SmartHouseKitchinBottomi.png")

    image kitchenact3BC = LiveComposite((1920,1080),
                                (0,0), "kitchen",
                                (0,0), "assets/backgrounds/SmartHouseKitchinBottomi.png",
                                (0,0), "assets/backgrounds/SmartHouseKitchinCarlos.png")

    image kitchenact3BD = LiveComposite((1920,1080),
                                (0,0), "kitchen",
                                (0,0), "assets/backgrounds/SmartHouseKitchinBottomi.png",
                                (0,0), "assets/backgrounds/SmartHouseKitchinAct3Drang.png")

    image kitchenact3BCD = LiveComposite((1920,1080),
                                (0,0), "kitchen",
                                (0,0), "assets/backgrounds/SmartHouseKitchinBottomi.png",
                                (0,0), "assets/backgrounds/SmartHouseKitchinAct3Drang.png",
                                (0,0), "assets/backgrounds/SmartHouseKitchinCarlos.png")

    image basewarehousepaul = LiveComposite((1920,1080),
                                (0,0), "basewarehouse",
                                (0,0), "assets/backgrounds/WarehousePaul.png")

    image TDC = LiveComposite((1920,1080),
                                (0,0), "assets/backgrounds/TDC_Base.png",
                                (0,0), ConditionSwitch("\"6\" in investigation2_cleareditems","sprites/Bottomi/Explode/Explode_1.png", "True", "assets/backgrounds/TDC_Shoe.png"))

    image OfficeNeering:
        "assets/backgrounds/OfficeNeering/OfficeNeering1.png"
        pause 4
        "assets/backgrounds/OfficeNeering/OfficeNeering2.png"
        pause 0.05
        "assets/backgrounds/OfficeNeering/OfficeNeering3.png"
        pause 0.05
        "assets/backgrounds/OfficeNeering/OfficeNeering4.png"
        pause 0.05
        "assets/backgrounds/OfficeNeering/OfficeNeering1.png"
        pause 3
        "assets/backgrounds/OfficeNeering/OfficeNeering2.png"
        pause 0.05
        "assets/backgrounds/OfficeNeering/OfficeNeering3.png"
        pause 0.05
        "assets/backgrounds/OfficeNeering/OfficeNeering4.png"
        pause 0.05
        "assets/backgrounds/OfficeNeering/OfficeNeering5.png"
        pause 0.05
        "assets/backgrounds/OfficeNeering/OfficeNeering6.png"
        pause 0.05
        "assets/backgrounds/OfficeNeering/OfficeNeering7.png"
        pause 0.05
        "assets/backgrounds/OfficeNeering/OfficeNeering8.png"
        pause 0.05
        "assets/backgrounds/OfficeNeering/OfficeNeering9.png"
        pause 0.05
        "assets/backgrounds/OfficeNeering/OfficeNeering10.png"
        pause 0.05
        repeat

    image OfficeNeeringAdditive:
        additive 0.4
        "OfficeNeering"
        linear 1.0 additive 0.5
        linear 1.0 additive 0.4
        linear 1.0 additive 0.5
        linear 1.0 additive 0.4
        linear 1.0 additive 0.5
        linear 1.0 additive 0.4
        linear 1.0 additive 0.5
        linear 1.0 additive 0.4
        linear 1.0 additive 0.5
        linear 1.0 additive 0.4
        linear 1.0 additive 0.5
        linear 1.0 additive 0.4
        repeat

    image OfficeLighted = LiveComposite((1920,1080),
                                (0,0), "OfficeLight",
                                (0,0), "OfficeNeeringAdditive")

    image Glittur:
        "gui/Glitter/Puff.png"

    image GlitterSparkle1:
        additive 1.0
        alpha 0
        "gui/Glitter/Sparkle1.png"
        linear 0.1 alpha 1
        linear 0.1 alpha 0
        pause 0.2
        repeat

    image GlitterSparkle2:
        additive 1.0
        alpha 0
        "gui/Glitter/Sparkle3.png"
        pause 0.1
        linear 0.1 alpha 1
        linear 0.1 alpha 0
        pause 0.2
        repeat


    image GlitterSparkle3:
        additive 1.0
        alpha 0
        "gui/Glitter/Sparkle4.png"
        pause 0.2
        linear 0.1 alpha 1
        linear 0.1 alpha 0
        pause 0.2
        repeat


    image GlitterSparkle4:
        additive 1.0
        alpha 0
        "gui/Glitter/Sparkle5.png"
        pause 0.3
        linear 0.1 alpha 1
        linear 0.1 alpha 0
        pause 0.2
        repeat


    image GlitterComp = LiveComposite((519,367),
                                (0,0), "Glittur",
                                (0,0), "GlitterSparkle1",
                                (0,0), "GlitterSparkle2",
                                (0,0), "GlitterSparkle3",
                                (0,0), "GlitterSparkle4",)

    image GlitterPuff:
        "GlitterComp"
        alpha 0
        zoom 1
        linear 0.2 alpha 1 zoom 1.3
        linear 0.3 alpha 0 zoom 2
        repeat

    image WarehouseD1 = LiveComposite((1920,1080),
                                (0,0), "basewarehouse",
                                (0,0), "assets/backgrounds/WarehouseGrates1.png")

    image WarehouseD2 = LiveComposite((1920,1080),
                                (0,0), "basewarehouse",
                                (0,0), "assets/backgrounds/WarehouseGrates2.png")

    image wper1:
        "assets/backgrounds/Persuasion_W1.png"
        xtile 4
        xoffset -1920
        linear 1 xoffset 0
        repeat

    image wper2:
        xtile 4
        "assets/backgrounds/Persuasion_W2.png"
        xoffset -1920
        linear 4 xoffset 0
        repeat

    image wper3:
        xtile 4
        "assets/backgrounds/Persuasion_W3.png"
        xoffset -1920
        linear 3 xoffset 0
        repeat

    image WarrenPers = LiveComposite((1920,1080),
                                (0,0), "wper1",
                                (0,0), "wper2",
                                (0,0), "wper3")

    image WarrenPersuasion = LiveCrop((0,0,1920,1080), "WarrenPers")

    image dper1:
        xtile 4
        "assets/backgrounds/Persuasion_D1.png"
        xoffset 0
        linear 1 xoffset -1920
        repeat

    image dper2:
        xtile 4
        "assets/backgrounds/Persuasion_D2.png"
        xoffset 0
        linear 4 xoffset -1920
        repeat

    image dper3:
        xtile 4
        "assets/backgrounds/Persuasion_D3.png"
        xoffset 0
        linear 3 xoffset -1920
        repeat

    image DrangPers = LiveComposite((1920,1080),
                                (0,0), "dper1",
                                (0,0), "dper2",
                                (0,0), "dper3")

    image DrangPersuasion = LiveCrop((0,0,1920,1080), "DrangPers")

    image cper1:
        xtile 3
        "assets/backgrounds/Persuasion_C1.png"
        xoffset 0
        linear 2.5 xoffset -3840
        repeat

    image cper2:
        xtile 3
        additive 1.0
        "assets/backgrounds/Persuasion_C2.png"
        xoffset 0
        linear 3.5 xoffset -3840
        repeat

    image cper3:
        xtile 4
        additive 1.0
        "assets/backgrounds/Persuasion_C3.png"
        xoffset 0
        linear 3.3 xoffset -3840
        repeat

    image ChritudePers = LiveComposite((1920,1080),
                                (0,0), "cper1",
                                (0,0), "cper2",
                                (0,0), "cper3"
                                )

    image ChritudePersuasion = LiveCrop((0,0,1920,1080), "ChritudePers")

    image nper1:
        xtile 4
        "assets/backgrounds/Persuasion_N7.png"
        xoffset 0
        linear 1.7 xoffset -1920
        repeat

    image nper2:
        additive 0.5
        xtile 4
        "assets/backgrounds/Persuasion_N7.png"
        xoffset 0
        linear 2 xoffset -1920
        repeat

    image nper3:
        xtile 4
        "assets/backgrounds/Persuasion_N5.png"
        xoffset -1920
        linear 10 xoffset 0
        repeat

    image NeeringPers = LiveComposite((1920,1080),
                                (0,0), "nper1",
                                (0,0), "nper2",
                                (0,0), "nper3"
                                )

    image NeeringPersuasion = LiveCrop((0,0,1920,1080), "NeeringPers")

    image perline1:
        alpha 0.5
        additive 1.0
        ytile 4
        "assets/backgrounds/PersuasionLine.png"
        yoffset 0
        linear 0.7 yoffset -1080
        repeat

    image perline2:
        alpha 0.5
        additive 1.0
        ytile 4
        "assets/backgrounds/PersuasionLine.png"
        yoffset -1080
        linear 1 yoffset 0
        repeat


    image WvDPersuasion = LiveComposite((3840,1080),
                                (0,0), "WarrenPersuasion",
                                (1920,0), "DrangPersuasion",
                                (1860,0), "perline1",
                                (1880,0), "perline2")

    image WvCPersuasion = LiveComposite((3840,1080),
                                (0,0), "WarrenPersuasion",
                                (1920,0), "ChritudePersuasion",
                                (1860,0), "perline1",
                                (1880,0), "perline2")

    image WvNPersuasion = LiveComposite((3840,1080),
                                (0,0), "WarrenPersuasion",
                                (1920,0), "NeeringPersuasion",
                                (1860,0), "perline1",
                                (1880,0), "perline2")


    image Witness:
        xoffset -1920
        "gui/WITNESS.png"
        linear 0.5 xoffset 0
        pause 1.5
        linear 0.5 alpha 0

    image Statement:
        xoffset 1920
        "gui/STATEMENT.png"
        linear 0.5 xoffset 0
        pause 1.5
        linear 0.5 alpha 0

    image Interro:
        yoffset -1080
        "gui/INTERRO.png"
        linear 0.25 yoffset -200
        pause 1.5
        linear 0.5 alpha 0

    image Gation:
        yoffset 1080
        "gui/GATION.png"
        linear 0.25 yoffset -200
        pause 1.5
        linear 0.5 alpha 0

    image BottomiLight:
        alpha 1.0
        "assets/backgrounds/BottomiLight.png"
        linear 0.7 alpha 0.0
        pause 0.3
        repeat

init python:

    def typingvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.sound.play("sound/typewriter.ogg", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")


init python:
    for file in renpy.list_files():
        if file.endswith('.png'): ##this is your file type
            name = file.replace('sprites/', '').replace('.png','')#Here we add ‘flip’ to our image
            renpy.image(name, Image(file))
