label demo_act_IV:
    if "1"  in cleared_items and "2" in cleared_items and "3" in cleared_items and "4" in cleared_items and "talk_1" in cleared_items and "talk_2" in cleared_items:
        $ cleared_area = 1

    if cleared_area == 0:
        $ current_talk = "demo_witness_talk_1"
        $ current_background = "demo_background"
        $ current_move = "demo_move_1"
        $ back_action = "demo_present_1"
        $ demo_background_1_response = 0
        $ bgpos = False
        show screen demo_background
        call nav_screen_label from _call_nav_screen_label

    e "Done talking/exploring."

    jump endgame

    return

screen demo_move_1:
    modal True
    imagemap:
        ground "assets/backgrounds/Map_Screen.png"

    hbox align (0.97,0.95):
        textbutton _("Return") action [Hide(current_move)]


label demo_present_1:
    if present_response == "chocolate":
        e "this is a chocolate bar"
        b "This reminds me of something..."
        $ presentedChocolate = 1
        jump demo_witness_talk_1

    if present_response == "banana":
        e "this is a banana"
        jump demo_witness_talk_1

    if present_response == "gun":
        b "This is not a person, it is a gun."
        e "Oh."
        jump demo_witness_talk_1

    if present_response == "Back":
        e "Hm, never mind."
        $ present_response = "None"
        jump demo_witness_talk_1
    else:
        b "I don't know anything about that!"
        jump demo_witness_talk_1

transform panRight:
    ease 1.0 xpos -1920
transform panLeft:
    ease 1.0 xpos 0

screen demo_background:
    imagemap:
        if (bgpos == True):
            at panRight
        if (bgpos == False):
            at panLeft
        ground "assets/backgrounds/BackgroundTest.png"
        hover "assets/backgrounds/BackgroundTest.png"
        hotspot (125, 130, 540, 335) action [SetVariable("demo_background_1_response", 1), Jump("demo_background_1_answer")]
        hotspot (3043, 630, 750, 380) action [SetVariable("demo_background_1_response", 2), Jump("demo_witness_talk_1"), Hide("demo_background")]

    hbox align (0.97,0.05):
        textbutton _("Return") action [SetVariable("demo_background_1_response", 0), SetVariable("loop2", 1), Jump("demo_background_1_answer")]

    hbox align (.5,.97):
        imagebutton idle "assets/menu/NavScreenArrow.png" action ToggleVariable("bgpos", True, False)

label demo_background_1_answer:
    hide screen demo_background
    hide butt
    hide mir default
    if demo_background_1_response == 1:
        "You clicked #1" with tinyshake
        $ cleared_items.append("1")
    elif demo_background_1_response == 2:
        "You clicked #2" with smallshake
        $ cleared_items.append("2")


    jump demo_act_IV

    return

label demo_witness_talk_1:
    hide screen demo_background
    show butt at right
    show mir default at left
    $loop = 1
    while loop == 1:
        menu:
            "Hello":
                b "..."
                scene black
                show butt at right
                show mir default at left
                with dissolve
                e "Hello."

                b "Hello there."
                scene BackgroundTest
                show butt at right
                show mir default at left
                with dissolve
                e "Bye."

                b "Goodbye."

                $ cleared_items.append("talk_1")

            "Choice Test":

                jump choice_Test_Dialogue


            "Chocolate Test" if presentedChocolate == 1:
                bsurprise "I think that chocolate is deeeeeeeeeeeeeee\neeeeeeeeeeeeeeeeeeeeeeeee\neeeeeeeeeeeeeeee\neeelicious!"

            "Can I ask you about something?":
                e "Can I ask you about something?"
                b "Well, what is it?"
                $ current_present = "demo_present_1"
                show screen present_evidence_screen
                show screen back_button
                pause


            "What do you think about this person?":
                e "What do you think about this person?"
                $ current_present = "demo_present_1"
                show screen present_profile_screen
                show screen back_button
                pause


            "Finished talking.":
                $ loop = 0

    call demo_act_IV from _call_demo_act_IV_1

label choice_Test_Dialogue:
    e "Hello there, sir."
    b "Who the hell are you?"
    menu:
        "My name is Miranda Warren. I'm the sherrif around these parts.":
            e "My name is Miranda Warren. I'm the sherrif around these parts."
            b "Good to know."

        "Let's just say I'm a concerned citizen asking around.":
            e "Let's just say I'm a concerned citizen asking around."
            b "Don't jerk me around, copper. I can see the badge on your shirt there."

        "That's not really a thing that's any of your business right now.":
            e "That's not really a thing that's any of your business right now."
            b "Jeez, sorry I asked."

    e "Now, do you mind answering a few questions?"
    jump demo_witness_talk_1


label demo_act_V:
    show tester at left:
        xzoom -1
    "fuck, theres nothing here"
    hide tester
    show tester at right
    "wait there it is"
    hide tester
