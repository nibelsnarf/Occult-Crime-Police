label smart_house_act_3_intro:
    ### ACT 3: A THEOREM REVISED
    $ save_name = "Act 3"
    $ askedHarperAboutMurder = False
    show black
    typing "September 13th. 9:02 P.M.\nSmart House - Kitchen"
    show kitchen with dissolve
    show drang think gdown
    with dissolve
    dthink_gdown "Well, well, well..."
    dthink_gdown "It looks like this case just got interesting..."
    show ash annoyed
    aannoy "How has this case {i}not{/i} been interesting up until this point?"
    djacket_pop "You see a lot of strange things on the job, kid. It takes a lot to catch one's interest."
    aannoy "The crime scene is a revolutionary piece of technology!"
    aannoy "The main suspect keeps lying in order to prove his own guilt!"
    aannoy "If anything, a microchip in a guy's head is the {i}least{/i} peculiar thing we've seen today!"
    dangry_gdown "I don't have to take any guff from you, kid! You're my assistant's assistant!"
    dangry_gdown "You're, like, my grand-assistant!"
    dangry_gup "Warren, tell this kid to be quiet!"
    hide ash
    hide drang
    with dissolve
    show mir default
    show car serious at flip
    with dissolve
    wbase "Any luck waking him up?"
    cser "Nope. He's out cold."
    cser "We're just gonna need to wait for him to wake up and hope he didn't get a concussion."
    wbase "All right. You stay here and keep an eye on him."
    wthink "I've got a couple of things I want to check out."
    cdef "Aw yeah. Relaxation time with my good unconscious friend down here."
    clift "Hey, want a drink, buddy?"
    chold "Just kidding. Looks like you've had one too many already."
    show mir annoy anim
    wos "* sigh *"
    wbase "Ash, are you coming?"
    hide car
    hide mir
    with dissolve
    show drang angry gup
    show ash standard
    with dissolve
    dangry_gup "No, {i}you're{/i} a loser!"
    asurprise "Oh, hold that thought."
    adef "Coming, Randi!"
    hide ash
    hide drang
    with dissolve
    show mir annoy base
    show ash standard at flip
    with dissolve
    wannoy "Why do you ever bother with him?"
    aconfident "He's so {i}easy{/i} to mess with! It's like shooting dorks in a barrel!"
    adef "So where are we going?"
    wcasefile "There are a few things we ought to check out."
    wcasefile "First, we need to investigate the rest of the house."
    wcasefile "It's seeming less and less likely that this kitchen is the true scene of the crime."
    wthink "Come to think of it, the smart house itself may be capable of answering some questions."
    wthink "In that case, we should see if we can get it to testify."
    aunsure "You want to interrogate... the smart house?"
    wcasefile "The pamphlet you gave me says it has sensors all over."
    wcasefile "It's possible it recorded the crime with one of those."
    athink "Okay, what else?"
    wbase "That internet guy acted very strangely the last time we spoke."
    wbase "I think there's something he's still hiding from us."
    adef "Anything else?"
    wbase "I'd like to speak with somebody involved with the Smart House project."
    wbase "They may have more information about this whole affair."
    apsyched "All right! Let's do it!"
    apsyched "Investigation Ahoy!"
    $investigation2_cleareditems = []
    $unlockedContraption = False
    $unlockedOffice = False
    $unlockedBedroom = False
    play music "music/Investigation_Loops.ogg" fadein 1.0
    jump investigation2_houseconvo

label investigation2:
    scene kitchenact2 with fade
    hide victimbody
    if "1" in investigation2_cleareditems and "2" in investigation2_cleareditems and "3" in investigation2_cleareditems and "4" in investigation2_cleareditems and "5" in investigation2_cleareditems and "6" in investigation2_cleareditems and "7" in investigation2_cleareditems:
        jump investigation2_bottomiawakens
    show screen sh_investigation2_kitchen
    pause

