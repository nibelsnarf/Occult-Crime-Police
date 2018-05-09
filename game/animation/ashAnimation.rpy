init:
    image Ash_Standard_Blink:
        "sprites/Ash/Standard/Eyes_1.png"
        pause 5.0
        "sprites/Ash/Standard/Eyes_2.png"
        pause 0.05
        "sprites/Ash/Standard/Eyes_3.png"
        pause 0.05
        "sprites/Ash/Standard/Eyes_4.png"
        pause 0.05
        "sprites/Ash/Standard/Eyes_3.png"
        pause 0.05
        "sprites/Ash/Standard/Eyes_2.png"
        pause 0.05
        repeat

    image Ash_Standard_Talk:
        "sprites/Ash/Standard/Mouth_1.png"
        pause 0.1
        "sprites/Ash/Standard/Mouth_2.png"
        pause 0.1
        "sprites/Ash/Standard/Mouth_3.png"
        pause 0.1
        "sprites/Ash/Standard/Mouth_4.png"
        pause 0.1
        "sprites/Ash/Standard/Mouth_2.png"
        pause 0.1
        repeat

    image ash standard = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Standard/Base.png",
                                (0,0), "sprites/Ash/Standard/Mouth_1.png",
                                (0,0), "Ash_Standard_Blink")

    image ash standard talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Standard/Base.png",
                                (0,0), "Ash_Standard_Talk",
                                (0,0), "Ash_Standard_Blink")

    image Ash_Camera_Polaroid:
        "sprites/Ash/Camera/Polaroid_1.png"
        pause 0.1
        "sprites/Ash/Camera/Polaroid_2.png"
        pause 0.1
        "sprites/Ash/Camera/Polaroid_3.png"
        pause 0.1
        "sprites/Ash/Camera/Polaroid_4.png"
        pause 0.1
        "sprites/Ash/Camera/Polaroid_5.png"
        pause 0.1
        "sprites/Ash/Camera/Polaroid_6.png"
        pause 0.1
        "sprites/Ash/Camera/Polaroid_7.png"
        pause 0.1
        "sprites/Ash/Camera/Polaroid_8.png"
        pause 0.1
        "sprites/Ash/Camera/Polaroid_9.png"
        pause 0.1
        "sprites/Ash/Camera/Polaroid_10.png"
        pause 0.1

    image Ash_Camera_Talk:
        "sprites/Ash/Camera/Mouth_1.png"
        pause 0.1
        "sprites/Ash/Camera/Mouth_2.png"
        pause 0.1
        "sprites/Ash/Camera/Mouth_3.png"
        pause 0.1
        "sprites/Ash/Camera/Mouth_4.png"
        pause 0.1
        "sprites/Ash/Camera/Mouth_2.png"
        pause 0.1
        repeat

    image ash camera = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Camera/Base.png",
                                (0,0), "sprites/Ash/Camera/Mouth_1.png")

    image ash camera talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Camera/Base.png",
                                (0,0), "Ash_Camera_Talk")

    image Ash_Annoy_Blink:
        "sprites/Ash/Annoy/Eyes_1.png"
        pause 5.0
        "sprites/Ash/Annoy/Eyes_2.png"
        pause 0.05
        "sprites/Ash/Annoy/Eyes_3.png"
        pause 0.05
        "sprites/Ash/Annoy/Eyes_4.png"
        pause 0.05
        "sprites/Ash/Annoy/Eyes_3.png"
        pause 0.05
        "sprites/Ash/Annoy/Eyes_2.png"
        pause 0.05
        repeat

    image Ash_Annoy_Talk:
        "sprites/Ash/Annoy/Mouth_1.png"
        pause 0.1
        "sprites/Ash/Annoy/Mouth_2.png"
        pause 0.1
        "sprites/Ash/Annoy/Mouth_3.png"
        pause 0.1
        "sprites/Ash/Annoy/Mouth_4.png"
        pause 0.1
        "sprites/Ash/Annoy/Mouth_2.png"
        pause 0.1
        repeat

    image ash annoyed = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Annoy/Base.png",
                                (0,0), "sprites/Ash/Annoy/Mouth_1.png",
                                (0,0), "Ash_Annoy_Blink")

    image ash annoyed talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Annoy/Base.png",
                                (0,0), "Ash_Annoy_Talk",
                                (0,0), "Ash_Annoy_Blink")

    image Ash_Confident_Talk:
        "sprites/Ash/Confident/Mouth_1.png"
        pause 0.1
        "sprites/Ash/Confident/Mouth_2.png"
        pause 0.1
        "sprites/Ash/Confident/Mouth_3.png"
        pause 0.1
        "sprites/Ash/Confident/Mouth_4.png"
        pause 0.1
        "sprites/Ash/Confident/Mouth_2.png"
        pause 0.1
        repeat

    image ash confident = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Confident/Base.png",
                                (0,0), "sprites/Ash/Confident/Mouth_1.png",)
    image ash confident talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Confident/Base.png",
                                (0,0), "Ash_Confident_Talk",)
    image Ash_Flippant_Talk:
        "sprites/Ash/Flippant/Mouth_1.png"
        pause 0.1
        "sprites/Ash/Flippant/Mouth_2.png"
        pause 0.1
        "sprites/Ash/Flippant/Mouth_3.png"
        pause 0.1
        "sprites/Ash/Flippant/Mouth_4.png"
        pause 0.1
        "sprites/Ash/Flippant/Mouth_2.png"
        pause 0.1
        repeat

    image Ash_Flippant_Blink:
        "sprites/Ash/Flippant/Eyes_1.png"
        pause 4.2
        "sprites/Ash/Flippant/Eyes_2.png"
        pause 0.05
        "sprites/Ash/Flippant/Eyes_3.png"
        pause 0.05
        "sprites/Ash/Flippant/Eyes_4.png"
        pause 0.05
        "sprites/Ash/Flippant/Eyes_3.png"
        pause 0.05
        "sprites/Ash/Flippant/Eyes_2.png"
        pause 0.05
        repeat

    image ash flippant = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Flippant/Base.png",
                                (0,0), "sprites/Ash/Flippant/Mouth_1.png",
                                (0,0), "Ash_Flippant_Blink")

    image ash flippant talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Flippant/Base.png",
                                (0,0), "Ash_Flippant_Talk",
                                (0,0), "Ash_Flippant_Blink")

    image Ash_Positing_Talk:
        "sprites/Ash/Positing/Mouth_1.png"
        pause 0.1
        "sprites/Ash/Positing/Mouth_2.png"
        pause 0.1
        "sprites/Ash/Positing/Mouth_3.png"
        pause 0.1
        "sprites/Ash/Positing/Mouth_4.png"
        pause 0.1
        "sprites/Ash/Positing/Mouth_2.png"
        pause 0.1
        repeat

    image Ash_Positing_Blink:
        "sprites/Ash/Positing/Eyes_1.png"
        pause 4.2
        "sprites/Ash/Positing/Eyes_2.png"
        pause 0.05
        "sprites/Ash/Positing/Eyes_3.png"
        pause 0.05
        "sprites/Ash/Positing/Eyes_4.png"
        pause 0.05
        "sprites/Ash/Positing/Eyes_3.png"
        pause 0.05
        "sprites/Ash/Positing/Eyes_2.png"
        pause 0.05
        repeat

    image ash positing = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Positing/Base.png",
                                (0,0), "sprites/Ash/Positing/Mouth_1.png",
                                (0,0), "Ash_Positing_Blink")

    image ash positing talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Positing/Base.png",
                                (0,0), "Ash_Positing_Talk",
                                (0,0), "Ash_Positing_Blink")

    image Ash_Psyched_Talk:
        "sprites/Ash/Psyched/Mouth_1.png"
        pause 0.1
        "sprites/Ash/Psyched/Mouth_2.png"
        pause 0.1
        "sprites/Ash/Psyched/Mouth_3.png"
        pause 0.1
        "sprites/Ash/Psyched/Mouth_4.png"
        pause 0.1
        "sprites/Ash/Psyched/Mouth_2.png"
        pause 0.1
        repeat

    image Ash_Psyched_Blink:
        "sprites/Ash/Psyched/Eyes_1.png"
        pause 4.2
        "sprites/Ash/Psyched/Eyes_2.png"
        pause 0.05
        "sprites/Ash/Psyched/Eyes_3.png"
        pause 0.05
        "sprites/Ash/Psyched/Eyes_4.png"
        pause 0.05
        "sprites/Ash/Psyched/Eyes_5.png"
        pause 0.05
        "sprites/Ash/Psyched/Eyes_4.png"
        pause 0.05
        "sprites/Ash/Psyched/Eyes_3.png"
        pause 0.05
        "sprites/Ash/Psyched/Eyes_2.png"
        pause 0.05
        repeat

    image Ash_Psyched_Arms:
        "sprites/Ash/Psyched/Arm_1.png"
        pause 4.2
        "sprites/Ash/Psyched/Arm_2.png"
        pause 0.07
        "sprites/Ash/Psyched/Arm_3.png"
        pause 0.07
        "sprites/Ash/Psyched/Arm_4.png"
        pause 0.07
        "sprites/Ash/Psyched/Arm_5.png"
        pause 0.07
        "sprites/Ash/Psyched/Arm_6.png"
        pause 0.07
        "sprites/Ash/Psyched/Arm_7.png"
        pause 0.07
        "sprites/Ash/Psyched/Arm_8.png"
        pause 0.07

    image ash psyched = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Psyched/Base.png",
                                (0,0), "sprites/Ash/Psyched/Mouth_1.png",
                                (0,0), "Ash_Psyched_Blink",
                                (0,0), "sprites/Ash/Psyched/Arm_1.png")

    image ash psyched talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Psyched/Base.png",
                                (0,0), "Ash_Psyched_Talk",
                                (0,0), "Ash_Psyched_Blink",
                                (0,0), "Ash_Psyched_Arms")

    image Ash_Sad_Talk:
        "sprites/Ash/Sad/Mouth_1.png"
        pause 0.1
        "sprites/Ash/Sad/Mouth_2.png"
        pause 0.1
        "sprites/Ash/Sad/Mouth_3.png"
        pause 0.1
        "sprites/Ash/Sad/Mouth_4.png"
        pause 0.1
        "sprites/Ash/Sad/Mouth_2.png"
        pause 0.1
        repeat

    image Ash_Sad_Blink:
        "sprites/Ash/Sad/Eyes_1.png"
        pause 4.2
        "sprites/Ash/Sad/Eyes_2.png"
        pause 0.05
        "sprites/Ash/Sad/Eyes_3.png"
        pause 0.05
        "sprites/Ash/Sad/Eyes_4.png"
        pause 0.05
        "sprites/Ash/Sad/Eyes_5.png"
        pause 0.05
        "sprites/Ash/Sad/Eyes_4.png"
        pause 0.05
        "sprites/Ash/Sad/Eyes_3.png"
        pause 0.05
        "sprites/Ash/Sad/Eyes_2.png"
        pause 0.05
        repeat

    image ash sad = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Sad/Base.png",
                                (0,0), "sprites/Ash/Sad/Mouth_1.png",
                                (0,0), "Ash_Sad_Blink")

    image ash sad talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Sad/Base.png",
                                (0,0), "Ash_Sad_Talk",
                                (0,0), "Ash_Sad_Blink")

    image Ash_Surprise_Talk:
        "sprites/Ash/Surprise/Mouth_1.png"
        pause 0.1
        "sprites/Ash/Surprise/Mouth_2.png"
        pause 0.1
        "sprites/Ash/Surprise/Mouth_3.png"
        pause 0.1
        "sprites/Ash/Surprise/Mouth_4.png"
        pause 0.1
        "sprites/Ash/Surprise/Mouth_2.png"
        pause 0.1
        repeat

    image Ash_Surprise_Blink:
        "sprites/Ash/Surprise/Eyes_1.png"
        pause 4.2
        "sprites/Ash/Surprise/Eyes_2.png"
        pause 0.05
        "sprites/Ash/Surprise/Eyes_3.png"
        pause 0.05
        "sprites/Ash/Surprise/Eyes_4.png"
        pause 0.05
        "sprites/Ash/Surprise/Eyes_3.png"
        pause 0.05
        "sprites/Ash/Surprise/Eyes_2.png"
        pause 0.05
        repeat

    image Ash_Surprise_Hair:
        "sprites/Ash/Surprise/Hair_2.png"
        pause 0.2
        "sprites/Ash/Surprise/Hair_1.png"
        pause 0.4
        "sprites/Ash/Surprise/Hair_2.png"
        pause 0.2
        "sprites/Ash/Surprise/Hair_3.png"
        pause 0.2
        "sprites/Ash/Surprise/Hair_4.png"
        pause 0.2

    image ash surprised = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Surprise/Base.png",
                                (0,0), "sprites/Ash/Surprise/Mouth_1.png",
                                (0,0), "Ash_Surprise_Blink",
                                (0,0), "sprites/Ash/Surprise/Hair_4.png")

    image ash surprised talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Surprise/Base.png",
                                (0,0), "Ash_Surprise_Talk",
                                (0,0), "Ash_Surprise_Blink",
                                (0,0), "Ash_Surprise_Hair")

    image Ash_Think_Talk:
        "sprites/Ash/Think/Mouth_1.png"
        pause 0.1
        "sprites/Ash/Think/Mouth_2.png"
        pause 0.1
        "sprites/Ash/Think/Mouth_3.png"
        pause 0.1
        "sprites/Ash/Think/Mouth_4.png"
        pause 0.1
        "sprites/Ash/Think/Mouth_2.png"
        pause 0.1
        repeat

    image Ash_Think_Blink:
        "sprites/Ash/Think/Eyes_1.png"
        pause 4.2
        "sprites/Ash/Think/Eyes_2.png"
        pause 0.05
        "sprites/Ash/Think/Eyes_3.png"
        pause 0.05
        "sprites/Ash/Think/Eyes_4.png"
        pause 0.05
        "sprites/Ash/Think/Eyes_3.png"
        pause 0.05
        "sprites/Ash/Think/Eyes_2.png"
        pause 0.05
        repeat

    image ash thinking = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Think/Base.png",
                                (0,0), "sprites/Ash/Think/Mouth_1.png",
                                (0,0), "Ash_Think_Blink")

    image ash thinking talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Think/Base.png",
                                (0,0), "Ash_Think_Talk",
                                (0,0), "Ash_Think_Blink")

    image Ash_Unsure_Talk:
        "sprites/Ash/Unsure/Mouth_1.png"
        pause 0.1
        "sprites/Ash/Unsure/Mouth_2.png"
        pause 0.1
        "sprites/Ash/Unsure/Mouth_3.png"
        pause 0.1
        "sprites/Ash/Unsure/Mouth_4.png"
        pause 0.1
        "sprites/Ash/Unsure/Mouth_2.png"
        pause 0.1
        repeat

    image Ash_Unsure_Blink:
        "sprites/Ash/Unsure/Eyes_1.png"
        pause 4.2
        "sprites/Ash/Unsure/Eyes_2.png"
        pause 0.05
        "sprites/Ash/Unsure/Eyes_3.png"
        pause 0.05
        "sprites/Ash/Unsure/Eyes_4.png"
        pause 0.05
        "sprites/Ash/Unsure/Eyes_3.png"
        pause 0.05
        "sprites/Ash/Unsure/Eyes_2.png"
        pause 0.05
        repeat

    image ash unsure = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Unsure/Base.png",
                                (0,0), "sprites/Ash/Unsure/Mouth_1.png",
                                (0,0), "Ash_Unsure_Blink")

    image ash unsure talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Unsure/Base.png",
                                (0,0), "Ash_Unsure_Talk",
                                (0,0), "Ash_Unsure_Blink")

init python:
    def astandardvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("ash standard talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("ash standard")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def acameravoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("ash camera talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("ash camera")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def aannoyedvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("ash annoyed talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("ash annoyed")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def aconfidentvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("ash confident talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("ash confident")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def aflippantvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("ash flippant talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("ash flippant")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def apositingvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("ash positing talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("ash positing")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def apsychedvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("ash psyched talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("ash psyched")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def asadvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("ash sad talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("ash sad")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def asurprisedvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("ash surprised talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("ash surprised")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def athinkingvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("ash thinking talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("ash thinking")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def aunsurevoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("ash unsure talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("ash unsure")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")
