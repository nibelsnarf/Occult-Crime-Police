init:
    image Carlos_Default_Blink:
        "sprites/Carlos/Standard/Eye_1.png"
        pause 6.0
        "sprites/Carlos/Standard/Eye_2.png"
        pause 0.05
        "sprites/Carlos/Standard/Eye_3.png"
        pause 0.05
        "sprites/Carlos/Standard/Eye_4.png"
        pause 0.05
        "sprites/Carlos/Standard/Eye_3.png"
        pause 0.05
        "sprites/Carlos/Standard/Eye_2.png"
        pause 0.05
        repeat


    image Carlos_Default_Talk:
        "sprites/Carlos/Standard/Mouth_1.png"
        pause 0.1
        "sprites/Carlos/Standard/Mouth_2.png"
        pause 0.1
        "sprites/Carlos/Standard/Mouth_3.png"
        pause 0.1
        "sprites/Carlos/Standard/Mouth_4.png"
        pause 0.1
        repeat

    image car default = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/Standard/Base.png",
                                (0,0), "sprites/Carlos/Standard/Mouth_1.png",
                                (0,0), "Carlos_Default_Blink" )

    image car default talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/Standard/Base.png",
                                (0,0), "Carlos_Default_Talk",
                                (0,0), "Carlos_Default_Blink")

    image Carlos_Agitated_Blink:
        "sprites/Carlos/Agitated/Eyes_1.png"
        pause 3.0
        "sprites/Carlos/Agitated/Eyes_2.png"
        pause 0.05
        "sprites/Carlos/Agitated/Eyes_3.png"
        pause 0.05
        "sprites/Carlos/Agitated/Eyes_4.png"
        pause 0.05
        "sprites/Carlos/Agitated/Eyes_5.png"
        pause 0.05
        "sprites/Carlos/Agitated/Eyes_4.png"
        pause 0.05
        "sprites/Carlos/Agitated/Eyes_3.png"
        pause 0.05
        "sprites/Carlos/Agitated/Eyes_2.png"
        pause 0.05
        repeat

    image Carlos_Agitated_Talk:
        "sprites/Carlos/Agitated/Mouth_1.png"
        pause 0.1
        "sprites/Carlos/Agitated/Mouth_2.png"
        pause 0.1
        "sprites/Carlos/Agitated/Mouth_3.png"
        pause 0.1
        "sprites/Carlos/Agitated/Mouth_4.png"
        pause 0.1
        "sprites/Carlos/Agitated/Mouth_2.png"
        pause 0.1
        repeat

    image Carlos_Agitated_Arms:
        "sprites/Carlos/Agitated/Arms_1.png"
        pause 0.1
        "sprites/Carlos/Agitated/Arms_2.png"
        pause 0.1
        "sprites/Carlos/Agitated/Arms_3.png"
        pause 0.05
        "sprites/Carlos/Agitated/Arms_4.png"
        pause 0.1
        "sprites/Carlos/Agitated/Arms_5.png"
        pause 5.0
        repeat

    image car agitated = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/Agitated/Base.png",
                                (0,0), "sprites/Carlos/Agitated/Mouth_1.png",
                                (0,0), "Carlos_Agitated_Blink",
                                (0,0), "Carlos_Agitated_Arms" )

    image car agitated talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/Agitated/Base.png",
                                (0,0), "Carlos_Agitated_Talk",
                                (0,0), "Carlos_Agitated_Blink",
                                (0,0), "Carlos_Agitated_Arms")

    image Carlos_Whisper_Blink:
        "sprites/Carlos/Whisper/Eyes_1.png"
        pause 5.0
        "sprites/Carlos/Whisper/Eyes_2.png"
        pause 0.05
        "sprites/Carlos/Whisper/Eyes_3.png"
        pause 0.05
        "sprites/Carlos/Whisper/Eyes_4.png"
        pause 0.05
        "sprites/Carlos/Whisper/Eyes_3.png"
        pause 0.05
        "sprites/Carlos/Whisper/Eyes_2.png"
        pause 0.05
        repeat

    image Carlos_Whisper_Talk:
        "sprites/Carlos/Whisper/Mouth_1.png"
        pause 0.1
        "sprites/Carlos/Whisper/Mouth_2.png"
        pause 0.1
        "sprites/Carlos/Whisper/Mouth_3.png"
        pause 0.1
        "sprites/Carlos/Whisper/Mouth_4.png"
        pause 0.1
        "sprites/Carlos/Whisper/Mouth_2.png"
        pause 0.1
        repeat

    image car whisper = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/Whisper.png")

    image car whisper talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/Whisper/Base.png",
                                (0,0), "Carlos_Whisper_Talk",
                                (0,0), "Carlos_Whisper_Blink",
                                (0,0), "sprites/Carlos/Whisper/Arm.png")

    image Carlos_HoldingDrink_Blink:
        "sprites/Carlos/HoldingDrink/Eyes_1.png"
        pause 5.5
        "sprites/Carlos/HoldingDrink/Eyes_2.png"
        pause 0.05
        "sprites/Carlos/HoldingDrink/Eyes_3.png"
        pause 0.05
        "sprites/Carlos/HoldingDrink/Eyes_4.png"
        pause 0.05
        "sprites/Carlos/HoldingDrink/Eyes_5.png"
        pause 0.05
        "sprites/Carlos/HoldingDrink/Eyes_4.png"
        pause 0.05
        "sprites/Carlos/HoldingDrink/Eyes_3.png"
        pause 0.05
        "sprites/Carlos/HoldingDrink/Eyes_2.png"
        pause 0.05
        repeat

    image Carlos_HoldingDrink_Talk:
        "sprites/Carlos/HoldingDrink/Mouth_1.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Mouth_2.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Mouth_3.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Mouth_4.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Mouth_2.png"
        pause 0.1
        repeat

    image Carlos_HoldingDrink_Arm:
        "sprites/Carlos/HoldingDrink/Arm_01.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_02.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_03.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_04.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_05.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_06.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_07.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_08.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_09.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_10.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_11.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_12.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_13.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_14.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_15.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_16.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_17.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_18.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_19.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_20.png"
        pause 0.1


    image car liftdrink = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/HoldingDrink/Base.png",
                                (0,0), "sprites/Carlos/HoldingDrink/Mouth_1.png",
                                (0,0), "Carlos_HoldingDrink_Blink",
                                (0,0), "sprites/Carlos/HoldingDrink/Arm_20.png" )

    image car liftdrink talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/HoldingDrink/Base.png",
                                (0,0), "Carlos_HoldingDrink_Talk",
                                (0,0), "Carlos_HoldingDrink_Blink",
                                (0,0), "Carlos_HoldingDrink_Arm")

    image car holdingdrink = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/HoldingDrink/Base.png",
                                (0,0), "sprites/Carlos/HoldingDrink/Mouth_1.png",
                                (0,0), "Carlos_HoldingDrink_Blink",
                                (0,0), "sprites/Carlos/HoldingDrink/Arm_20.png")

    image car holdingdrink talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/HoldingDrink/Base.png",
                                (0,0), "Carlos_HoldingDrink_Talk",
                                (0,0), "Carlos_HoldingDrink_Blink",
                                (0,0), "sprites/Carlos/HoldingDrink/Arm_20.png")


    image Carlos_Serious_Blink:
        "sprites/Carlos/Serious/Eyes_1.png"
        pause 4.5
        "sprites/Carlos/Serious/Eyes_2.png"
        pause 0.05
        "sprites/Carlos/Serious/Eyes_3.png"
        pause 0.05
        "sprites/Carlos/Serious/Eyes_4.png"
        pause 0.05
        "sprites/Carlos/Serious/Eyes_3.png"
        pause 0.05
        "sprites/Carlos/Serious/Eyes_2.png"
        pause 0.05
        repeat


    image Carlos_Serious_Talk:
        "sprites/Carlos/Serious/Mouth_1.png"
        pause 0.1
        "sprites/Carlos/Serious/Mouth_2.png"
        pause 0.1
        "sprites/Carlos/Serious/Mouth_3.png"
        pause 0.1
        "sprites/Carlos/Serious/Mouth_4.png"
        pause 0.1
        "sprites/Carlos/Serious/Mouth_2.png"
        pause 0.1
        repeat

    image car serious = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/Serious/Base.png",
                                (0,0), "sprites/Carlos/Serious/Mouth_1.png",
                                (0,0), "Carlos_Serious_Blink" )

    image car serious talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/Serious/Base.png",
                                (0,0), "Carlos_Serious_Talk",
                                (0,0), "Carlos_Serious_Blink")

    image car confused = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/Confused.png")

    image car gloves = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/Gloves.png")

init python:
    def cdefvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("car default talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("car default")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def cagitvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("car agitated talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("car agitated")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def cwhisvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("car whisper")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("car whisper")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def cliftvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("car liftdrink talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("car liftdrink")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def choldvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("car holdingdrink talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("car holdingdrink")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def cservoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("car serious talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("car serious")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def cconfusevoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("car confused")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("car confused")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def cglovesvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("car gloves")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("car gloves")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")