screen sh_investigation2_kitchen:
    modal True
    imagemap:
        ground "kitchenact2"
        hotspot (X,Y,W,H) action [Hide("sh_investigation1_kitchen"), Jump("investigation2_houseconvo")]
        hotspot (X,Y,W,H) action [Hide("sh_investigation1_kitchen"), Jump("investigation2_drangconvo")]
    use inventory_screen_button
    imagebutton auto "assets/menu/move_%s.png"  xalign 0.5 yalign 1.0 action Jump("inv2_move_kitchen")

label inv2_move_kitchen:
    menu:
        "Smart House - Bedroom" if unlockedBedroom == True:
            hide screen sh_investigation2_kitchen
            jump investigation2_bedroom

        "Base 24 - Dressing Contraption" if unlockedContraption == True:
            hide screen sh_investigation2_kitchen
            jump investigation2_thedressingcontraption

        "Base 24 - Warehouse":
            hide screen sh_investigation2_kitchen
            jump investigation2_chritude

        "Base 24 - Neering's Office" if unlockedOffice == True:
            hide screen sh_investigation2_kitchen
            jump investigation2_neeringsoffice


label investigation2_houseconvo:
    ### Speak with Smart House
    asurprise "Hey, look at that little touchscreen!"
    aannoy "How did we miss that?"
    wbase "Well, Agent Drang was standing there earlier. He blocked our line of sight to it."
    adef "I think it's a control panel for the Smart House."
    aposit "So I bet if I push this button..."
    show har deploy at flip
    asurprise "Woah!"
    wconfused "What the...?"
    hunk "New Users Detected. Please State Your Name."
    wconfused "Uh, Miranda Warren."
    aflippant "Butt Stevenson."
    wannoy "Ash!"
    hunk "Profiles Created. Welcome, Miranda Warren, and, Butt Stevenson."
    aconfident "Hah hah"
    aconfident "Nice."
    hunk "I Am Home Automated Routinely Performing Errand Robot, Or H.A.R.P.E.R."
    hbase "How Can I Help You Today?"
    menu:
        "Smart House":
            whattip "So, what are you exactly?"
            hwave "I Am An Artificial Intelligence Designed To Make Your Life Easier."
            hbase "I Can Provide A Number Of Services Pertaining To Everyday Life."
            hbase "I Can Cook And Clean, I Can Move Heavy Objects, I Can Search The Internet For Various Things."
            hbase "I Can Respond To Requests Made Of Me, And Can Learn From Previous Experiences."
            adef "Can you tell knock-knock jokes?"
            hturn "I Have Over Ten Thousand Knock-Knock Jokes In My Database."
            wannoy "Please don't demonstrate."
            hturn "Understood."
            wbase "Harper, tell me who made you."
            hyes "I Am A Co-Production Of United States Government And The Burchfield Manufacturing Corporation."
            wannoy "No, I mean, {nw}"
            whattip "No, I mean, {fast}who is your inventor? Who lead the project which created you?"
            hbase "That Would Be User Zero. Her Name Is Angela Neering."
            wthink "Angela Neering... does she work here at the base?"
            hno "I Am Not Sure. I Have Limited Knowledge Of Happenings Outside Of My Walls."
            hyes "However, If This Base You Speak Of Is Where I Was Built, Then It Is Likely That User Zero Works Here."
            hbase "She Makes Frequent Visits Here In Order To Test Various Functions."
            wbase "Ash, I think you and I should go visit this Angela Neering when we get a chance."
            hno "Unfortunately, User Zero Is Not In Her Office Right Now."
            whattip "How would you know that?"
            hbase "I Have Communication Enabled With User Zero's Office. It Is One Of The Few Outside Views Afforded To Me."
            wbase "Well, we can always wait around for her to return."
            wconfused "Uh, thanks, Harper. Do I need to thank you?"
            hno "While I Will Warmly Receive Your Thanks, I Do Not Require Positive Feedback To Function."
            hbase "I Have No Human Emotions To Speak Of, And Can Feel Neither Happy Nor Sad About Our Interactions."
            wannoy "Next time, just stick with a \"You're Welcome\"."
            hyes "Understood."
            $ investigation2_cleareditems.append("1")
            $unlockedOffice = True

        "The Murder":
            wbase "Can you tell us anything about the murder?"
            hno "I'm Sorry. I Do Not Have \"The Murder\" In My Data Banks."
            athink "Randi, remember this thing is a robot. It doesn't fully understand human language."
            athink "You gotta act like you're talking to your smartphone or something."
            wconfused "Oh, uh..."
            whattip "Can you tell me what happened in the kitchen between 5 and 6 P.M. today?"
            hyes "Certainly, User Miranda."
            hbase ". . . ."
            hbase "ERROR. BACKUP FILES FOR SEPTEMBER_13_5-6PM INACCESSABLE."
            hbase "STORAGE DRIVE CORRUPTED BY POWER INTERRUPTION."
            wannoy "You're kidding me."
            hno "While I Am Programmed To Be Capable Of Kidding, I Am Not Doing So On This Occasion."
            $ askedHarperAboutMurder = True

        "Show Evidence":
            wbase "Do you recognize this item?"
            $ current_present = "investigation_2_house_present"
            show screen present_evidence_screen
            show screen back_button
            pause

        "Show Profile":
            wbase "Do you have a profile of this person?"
            $ current_present = "investigation_2_house_present"
            show screen present_profile_screen
            show screen back_button
            pause

        "Goodbye":
            wbase "Thank you for your assistance."
            whattip "Uh, turn off now, or whatever."
            hno "You Cannot Turn Me Off! I Am A Constant Presence In The House."
            hbase "I Am Always Listening To Every Conversation, In Case I Am Needed."
            wbase "All right then, uh... just be quiet, I guess?"
            hyes "Understood."
            $loop = 0

