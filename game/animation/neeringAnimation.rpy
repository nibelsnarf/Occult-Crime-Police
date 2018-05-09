init:
    image GreenGlow:
        "sprites/Neering/GreenGlow.png"
        alpha 1
        pause 0.1
        alpha 0.96
        pause 0.1
        repeat

    image RedGlow:
        "sprites/Neering/RedGlow.png"
        alpha 1
        pause 0.1
        alpha 0.96
        pause 0.1
        repeat

    image GlitchGlow:
        "sprites/Neering/GlitchGlow.png"
        alpha 1
        pause 0.1
        alpha 0.96
        pause 0.1
        repeat

    image Neering_Standard_Blink:
        "sprites/Neering/Standard/Eyes_1.png"
        pause 4.0
        "sprites/Neering/Standard/Eyes_2.png"
        pause 0.07
        "sprites/Neering/Standard/Eyes_3.png"
        pause 0.07
        "sprites/Neering/Standard/Eyes_4.png"
        pause 0.07
        "sprites/Neering/Standard/Eyes_3.png"
        pause 0.07
        "sprites/Neering/Standard/Eyes_2.png"
        pause 0.07
        repeat

    image Neering_Standard_Talk:
        "sprites/Neering/Standard/Frown_1.png"
        pause 0.1
        "sprites/Neering/Standard/Frown_2.png"
        pause 0.1
        "sprites/Neering/Standard/Frown_3.png"
        pause 0.1
        "sprites/Neering/Standard/Frown_4.png"
        pause 0.1
        "sprites/Neering/Standard/Frown_2.png"
        pause 0.1
        repeat

    image Neering_Standard_Smile:
        "sprites/Neering/Standard/Smile_1.png"
        pause 0.1
        "sprites/Neering/Standard/Smile_2.png"
        pause 0.1
        "sprites/Neering/Standard/Smile_3.png"
        pause 0.1
        "sprites/Neering/Standard/Smile_4.png"
        pause 0.1
        "sprites/Neering/Standard/Smile_2.png"
        pause 0.1
        repeat

    image neering off = LiveComposite((1700,1080),
                                (0,0), "sprites/Neering/TVBase.png",
                                (0,0), "sprites/Neering/Off.png")

    image neering wheelin:
        "neering off"
        xoffset 900
        ease 1 xoffset 600
        pause 0.3
        ease 1 xoffset 300
        pause 0.3
        ease 1 xoffset 0
        pause 0.3

    image neering default = LiveComposite((1700,1080),
                                (0,0), "sprites/Neering/TVBase.png",
                                (0,0), "GreenGlow",
                                (0,0), "sprites/Neering/Standard/Base.png",
                                (0,0), "sprites/Neering/Standard/Frown_1.png",
                                (0,0), "Neering_Standard_Blink",
                                (0,0), "sprites/Neering/Standard/Glasses.png")

    image neering default talk= LiveComposite((1700,1080),
                                (0,0), "sprites/Neering/TVBase.png",
                                (0,0), "GreenGlow",
                                (0,0), "sprites/Neering/Standard/Base.png",
                                (0,0), "Neering_Standard_Talk",
                                (0,0), "Neering_Standard_Blink",
                                (0,0), "sprites/Neering/Standard/Glasses.png")

    image neering smile = LiveComposite((1700,1080),
                                (0,0), "sprites/Neering/TVBase.png",
                                (0,0), "GreenGlow",
                                (0,0), "sprites/Neering/Standard/Base.png",
                                (0,0), "sprites/Neering/Standard/Smile_1.png",
                                (0,0), "Neering_Standard_Blink",
                                (0,0), "sprites/Neering/Standard/Glasses.png")

    image neering smile talk= LiveComposite((1700,1080),
                                (0,0), "sprites/Neering/TVBase.png",
                                (0,0), "GreenGlow",
                                (0,0), "sprites/Neering/Standard/Base.png",
                                (0,0), "Neering_Standard_Smile",
                                (0,0), "Neering_Standard_Blink",
                                (0,0), "sprites/Neering/Standard/Glasses.png")

    image Neering_Angry_Blink:
        "sprites/Neering/Angry/Eyes_1.png"
        pause 4.0
        "sprites/Neering/Angry/Eyes_2.png"
        pause 0.07
        "sprites/Neering/Angry/Eyes_3.png"
        pause 0.07
        "sprites/Neering/Angry/Eyes_4.png"
        pause 0.07
        "sprites/Neering/Angry/Eyes_3.png"
        pause 0.07
        "sprites/Neering/Angry/Eyes_2.png"
        pause 0.07
        repeat

    image Neering_Angry_Talk:
        "sprites/Neering/Angry/Mouth_1.png"
        pause 0.1
        "sprites/Neering/Angry/Mouth_2.png"
        pause 0.1
        "sprites/Neering/Angry/Mouth_3.png"
        pause 0.1
        "sprites/Neering/Angry/Mouth_4.png"
        pause 0.1
        "sprites/Neering/Angry/Mouth_2.png"
        pause 0.1
        repeat

    image neering angry = LiveComposite((1700,1080),
                                (0,0), "sprites/Neering/TVBase.png",
                                (0,0), "GreenGlow",
                                (0,0), "sprites/Neering/Angry/Base.png",
                                (0,0), "sprites/Neering/Angry/Mouth_1.png",
                                (0,0), "Neering_Angry_Blink",
                                (0,0), "sprites/Neering/Angry/Glasses.png")

    image neering angry talk= LiveComposite((1700,1080),
                                (0,0), "sprites/Neering/TVBase.png",
                                (0,0), "GreenGlow",
                                (0,0), "sprites/Neering/Angry/Base.png",
                                (0,0), "Neering_Angry_Talk",
                                (0,0), "Neering_Angry_Blink",
                                (0,0), "sprites/Neering/Angry/Glasses.png")

    image Neering_Dismissive_Talk:
        "sprites/Neering/Dismissive/Mouth_1.png"
        pause 0.1
        "sprites/Neering/Dismissive/Mouth_2.png"
        pause 0.1
        "sprites/Neering/Dismissive/Mouth_3.png"
        pause 0.1
        "sprites/Neering/Dismissive/Mouth_4.png"
        pause 0.1
        "sprites/Neering/Dismissive/Mouth_2.png"
        pause 0.1
        repeat

    image neering dismissive = LiveComposite((1700,1080),
                                (0,0), "sprites/Neering/TVBase.png",
                                (0,0), "GreenGlow",
                                (0,0), "sprites/Neering/Dismissive/Base.png",
                                (0,0), "sprites/Neering/Dismissive/Mouth_1.png",
                                (0,0), "sprites/Neering/Dismissive/Glasses.png")

    image neering dismissive talk= LiveComposite((1700,1080),
                                (0,0), "sprites/Neering/TVBase.png",
                                (0,0), "GreenGlow",
                                (0,0), "sprites/Neering/Dismissive/Base.png",
                                (0,0), "Neering_Dismissive_Talk",
                                (0,0), "sprites/Neering/Dismissive/Glasses.png")

    image Neering_Grumble_Blink:
        "sprites/Neering/Grumble/Eyes_1.png"
        pause 4.0
        "sprites/Neering/Grumble/Eyes_2.png"
        pause 0.07
        "sprites/Neering/Grumble/Eyes_3.png"
        pause 0.07
        "sprites/Neering/Grumble/Eyes_4.png"
        pause 0.07
        "sprites/Neering/Grumble/Eyes_3.png"
        pause 0.07
        "sprites/Neering/Grumble/Eyes_2.png"
        pause 0.07
        repeat

    image Neering_Grumble_Talk:
        "sprites/Neering/Grumble/Mouth_1.png"
        pause 0.1
        "sprites/Neering/Grumble/Mouth_2.png"
        pause 0.1
        "sprites/Neering/Grumble/Mouth_3.png"
        pause 0.1
        "sprites/Neering/Grumble/Mouth_4.png"
        pause 0.1
        "sprites/Neering/Grumble/Mouth_2.png"
        pause 0.1
        repeat

    image neering grumble = LiveComposite((1700,1080),
                                (0,0), "sprites/Neering/TVBase.png",
                                (0,0), "GreenGlow",
                                (0,0), "sprites/Neering/Grumble/Base.png",
                                (0,0), "sprites/Neering/Grumble/Mouth_1.png",
                                (0,0), "Neering_Grumble_Blink",
                                (0,0), "sprites/Neering/Grumble/Glasses.png")

    image neering grumble talk= LiveComposite((1700,1080),
                                (0,0), "sprites/Neering/TVBase.png",
                                (0,0), "GreenGlow",
                                (0,0), "sprites/Neering/Grumble/Base.png",
                                (0,0), "Neering_Grumble_Talk",
                                (0,0), "Neering_Grumble_Blink",
                                (0,0), "sprites/Neering/Grumble/Glasses.png")

    image Neering_Laugh_Talk:
        "sprites/Neering/Laugh/Mouth_1.png"
        pause 0.1
        "sprites/Neering/Laugh/Mouth_2.png"
        pause 0.1
        "sprites/Neering/Laugh/Mouth_3.png"
        pause 0.1
        "sprites/Neering/Laugh/Mouth_4.png"
        pause 0.1
        "sprites/Neering/Laugh/Mouth_2.png"
        pause 0.1
        repeat

    image neering laugh = LiveComposite((1700,1080),
                                (0,0), "sprites/Neering/TVBase.png",
                                (0,0), "GreenGlow",
                                (0,0), "sprites/Neering/Laugh/Base.png",
                                (0,0), "sprites/Neering/Laugh/Mouth_1.png",
                                (0,0), "sprites/Neering/Laugh/Glasses.png")

    image neering laugh talk= LiveComposite((1700,1080),
                                (0,0), "sprites/Neering/TVBase.png",
                                (0,0), "GreenGlow",
                                (0,0), "sprites/Neering/Laugh/Base.png",
                                (0,0), "Neering_Laugh_Talk",
                                (0,0), "sprites/Neering/Laugh/Glasses.png")

    image Neering_Smug_Talk:
        "sprites/Neering/Smug/Mouth_1.png"
        pause 0.1
        "sprites/Neering/Smug/Mouth_2.png"
        pause 0.1
        "sprites/Neering/Smug/Mouth_3.png"
        pause 0.1
        "sprites/Neering/Smug/Mouth_4.png"
        pause 0.1
        "sprites/Neering/Smug/Mouth_2.png"
        pause 0.1
        repeat

    image Neering_Smug_GlassesA:
        "sprites/Neering/Smug/Glasses_1.png"
        pause 0.5
        "sprites/Neering/Smug/Glasses_2.png"
        pause 0.1
        "sprites/Neering/Smug/Glasses_3.png"
        pause 0.1
        "sprites/Neering/Smug/Glasses_4.png"
        pause 0.1
        "sprites/Neering/Smug/Glasses_5.png"
        pause 0.1
        "sprites/Neering/Smug/Glasses_6.png"
        pause 0.1
        "sprites/Neering/Smug/Glasses_7.png"
        pause 0.1
        "sprites/Neering/Smug/Glasses_8.png"
        pause 0.1

    image Neering_Smug_GlassesB:
        "sprites/Neering/Smug/Glasses_8.png"
        pause 0.07
        "sprites/Neering/Smug/Glasses_9.png"
        pause 0.07
        "sprites/Neering/Smug/Glasses_10.png"
        pause 0.07
        "sprites/Neering/Smug/Glasses_11.png"
        pause 0.07
        "sprites/Neering/Smug/Glasses_12.png"
        pause 0.3
        "sprites/Neering/Smug/Glasses_13.png"
        pause 0.07
        "sprites/Neering/Smug/Glasses_14.png"
        pause 0.07
        "sprites/Neering/Smug/Glasses_15.png"
        pause 0.07
        "sprites/Neering/Smug/Glasses_16.png"
        pause 0.3
        "sprites/Neering/Smug/Glasses_17.png"
        pause 0.07
        "sprites/Neering/Smug/Glasses_18.png"
        pause 0.07
        "sprites/Neering/Smug/Glasses_19.png"
        pause 0.07
        "sprites/Neering/Smug/Glasses_20.png"
        pause 0.07
        "sprites/Neering/Smug/Glasses_1.png"
        pause 0.07

    image neering smug = LiveComposite((1700,1080),
                                (0,0), "sprites/Neering/TVBase.png",
                                (0,0), "GreenGlow",
                                (0,0), "sprites/Neering/Smug/Base.png",
                                (0,0), "sprites/Neering/Smug/Mouth_1.png",
                                (0,0), "Neering_Smug_GlassesB")

    image neering smug talk= LiveComposite((1700,1080),
                                (0,0), "sprites/Neering/TVBase.png",
                                (0,0), "GreenGlow",
                                (0,0), "sprites/Neering/Smug/Base.png",
                                (0,0), "Neering_Smug_Talk",
                                (0,0), "Neering_Smug_GlassesA")

    image Neering_Uneasy_Blink:
          "sprites/Neering/Uneasy/Eyes_1.png"
          pause 4.0
          "sprites/Neering/Uneasy/Eyes_2.png"
          pause 0.07
          "sprites/Neering/Uneasy/Eyes_3.png"
          pause 0.07
          "sprites/Neering/Uneasy/Eyes_4.png"
          pause 0.07
          "sprites/Neering/Uneasy/Eyes_3.png"
          pause 0.07
          "sprites/Neering/Uneasy/Eyes_2.png"
          pause 0.07
          repeat

    image Neering_Uneasy_Talk:
          "sprites/Neering/Uneasy/Mouth_1.png"
          pause 0.1
          "sprites/Neering/Uneasy/Mouth_2.png"
          pause 0.1
          "sprites/Neering/Uneasy/Mouth_3.png"
          pause 0.1
          "sprites/Neering/Uneasy/Mouth_4.png"
          pause 0.1
          "sprites/Neering/Uneasy/Mouth_2.png"
          pause 0.1
          repeat

    image neering uneasy = LiveComposite((1700,1080),
                                  (0,0), "sprites/Neering/TVBase.png",
                                  (0,0), "GreenGlow",
                                  (0,0), "sprites/Neering/Uneasy/Base.png",
                                  (0,0), "sprites/Neering/Uneasy/Mouth_1.png",
                                  (0,0), "Neering_Uneasy_Blink",
                                  (0,0), "sprites/Neering/Uneasy/Glasses.png")

    image neering uneasy talk= LiveComposite((1700,1080),
                                  (0,0), "sprites/Neering/TVBase.png",
                                  (0,0), "GreenGlow",
                                  (0,0), "sprites/Neering/Uneasy/Base.png",
                                  (0,0), "Neering_Uneasy_Talk",
                                  (0,0), "Neering_Uneasy_Blink",
                                  (0,0), "sprites/Neering/Uneasy/Glasses.png")

    image Narper_Talk:
        "sprites/Neering/Narper/Mouth_1.png"
        pause 0.2
        "sprites/Neering/Narper/Mouth_2.png"
        pause 0.2
        "sprites/Neering/Narper/Mouth_3.png"
        pause 0.2
        "sprites/Neering/Narper/Mouth_4.png"
        pause 0.2
        "sprites/Neering/Narper/Mouth_2.png"
        pause 0.2
        repeat

    image neering narper = LiveComposite((1700,1080),
                                  (0,0), "sprites/Neering/TVBase.png",
                                  (0,0), "RedGlow",
                                  (0,0), "sprites/Neering/Narper/Base.png",
                                  (0,0), "sprites/Neering/Narper/Mouth_1.png")

    image neering narper talk= LiveComposite((1700,1080),
                                  (0,0), "sprites/Neering/TVBase.png",
                                  (0,0), "RedGlow",
                                  (0,0), "sprites/Neering/Narper/Base.png",
                                  (0,0), "Narper_Talk")

    image Neering_Glitch:
        "sprites/Bottomi/Explode/Explode_1.png"
        pause 0.7
        "sprites/Neering/Glitch/G1.png"
        pause 0.07
        "sprites/Neering/Glitch/G11.png"
        pause 0.07
        "sprites/Neering/Glitch/G12.png"
        pause 0.07
        "sprites/Neering/Glitch/G13.png"
        pause 0.07
        "sprites/Neering/Glitch/G14.png"
        pause 0.07
        "sprites/Neering/Glitch/G15.png"
        pause 0.07
        "sprites/Neering/Glitch/G2.png"
        pause 0.07
        "sprites/Bottomi/Explode/Explode_1.png"
        pause 0.5
        "sprites/Neering/Glitch/G3.png"
        pause 0.07
        "sprites/Neering/Glitch/G13.png"
        pause 0.07
        "sprites/Neering/Glitch/G4.png"
        pause 0.07
        "sprites/Bottomi/Explode/Explode_1.png"
        pause 2.0
        repeat

    image neering glitch = LiveComposite((1700,1080),
                                (0,0), "sprites/Neering/TVBase.png",
                                (0,0), "GreenGlow",
                                (0,0), "sprites/Neering/Standard/Base.png",
                                (0,0), "sprites/Neering/Standard/Frown_1.png",
                                (0,0), "Neering_Standard_Blink",
                                (0,0), "sprites/Neering/Standard/Glasses.png",
                                (0,0), "Neering_Glitch")

    image neering glitch talk= LiveComposite((1700,1080),
                                (0,0), "sprites/Neering/TVBase.png",
                                (0,0), "GreenGlow",
                                (0,0), "sprites/Neering/Standard/Base.png",
                                (0,0), "Neering_Standard_Talk",
                                (0,0), "Neering_Standard_Blink",
                                (0,0), "sprites/Neering/Standard/Glasses.png",
                                (0,0), "Neering_Glitch")

    image Narper_Glitch:
        "sprites/Bottomi/Explode/Explode_1.png"
        pause 0.4
        "sprites/Neering/Glitch/G9.png"
        pause 0.07
        "sprites/Neering/Glitch/G11.png"
        pause 0.07
        "sprites/Neering/Glitch/G8.png"
        pause 0.07
        "sprites/Bottomi/Explode/Explode_1.png"
        pause 0.07
        "sprites/Neering/Glitch/G12.png"
        pause 0.07
        "sprites/Bottomi/Explode/Explode_1.png"
        pause 0.4
        "sprites/Neering/Glitch/G16.png"
        pause 0.07
        "sprites/Bottomi/Explode/Explode_1.png"
        pause 0.07
        "sprites/Neering/Glitch/G14.png"
        pause 0.07
        repeat

    image neering narper glitch = LiveComposite((1700,1080),
                                  (0,0), "sprites/Neering/TVBase.png",
                                  (0,0), "RedGlow",
                                  (0,0), "sprites/Neering/Narper/Base.png",
                                  (0,0), "sprites/Neering/Narper/Mouth_1.png",
                                  (0,0), "Narper_Glitch")

    image neering narper glitch talk= LiveComposite((1700,1080),
                                  (0,0), "sprites/Neering/TVBase.png",
                                  (0,0), "RedGlow",
                                  (0,0), "sprites/Neering/Narper/Base.png",
                                  (0,0), "Narper_Talk",
                                  (0,0), "Narper_Glitch")

    image Neering_Reveal:
        "sprites/Neering/Glitch/G0.png"
        pause 0.5
        "sprites/Neering/Glitch/G1.png"
        pause 0.07
        "sprites/Neering/Glitch/G2.png"
        pause 0.07
        "sprites/Neering/Glitch/G3.png"
        pause 0.07
        "sprites/Neering/Glitch/G4.png"
        pause 0.07
        "sprites/Neering/Glitch/G5.png"
        pause 0.07
        "sprites/Neering/Glitch/G11.png"
        pause 0.07
        "sprites/Neering/Glitch/G12.png"
        pause 0.07
        "sprites/Neering/Glitch/G13.png"
        pause 0.07
        "sprites/Neering/Glitch/G14.png"
        pause 0.07
        "sprites/Neering/Glitch/G15.png"
        pause 0.07
        "sprites/Neering/Glitch/G6.png"
        pause 0.07
        "sprites/Neering/Glitch/G7.png"
        pause 0.07
        "sprites/Neering/Glitch/G8.png"
        pause 0.07
        "sprites/Neering/Glitch/G9.png"
        pause 0.07
        "sprites/Neering/Glitch/G10.png"
        pause 0.07
        "sprites/Neering/Glitch/G16.png"
        pause 0.07

    image Neering_Reveal_Glow:
        "GreenGlow"
        pause 0.85
        "GlitchGlow"
        pause 0.35
        "RedGlow"


    image neering reveal= LiveComposite((1700,1080),
                                (0,0), "sprites/Neering/TVBase.png",
                                (0,0), "Neering_Reveal_Glow",
                                (0,0), "Neering_Reveal")

init python:
    def noffvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("neering off")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("neering off")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")


    def ndefvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("neering default talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("neering default")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def nsmilevoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("neering smile talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("neering smile")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def nangryvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("neering angry talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("neering angry")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def ndismissivevoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("neering dismissive talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("neering dismissive")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def ngrumblevoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("neering grumble talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("neering grumble")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def nlaughvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("neering laugh talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("neering laugh")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def nsmugvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("neering smug talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("neering smug")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def nuneasyvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("neering uneasy talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("neering uneasy")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def narpervoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("neering narper talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("neering narper")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def narperglitchvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("neering narper glitch talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("neering narper glitch")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def nglitchvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("neering glitch talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("neering glitch")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")
