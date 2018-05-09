init:
    image Drang_Standard_Talk:
        "sprites/Drang/Standard/Mouth_1.png"
        pause 0.1
        "sprites/Drang/Standard/Mouth_2.png"
        pause 0.1
        "sprites/Drang/Standard/Mouth_3.png"
        pause 0.1
        "sprites/Drang/Standard/Mouth_4.png"
        pause 0.1
        "sprites/Drang/Standard/Mouth_2.png"
        pause 0.1
        repeat

    image Drang_Standard_Blink:
        "sprites/Drang/Standard/Eyes_1.png"
        pause 5.0
        "sprites/Drang/Standard/Eyes_2.png"
        pause 0.05
        "sprites/Drang/Standard/Eyes_3.png"
        pause 0.05
        "sprites/Drang/Standard/Eyes_4.png"
        pause 0.05
        "sprites/Drang/Standard/Eyes_3.png"
        pause 0.05
        "sprites/Drang/Standard/Eyes_2.png"
        pause 0.05
        repeat

    image Drang_Standard_Frown:
        "sprites/Drang/Standard/Frown_1.png"
        pause 0.1
        "sprites/Drang/Standard/Frown_2.png"
        pause 0.1
        "sprites/Drang/Standard/Frown_3.png"
        pause 0.1
        "sprites/Drang/Standard/Frown_4.png"
        pause 0.1
        "sprites/Drang/Standard/Frown_2.png"
        pause 0.1
        repeat

    image drang default gdown = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Standard/Base.png",
                                (0,0), "sprites/Drang/Standard/Mouth_1.png",
                                (0,0), "Drang_Standard_Blink",
                                (0,0), "sprites/Drang/Standard/Glasses_1.png" )

    image drang default gdown talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Standard/Base.png",
                                (0,0), "Drang_Standard_Talk",
                                (0,0), "Drang_Standard_Blink",
                                (0,0), "sprites/Drang/Standard/Glasses_1.png" )

    image drang default gup = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Standard/Base.png",
                                (0,0), "sprites/Drang/Standard/Mouth_1.png",
                                (0,0), "Drang_Standard_Blink",
                                (0,0), "sprites/Drang/Standard/Glasses_2.png" )

    image drang default gup talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Standard/Base.png",
                                (0,0), "Drang_Standard_Talk",
                                (0,0), "Drang_Standard_Blink",
                                (0,0), "sprites/Drang/Standard/Glasses_2.png" )

    image drang frown gdown = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Standard/Base.png",
                                (0,0), "sprites/Drang/Standard/Frown_1.png",
                                (0,0), "Drang_Standard_Blink",
                                (0,0), "sprites/Drang/Standard/Glasses_1.png" )

    image drang frown gdown talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Standard/Base.png",
                                (0,0), "Drang_Standard_Frown",
                                (0,0), "Drang_Standard_Blink",
                                (0,0), "sprites/Drang/Standard/Glasses_1.png" )

    image drang frown gup = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Standard/Base.png",
                                (0,0), "sprites/Drang/Standard/Frown_1.png",
                                (0,0), "Drang_Standard_Blink",
                                (0,0), "sprites/Drang/Standard/Glasses_2.png" )

    image drang frown gup talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Standard/Base.png",
                                (0,0), "Drang_Standard_Frown",
                                (0,0), "Drang_Standard_Blink",
                                (0,0), "sprites/Drang/Standard/Glasses_2.png" )


    image Drang_Thinking_Talk:
        "sprites/Drang/Thinking/Mouth_1.png"
        pause 0.1
        "sprites/Drang/Thinking/Mouth_2.png"
        pause 0.1
        "sprites/Drang/Thinking/Mouth_3.png"
        pause 0.1
        "sprites/Drang/Thinking/Mouth_4.png"
        pause 0.1
        "sprites/Drang/Thinking/Mouth_2.png"
        pause 0.1
        repeat

    image Drang_Thinking_Blink:
        "sprites/Drang/Thinking/Eyes_1.png"
        pause 5.0
        "sprites/Drang/Thinking/Eyes_2.png"
        pause 0.05
        "sprites/Drang/Thinking/Eyes_3.png"
        pause 0.05
        "sprites/Drang/Thinking/Eyes_4.png"
        pause 0.05
        "sprites/Drang/Thinking/Eyes_3.png"
        pause 0.05
        "sprites/Drang/Thinking/Eyes_2.png"
        pause 0.05
        repeat

    image Drang_Thinking_Hand:
        "sprites/Drang/Thinking/Hand_1.png"
        pause 1.0
        "sprites/Drang/Thinking/Hand_2.png"
        pause 0.2
        "sprites/Drang/Thinking/Hand_3.png"
        pause 1.0
        "sprites/Drang/Thinking/Hand_2.png"
        pause 0.2
        repeat

    image drang think gdown = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Thinking/Base.png",
                                (0,0), "sprites/Drang/Thinking/Mouth_1.png",
                                (0,0), "Drang_Thinking_Blink",
                                (0,0), "sprites/Drang/Thinking/Glasses_1.png",
                                (0,0), "Drang_Thinking_Hand" )

    image drang think gdown talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Thinking/Base.png",
                                (0,0), "Drang_Thinking_Talk",
                                (0,0), "Drang_Thinking_Blink",
                                (0,0), "sprites/Drang/Thinking/Glasses_1.png",
                                (0,0), "Drang_Thinking_Hand"  )

    image drang think gup = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Thinking/Base.png",
                                (0,0), "sprites/Drang/Thinking/Mouth_1.png",
                                (0,0), "Drang_Thinking_Blink",
                                (0,0), "sprites/Drang/Thinking/Glasses_2.png",
                                (0,0), "Drang_Thinking_Hand"  )

    image drang think gup talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Thinking/Base.png",
                                (0,0), "Drang_Thinking_Talk",
                                (0,0), "Drang_Thinking_Blink",
                                (0,0), "sprites/Drang/Thinking/Glasses_2.png",
                                (0,0), "Drang_Thinking_Hand" )

    image Drang_Angry_Talk:
        "sprites/Drang/Angry/Mouth_1.png"
        pause 0.1
        "sprites/Drang/Angry/Mouth_2.png"
        pause 0.1
        "sprites/Drang/Angry/Mouth_3.png"
        pause 0.1
        "sprites/Drang/Angry/Mouth_4.png"
        pause 0.1
        "sprites/Drang/Angry/Mouth_2.png"
        pause 0.1
        repeat

    image Drang_Angry_Blink:
        "sprites/Drang/Angry/Eyes_1.png"
        pause 5.0
        "sprites/Drang/Angry/Eyes_2.png"
        pause 0.05
        "sprites/Drang/Angry/Eyes_3.png"
        pause 0.05
        "sprites/Drang/Angry/Eyes_4.png"
        pause 0.05
        "sprites/Drang/Angry/Eyes_3.png"
        pause 0.05
        "sprites/Drang/Angry/Eyes_2.png"
        pause 0.05
        repeat

    image drang angry gdown = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Angry/Base.png",
                                (0,0), "sprites/Drang/Angry/Mouth_1.png",
                                (0,0), "Drang_Angry_Blink",
                                (0,0), "sprites/Drang/Angry/Glasses_1.png" )

    image drang angry gdown talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Angry/Base.png",
                                (0,0), "Drang_Angry_Talk",
                                (0,0), "Drang_Angry_Blink",
                                (0,0), "sprites/Drang/Angry/Glasses_1.png" )

    image drang angry gup = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Angry/Base.png",
                                (0,0), "sprites/Drang/Angry/Mouth_1.png",
                                (0,0), "Drang_Angry_Blink",
                                (0,0), "sprites/Drang/Angry/Glasses_2.png" )

    image drang angry gup talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Angry/Base.png",
                                (0,0), "Drang_Angry_Talk",
                                (0,0), "Drang_Angry_Blink",
                                (0,0), "sprites/Drang/Angry/Glasses_2.png" )


    image Drang_Dril_Talk:
        "sprites/Drang/Dril/Mouth_1.png"
        pause 0.15
        "sprites/Drang/Dril/Mouth_2.png"
        pause 0.15
        "sprites/Drang/Dril/Mouth_3.png"
        pause 0.15
        "sprites/Drang/Dril/Mouth_4.png"
        pause 0.15
        "sprites/Drang/Dril/Mouth_2.png"
        pause 0.15
        repeat

    image Drang_Dril_Blink:
        "sprites/Drang/Dril/Eyes_1.png"
        pause 5.0
        "sprites/Drang/Dril/Eyes_2.png"
        pause 0.05
        "sprites/Drang/Dril/Eyes_3.png"
        pause 0.05
        "sprites/Drang/Dril/Eyes_4.png"
        pause 0.05
        "sprites/Drang/Dril/Eyes_3.png"
        pause 0.05
        "sprites/Drang/Dril/Eyes_2.png"
        pause 0.05
        repeat

    image drang dril gdown = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Dril/Base.png",
                                (0,0), "sprites/Drang/Dril/Mouth_1.png",
                                (0,0), "Drang_Dril_Blink",
                                (0,0), "sprites/Drang/Dril/Glasses_1.png" )

    image drang dril gdown talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Dril/Base.png",
                                (0,0), "Drang_Dril_Talk",
                                (0,0), "Drang_Dril_Blink",
                                (0,0), "sprites/Drang/Dril/Glasses_1.png" )

    image drang dril gup = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Dril/Base.png",
                                (0,0), "sprites/Drang/Dril/Mouth_1.png",
                                (0,0), "Drang_Dril_Blink",
                                (0,0), "sprites/Drang/Dril/Glasses_2.png" )

    image drang dril gup talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Dril/Base.png",
                                (0,0), "Drang_Dril_Talk",
                                (0,0), "Drang_Dril_Blink",
                                (0,0), "sprites/Drang/Dril/Glasses_2.png" )

    image Drang_Jacket_Talk:
        "sprites/Drang/Jacket/Mouth_1.png"
        pause 0.1
        "sprites/Drang/Jacket/Mouth_2.png"
        pause 0.1
        "sprites/Drang/Jacket/Mouth_3.png"
        pause 0.1
        "sprites/Drang/Jacket/Mouth_4.png"
        pause 0.1
        "sprites/Drang/Jacket/Mouth_2.png"
        pause 0.1
        repeat

    image Drang_Jacket_Arms:
        "sprites/Drang/Jacket/Arms_01.png"
        pause 0.15
        "sprites/Drang/Jacket/Arms_03.png"
        pause 0.15
        "sprites/Drang/Jacket/Arms_05.png"
        pause 0.4
        "sprites/Drang/Jacket/Arms_10.png"
        pause 0.075
        "sprites/Drang/Jacket/Arms_11.png"
        pause 0.05
        "sprites/Drang/Jacket/Arms_12.png"
        pause 0.05
        "sprites/Drang/Jacket/Arms_13.png"
        pause 0.05
        "sprites/Drang/Jacket/Arms_14.png"
        pause 0.05
        "sprites/Drang/Jacket/Arms_15.png"
        pause 0.05
        "sprites/Drang/Jacket/Arms_16.png"
        pause 0.05
        "sprites/Drang/Jacket/Arms_17.png"
        pause 0.05
        "sprites/Drang/Jacket/Arms_18.png"
        pause 0.05


    image drang jacket pop = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Jacket/Base.png",
                                (0,0), "sprites/Drang/Jacket/Mouth_1.png",
                                (0,0), "Drang_Jacket_Arms",
                                (0,0), "sprites/Drang/Jacket/Glasses.png" )

    image drang jacket pop talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Jacket/Base.png",
                                (0,0), "Drang_Jacket_Talk",
                                (0,0), "sprites/Drang/Jacket/Arms_01.png",
                                (0,0), "sprites/Drang/Jacket/Glasses.png" )

    image drang jacket popped = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Jacket/Base.png",
                                (0,0), "sprites/Drang/Jacket/Mouth_1.png",
                                (0,0), "sprites/Drang/Jacket/Arms_18.png",
                                (0,0), "sprites/Drang/Jacket/Glasses.png" )

    image drang jacket popped talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Jacket/Base.png",
                                (0,0), "Drang_Jacket_Talk",
                                (0,0), "sprites/Drang/Jacket/Arms_18.png",
                                (0,0), "sprites/Drang/Jacket/Glasses.png" )

    image Drang_Frazzled_Talk:
        "sprites/Drang/Frazzled/Mouth_1.png"
        pause 0.15
        "sprites/Drang/Frazzled/Mouth_2.png"
        pause 0.15
        "sprites/Drang/Frazzled/Mouth_3.png"
        pause 0.15
        "sprites/Drang/Frazzled/Mouth_4.png"
        pause 0.15
        "sprites/Drang/Frazzled/Mouth_2.png"
        pause 0.15
        repeat

    image Drang_Frazzled_Blink:
        "sprites/Drang/Frazzled/Eyes_1.png"
        pause 5.0
        "sprites/Drang/Frazzled/Eyes_2.png"
        pause 0.05
        "sprites/Drang/Frazzled/Eyes_3.png"
        pause 0.05
        "sprites/Drang/Frazzled/Eyes_4.png"
        pause 0.05
        "sprites/Drang/Frazzled/Eyes_3.png"
        pause 0.05
        "sprites/Drang/Frazzled/Eyes_2.png"
        pause 0.05
        repeat

    image drang frazzled = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Frazzled/Base.png",
                                (0,0), "sprites/Drang/Frazzled/Mouth_1.png",
                                (0,0), "Drang_Frazzled_Blink",
                                (0,0), "sprites/Drang/Frazzled/Glasses.png" )

    image drang frazzled talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Frazzled/Base.png",
                                (0,0), "Drang_Frazzled_Talk",
                                (0,0), "Drang_Frazzled_Blink",
                                (0,0), "sprites/Drang/Frazzled/Glasses.png" )

init python:
    def ddefgdownvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang default talk gdown")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang default gdown")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def ddefgupvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang default talk gup")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang default gup")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def dfrowngdownvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang frown talk gdown")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang frown gdown")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def dfrowngupvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang frown talk gup")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang frown gup")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def dthinkgdownvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang think gdown talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang think gdown")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def dthinkgupvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang think gup talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang think gup")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def dangrygdownvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang angry gdown talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang angry gdown")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def dangrygupvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang angry gup talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang angry gup")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def ddrilgdownvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang dril gdown talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang dril gdown")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def ddrilgupvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang dril gup talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang dril gup")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def djpopvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang jacket pop talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang jacket pop")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def djpoppedvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang jacket popped talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang jacket popped")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def dfrazzledvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang frazzled talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang frazzled")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")