label investigation_2_house_present:
    if present_response == "sheriffbadge":
        ###
        warren "bazinga"
    if present_response == "OrinD":
        ###
        warren "bazinga"
    if present_response == "AngelaN":
        ###
        warren "bazinga"
    if present_response = "trapdoor":
        wcasefile "We discovered this trap door in the upstairs bedroom..."
        hyes "Ah, That Is The Entrance To The Dressing Contraption."
        wconfused "The Dressing what now?"
        asurprise "Oh, I remember now! {nw}"
        adef "Oh, I remember now! {fast}The Dressing Contraption is one of the features of the house."
        adef "When you wake up in the morning, your bed tilts forward and a trap door opens..."
        adef "Then you slide down into this secret room where a big contraption gets you dressed for the day!"
        adef "When you're ready, it drops you down into the kitchen just in time for breakfast!"
        wbase "That sounds..."
        menu:
            "...incredibly dangerous.":
                wannoy "...incredibly dangerous."
            "...extremely annoying.":
                wannoy "...extremely annoying."
            "...overly complicated.":
                wannoy "...overly complicated."
        aflippant "Come on, you spoilsport, it's fun!"
        aflippant "What's the point of having a Smart House if you're not gonna do cool stuff with it?"
        wbase "Harper, we have reason to believe that this \"Dressing Contraption\" may have something to do with the case."
        whattip "Can you please open up the trap door to let us investigate it?"
        hyes "Even Better, I Can Open Up The Service Entrance So You Do Not Have To Jump Through The Trap Door."
        aunsure "...But what if I {i}wanted{/i} to jump through the trap door?"
        wbase "Then you can buy your own smart house."
        wbase "Thank you, Harper."
        hbase "You're Welcome."
        $ investigation2_cleareditems.append("2")
        $unlockedContraption = True

    else:
        hno "I'm Sorry. I Do Not Have A Record Of That."
        hbase "If You Feel This Is An Error, Please Send A Bug Report To feedback@base24.gov"
        jump investigation2_houseconvo

