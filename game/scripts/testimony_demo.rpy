label case_2:
    $ inventory.add(chocolate)
    show butt
    show sizetest at right
    b "Time for the testimony!"

    $ current_present = "objectA"
    $ knowsA5 = False

label testiA1:
    $ settesti("testiA1", None, "testiA2", "pressA1","advA1")
    show screen testi
    b "Um, I... I was there, it's true..."
    jump testiA2

label pressA1:
    hide screen testi
    e "That sounds fake but ok"
    jump testiA2

label testiA2:
    $ settesti("testiA2", "testiA1", "testiA3", "pressA2","advA1")
    show screen testi
    b "I ate a bunch of fucking ham."
    jump testiA3

label pressA2:
    hide screen testi
    e "Do you even like Ham?"
    b "No, thats whats so fucked up about it."
    jump testiA3

label testiA3:
    $ settesti("testiA3", "testiA2", "testiA4", "pressA3","advA1")
    show screen testi
    b "Then I shit all over the floor."
    jump testiA4

label pressA3:
    hide screen testi
    e "That sounds like a hard day."
    b "Eh. Pretty regular Tuesday, to be honest."
    jump testiA3

label testiA4:
    if knowsA5:
        $ settesti("testiA4", "testiA3", "testiA5", "pressA4", "advA1")
    else:
        $ settesti("testiA4", "testiA3", None, "pressA4", "advA1")

    b "I've never even talked to that British snob!" with smallshake

    if knowsA5:
        jump testiA5
    else:
        jump testiA1

label pressA4:
    e "then howd you know he was british bitch"
    b "um, fuck, he had flag"
    $ knowsA5 = True
    jump testiA5

label testiA5:
    $ settesti("testiA5", "testiA4", None, "pressA5","advA1")
    show screen testi
    b "HAD FLAG"
    jump testiA1

label pressA5:
    e "Yarp?"
    b "Narp."
    jump testiA1

label advA1:
    hide screen testi
    "nards"
    jump testiA1

label objectA:
    hide screen testi
    if testipart == "testiA3" and present_response == "chocolate":
        jump correctA
    else:
        jump fakeA

label correctA:
    e "This chocolate somehow proves that you DIDNT shit on the floor"
    b "FUUUUUUUUUUUCKKK!!!!"
    "the, end"
    jump endgame

label fakeA:
    e "Um, is this it...?"
    b "No"
    $ mc_health -= 1
    e "FUCK"
    if mc_health == 0:
        jump game_over
    else:
        jump testiA1

label game_over:
    b "you really blew it dog"
    jump endgame
