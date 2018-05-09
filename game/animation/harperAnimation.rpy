init:

    image har base = LiveComposite((1920,1080),
                                (0,0), "sprites/Harper/No/Motion-01.png")

    image Harper_Deploy_Anim:
        "sprites/Harper/Deploy/Motion-03.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-04.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-05.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-06.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-07.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-08.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-09.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-10.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-11.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-12.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-13.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-14.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-15.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-16.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-17.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-18.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-19.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-20.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-21.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-22.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-23.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-24.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-25.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-26.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-27.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-28.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-29.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-30.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-31.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-32.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-33.png"
        pause 0.07
        "sprites/Harper/Deploy/Motion-34.png"
        pause 0.07

    image har deploy = LiveComposite((1920,1080),
                                (0,0), "Harper_Deploy_Anim")

    image Harper_No_Anim:
        "sprites/Harper/No/Motion-01.png"
        pause 0.07
        "sprites/Harper/No/Motion-02.png"
        pause 0.07
        "sprites/Harper/No/Motion-03.png"
        pause 0.07
        "sprites/Harper/No/Motion-04.png"
        pause 0.07
        "sprites/Harper/No/Motion-05.png"
        pause 0.07
        "sprites/Harper/No/Motion-06.png"
        pause 0.07
        "sprites/Harper/No/Motion-07.png"
        pause 0.07
        "sprites/Harper/No/Motion-08.png"
        pause 0.07
        "sprites/Harper/No/Motion-09.png"
        pause 0.07
        "sprites/Harper/No/Motion-10.png"
        pause 0.07
        "sprites/Harper/No/Motion-11.png"
        pause 0.07
        "sprites/Harper/No/Motion-12.png"
        pause 0.07
        "sprites/Harper/No/Motion-13.png"
        pause 0.07
        "sprites/Harper/No/Motion-14.png"
        pause 0.07
        "sprites/Harper/No/Motion-15.png"
        pause 0.07
        "sprites/Harper/No/Motion-16.png"
        pause 0.07
        "sprites/Harper/No/Motion-17.png"
        pause 0.07
        "sprites/Harper/No/Motion-18.png"
        pause 0.07
        "sprites/Harper/No/Motion-19.png"
        pause 0.07

    image har no = LiveComposite((1920,1080),
                                (0,0), "Harper_No_Anim")

    image Harper_Yes_Anim:
        "sprites/Harper/Yes/Motion-01.png"
        pause 0.07
        "sprites/Harper/Yes/Motion-02.png"
        pause 0.07
        "sprites/Harper/Yes/Motion-03.png"
        pause 0.07
        "sprites/Harper/Yes/Motion-04.png"
        pause 0.07
        "sprites/Harper/Yes/Motion-05.png"
        pause 0.07
        "sprites/Harper/Yes/Motion-06.png"
        pause 0.07
        "sprites/Harper/Yes/Motion-07.png"
        pause 0.07
        "sprites/Harper/Yes/Motion-08.png"
        pause 0.07
        "sprites/Harper/Yes/Motion-09.png"
        pause 0.07
        "sprites/Harper/Yes/Motion-10.png"
        pause 0.07
        "sprites/Harper/Yes/Motion-11.png"
        pause 0.07
        "sprites/Harper/Yes/Motion-12.png"
        pause 0.07
        "sprites/Harper/Yes/Motion-13.png"
        pause 0.07
        "sprites/Harper/Yes/Motion-14.png"
        pause 0.07
        "sprites/Harper/Yes/Motion-15.png"
        pause 0.07
        "sprites/Harper/Yes/Motion-16.png"
        pause 0.07
        "sprites/Harper/Yes/Motion-17.png"
        pause 0.07
        "sprites/Harper/Yes/Motion-18.png"
        pause 0.07
        "sprites/Harper/Yes/Motion-19.png"
        pause 0.07
        "sprites/Harper/Yes/Motion-20.png"
        pause 0.07
        "sprites/Harper/Yes/Motion-21.png"
        pause 0.07
        "sprites/Harper/Yes/Motion-22.png"
        pause 0.07
        "sprites/Harper/Yes/Motion-23.png"
        pause 0.07

    image har yes = LiveComposite((1920,1080),
                                (0,0), "Harper_Yes_Anim")

    image Harper_Wave_Anim:
        "sprites/Harper/Wave/Motion-01.png"
        pause 1.0
        "sprites/Harper/Wave/Motion-02.png"
        pause 0.14
        "sprites/Harper/Wave/Motion-03.png"
        pause 0.14
        "sprites/Harper/Wave/Motion-04.png"
        pause 1.0
        "sprites/Harper/Wave/Motion-03.png"
        pause 0.14
        "sprites/Harper/Wave/Motion-02.png"
        pause 0.14
        repeat

    image har wave = LiveComposite((1920,1080),
                                (0,0), "Harper_Wave_Anim")

    image Harper_Turn_Anim:
        "sprites/Harper/Turn/Motion-01.png"
        pause 0.5
        "sprites/Harper/Turn/Motion-02.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-03.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-04.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-05.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-06.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-07.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-08.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-09.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-10.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-11.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-12.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-13.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-14.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-15.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-16.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-17.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-18.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-19.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-20.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-21.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-22.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-23.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-24.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-25.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-26.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-27.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-28.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-29.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-30.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-31.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-32.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-33.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-34.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-35.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-36.png"
        pause 1.5
        "sprites/Harper/Turn/Motion-37.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-38.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-39.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-40.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-41.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-42.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-43.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-44.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-45.png"
        pause 0.07
        "sprites/Harper/Turn/Motion-46.png"
        pause 0.07

    image har turn = LiveComposite((1920,1080),
                                (0,0), "Harper_Turn_Anim")

    image har turned = LiveComposite((1920,1080),
                                (0,0), "sprites/Harper/Turn/Motion-46.png")

init python:
    def hbasevoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("har base")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("har base")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")


    def hnovoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("har no")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("har base")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def hyesvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("har yes")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("har base")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def hwavevoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("har wave")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("har wave")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def hturnvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("har turn")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("har turned")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")