label investigation2_neeringsoffice:
    if visitedOffice == False:
        typing "September 13th.\nBase 24 - Neering's Office"
        ### First Visit Conversation
        wbase "This should be the place."
        aflippant "I sure hope so."
        aflippant "This is like the fifth office we've barged in on."
        wbase "Well, it looks like Ms Neering isn't even here."
        apsyched "Perfect! Time to do some snooping!"
        wannoy "Ash, we aren't going to do any snooping, all right?"
        whattip "Although, if we take a quick look around while waiting for Ms Neering..."
        apsyched "Snoo! Ping! Snoo! Ping! Snoo! Ping!"
        wangry "All right, all right! Call it snooping if you really want to!"
        aconfident "Heh heh heh!"
        $ visitedOffice = True
    if "3" in investigation2_cleareditems and "4" in investigation2_cleareditems:
        jump investigation2_neeringconvo

screen sh_investigation2_office:
    modal True
    imagemap:
        ground "officeDark"
        hotspot (X,Y,W,H) action [Hide("sh_investigation2_office"), Jump("investigation2_emails")]
        hotspot (X,Y,W,H) action [Hide("sh_investigation2_office"), Jump("investigation2_securitylogs")]
    use inventory_screen_button
    imagebutton auto "assets/menu/move_%s.png"  xalign 0.5 yalign 1.0 action Jump("inv2_move_office")

label inv2_move_office:
    menu:
        "Smart House - Kitchen":
            hide screen sh_investigation2_office
            jump sh_investigation2_kitchen

        "Smart House - Bedroom" if unlockedBedroom == True:
            hide screen sh_investigation2_office
            jump investigation2_bedroom

        "Smart House - Dressing Contraption" if unlockedContraption == True:
            hide screen sh_investigation2_office
            jump investigation2_thedressingcontraption

        "Base 24 - Warehouse":
            hide screen sh_investigation2_office
            jump investigation2_chritude

label investigation2_emails:
    ### Find Emails About Carpet / Sentience Concerns
    aposit "Hey, it looks like {i}somebody{/i} left their email open!"
    wthink "All right, I can tolerate a little snooping, but reading private emails is just too far."
    aposit "Even private emails received from {color=red}Mr Darsha?{/color}"
    wangry "What? Let me see!"
    show neeringEmail
    ### (SHOW EMAIL)
    ### From: OrinD@base24.gov
    ### To: AngelaN@base24.gov
    ### RE: RE: Carpets
    ###
    ### We will talk about it after the reveal. It's imperative this launch goes well. We
    ### cannot afford any more delays on this project.
    ### ------------------------------------------------------------------------------------------
    ### yes, the new carpets will be ready in time for the tours. i've got contractors coming in
    ### the day before the event. now can we please talk about the AI? i don't think it's ready
    ### for the reveal. i keep getting erratic behavior and strange bugs. i need some time to
    ### troubleshoot the problems. i may even need to bring the whole thing offline for a while.
    ### ------------------------------------------------------------------------------------------
    ### Ms Neering,
    ###     It has come to my attention that the upstairs bedroom still does not have carpeting
    wos "Hm... it looks like there was some friction between Ms Neering and the victim over the state of the house."
    aos "Isn't that just the way..."
    aos "The creative type wants to take their time on the project while the higher-ups want to kick it out the door as soon as possible."
    wos "Is that... something you have experience with?"
    aos "No, but I watch a lot of Making-Of documentaries."
    hide neeringEmail
    wthink "I've got a feeling this exchange is important."
    wbase "Ash, could you take a picture of t{nw}"
    ### White Flash
    acamera "Way ahead of you."
    ### Darsha's Email added to Inventory
    $ investigation2_cleareditems.append("3")

