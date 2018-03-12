init:
    image Guard_Talk:
        "sprites/Guard/Standard/Mouth_1.png"
        pause 0.1
        "sprites/Guard/Standard/Mouth_2.png"
        pause 0.1
        "sprites/Guard/Standard/Mouth_3.png"
        pause 0.1
        "sprites/Guard/Standard/Mouth_4.png"
        pause 0.1
        repeat

    image Guard_Blink:
        "sprites/Guard/Standard/Eyes_1.png"
        pause 5.0
        "sprites/Guard/Standard/Eyes_2.png"
        pause 0.04
        "sprites/Guard/Standard/Eyes_3.png"
        pause 0.04
        "sprites/Guard/Standard/Eyes_4.png"
        pause 0.04
        "sprites/Guard/Standard/Eyes_3.png"
        pause 0.04
        "sprites/Guard/Standard/Eyes_2.png"
        pause 0.04
        "sprites/Guard/Standard/Eyes_2.png"
        pause 0.04
        "sprites/Guard/Standard/Eyes_3.png"
        pause 0.04
        "sprites/Guard/Standard/Eyes_4.png"
        pause 0.04
        "sprites/Guard/Standard/Eyes_3.png"
        pause 0.04
        "sprites/Guard/Standard/Eyes_2.png"
        pause 0.04
        repeat

    image Guard_Remove_Glasses:
        "sprites/Guard/RemoveGlasses/Glasses_1.png"
        pause 0.5
        "sprites/Guard/RemoveGlasses/Glasses_2.png"
        pause 0.05
        #show white
        #pause 0.05
        #hide white
        "sprites/Guard/RemoveGlasses/Glasses_3.png"
        pause 0.05
        "sprites/Guard/RemoveGlasses/Glasses_4.png"
        pause 0.1
        "sprites/Guard/RemoveGlasses/Glasses_5.png"
        pause 0.1

    image guard glasses talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Guard/Standard/Base.png",
                                (0,0), "Guard_Talk",
                                (0,0), "sprites/Guard/Standard/Glasses.png")

    image guard glasses = LiveComposite((1920,1080),
                                (0,0), "sprites/Guard/Standard/Base.png",
                                (0,0), "sprites/Guard/Standard/Mouth_1.png",
                                (0,0), "sprites/Guard/Standard/Glasses.png")

    image guard eyes talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Guard/Standard/Base.png",
                                (0,0), "Guard_Talk",
                                (0,0), "Guard_Blink")

    image guard eyes = LiveComposite((1920,1080),
                                (0,0), "sprites/Guard/Standard/Base.png",
                                (0,0), "sprites/Guard/Standard/Mouth_1.png",
                                (0,0), "Guard_Blink")

    image guard removeglasses talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Guard/RemoveGlasses/Base.png",
                                (0,0), "Guard_Talk",
                                (0,0), "Guard_Blink",
                                (0,0), "sprites/Guard/RemoveGlasses/Glasses_1.png")

    image guard removeglasses = LiveComposite((1920,1080),
                                (0,0), "sprites/Guard/RemoveGlasses/Base.png",
                                (0,0), "sprites/Guard/Standard/Mouth_1.png",
                                (0,0), "Guard_Blink",
                                (0,0), "Guard_Remove_Glasses")

    image guard holdglasses talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Guard/RemoveGlasses/Base.png",
                                (0,0), "Guard_Talk",
                                (0,0), "Guard_Blink",
                                (0,0), "sprites/Guard/RemoveGlasses/Glasses_5.png")

    image guard holdglasses = LiveComposite((1920,1080),
                                (0,0), "sprites/Guard/RemoveGlasses/Base.png",
                                (0,0), "sprites/Guard/Standard/Mouth_1.png",
                                (0,0), "Guard_Blink",
                                (0,0), "sprites/Guard/RemoveGlasses/Glasses_5.png")

    image guard returnglasses = LiveComposite((1920,1080),
                                (0,0), "sprites/Guard/RemoveGlasses/Base.png",
                                (0,0), "sprites/Guard/Standard/Mouth_1.png",
                                (0,0), "Guard_Blink",
                                (0,0), "sprites/Guard/RemoveGlasses/Glasses_1.png")

init python:
    def gglassesvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("guard glasses talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("guard glasses")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def geyesvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("guard eyes talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("guard eyes")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def gremglassesvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("guard removeglasses talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("guard removeglasses")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def gholdglassesvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("guard holdglasses talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("guard holdglasses")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def greturnglassesvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("guard removeglasses talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("guard returnglasses")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")
