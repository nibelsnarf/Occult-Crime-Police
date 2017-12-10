label pitchdemo:
    show black
    typing "October 5th, 2017\nCrime Scene"
    show background3a with fade
    pause 2
    show mir default at left with dissolve
    show ash default at right, flip with dissolve
    e "Well, here we are in the engine demo."
    a "What kinds of things can we do in here?"
    e "We {alpha=0.5}have{/alpha} {b}all{/b} {i}kinds{/i} {color=#f00}of{/color} {u}text{/u} {s}formatting{/s} options."
    e "We can also control the flow of text to make the player shiver with antici{w=5.0}pation."
    a "Those things are boring! What else do we have?"
    e "Well... {w=1.0}how about {nw}"
    #show white with Pause(0.05)
    #hide white
    play audio "Bwaaah.ogg"
    e "Well... how about {fast}AN EXPLOSION!" with bigshake
    play audio "Bwaaah.ogg"
    ayell "AAAAAAA AAAAAAAAAAAAA AAAAAAAAAAAAAA AAAAAAAAAAAA{nw}" with bigshake
    play audio "Bwaaah.ogg"
    ayell "AAAAAAAAAA AAAAAAAAAAAAA AAAAAAAA AAAAAAAAAAA{nw}" with bigshake
    play audio "Bwaaah.ogg"
    ayell "AAAAAA AAAAAA AAAAAAAAAAAA AAAAAAAAAA AAAAAAA AAAAA AAAAAAAAA AAAAAAAA AAAAAAAAA AAAAAA AAAAAA AAAAAAAAA AAAAAAA" with bigshake
    a "That was very frightening."
    e "Thank you for demonstrating the way characters can change expressions on the fly."
    e "Now, what else would you like to know more about?"
    $triedallthree = []
    jump demochoice

label demochoice:
    if "1" in triedallthree and "2" in triedallthree and "3" in triedallthree:
        jump demofinale

    e "So..."
    e "What else would you like to know more about?"
    menu:
        "Music":
            a "Can you play music in this engine?"
            e "Of course! Take a listen to {nw}!"
            play music "drunkBoy_demo.mp3"
            e "Of course! Take a listen to {fast}this!"
            a "I love this song!"
            e "That's great, because it will loop forever until somebody stops it."
            a "Awesome!"
            a "..."
            a ".  .  .  .  ."
            a ".  .  .  .  .  .  .  .  ."
            a "Okay I'm bored of it."
            stop music
            play audio "Ding.ogg"
            e "No problem."
            $triedallthree.append("1")
            jump demochoice
        "Other Characters":
            a "How does the engine handle more than two characters?"
            e "Allow me to ask my very good friend...\nthis other guy!"
            hide mir default at left with dissolve
            show carlos default at left with dissolve
            c "Now it is me who is here."
            a "I understand completely!"
            a "Please go away now."
            c "Okey dokey."
            hide carlos default at left with dissolve
            show mir default at left with dissolve
            $triedallthree.append("2")
            jump demochoice
        "Collecting Evidence":
            a "So, this is a game about solving crimes, right?"
            e "I sure hope so. Otherwise I dressed up like this for nothing."
            a "How do you collect evidence, then?"
            e "I'll show you."
            e "See if you can pick up the conspicuously shitty envelope on the ground over there."
            hide mir default at left
            hide ash default at right, flip
            with dissolve
            show screen examinetest
            pause

screen examinetest:
    modal True
    imagemap:
        ground "assets/backgrounds/background3a.png"
        hotspot (1040, 906, 188, 111) action [Hide("examinetest"), Jump("bazinga")]

screen inventorybutton:
    hbox align (0.93,0.04) spacing 20:
        textbutton "Show Inventory" action [Show("inventory_screen"), Hide("inventorybutton")]

label bazinga:
    show background3a
    $inventory.add(autopsy)
    show background3b with dissolve
    show mir default at left
    show ash default at right, flip
    with dissolve
    a "I did it! I got it!"
    e "You sure clicked on that thing really good."
    a "So...what can I do with it?"
    e "Well, you can examine it in the inventory screen which will appear riiiight...{nw}"
    show screen inventorybutton
    play audio "Ding.ogg"
    e "Well, you can examine it in the inventory screen which will appear riiiight...{fast} Now!"
    a "Look at this wealth of information!"
    a "Like an entire world at my fingertips!"
    e "In the full game, you'll be able to present evidence to prove your case in various ways."
    a "Can you show me?"
    e ".{w=0.5} .{w=0.5} .{w=1.0} No."
    $triedallthree.append("3")
    jump demochoice


label demofinale:
    e "So that's the end of this demo!"
    e "There's other stuff built into this engine but it's not very interesting to show."
    e "And with that... {w=1.0} {b}I DIE.{/b}"
    hide mir default at left with moveoutbottom
    pause 1.0
    a "I will miss her always."
    "AND THEN CAMERON SPENT AN HOUR TRYING TO MAKE THE GAME QUIT"
    "BUT IT REFUSED TO DO SO"
    "SO INSTEAD THE CHARCTERS BECAME TRAPPED IN AN ENDLESS LOOP"
    "YOU WOULD THINK THAT MAKING THE GAME QUIT WOULD BE THE EASIEST THING"
    "WOULDN'T YOU"
    "HAH HAH HAH"