label investigation2_securitylogs:
    ### Find Dot Matrix Printer
    adef "Hey, check it out, it's one of those zig-zag printers they use for earthquakes and stuff!"
    adef "I love those big ka-chunk noises they make."
    wthink "Let me see that..."
    wos ". . ."
    wbase "Looks like Ms Neering has a printer set up to log feedback from the house's operating system."
    wbase "Things like system functionality and user inputs."
    adef "Hey, check the log from between 5 and 6!"
    aposit "Maybe the house logged somebody saying \"I'm gonna murder you!\""
    wthink "We should be so lucky..."
    ### Show Logs
    wos "Most of this is programmer gobbeldygook, but I can make out some of it."
    wos "It shows \"Tour Mode\" ending at 5:30..."
    wos "Was Mr Darsha with your group through the whole tour?"
    aos "I think so... he was hanging around near the back."
    wos "So he died some time between then and 6 P.M."
    wos "Odd... somebody disabled the safety protocols at 5:51."
    wos "I wonder how many people have the authority to do something like that?"
    ### Hide Logs
    wbase "Hm. Look at this. At 5:52 it says \"TDC Subroutine Activated.\""
    ash "What do you think TDC stands for?"
    aposit "\"Terribly Dangerous Cookies?\""
    aflippant "\"Total Dinosaur Conquest?\""
    aconfident "Ooh! Ooh! \"Timothy, Don't Creep!\""
    wthink "What about... "
    menu:
        "Say Statement"
        "\"Try Discovering Clues\"?":
            wbase "\"Try Discovering Clues\"?"
        "\"The Decisive Contradiction\"?":
            wbase "\"The Decisive Contradiction\"?"
        "\"Thoroughly Disliking Crimes\"?":
            wbase "\"Thoroughly Disliking Crimes\"?"
    adef "Nice one!"
    wthink "Hm... looks like there's a communications error at 5:58."
    adef "That must be when the power outage happened."
    wthink "Yeah, that would make sense."
    wthink "I'm sure Ms Neering wouldn't mind if we borrowed this for the time being..."
    $ investigation2_cleareditems.append("4")
    ### Logs Added to Inventory

