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
    transform flip:
        xzoom -1

    transform menuFade:
        zoom 0.0
        linear 0.3 zoom 1.1
        linear 0.1 zoom 1.0


    image kitchendrang = LiveComposite((1920,1080),
                                (0,0), "kitchen",
                                (0,0), "assets/backgrounds/KitchenDrang1.png")

    image basewarehousepaul = LiveComposite((1920,1080),
                                (0,0), "basewarehouse",
                                (0,0), "assets/backgrounds/WarehousePaul.png")


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
