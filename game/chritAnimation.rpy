init:
    image Chritude_Concieted_Arm:
        "sprites/Chritude/Conceited/Arm_2.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_3.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_4.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_5.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_6.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_7.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_8.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_9.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_10.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_11.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_12.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_13.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_14.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_15.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_16.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_17.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_18.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_19.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_20.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_21.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_22.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_23.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_24.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_25.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_26.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_27.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_28.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_29.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_30.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_31.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_32.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_33.png"
        pause 0.07
        "sprites/Chritude/Conceited/Arm_1.png"
        pause 7.0
        repeat

    image Chritude_Concieted_Talk:
        "sprites/Chritude/Conceited/Mouth_1.png"
        pause 0.1
        "sprites/Chritude/Conceited/Mouth_2.png"
        pause 0.1
        "sprites/Chritude/Conceited/Mouth_3.png"
        pause 0.1
        "sprites/Chritude/Conceited/Mouth_4.png"
        pause 0.1
        repeat


    image chritude conceited = LiveComposite((1920,1080),
                                (0,0), "sprites/Chritude/Conceited/Base.png",
                                (0,0), "Chritude_Concieted_Arm",
                                (0,0), "sprites/Chritude/Conceited/Mouth_1.png")

    image chritude conceited talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Chritude/Conceited/Base.png",
                                (0,0), "sprites/Chritude/Conceited/Arm_1.png",
                                (0,0), "Chritude_Concieted_Talk")

    image Chritude_Glitter_Base:
        "sprites/Chritude/Glitter/Base_1.png"
        pause 0.07
        "sprites/Chritude/Glitter/Base_2.png"
        pause 0.07
        "sprites/Chritude/Glitter/Base_3.png"
        pause 0.07
        "sprites/Chritude/Glitter/Base_4.png"
        pause 0.07
        "sprites/Chritude/Glitter/Base_5.png"
        pause 0.07

    image Chritude_Glitter_Arm:
        "sprites/Chritude/Glitter/Arm_1.png"
        pause 0.07
        "sprites/Chritude/Glitter/Arm_2.png"
        pause 0.07
        "sprites/Chritude/Glitter/Arm_3.png"
        pause 0.07
        "sprites/Chritude/Glitter/Arm_4.png"
        pause 0.07
        "sprites/Chritude/Glitter/Arm_5.png"
        pause 0.07
        "sprites/Chritude/Glitter/Arm_6.png"
        pause 0.07
        "sprites/Chritude/Glitter/Arm_7.png"
        pause 0.07

    image Chritude_Glitter_Blink:
        "sprites/Chritude/Glitter/Eyes_1.png"
        pause 5.0
        "sprites/Chritude/Glitter/Eyes_2.png"
        pause 0.05
        "sprites/Chritude/Glitter/Eyes_3.png"
        pause 0.05
        "sprites/Chritude/Glitter/Eyes_4.png"
        pause 0.05
        "sprites/Chritude/Glitter/Eyes_5.png"
        pause 0.05
        "sprites/Chritude/Glitter/Eyes_4.png"
        pause 0.05
        "sprites/Chritude/Glitter/Eyes_3.png"
        pause 0.05
        "sprites/Chritude/Glitter/Eyes_2.png"
        pause 0.05
        repeat


    image chritude glitterin = LiveComposite((1920,1080),
                                (0,0), "Chritude_Glitter_Base",
                                (0,0), "Chritude_Glitter_Blink",
                                (0,0), "Chritude_Glitter_Arm")

    image chritude glitter = LiveComposite((1920,1080),
                                (0,0), "sprites/Chritude/Glitter/Base_5.png",
                                (0,0), "Chritude_Glitter_Blink",
                                (0,0), "sprites/Chritude/Glitter/Arm_7.png")

    image Chritude_Laugh_Blink:
        "sprites/Chritude/Laugh/Eyes_1.png"
        pause 5.0
        "sprites/Chritude/Laugh/Eyes_2.png"
        pause 0.05
        "sprites/Chritude/Laugh/Eyes_3.png"
        pause 0.05
        "sprites/Chritude/Laugh/Eyes_4.png"
        pause 0.05
        "sprites/Chritude/Laugh/Eyes_3.png"
        pause 0.05
        "sprites/Chritude/Laugh/Eyes_2.png"
        pause 0.05
        repeat

    image Chritude_Laugh_Talk:
        "sprites/Chritude/Laugh/Mouth_1.png"
        pause 0.1
        "sprites/Chritude/Laugh/Mouth_2.png"
        pause 0.1
        "sprites/Chritude/Laugh/Mouth_3.png"
        pause 0.1
        "sprites/Chritude/Laugh/Mouth_2.png"
        pause 0.1
        repeat

    image chritude laugh = LiveComposite((1920,1080),
                                (0,0), "sprites/Chritude/Laugh/Base.png",
                                (0,0), "sprites/Chritude/Laugh/Mouth_1.png",
                                (0,0), "Chritude_Laugh_Blink")

    image chritude laugh talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Chritude/Laugh/Base.png",
                                (0,0), "Chritude_Laugh_Talk",
                                (0,0), "Chritude_Laugh_Blink")

    image Chritude_Outrage_Blink:
        "sprites/Chritude/Outrage/Eyes_1.png"
        pause 5.0
        "sprites/Chritude/Outrage/Eyes_2.png"
        pause 0.05
        "sprites/Chritude/Outrage/Eyes_3.png"
        pause 0.05
        "sprites/Chritude/Outrage/Eyes_4.png"
        pause 0.05
        "sprites/Chritude/Outrage/Eyes_3.png"
        pause 0.05
        "sprites/Chritude/Outrage/Eyes_2.png"
        pause 0.05
        repeat

    image Chritude_Outrage_Talk:
        "sprites/Chritude/Outrage/Mouth_1.png"
        pause 0.1
        "sprites/Chritude/Outrage/Mouth_2.png"
        pause 0.1
        "sprites/Chritude/Outrage/Mouth_3.png"
        pause 0.1
        "sprites/Chritude/Outrage/Mouth_4.png"
        pause 0.1
        "sprites/Chritude/Outrage/Mouth_3.png"
        pause 0.1
        repeat

    image chritude outrage = LiveComposite((1920,1080),
                                (0,0), "sprites/Chritude/Outrage/Base.png",
                                (0,0), "sprites/Chritude/Outrage/Mouth_1.png",
                                (0,0), "Chritude_Outrage_Blink")

    image chritude outrage talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Chritude/Outrage/Base.png",
                                (0,0), "Chritude_Outrage_Talk",
                                (0,0), "Chritude_Outrage_Blink")

    image Chritude_Sad_Blink:
        "sprites/Chritude/Sad/Eyes_1.png"
        pause 5.0
        "sprites/Chritude/Sad/Eyes_2.png"
        pause 0.05
        "sprites/Chritude/Sad/Eyes_3.png"
        pause 0.05
        "sprites/Chritude/Sad/Eyes_4.png"
        pause 0.05
        "sprites/Chritude/Sad/Eyes_5.png"
        pause 0.05
        "sprites/Chritude/Sad/Eyes_4.png"
        pause 0.05
        "sprites/Chritude/Sad/Eyes_3.png"
        pause 0.05
        "sprites/Chritude/Sad/Eyes_2.png"
        pause 0.05
        repeat

    image Chritude_Sad_Talk:
        "sprites/Chritude/Sad/Mouth_1.png"
        pause 0.1
        "sprites/Chritude/Sad/Mouth_2.png"
        pause 0.1
        "sprites/Chritude/Sad/Mouth_3.png"
        pause 0.1
        "sprites/Chritude/Sad/Mouth_4.png"
        pause 0.1
        "sprites/Chritude/Sad/Mouth_3.png"
        pause 0.1
        repeat

    image Chritude_Sad_Pupils:
        "sprites/Chritude/Sad/Pupils_1.png"
        pause 0.2
        "sprites/Chritude/Sad/Pupils_2.png"
        pause 0.2
        repeat

    image chritude sad = LiveComposite((1920,1080),
                                (0,0), "sprites/Chritude/Sad/Base.png",
                                (0,0), "sprites/Chritude/Sad/Mouth_1.png",
                                (0,0), "Chritude_Sad_Pupils",
                                (0,0), "Chritude_Sad_Blink")

    image chritude sad talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Chritude/Sad/Base.png",
                                (0,0), "Chritude_Sad_Talk",
                                (0,0), "Chritude_Sad_Pupils",
                                (0,0), "Chritude_Sad_Blink")

    image Chritude_Standard_Blink:
        "sprites/Chritude/Standard/EyeDown_2.png"
        pause 0.05
        "sprites/Chritude/Standard/EyeDown_3.png"
        pause 0.05
        "sprites/Chritude/Standard/Eyes_4.png"
        pause 0.05
        "sprites/Chritude/Standard/Eyes_3.png"
        pause 0.05
        "sprites/Chritude/Standard/Eyes_2.png"
        pause 0.05
        "sprites/Chritude/Standard/Eyes_1.png"
        pause 5.0
        "sprites/Chritude/Standard/Eyes_2.png"
        pause 0.05
        "sprites/Chritude/Standard/Eyes_3.png"
        pause 0.05
        "sprites/Chritude/Standard/Eyes_4.png"
        pause 0.05
        "sprites/Chritude/Standard/EyeDown_3.png"
        pause 0.05
        "sprites/Chritude/Standard/EyeDown_2.png"
        pause 0.05
        "sprites/Chritude/Standard/EyeDown_1.png"
        pause 5.0
        repeat

    image Chritude_Standard_Talk:
        "sprites/Chritude/Standard/Mouth_1.png"
        pause 0.1
        "sprites/Chritude/Standard/Mouth_2.png"
        pause 0.1
        "sprites/Chritude/Standard/Mouth_3.png"
        pause 0.1
        "sprites/Chritude/Standard/Mouth_4.png"
        pause 0.1
        "sprites/Chritude/Standard/Mouth_3.png"
        pause 0.1
        repeat

    image chritude standard = LiveComposite((1920,1080),
                                (0,0), "sprites/Chritude/Standard/Base.png",
                                (0,0), "sprites/Chritude/Standard/Mouth_1.png",
                                (0,0), "Chritude_Standard_Blink")

    image chritude standard talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Chritude/Standard/Base.png",
                                (0,0), "Chritude_Standard_Talk",
                                (0,0), "Chritude_Standard_Blink")

    image Chritude_Nervous_Blink:
        "sprites/Chritude/Nervous/Eyes_1.png"
        pause 5.0
        "sprites/Chritude/Nervous/Eyes_2.png"
        pause 0.05
        "sprites/Chritude/Nervous/Eyes_3.png"
        pause 0.05
        "sprites/Chritude/Nervous/Eyes_4.png"
        pause 0.05
        "sprites/Chritude/Nervous/Eyes_3.png"
        pause 0.05
        "sprites/Chritude/Nervous/Eyes_2.png"
        pause 0.05
        repeat

    image Chritude_Nervous_Talk:
        "sprites/Chritude/Nervous/Mouth_1.png"
        pause 0.1
        "sprites/Chritude/Nervous/Mouth_2.png"
        pause 0.1
        "sprites/Chritude/Nervous/Mouth_3.png"
        pause 0.1
        "sprites/Chritude/Nervous/Mouth_4.png"
        pause 0.1
        "sprites/Chritude/Nervous/Mouth_3.png"
        pause 0.1
        repeat

    image Chritude_Nervous_Arm:
        "sprites/Chritude/Nervous/Arm_1.png"
        pause 3.0
        "sprites/Chritude/Nervous/Arm_2.png"
        pause 0.07
        "sprites/Chritude/Nervous/Arm_3.png"
        pause 0.07
        "sprites/Chritude/Nervous/Arm_4.png"
        pause 0.07
        "sprites/Chritude/Nervous/Arm_5.png"
        pause 0.07
        "sprites/Chritude/Nervous/Arm_6.png"
        pause 0.07
        "sprites/Chritude/Nervous/Arm_7.png"
        pause 0.07
        "sprites/Chritude/Nervous/Arm_8.png"
        pause 0.07
        "sprites/Chritude/Nervous/Arm_9.png"
        pause 0.07
        "sprites/Chritude/Nervous/Arm_10.png"
        pause 0.07
        "sprites/Chritude/Nervous/Arm_11.png"
        pause 0.07
        "sprites/Chritude/Nervous/Arm_12.png"
        pause 0.07
        "sprites/Chritude/Nervous/Arm_13.png"
        pause 0.07
        repeat

    image Chritude_Nervous_Sweat:
        "sprites/Chritude/Nervous/Sweat_1.png"
        pause 0.2
        "sprites/Chritude/Nervous/Sweat_2.png"
        pause 0.2
        "sprites/Chritude/Nervous/Sweat_3.png"
        pause 0.2
        "sprites/Chritude/Nervous/Sweat_4.png"
        pause 0.2
        "sprites/Chritude/Nervous/Sweat_5.png"
        pause 0.2
        repeat

    image chritude nervous = LiveComposite((1920,1080),
                                (0,0), "sprites/Chritude/Nervous/Base.png",
                                (0,0), "sprites/Chritude/Nervous/Mouth_1.png",
                                (0,0), "Chritude_Nervous_Blink",
                                (0,0), "Chritude_Nervous_Arm",
                                (0,0), "Chritude_Nervous_Sweat")

    image chritude nervous talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Chritude/Nervous/Base.png",
                                (0,0), "Chritude_Nervous_Talk",
                                (0,0), "Chritude_Nervous_Blink",
                                (0,0), "Chritude_Nervous_Arm",
                                (0,0), "Chritude_Nervous_Sweat")

    image Chritude_Surprise_Base:
        "sprites/Chritude/Surprise/Base_1.png"
        pause 0.07
        "sprites/Chritude/Surprise/Base_2.png"
        pause 0.07
        "sprites/Chritude/Surprise/Base_3.png"
        pause 0.07
        "sprites/Chritude/Surprise/Base_4.png"
        pause 0.07
        "sprites/Chritude/Surprise/Base_5.png"
        pause 0.07
        "sprites/Chritude/Surprise/Base_5.png"
        pause 0.07

    image Chritude_Surprise_Blink:
        "sprites/Chritude/Surprise/Eyes_1.png"
        pause 5.0
        "sprites/Chritude/Surprise/Eyes_2.png"
        pause 0.05
        "sprites/Chritude/Surprise/Eyes_3.png"
        pause 0.05
        "sprites/Chritude/Surprise/Eyes_4.png"
        pause 0.05
        "sprites/Chritude/Surprise/Eyes_3.png"
        pause 0.05
        "sprites/Chritude/Surprise/Eyes_2.png"
        pause 0.05
        repeat

    image chritude surprised = LiveComposite((1920,1080),
                                (0,0), "Chritude_Surprise_Base",
                                (0,0), "Chritude_Surprise_Blink")

init python:
    def pconceitedvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("chritude conceited talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("chritude conceited")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def pglitterinvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("chritude glitterin")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("chritude glitter")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def pglittervoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("chritude glitter")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("chritude glitter")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def plaughvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("chritude laugh talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("chritude laugh")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def poutragevoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("chritude outrage talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("chritude outrage")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def psadvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("chritude sad talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("chritude sad")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def pstandardvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("chritude standard talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("chritude standard")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def pnervousvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("chritude nervous talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("chritude nervous")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")