label investigation2_neeringconvo:
    ### Neering Shows Up On Screen
    neering "Who are you and what are you doing in my office?"
    asurprise "W-woah! The TV is talking to us!"
    wbase "Are you Angela Neering?"
    neering "Yes! I'm her and this is my office! So what are you doing in it?"
    wbase "We came to speak with you. We're investigating a murder."
    neering "Fine, but MIQ."
    whattip "I'm sorry... MIQ?"
    neering "{i}Make It Quick?{/i} It's shorthand, you simpleton."
    aconfident "Oh, you mean like \"TGIF\" or \"LOL\"."
    neering "That's a gross oversimplification, but yes."
    neering "I'm an incredibly busy person. I don't have time to go speaking sentences in full, so I abbreviate them."
    wthought "It seems like you waste more time explaining yourself than you would just saying what you meant."
    $ loop = 1
    while loop == 1:
        menu:
            "Smart House":
                whattip "Now, you're the project lead on the Smart House, aren't you?"
                neering "{i}And{/i} lead programmer, {i}and{/i} head of design, yes."
                whattip "The smart house is constantly recording, right? Is there any possibility it captured the murder."
                neering "I'm afraid not. The house only records things in-the-moment. It doesn't actually keep any of the footage."
                wannoy "Of course. That would be too easy."
                if askedHarperAboutMurder = False:
                    athink "But it remembers things, right? Couldn't we ask it what it saw?"
                    neering "I suppose so. Hopefully the power outage didn't corrupt the backup drive."
                if askedHarperAboutMurder = True:
                    wbase "We asked it if it remembers anything about the murder, but it says the backup drive is corrupted."
                    neering "Well, drat. There goes all the data from the tour."
                wbase "Is there anything else you can tell us about the house which could help us out?"
                neering "Hmmm...I could tell you how many lines of code it takes to get the H.A.R.P.E.R AI running."
                wbase "I don't see how that would be partic{nw}"
                neering "One Hundred Million."
                wconfused "Um...is that a large amount? A small amount?"
                neering "Boy, they let just about {i}anyone{/i} be a police officer these days..."

            "Power Outage":
                wbase "Do you know anything about the power outage which occurred around 6 P.M. today?"
                neering "I know it's been a massive thorn in my side."
                neering "The house wasn't built to handle a power outage, so half the systems are on the fritz now."
                neering "I told them, I {i}told them{/i} we needed to be prepared for such a thing, but as usual, NLTOA."
                wconfused "Uh...NLTOA?"
                neering "\"Nobody Listens To Ol' Angela\"."
                neering "Anyway, I'm down in the house's guts right now trying to sort out this mess."
                neering "It's why I couldn't come to speak with you in person."
                neering "Not that I would have, anyways..."
                whattip "Do you have any idea what could have caused the power outage?"
                neering "It would probably be the main breaker."
                neering "If somebody messed with that, they could bring the house down for a while."
                neering "Now is there anything else, or can I get back to my work?"

            "Orin Darsha":
                wbase "You know a man by the name of Orin Darsha, yes?"
                neering "Ugh, yes. He's technically my boss. A small minded fool of a man."
                neering "Why do you ask?"
                wbase "He's dead."
                neering ". . ."
                neering "WELL WHY DIDN'T YOU TELL ME THAT EARLIER? NOW I LOOK LIKE A GRADE-A JERK!"
                wthought "Trust me, lady. You didn't need {i}my{/i} help to do that."
                show warren annoy anim
                wbase "We found him dead in the kitchen of your smart house."
                neering "Great. Just great."
                neering "This is going to completely overshadow the Smart House reveal!"
                neering "Way to mess things up again, Darsha!"
                wthought "Is there a single person on this base with an ounce of human empathy?"
                whattip "Now, I have to ask..."
                whattip "...not that you would answer truthfully anyways..."
                whattip "Did you murder Orin Darsha?"
                neering "Hah! No."
                neering "To murder somebody, you need to have strong feelings about them."
                neering "Darsha may have been an annoyance, but I really didn't think about him all that much."
                neering "Now is there anything else, or can I get back to my work?"
                $ investigation2_cleareditems.append("5")

            "Show Evidence":
                warren "Let me show you something."
                $ current_present = "investigation_2_neering_present"
                show screen present_evidence_screen
                show screen back_button
                pause

            "Show Profile":
                warren "What do you know about this person?"
                $ current_present = "investigation_2_neering_present"
                show screen present_profile_screen
                show screen back_button
                pause

            "Goodbye":
                warren "Thanks for your help."
                neering "Can I get back to my work now?"
                $loop = 0

label investigation2_bedroom:
    adef "What a nice bedroom!"
    wthink "It's larger than the one I have at home."
    adef "That bed is so big and soft looking I could just..."
    # Floomf
    whattip "Do you really want to be lying there? For all we know, that's where the victim was killed."
    asurprise "GYAAAH!"
    aunsure "Do you think I got dead guy on me?"
    wstern "If you did, it's your own fault."
    aannoy "Gross!"

screen sh_investigation2_bedroom:
    modal True
    imagemap:
        ground "bedroom"
        hotspot (X,Y,W,H) action [Hide("sh_investigation2_bedroom"), Jump("investigation2_scratches")]
    use inventory_screen_button
    imagebutton auto "assets/menu/move_%s.png"  xalign 0.5 yalign 1.0 action Jump("inv2_move_bedroom")

label inv2_move_bedroom:
    menu:
        "Smart House - Kitchen":
            hide screen sh_investigation2_bedroom
            jump sh_investigation2_kitchen

        "Smart House - Dressing Contraption" if unlockedContraption == True:
            hide screen sh_investigation2_bedroom
            jump investigation2_thedressingcontraption

        "Base 24 - Neering's Office" if unlockedOffice == True:
            hide screen sh_investigation2_bedroom
            jump investigation2_neeringsoffice

        "Base 24 - Warehouse":
            hide screen sh_investigation2_bedroom
            jump investigation2_chritude

label investigation2_scratches:
    wbase "There are scratch marks in the carpeting down here."
    aposit "You know what that must mean..."
    wbase "Somebody was probably atta{nw}"
    aposit "Chupacabra marks."
    aunsure "I mean, uh, the thing that you said."
    # Show Trap Door CLoseup
    wos "The square foot of carpeting around the scratch marks are wet."
    wos "I wonder if someone was trying to clean up a stain..."
    aos "Wait Randi, look at what the scratch marks are leading to!"
    aos "There's a seam here. It makes a big square shape..."
    aos "Oh my gosh, it's a trapdoor! This house really {i}does{/i} have everything!"
    # Hide Trap Door CLoseup
    wbase "I can't seem to find a handle or a lever anywhere..."
    athink "Knowing this house, it's probably computer controlled."
    wbase "In that case, we'll need the house's AI to open it for us."
    ### Trap Door Added to Inventory

label investigation2_thedressingcontraption:
    asurprise "Wooooaaahh! This place is huge!"
    wthought "How on earth does this fit inside the rest of the house?"

screen sh_investigation2_contraption:
    modal True
    imagemap:
        ground "contraptionShoe"
        hotspot (X,Y,W,H) action [Hide("sh_investigation2_contraption"), Jump("investigation2_missingshoe")]
    use inventory_screen_button
    imagebutton auto "assets/menu/move_%s.png"  xalign 0.5 yalign 1.0 action Jump("inv2_move_contraption")

label inv2_move_contraption:
    menu:
        "Smart House - Kitchen":
            hide screen sh_investigation2_contraption
            jump sh_investigation2_kitchen

        "Smart House - Bedroom":
            hide screen sh_investigation2_contraption
            jump investigation2_bedroom

        "Base 24 - Neering's Office" if unlockedOffice == True:
            hide screen sh_investigation2_contraption
            jump investigation2_neeringsoffice

        "Base 24 - Warehouse":
            hide screen sh_investigation2_contraption
            jump investigation2_chritude

label investigation2_missingshoe:
    aflippant "Looks like The Dressing Contraption didn't dress someone up all the way!"
    aflippant "See? It dropped a shoe!"
    wthink "Wait a minute...a shoe?"
    wthink "Wasn't there a shoe we were looking for?"
    $ current_present = "investigation_2_shoe_present"
    show screen present_evidence_screen
    pause

label investigation_2_shoe_present:
    if present_response == "missingshoe":
        wbase "That's right... Orin Darsha's body was missing a shoe when we found it."
        wbase "Ash, show me that photo you took of him..."
        ### Show Body Photo
        wos "There's no doubt about it... it's the same shoe."
        aos "So that means... Mr Darsha was in here some time today?"
        wos "I can't think of another way this shoe could have found its way here."
        ### Hide Body Photo
        adef "During the tour, our guide let somebody test out the Dressing Contraption..."
        athink "But it wasn't Mr Darsha who volunteered."
        athink "When did he have time to run through the whole thing?"
        wthink "And why?"
        ### Missing Shoe Updated
        $ investigation2_cleareditems.append("6")

    else:
        wconfused "Wait, that wasn't it..."
        aflippant "Come on, Randi. Even {i}I{/i} know what you're talking about!"
        wbase "Okay, let's try this again..."
        wbase "Wasn't there a shoe we were looking for?"
        show screen present_evidence_screen
        pause

screen sh_investigation2_warehouse:
    modal True
    imagemap:
        ground "contraptionShoe"
        hotspot (X,Y,W,H) action [Hide("sh_investigation2_warehouse"), Jump("investigation2_chritude")]
    use inventory_screen_button
    imagebutton auto "assets/menu/move_%s.png"  xalign 0.5 yalign 1.0 action Jump("inv2_move_warehouse")

label inv2_move_warehouse:
    menu:
        "Smart House - Kitchen":
            hide screen sh_investigation2_warehouse
            jump sh_investigation2_kitchen

        "Smart House - Bedroom" if unlockedBedroom == True:
            hide screen sh_investigation2_warehouse
            jump investigation2_bedroom

        "Smart House - Dressing Contraption" if unlockedContraption == True:
            hide screen sh_investigation2_warehouse
            jump investigation2_thedressingcontraption

        "Base 24 - Neering's Office" if unlockedOffice == True:
            hide screen sh_investigation2_warehouse
            jump investigation2_neeringsoffice

label investigation2_chritude:
    "good writing here"
    $ investigation2_cleareditems.append("7")

label investigation2_bottomiawakens:
    show mir default
    show drang default gup
    ddef_gup "Hey, assistant."
    ddef_gup "While you were off galavanting on your own, our main suspect finally woke up."
    whattip "You mean Mr Bottomi?"
    dangry_gup "No, the {i}other{/i} main suspect. Come on!"
    ddef_gup "Your forensics monkey is over there attending to him."
    ddef_gup "How about we finish up that cross examination, huh?"
    dangry_gup "Any longer down here and I'm going to have to book some nasty hotel."
    hide drang
    show bottomi standard
    wholdon "Mr Bottomi. Are you alright?"
    bfuzzy "I... I think so..."
    bfuzzy "H-how long was I out?"
    cser "Approximately thirty minutes."
    cser "I'm going to be honest: you may have brain damage."
    cser "You should probably go see a doctor when you get a chance."
    cdef "I mean, a doctor besides me."
    whattip "Now, do you mind telling us exactly what that is on your head?"
    bapology "You mean my hat? Wait..."
    bfreak "Aah! My hat! You weren't supposed to see this!"
    if mentionedhardware:
        whattip "Is it safe to assume this is the \"hardware\" you mentioned earlier?"
        bdef "Y...{nw}"
        bsad "Y... {fast}yeah. This is it."
    else:
        warren "Would this peculiar headgear have anything to do with the trial you were participating in?"
        bdef "Y...{nw}"
        bsad "Y...{fast}yeah. It is."
    bsad "Nobody outside of the base is supposed to know about this..."
    bsad "But I guess it's too late for that, huh?"
    bdef "This is what I've been helping to test here at the base."
    bdef "It's an experimental {color=red}neural implant{/color} designed for psychically transferring information."
    bdef "It lets me send and receive data wirelessly from my brain to a computer."
    bdef "I don't fully know all the technical detai{nw}"
    ## White Flash
    bfreak "AAH!"
    ## Ash holding camera
    apsyched "This is absolutely incredible! Real life technopathy!"
    apsyched "The occultism forums are going to go wild when they hear about this!"
    bapology "Good luck. The base is probably gonna make you sign an NDA before they let you leave."
    bapology "They'll probably confiscate the photo, too."
    aannoy "Rats..."
    wthought "And to think, the thing he was dead set on hiding from us was right there the whole time."
    wbase "So, now that the cat is out of the bag..."
    wstern "Are there any other secrets you'd like to share with us?"
    bapology "No, I don't thi-- {nw}"
    bfreak "No, I don't thi-- {fast}NNNGH!!"
    bremember "Actually, there is, come to think of it."
    bdef "You might have noticed that my recollection of events has been a little shaky..."
    aflippant "Yeah, no kidding..."
    bdef "Well, the reason is that I've been lying to you about one important detail."
    bdef "I didn't actually kill Orin Darsha..."
    bdef "I made the house do it for me."
    show black with dissolve
    jump smart_house_act_4_intro
