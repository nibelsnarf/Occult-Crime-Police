label smart_house_act_3_intro:
    scene act3 with fade
    $ save_name = "Act 3"
    $bHat = 2
    $askedHarperAboutMurder = False
    $renpy.stop_predict("sprites/Bottomi*.*")
    pause 3.0
    show black with dissolve
    typing "September 13th. 9:02 P.M.\nSmart House - Kitchen"
    scene kitchenact3B with dissolve
    show screen inventory_screen_button
    show drang think gdown
    with dissolve
    dthink_gdown "Well, well, well..."
    dthink_gdown "It looks like this case just got interesting..."
    show ash annoyed
    aannoy "How has this case {i}not{/i} been interesting up until this point?"
    djacket_pop "You see a lot of strange things on the job, kid. It takes a lot to catch one's interest."
    aannoy "The crime scene is a revolutionary piece of technology!"
    aannoy "The main suspect keeps lying in order to prove his own guilt!"
    aannoy "If anything, a weird chip in a guy's head is the {i}least{/i} peculiar thing we've seen today!"
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
    scene kitchenact3BC
    show mir thinking
    hide car
    with dissolve
    cos "Aw yeah. Relaxation time with my good unconscious friend down here."
    cos "Hey, want a drink, buddy?"
    cos "Just kidding. Looks like you've had one too many already."
    show mir annoy anim
    wos "* sigh *"
    wbase "Ash, are you coming?"
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
    scene kitchenact3BCD
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
    $unlockedBedroom = True
    $paulLied = False
    $visitedOffice = False
    $visitedBedroom = False
    $visitedHarper = False
    $visitedPaul = False
    $visitedTDC = False
    $paulSecret = False
    $persuasionComplete = False
    play music "music/Investigation_Spookier.ogg" fadein 1.0
    scene kitchenact3BCD
    jump sh_investigation2_kitchen

label sh_investigation2_kitchen:
    if "1" in investigation2_cleareditems and "2" in investigation2_cleareditems and "3" in investigation2_cleareditems and "4" in investigation2_cleareditems and "5" in investigation2_cleareditems and "6" in investigation2_cleareditems and "7" in investigation2_cleareditems:
        jump investigation2_bottomiawakens
    scene kitchenact3BCD with dissolve
    show screen sh_investigation2_kitchen
    pause

screen sh_investigation2_kitchen:
    modal True
    imagemap:
        ground "kitchenact3BCD"
        hotspot (1,1,1920,1080) action [Hide("sh_investigation2_kitchen"), Jump("investigation2_further")]
        hotspot (1412,386,85,100) action [Hide("sh_investigation2_kitchen"), Jump("investigation2_houseconvo")]
        hotspot (450,209,200,483) action [Hide("sh_investigation2_kitchen"), Jump("investigation2_drangconvo")]
        hotspot (300,640,260,177) action [Hide("sh_investigation2_kitchen"), Jump("investigation2_darsha")]
        hotspot (1000,540,510,477) action [Hide("sh_investigation2_kitchen"), Jump("investigation2_carlos")]
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
            jump investigation2_warehouse

        "Base 24 - Neering's Office" if unlockedOffice == True:
            hide screen sh_investigation2_kitchen
            jump investigation2_neeringsoffice


label investigation2_houseconvo:
    show ash standard at flip
    show mir default
    with dissolve
    if visitedHarper == True:
        show har deploy at flip
        hos "Hello, User Miranda."
    if visitedHarper == False:
        asurprise "Hey, look at that little touchscreen!"
        aannoy "How did we miss that the first time we looked around?"
        wbase "Well, Agent Drang was standing there earlier. He blocked our line of sight to it."
        adef "I think it's a control panel for the Smart House."
        aposit "So I bet if I push this button..."
        show har deploy at flip
        asurprise "Woah!"
        wconfused "What the...?"
        hunk "New Users Detected. Please State Your Name."
        wconfused "Uh, Miranda Warren."
        aflippant "Butt Stevenson."
        wangry "Ash!"
        hunk "Profiles Created. Welcome, Miranda Warren, and, Butt Stevenson."
        aconfident "Hah hah..."
        aconfident "Nice."
        hunk "I Am Home Automated Routinely Performing Errand Robot, Or H.A.R.P.E.R."
        $profile.add(harper)
        $visitedHarper = True
    $loop = 1
    hbase "How Can I Help You Today?"
    while loop == 1:
        menu:
            "Smart House":
                whattip "So, what are you exactly?"
                show har wave at flip
                hos "I Am An Artificial Intelligence Designed To Make Your Life Easier."
                hbase "I Can Provide A Number Of Services Pertaining To Everyday Life."
                hbase "I Can Cook And Clean, I Can Move Heavy Objects, I Can Search The Internet For Various Things."
                hbase "I Can Respond To Requests Made Of Me, And Can Learn From Previous Experiences."
                adef "Can you tell knock-knock jokes?"
                show har turn at flip
                hos "I Have Over Ten Thousand Knock-Knock Jokes In My Database."
                wannoy "Please don't demonstrate."
                show har yes at flip
                hos "Understood."
                wbase "Harper, tell me who made you."
                show har yes at flip
                hos "I Am A Co-Production Of United States Government And The Burchfield Manufacturing Corporation."
                whattip "No, I mean, who is your inventor? Who is in charge of the project which created you?"
                hbase "That Would Be User Zero. Her Name Is Angela Neering."
                $profile.add(neeringunk)
                wthink "Angela Neering... does she work here at the base?"
                hno "I Am Not Sure. I Have Limited Knowledge Of Happenings Outside Of My Walls."
                show har yes at flip
                hos "However, If This Base You Speak Of Is Where I Was Built, Then It Is Likely That User Zero Works Here."
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
                show har yes at flip
                hos "Understood."
                $investigation2_cleareditems.append("1")
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
                hide mir
                hide ash
                hide har
                with dissolve
                $loop = 0
                call sh_investigation2_kitchen from sh_investigation2_kitchen_1

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
    if present_response == "trapdoor":
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
        jump investigation2_houseconvo

    if present_response == "Back":
        wbase "On second thought, never mind."
        jump investigation2_houseconvo

    else:
        hno "I'm Sorry. I Do Not Have A Record Of That."
        hbase "If You Feel This Is An Error, Please Send A Bug Report To feedback@base24.gov"
        jump investigation2_houseconvo

label investigation2_drangconvo:
    show mir default
    show ash standard at flip
    with dissolve
    adef "Should we ask Mister Hotshot Agent any questions about the case?"
    wbase "Not right now. He looks pretty busy trying to open that fridge."
    hide mir
    hide ash
    with dissolve
    dos "Open Fridge."
    dos "Open! Fridge!" with smallshake
    dos "{b}OPEN UP THE FRIDGE!{/b}" with shake
    show mir default
    show ash standard at flip
    with dissolve
    adef "Should we tell him that refrigerator isn't voice-activated?"
    wbase "I'm sure he'll figure it out himself."
    wbase "...Eventually."
    hide mir
    hide ash
    call sh_investigation2_kitchen from sh_investigation2_kitchen_2

label investigation2_darsha:
    wthought "I think I've gotten everything I could off of the body..."
    wthought "I'll just leave it be for the time being."
    call sh_investigation2_kitchen from sh_investigation2_kitchen_3

label investigation2_carlos:
    scene kitchenact3BD
    show mir default
    show car serious at flip
    with dissolve
    wbase "Hey Tsukada, how's Mister Bottomi holding up?"
    cser "Still breathing, at least."
    wbase "Any chance he's going to wake up soon?"
    cser "No, I don't think that he -{nw}"
    cagit "No, I don't think that he -{fast} Wait!"
    wholdon "!"
    cagit "He's doing something!"
    cos ".   .   .   .   ."
    cthink "Sorry, false alarm. Just muscle spasms."
    wannoy "* sigh *"
    cser "Yeah, this might be a while."
    cser "You go on ahead. I'll keep an eye on him."
    hide mir
    hide car
    scene kitchenact3BCD
    with dissolve
    call sh_investigation2_kitchen from sh_investigation2_kitchen_4

label investigation2_further:
    wthought "I don't think that requires further investigation."
    call sh_investigation2_kitchen from sh_investigation2_kitchen_5

label investigation2_neeringsoffice:
    scene OfficeDark
    with dissolve
    if visitedOffice == False:
        typing "September 13th.\nBase 24 - Neering's Office"
        pause 0.5
        show mir default
        show ash standard at flip
        with dissolve
        show screen inventory_screen_button
        wbase "This should be the place."
        aflippant "I sure hope so."
        aflippant "This is like the fifth office we've barged in on."
        wbase "Well, it looks like Ms Neering isn't even here."
        apsyched "Perfect!{w=0.1} Time to do some snooping!"
        wannoy "Ash,{w=0.1} we aren't going to do any snooping, all right?"
        whattip "Although,{w=0.2} if we take a quick look around while waiting for Ms Neering..."
        apsyched "Snoo!{w=0.1} Ping!{w=0.1} Snoo!{w=0.1} Ping!{w=0.1} Snoo!{w=0.1} Ping!"
        wangry "All right, all right!{w=0.1} Call it snooping if you really want to!"
        aconfident "Heh heh heh!"
        aannoy "Man,{w=0.1} can we get some light in here?"
        whattip "I don't see any switches in here..."
        aposit "Maybe it's automated."
        aconfident "Turn On Lights!"
        hos "Administrative Access Required.{w=0.1} User Zero Not Detected."
        aannoy "Aw, come on,{w=0.1} Harper!{w=0.1} Be a pal!"
        wbase "Looks like we're going to have to do some exploring in the dark."
        hide mir
        hide ash
        with dissolve
        $ visitedOffice = True
    if "3" in investigation2_cleareditems and "4" in investigation2_cleareditems:
        if "5" in investigation2_cleareditems:
            show screen sh_investigation2_office
            pause
        else:
            jump investigation2_neeringconvo
    else:
        show screen sh_investigation2_office
        pause

screen sh_investigation2_office:
    modal True
    imagemap:
        ground "OfficeDark"
        hotspot (1,1,1920,1080) action [Hide("sh_investigation2_office"), Jump("investigation2_etc")]
        hotspot (1334,518,100,100) action [Hide("sh_investigation2_office"), Jump("investigation2_emails")]
        hotspot (550,712,490,95) action [Hide("sh_investigation2_office"), Jump("investigation2_securitylogs")]
        hotspot (314,620,220,200) action [Hide("sh_investigation2_office"), Jump("investigation2_books1")]
        hotspot (1564,864,100,100) action [Hide("sh_investigation2_office"), Jump("investigation2_books2")]
        hotspot (1,1,450,600) action [Hide("sh_investigation2_office"), Jump("investigation2_poster")]
        hotspot (550,812,490,170) action [Hide("sh_investigation2_office"), Jump("investigation2_papers")]
        hotspot (600,1,1300,450) action [Hide("sh_investigation2_office"), Jump("investigation2_screens")]
        hotspot (1565,380,190,260) action [Hide("sh_investigation2_office"), Jump("investigation2_lamp")]
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
            jump investigation2_warehouse

label investigation2_emails:
    show mir default
    show ash standard at flip
    with dissolve
    aposit "Hey, it looks like {i}somebody{/i} left their email open!"
    wthink "All right, I can tolerate a little snooping, but reading private emails is just too far."
    aposit "Even private emails received from {color=#FF9966}Mr. Darsha?{/color}"
    wangry "What?{w=0.1} Let me see!" with shake
    show neeringEmail with dissolve
    wos "Hm... it looks like there was some friction between Ms Neering and the victim over the state of the house."
    aos "Isn't that just the way..."
    aos "The creative type wants to take their time on the project while the higher-ups want to kick it out the door as soon as possible."
    wos "Is that... something you have experience with?"
    aos "No, but I watch a lot of Making-Of documentaries."
    hide neeringEmail with dissolve
    wthink "I've got a feeling this exchange is important."
    wbase "Ash, could you take a picture of t{nw}"
    show ash camera at flip
    show Ash_Camera_Polaroid at flip
    call flash from _call_flash
    acam "Way ahead of you."
    $inventory.add(email)
    typing "Neering's Email Added to Evidence"
    $ investigation2_cleareditems.append("3")
    hide mir
    hide ash
    hide Ash_Camera_Polaroid
    with dissolve
    call investigation2_neeringsoffice from _call_investigation2_neeringsoffice_1

label investigation2_securitylogs:
    show mir default
    show ash standard at flip
    with dissolve
    adef "Hey, check it out, it's one of those zig-zag printers they use for earthquakes and stuff!"
    adef "I love those \"Preeeow\" noises they make."
    wthink "Let me see that..."
    wos ". . ."
    wbase "Looks like Ms Neering has a printer set up to log feedback from the house's operating system."
    wbase "Things like system functionality and user inputs."
    adef "Hey, check the log from between 5 and 6!"
    aposit "Maybe the house logged somebody saying \"I'm gonna murder you!\""
    wthink "We should be so lucky..."
    show thePaper with dissolve
    wos "Most of this is programmer gobbeldygook, but I can make out some of it."
    wos "It shows \"Tour Mode\" ending at 5:30..."
    wos "Was Mr. Darsha with your group through the whole tour?"
    aos "I think so... he was hanging around near the back."
    wos "So he died some time between then and 6 P.M."
    wos "Odd... somebody disabled the safety protocols at 5:51."
    wos "I wonder how many people have the authority to do something like that?"
    hide thePaper with dissolve
    wbase "Hm. Look at this. At 5:52 it says \"TDC Subroutine Activated.\""
    athink "What do you think TDC stands for?"
    aposit "\"Terribly{w=0.1} Dangerous{w=0.1} Cookies?\""
    aflippant "\"Total{w=0.1} Dinosaur{w=0.1} Conquest?\""
    apsyched "Ooh! Ooh! \"Timothy,{w=0.1} Don't Creep!\""
    wthink "What about... "
    menu:
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
    hide mir
    hide ash
    with dissolve
    $inventory.add(logs)
    typing "Feedback Logs Added to Evidence"
    call investigation2_neeringsoffice from _call_investigation2_neeringsoffice_2


label investigation2_books1:
    wthought "There's a stack of books on this table. They look to be computer programming manuals."
    wthought "\"3-B File Structuring\"..."
    wthought "\"Guide To Raskal Programming Style\"..."
    wthought "\"Date Saving in Assembly\"..."
    wthought "\"F.I.T.E. Class Compiling\"..."
    wthought "\"Bear's Guide to Artificial Intelligence\"..."
    wthought "\"Getting Through The Woods: Data Trees and You\"..."
    wthought "I can't even begin to imagine what any of this means..."
    call investigation2_neeringsoffice from _call_investigation2_neeringsoffice_3

label investigation2_books2:
    wthought "There's more computer programming manuals over here."
    wthought "\"Hook Up with Keyboard Event Hooks\"..."
    wthought "\"Fowl Play: A Guide to Rubber Duck Programming\"..."
    wthought "\"Achieving Syntax Harmony\"..."
    wthought "It's all Greek to me. Or perhaps Python..."
    call investigation2_neeringsoffice from _call_investigation2_neeringsoffice_4

label investigation2_poster:
    wthought "There's a big poster hanging here that just says \"Science\" on it."
    wthought "Seems like you could come up with a better slogan than that..."
    call investigation2_neeringsoffice from _call_investigation2_neeringsoffice_5

label investigation2_papers:
    wthought "There are papers strewn all about the office."
    wthought "They're filled to the brim with scrawled equations and diagrams."
    wthought "I can't understand any of it..."
    wthought "Except for this one note here in the margins, which says,"
    wthought "\"New Idea: Religion for Dogs? Must consider further.\""
    wthought "I assume this one was written {i}very{/i} late at night."
    call investigation2_neeringsoffice from _call_investigation2_neeringsoffice_6

label investigation2_screens:
    show mir default
    show ash standard at flip
    with dissolve
    wbase "Who on earth could possibly need all these screens?"
    wthink "Heck, who needs more than {i}one{/i} screen?"
    adef "Are you kidding? I've got no more than three screens running at all times, usually."
    wconfused "What are you even doing with all of them?"
    aposit "Well, I've got my main screen for video games..."
    aposit "Another screen is for having a TV show on in the background..."
    aposit "And then on the last one I'm chatting with my friends."
    wthought "I'm astounded you don't melt your brain with all that stimuli!"
    hide mir
    hide ash
    with dissolve
    call investigation2_neeringsoffice from _call_investigation2_neeringsoffice_7

label investigation2_lamp:
    show mir default
    show ash standard at flip
    with dissolve
    adef "Hey, let's try turning on this lamp!"
    aos ". . . . ."
    aannoy "Are you kidding? This switch doesn't work!"
    wthought "I guess Harper controls the power on all of this..."
    hide mir
    hide ash
    with dissolve
    call investigation2_neeringsoffice from _call_investigation2_neeringsoffice_8

label investigation2_etc:
    wthought "Nothing interesting here..."
    call investigation2_neeringsoffice from _call_investigation2_neeringsoffice_9

label investigation2_neeringconvo:
    hide OfficeDark
    scene OfficeLighted
    show mir holdon
    show ash surprised at flip
    call flash from _call_flash_1
    nos "Who are you and what are you doing in my office?"
    asurprise "W-woah! The TV is talking to us!"
    wbase "Are you Angela Neering?"
    nos "Yes! I'm her and this is my office! So what are you doing here?"
    $profile.drop(neeringunk)
    $profile.add(neering)
    wbase "We came to speak with you. We're investigating a murder."
    wbase "I'm Sheriff Miranda Warren and this is my associate, Ash Jager."
    wbase "Do you mind if we ask you a few questions?"
    nos "Fine, but MIQ."
    whattip "I'm sorry... MIQ?"
    nos "{i}Make It Quick?{/i} It's shorthand, you simpleton."
    aflippant "Oh, you mean like \"TGIF\" or \"LOL\"."
    nos "That's a gross oversimplification, but yes."
    nos "I'm an incredibly busy person. I don't have time to go speaking sentences in full, so I abbreviate them."
    wthought "It seems like you waste more time explaining yourself than you would just saying what you meant."
label meeting_neering_conversation:
    $ meeting_neering_cleared_items = []
    $ meeting_neering_cleared = False

    while meeting_neering_cleared == False:
        menu:
            "Smart House":
                whattip "Now, you're the project lead on the Smart House, aren't you?"
                nos "{i}And{/i} lead programmer, {i}and{/i} head of design, yes."
                whattip "I've heard the smart house is constantly recording. Is there any possibility it captured the murder?"
                nos "I'm afraid not. The house only records things in-the-moment. It doesn't actually keep any of the footage."
                wannoy "Of course. That would be too easy."
                if askedHarperAboutMurder == False:
                    athink "But it remembers things, right? Couldn't we ask it what it saw?"
                    nos "I suppose so. You better hope the power outage didn't corrupt the backup drive."
                if askedHarperAboutMurder == True:
                    wbase "We asked it if it remembers anything about the murder, but it says the backup drive is corrupted."
                    nos "Well, drat. There goes all the data from the tour."
                wbase "Is there anything else you can tell us about the house which could help us out?"
                nos "Hmmm...I could tell you how many lines of code it takes to get the HARPER A.I. running."
                wbase "I don't see how that would be partic{nw}"
                nos "One Hundred Million."
                wconfused "Um...is that a large amount? A small amount?"
                nos "Boy, they let just about {i}anyone{/i} be a police officer these days..."
                $ meeting_neering_cleared_items.append("1")

            "Power Outage":
                wbase "Do you know anything about the power outage which occurred around 6 P.M. today?"
                nos "I know it's been a massive thorn in my side."
                nos "The house wasn't built to handle a power outage, so half the systems are on the fritz now."
                nos "I told them, I {i}told them{/i} we needed to be prepared for such a thing, but as usual, NLTOA."
                wconfused "Uh...NLTOA?"
                nos "\"Nobody Listens To Ol' Angela\"."
                nos "Anyway, I'm down in the house's guts right now trying to sort out this mess."
                nos "It's why I couldn't come to speak with you in person."
                nos "Not that I would have, anyways..."
                whattip "Do you have any idea what could have caused the power outage?"
                nos "It would probably be the main breaker."
                nos "If somebody messed with that, they could bring the whole house down for at least a little while."
                $ meeting_neering_cleared_items.append("2")

            "Orin Darsha":
                wbase "You know a man by the name of Orin Darsha, yes?"
                nos "Ugh, yes. He's technically my boss. A small minded fool of a man."
                nos "Why do you ask?"
                wbase "He's dead."
                nos ". . ."
                nos "WELL WHY DIDN'T YOU TELL ME THAT EARLIER?{w=0.1} NOW I LOOK LIKE A GRADE-A JERK!" with shake
                show mir annoy anim
                wthought "Trust me, lady. You didn't need {i}my{/i} help to do that."
                wbase "We found him dead in the kitchen of your smart house."
                nos "Great.{w=0.1} Just great."
                nos "This is going to completely overshadow the Smart House reveal!"
                nos "Way to mess things up again, Darsha!"
                wthought "Is there a single person on this base with an ounce of human empathy?"
                whattip "Now, I have to ask..."
                whattip "...not that you would answer truthfully anyways..."
                whattip "Did you murder Orin Darsha?"
                nos "Hah!{w=0.1} No."
                nos "To murder somebody, you need to have strong feelings about them."
                nos "Darsha may have been an annoyance, but I really didn't think about him all that much."
                $ meeting_neering_cleared_items.append("3")

        if "1" in meeting_neering_cleared_items and "2" in meeting_neering_cleared_items and "3" in meeting_neering_cleared_items:
            $meeting_neering_cleared = True
            $investigation2_cleareditems.append("5")

    nos "Now is there anything else, or can I get back to my work?"
    wthink "Hmm... I suppose that's it for now."
    whattip "How can I get in contact with you for any further questions?"
    nos "You can't.{w=0.2} I'm busy."
    nos "Please get out of my office now."
    wangry "Well, hold on one gosh-dar{nw}"
    scene OfficeDark
    call flash from _call_flash_2
    pause 1.0
    with dissolve
    show ash standard at flip
    adef "Well...{w=0.2} she was rude."
    wbase "I'll say."
    hide mir
    hide ash
    with dissolve
    call investigation2_neeringsoffice from _call_investigation2_neeringsoffice_10


label investigation2_bedroom:
    scene bedroom
    with dissolve
    if visitedBedroom == False:
        typing "September 13th\nSmart House - Bedroom"
        show mir default
        show ash standard at flip
        with dissolve
        adef "What a nice bedroom!"
        adef "That bed is so big and soft looking I could just..."
        hide ash with dissolve
        typing "* floomf *"
        whattip "Do you really want to be lying there? For all we know, that's where the victim was killed."
        show ash surprised at flip
        asurprise "GYAAAH!" with smallshake
        aunsure "Do you think I got dead guy on me?"
        wbase "If you did, it's your own fault."
        aunsure "Gross!"
        hide mir
        hide ash
        with dissolve
        $ visitedBedroom = True
    show screen sh_investigation2_bedroom
    pause

screen sh_investigation2_bedroom:
    modal True
    imagemap:
        ground "bedroom"
        hotspot (1,1,1920,1080) action [Hide("sh_investigation2_bedroom"), Jump("investigation2_nothing")]
        hotspot (50,860,740,220) action [Hide("sh_investigation2_bedroom"), Jump("investigation2_scratches")]
        hotspot (1,1,1100,700) action [Hide("sh_investigation2_bedroom"), Jump("investigation2_window")]
        hotspot (1,300,740,300) action [Hide("sh_investigation2_bedroom"), Jump("investigation2_teevee")]
        hotspot (1500,400,100,100) action [Hide("sh_investigation2_bedroom"), Jump("investigation2_famphoto")]
        hotspot (1420,560,120,200) action [Hide("sh_investigation2_bedroom"), Jump("investigation2_lamps")]
        hotspot (910,500,120,160) action [Hide("sh_investigation2_bedroom"), Jump("investigation2_lamps")]
        hotspot (1700,100,140,900) action [Hide("sh_investigation2_bedroom"), Jump("investigation2_lamps")]
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
            jump investigation2_warehouse

label investigation2_scratches:
    show mir default
    show ash standard at flip
    with dissolve
    wbase "There are scratch marks in the carpeting down here."
    aposit "You know what that must mean..."
    wbase "Somebody was probably atta{nw}"
    aposit "Chupacabra marks."
    asurprise "I mean, uh, the thing that you said."
    show TrapDoor with dissolve
    wos "The square foot of carpeting around the scratch marks are wet."
    wos "I wonder if someone was trying to clean up a stain..."
    aos "Wait Randi, look at what the scratch marks are leading to!"
    aos "There's a seam here. It makes a big square shape..."
    aos "Oh my gosh, it's a trapdoor! This house really {i}does{/i} have everything!"
    hide TrapDoor with dissolve
    wbase "I can't seem to find a handle or a lever anywhere..."
    athink "Knowing this house, it's probably computer controlled."
    wbase "In that case, we'll need the house's AI to open it for us."
    $inventory.add(trapdoor)
    typing "Trap Door Added to Evidence"
    hide mir
    hide ash
    with dissolve
    call investigation2_bedroom from _call_investigation2_bedroom_1

label investigation2_teevee:
    show screen inventory_screen_button
    wthought "A TV that comes down from the ceiling?"
    wthought "Finally, the American Dream has been realized."
    call investigation2_bedroom from _call_investigation2_bedroom_2

label investigation2_famphoto:
    show mir default
    show ash standard at flip
    with dissolve
    adef "Aww, look at this cute family photo!"
    adef "They look so happy!"
    wbase "Considering this is a model home, I'm pretty sure that's just a stock photo."
    show ash surprised at flip
    wbase "Those people are just actors."
    asad ".....They're still real to me, darn it!"
    hide mir
    hide ash
    with dissolve
    call investigation2_bedroom from _call_investigation2_bedroom_3

label investigation2_window:
    wthought "There's a massive window through which you can see the warehouse."
    wthought "I wonder where Mister Bottomi goes for his tests?"
    call investigation2_bedroom from _call_investigation2_bedroom_4

label investigation2_lamps:
    wthought "No switches on any of these lamps."
    wthought "They must all be controlled by the house."
    call investigation2_bedroom from _call_investigation2_bedroom_5

label investigation2_nothing:
    wthought "Eh, nothing unusual there."
    call investigation2_bedroom from _call_investigation2_bedroom_6


label investigation2_thedressingcontraption:
    scene TDC with dissolve
    if visitedTDC == False:
        show mir default
        show ash surprised at flip
        with dissolve
        asurprise "Wooooaaahh! This place is huge!"
        wthought "How on earth does this fit inside the rest of the house?"
        hide mir
        hide ash
        with dissolve
        $visitedTDC = True
    show screen sh_investigation2_contraption with dissolve
    pause

screen sh_investigation2_contraption:
    modal True
    imagemap:
        ground "TDC"
        hotspot (1,1,1920,1080) action [Hide("sh_investigation2_contraption"), Jump("investigation2_helpverymuch")]
        hotspot (1040,850,130,100) action [Hide("sh_investigation2_contraption"), Jump("investigation2_missingshoe")]
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
            jump investigation2_warehouse

label investigation2_missingshoe:
    if "6" in investigation2_cleareditems:
        wthought "That's where we found Orin Darsha's missing shoe."
        wthought "We already picked it up, though, so there's nothing there anymore."
        call investigation2_thedressingcontraption from _call_investigation2_thedressingcontraption_1
    show mir default
    show ash flippant at flip
    with dissolve
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
        wbase "Ash, show me that photo you took..."
        show victimbody with dissolve
        wos "There's no doubt about it... it's the same shoe."
        aos "So that means... Mr. Darsha was in here some time today?"
        wos "I can't think of another way this shoe could have found its way here."
        hide victimbody with dissolve
        adef "During the tour, our guide let somebody test out the Dressing Contraption..."
        athink "But it wasn't Mr. Darsha who volunteered."
        athink "When did he have time to run through the whole thing?"
        wthink "And why?"
        $inventory.add(shoe)
        $inventory.drop(missingshoe)
        typing "Missing Shoe Updated"
        $ investigation2_cleareditems.append("6")
        hide mir
        hide ash
        with dissolve
        call investigation2_thedressingcontraption from _call_investigation2_thedressingcontraption_2

    else:
        wconfused "Wait, that wasn't it..."
        aflippant "Come on, Randi. Even {i}I{/i} know what you're talking about!"
        wbase "Okay, let's try this again..."
        wbase "Wasn't there a shoe we were looking for?"
        show screen present_evidence_screen
        pause

label investigation2_helpverymuch:
    wthought "I don't think this is going to aid in the investigation very much."
    call investigation2_thedressingcontraption from _call_investigation2_thedressingcontraption_3

label investigation2_warehouse:
    scene basewarehousepaul with dissolve
    $renpy.start_predict("sprites/Chritude*.*")
    show screen sh_investigation2_warehouse
    pause

screen sh_investigation2_warehouse:
    modal True
    imagemap:
        ground "basewarehousepaul"
        hotspot (1,1,1920,1080) action [Hide("sh_investigation2_warehouse"), Jump("investigation2_toobig")]
        hotspot (1220,666,100,200) action [Hide("sh_investigation2_warehouse"), Jump("investigation2_chritude")]
        hotspot (560,666,80,140) action [Hide("sh_investigation2_warehouse"), Jump("investigation2_breaker")]
    use inventory_screen_button
    imagebutton auto "assets/menu/move_%s.png"  xalign 0.5 yalign 1.0 action Jump("inv2_move_warehouse")

label inv2_move_warehouse:
    menu:
        "Smart House - Kitchen":
            hide screen sh_investigation2_warehouse
            jump sh_investigation2_kitchen
            $renpy.stop_predict("sprites/Chritude*.*")

        "Smart House - Bedroom" if unlockedBedroom == True:
            hide screen sh_investigation2_warehouse
            jump investigation2_bedroom
            $renpy.stop_predict("sprites/Chritude*.*")

        "Smart House - Dressing Contraption" if unlockedContraption == True:
            hide screen sh_investigation2_warehouse
            jump investigation2_thedressingcontraption
            $renpy.stop_predict("sprites/Chritude*.*")

        "Base 24 - Neering's Office" if unlockedOffice == True:
            hide screen sh_investigation2_warehouse
            jump investigation2_neeringsoffice
            $renpy.stop_predict("sprites/Chritude*.*")

label investigation2_breaker:
    show screen inventory_screen_button
    if persuasionComplete == True:
        jump investigation2_socket
    if "5" in investigation2_cleareditems:
        wthought "Looks like the main circuit breaker for the whole house."
        wthought "Ms Neering said that this is probably what was tampered with to cause the power outage..."
        wthought "Unfortunately, I don't know how I could find proof of such a thing."
    else:
        wthought "Looks like the main circuit breaker for the house."
        wthought "I wonder if somebody could have tampered with it to cause the power outage..."
        wthought "Unfortunately, I don't know how I could find proof of such a thing."
    call investigation2_warehouse from _call_investigation2_warehouse_1


label investigation2_socket:
    show screen inventory_screen_button
    show mir default
    show ash positing at flip
    with dissolve
    aposit "Here's an idea..."
    aposit "If Paul's glitter is what caused the power outage..."
    adef "...maybe some of it ended up in the fuse box!"
    wbase "That's...not a bad theory!"
    hide mir
    hide ash
    scene FuseBoxOpen
    with dissolve
    aos "Let's open this thing up!"
    aos "Yeah, I think there's something stuck in here!"
    aos "Lemme see if I can clear some of it out."
    typing "Blow on the mic to clear out the glitter!{w=5.0}{nw}"
    typing "Nah, just kidding."
    show GlitterPuff at top
    scene FuseBoxGlitter with dissolve
    aos "PPPFFFFFFTTTT"
    aos "Hey! There we go!"
    wos "\"Master Style\" can't possibly explain this away."
    wos "Ash, can you snap a photo of thi{nw}"
    call flash from _call_flash_3
    aos "There we go!"
    aos "Oh, sorry if that was a little bright."
    wos "Don't worry about it."
    wthought "I've learned to keep my eyes closed at this point."
    $inventory.add(glitter)
    call investigation2_warehouse from _call_investigation2_warehouse_2

label investigation2_chritude:
    show mir default
    show chritude standard at flip
    with dissolve
    if visitedPaul == False:
        pdef "Ah, miss lady cop!"
        wbase "Mr. Chritude..."
        pconceited "Oh, please, Mr. Chritude was my father! Call me Master Style."
        wbase ".{w=0.1} .{w=0.1} .{w=0.2} No."
        whattip "Now, do you have some time to speak with us?"
        pdef "Oh, it's no problem at all. I was just working on my Fake Apology."
        wannoy "Your...{i}fake apology?{/i}"
        pdef "Yes! For the photo of the body I posted."
        pconceited "It's common practice amongst us Social Media gurus."
        pconceited "Before you can apologize for anything, you have to issue a Fake Apology."
        plaugh "This apology needs to be transparently unapologetic."
        pdef "Then, after everyone calls you out for your Fake Apology, you can issue a Real Apology."
        pdef "Everybody is impressed with you for taking the criticism, and your apology video goes viral!"
        wannoy "Well, I'm sorry I ever thought you were dumb, Mr. Chritude."
        wannoy "It's now obvious that you are just frighteningly sociopathic."
        pdef "Which one of these sounds better?"
        psad "\"I'm sorry you got offended\"?"
        poutrage "Or maybe \"I already apologized! What more do you want from me\"?"
        wthought "I can't take much more of this."
        wthought "I should just ask him about what I came here to ask."
        $visitedPaul = True
        pdef "So what did you come here to talk about?"
    $loop = 1
    while loop == 1:
        menu:
            "Power Outage":
                wcasefile "Can you tell me what you were doing around the time of the power outage?"
                psad "This again? Why do you keep pestering me about the power outage?"
                wangry "Because you still haven't given us a straight answer!"
                poutrage "Honestly, I think I'm just going to unsubscribe from this conversation."
                wangry "That's not a thing you can do in real life."
                show chritude standard at flip
                pos ". . . . ."
                show mir default
                if persuasionComplete == False:
                    wthought "Okay, we're gonna play it like this, huh?"
                    wthought "It's time to take up a different strategy."
                    pause 0.2
                    call persuasion from _call_persuasion
                    scene WvCPersuasion
                    show mir default
                    show chritude standard at flip
                    pause 0.1
                    wthought "He's going to be cagey unless I can open him up somehow."
                    wthought "I need to push his buttons until he lets something slip."
                    wthought "Then I'll have to pick the right moment to attack."
                    whattip "All right, we can get off the power outage thing."
                    jump CPersuasion1
                if persuasionComplete == True:
                    wthought "Stay silent all you want, Chritude."
                    wthought "I know there's proof of whatever you did somewhere around here."
                    wthought "I just need to search the perimeter of the house..."

            "What Happened" if paulSecret == True:
                wbase "So, can you finally tell me what happened?"
                psad "Even better... I can show you."
                psad "I've got a clip saved on my phone."
                if paulLied == True:
                    wbase "I thought you said you deleted all your footage."
                    pnervous "Wellll... I may have... kind of... lied?"
                psad "Okay, here it is."
                show PVid1 with dissolve
                typing "* tap *"
                pos "Hey guys, Master Style here!"
                pos "This house is supposed to be {i}pretty good{/i} at cleaning..."
                pos "Well, let's see how it likes cleaning up GLITTER!"
                hide PVid1
                show PVid2
                pos "Wait, shi-"
                hide PVid2
                show PVid3
                pos "Oof!"
                hide PVid3
                show PVid4
                "* POP *"
                hide PVid4
                show PVid5
                "{b}* BOOOOM *{/b}" with shake
                hide PVid5
                show PVid6
                pos "...uh oh."
                typing "* tap *"
                hide PVid6 with dissolve
                psad "You see? It was just a mistake!"
                wbase "I understand. Can I keep this footage?"

                if "7" in investigation2_cleareditems:
                    psad "Didn't I already give it to you?"
                    wbase "Oh. Yes. That's right."
                else:
                    psad "...Fine."
                    $inventory.add(prank)
                    typing "Prank Footage Added to Evidence"
                    pdef "Just so long as {i}I{/i} can keep {i}that{/i} photo."
                    $inventory.drop(glitter)
                    hide chritude
                    show ash surprised at flip
                    call flash from _call_flash_4
                    asurprise "Hey! My photo!"
                    typing "Glitter Photo Unceremoniously Snatched"
                    wbase "Don't worry about it. I don't think we're going to need it anymore."
                    hide ash
                    show chritude standard at flip
                    with dissolve
                pdef "So like...are we done here? Am I good?"
                wbase "Yes, you can go."
                pconceited "Finally!"
                pconceited "Honestly, you have got to be the most annoying police officer I've never been arrested by!"
                $ investigation2_cleareditems.append("7")

            "Show Evidence":
                wbase "What do you make of this right here?"
                $ current_present = "investigation_2_chritude_present"
                show screen present_evidence_screen
                show screen back_button
                pause

            "Show Profile":
                wbase "What do you think of this person?"
                $ current_present = "investigation_2_chritude_present"
                show screen present_profile_screen
                show screen back_button
                pause

            "Goodbye":
                wbase "Thank you for speaking with us. It's been very, um, helpful."
                pdef "Oh, any time, darling."
                $loop = 0
                call investigation2_warehouse from _call_investigation2_warehouse_3

label investigation_2_chritude_present:
    if present_response == "glitter":
        wbase "Mr. Chritude..."
        pdef "Oh, you're back?"
        pdef "Do you have more tedious questions for me?"
        wobjectionA "Oh, don't worry. I think you're going to find this {i}very interesting.{/i}"
        wobjectionA "After all... you like glitter, don't you?"
        pnervous "I-is that the circuit breaker?"
        wobjectionA "You bet."
        wobjectionC "And look what we found clogging up the electrical socket!"
        show chritude surprised
        pos "IMPOSSIBLE! HOW DID YOU FIND THAT?"
        wbase "You seem pretty familiar with this glitter, Master Style. Care to explain how it got there?"
        psad "NNNNNNNNOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO" with bigshake
        psad "Fine. I'll explain what happened. But you have to promise to not tell the base."
        pnervous "I've heard stories about this place. If you make them mad, they make you disappear!"
        poutrage "Can you imagine it? ME, DISAPPEARING!"
        poutrage "Never again would my incredible Content grace my subscribers' inboxes!"
        psad "It's...it's too much to bear!"
        wannoy "Fine. I promise. Just tell me what happened."
        psad "Okay... fine..."
        $paulSecret = True
        jump investigation2_chritude
    if present_response == "Back":
        wbase "Actually, never mind."
    else:
        pconceited "Fabulous! Daring! I love it!"
        wannoy "Um, you haven't even looked at it."
        pconceited "I've never seen something so marvelous in all my life!"
        wannoy "All right, sheesh, never mind."
    jump investigation2_chritude


label CPersuasion1:
    whattip "Let's talk about something else."
    pdef "Oh? And what did you have in mind?"
    menu:
        "Enthuse: Can you give me a sneak peek of your next video?":
            wbase "Can you give me a sneak peek of your next video?"
            wbase "I'm really interested to see what you've got cooking."
            pconceited "Well of course you are!"
            pconceited "Unfortunately for you, I only give previews to my top tier subscribers."
            pglitterin "Besides, this next video is {i}super top secret.{/i}"
            pglitter "Not even my patrons have heard about it yet."
            show screen healthBar
            pdef "I can't go telling anybody about it all willy-nilly."
            pdef "You'll just have to smash that subscribe button and wait like everyone else."
            $mc_health -= 1
            call healthDrain from _call_healthDrain
            wthought "Well, that didn't work out the way I was hoping."
            hide screen healthBar
            if mc_health == 0:
                jump CPersuasionGameOver
            else:
                jump CPersuasion1

        "Provoke: Are you sure you're all that popular?":
            whattip "Are you sure you're all that popular?"
            whattip "I mean, I'd never even heard of you until today."
            poutrage "How dare you!"
            poutrage "I'll have you know I have one of the most subscribed channels online!"
            pnervous "Sure, maybe it's not as big as \"DaPrankBoyz\"..."
            plaugh "But I've got something cooking that's going to knock those clowns down a peg!"
            plaugh "I'll show them how a real prankster operates!"
            jump CPersuasion2

        "Confront: Fess up, Chritude. I know exactly what happened.":
            wobjectionA "Fess up, Chritude. I know exactly what happened."
            pdef "And what exactly do you know?"
            wconfused "I know that you... did {i}something{/i} to cause the power outage."
            pdef "Do you have any proof it was me?"
            wconfused "I... well... not yet, but clearly you{nw}"
            pdef "Just as I thought."
            pdef "I know all about police work, lady."
            pconceited "I once played a cadaver on a cop show."
            show screen healthBar
            pglitterin "And one thing I know for certain... is that you need {i}evidence{/i} to accuse someone of a crime!"
            $mc_health -= 1
            show mir recoil anim
            call healthDrain from _call_healthDrain_1
            wos "NNGHG!"
            hide screen healthBar
            pconceited "Come back to me when you've got some proof..."
            wannoy "All right... fine... I'll stop asking about that."
            if mc_health == 0:
                jump CPersuasionGameOver
            else:
                jump CPersuasion1

label CPersuasion2:
    menu:
        "Enthuse: You have a prank video coming out? I love pranks!":
            wbase "You have a prank video coming out? I love pranks!"
            wbase "Why, you should see the kind of stuff I pull on my fellow officers back at the precinct."
            wbase "Of course, I'm sure your stuff is way, way better."
            wbase "What have you been doing lately?"
            pdef "Well, right now I'm really fond of what I like to call {nw}"
            pglitterin "Well, right now I'm really fond of what I like to call {fast}\"Glitterbombs\"."
            whattip "Are those what I think they are?"
            pdef "That depends: do you think they're spring-loaded tubes full of glitter?"
            pdef "See, there's two advantages to using glitter in pranks:"
            pconceited "The first, naturally, is that it looks {i}fabulous.{/i}"
            plaugh "But the second, and here's the real kicker, is that it gets {i}everywhere!{/i}"
            plaugh "I mean, you're still finding this stuff hidden around for {i}weeks{/i}."
            pdef "So lately, I've been hiding them just about any place I can."
            pdef "Bathtubs, cereal boxes, inside people's cars, even during weddings and funerals!"
            wannoy "Wait, what was that last one?"
            pdef "I've almost finished up a supercut of all my best glitter pranks."
            jump CPersuasion3

        "Provoke: DaPrankBoyz are a class act. You can't possibly hope to compete.":
            wbase "Hah! DaPrankBoyz are a class act. You can't possibly hope to compete with them!"
            wbase "What have you got that's so special?"
            pdef "Hold on... I thought you didn't know anything about internet culture!"
            wconfused "Oh, well, uh... everyone knows about DaPrankBoyz! Those guys are hilarious!"
            pdef "Oh yeah? What's your favorite DPB video?"
            wconfused "Me? Well, I really like the one where they, uh..."
            menu:
                "...trip a baby?":
                    wconfused "...trip a baby?"
                "...throw the pie in the guy's face?":
                    wconfused "...throw the pie in the guy's face?"
                "...replace someone's dog with another dog?":
                    wconfused "...replace someone's dog with another dog?"
            plaugh "Just as I thought..."
            show screen healthBar
            plaugh "You don't know anything about DaPrankBoyz!"
            plaugh "You were just trying to get my goat!"
            pglitterin "WELL, LOOK WHO'S THE GOATHAVER NOW!"
            $mc_health -= 1
            show mir recoil anim
            call healthDrain from _call_healthDrain_2
            wos "BWAUGH!"
            hide screen healthBar
            pconceited "Now it should be clear that I'm Prankmaster General around these parts."
            pconceited "My new video will just be icing on the cake at this point!"
            if mc_health == 0:
                jump CPersuasionGameOver
            else:
                jump CPersuasion2

        "Confront: Aha! You shut down the power grid as part of your prank!":
            wobjectionA "Aha! You shut down the power grid as part of your prank!"
            wobjectionA "That's why you don't want to talk about it!"
            wobjectionA "You want to keep the secret safe until you publish the video!"
            poutrage "How preposterous! What's funny about a power outage?"
            poutrage "With the lights out, nothing would even show up on the camera!"
            pconceited "Besides, I've got a {i}little{/i} more finesse than DaPrankBoyz, thank you very much."
            pconceited "I don't just go around breaking things and calling it a prank!"
            show screen healthBar
            poutrage "Frankly, I'm offended you would even imply something like that!"
            $mc_health -= 1
            show mir recoil anim
            call healthDrain from _call_healthDrain_3
            wos "Oof!"
            hide screen healthBar
            wthought "Well, he {i}seems{/i} to be telling the truth..."
            wthought "But if the power outage wasn't part of his prank, then why is he so jumpy?"
            wthought "I think I need more information."
            if mc_health == 0:
                jump CPersuasionGameOver
            else:
                jump CPersuasion2

label CPersuasion3:
    menu:
        "Enthuse: You must have done one here at the base, right?":
            whattip "Pretty cool! So, you must have done one here at the base, right?"
            whattip "There's got to be lots of great opportunities here with the Smart House."
            pnervous "Oh...yeah... I guess you're right..."
            pnervous "I don't know, though, if this is really the right place for pranks."
            wbase "But you said yourself you'd set off bombs during weddings and funerals!"
            wbase "If those places are fair game, surely some stuffy government base would be fine!"
            pnervous "W-well, of course I shot some footage here..."
            pnervous "But I don't think any of it was funny enough to make the cut..."
            whattip "Can you show me what you shot? Maybe it's better than you think."
            show screen healthBar
            show chritude surprised at flip
            pos "Nope! Sorry! Already deleted it!"
            $mc_health -= 1
            call healthDrain from _call_healthDrain_4
            pnervous "Just taking up space on my phone, you know?"
            $ paulLied = True
            hide screen healthBar
            wthought "All right. Time to stop beating around the bush with this guy."
            if mc_health == 0:
                jump CPersuasionGameOver
            else:
                jump CPersuasion3

        "Provoke: Glitter isn't funny. It's just annoying!":
            wangry "Glitter isn't funny. It's just annoying!"
            poutrage "Well, sheesh. Sorry you don't get the joke..."
            wbase "That's not a real apology and you know it!"
            psad "Man, you're right. I should have seen it from your perspective."
            psad "A joke isn't funny if it's at the expense of somebody else."
            psad "I'll try to do better in the future."
            wbase "Well. Good."
            whattip "It's good to see you've learned your lesso{nw}"
            wangry "It's good to see you've learned your lesso--{fast}HEY WAIT A MINUTE!"
            wangry "You're just doing the \"Fake Apology\" bit, aren't you!?"
            show screen healthBar
            plaugh "You see? It's a very effective strategy."
            $mc_health -= 1
            show mir recoil anim
            call healthDrain from _call_healthDrain_5
            wos "Gah!"
            hide screen healthBar
            wthought "I can't believe I fell for that!"
            if mc_health == 0:
                jump CPersuasionGameOver
            else:
                jump CPersuasion3

        "Confront: You glitter bombed the house, didn't you?":
            wobjectionA "So {i}that's{/i} what happened!"
            wobjectionA "You glitter bombed the house, didn't you?"
            wobjectionC "You fired a bomb into the circuits so you could blow out the power!"
            pnervous "No I didn't! It was an accident!"
            show chritude surprised at flip
            pos "I MEAN--"
            wsettle "Aha!"
            poutrage "YOU HAVE NO PROOF!"
            poutrage "EVEN IF YOU WERE TO CHECK THE CIRCUIT BREAKER, YOU WOULDN'T FIND ANYTHING!"
            wgotcha "The circuit breaker, huh?"
            show chritude surprised at flip
            pos "AAAAH! UNDO! DELETE MESSAGE!"
            ## Persuasion Complete Anim
            scene basewarehouse
            show mir default
            show chritude nervous at flip
            call flash from _call_flash_5
            pause 0.5
            show screen healthBar
            $mc_health = mc_maxhealth
            call healthGain from _call_healthGain
            hide screen healthBar
            wbase "So, are you going to come clean or do I need to go search the breaker?"
            pnervous "H-hah! Good luck!"
            pnervous "Even if there ever was anything around there - which there definitely wasn't - "
            pnervous "Surely I would have cleaned up any evidence of it!"
            wbase "You're still gonna keep pretending? Fine."
            wbase "Let's go, Ash."
            wbase "We've got to go check out the breaker."
            pnervous "Y-you're just wasting your time!"
            $persuasionComplete = True
            hide chritude
            show ash standard at flip
            with dissolve
            wthink "Okay, somewhere hidden here is the proof we need to make Chritude crack."
            wthink "Just a little bit of glitter should be enough."
            aunsure "But what if he's right, and he already cleaned up the mess?"
            wbase "Remember that thing Mr. Chritude said about glitter?"
            asurprise "It gets everywhere!"
            wbase "Exactly. If a glitter bomb went off around here, we'll be sure to find a trace."
            hide mir
            hide ash
            with dissolve
            call investigation2_warehouse from _call_investigation2_warehouse_4

label CPersuasionGameOver:
    pdef "All right, I'm bored now."
    wbase "We've been talking for five minutes."
    pdef "Well, my generation has an infamously short attention span."
    pconceited "And besides, my notifications are just {i}blowing up.{/i}"
    pdef "So sorry, I'm going to have to respond to these."
    wbase "Sorry, Mr. Chritude, you can't just ignore this."
    pos ". . . . ."
    wannoy "O-okay, I guess you {i}can{/i} ignore this..."
    scene basewarehouse
    show mir default
    show chritude standard at flip
    call flash from _call_flash_6
    wthought "Fine... I'll try again with this guy later..."
    call resetHealth from _call_resetHealth
    hide mir
    hide chritude
    with dissolve
    call investigation2_warehouse from _call_investigation2_warehouse_5

label investigation2_toobig:
    wthought "This warehouse is too big to try and search every little nook and cranny."
    wthought "I need to focus on the important things."
    call investigation2_warehouse from _call_investigation2_warehouse_6


label investigation2_bottomiawakens:
    $renpy.start_predict("sprites/Bottomi*.*")
    scene kitchen
    show mir default
    show drang default gup
    with fade
    ddef_gup "Hey, assistant."
    ddef_gup "While you were off gallivanting on your own, our main suspect finally woke up."
    whattip "You mean Mr. Bottomi?"
    ddef_gup "Obviously. Your forensics monkey is over there attending to him."
    ddef_gup "How about we finish up that cross examination, huh?"
    hide drang
    show bottomi standard
    with dissolve
    wholdon "Mr. Bottomi. Are you alright?"
    bfuzzy "I... I think so..."
    bfuzzy "H-how long was I out?"
    hide mir
    show car serious
    with dissolve
    cser "Approximately thirty minutes."
    cser "I'm going to be honest: you may have brain damage."
    cser "You should probably go see a doctor when you get a chance."
    cdef "I mean, a doctor besides me."
    hide car
    show mir default
    with dissolve
    whattip "Now, do you mind telling us about that thing on your head?"
    bapology "You mean my hat? Wait..."
    show bottomi freak
    bos "Aah! My hat! You weren't supposed to see this!"
    if mentionedhardware == True:
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
    bdef "It's an experimental {color=#FF9966}neural implant{/color} designed for psychically transferring information."
    bdef "It lets me send and receive data wirelessly from my brain to a computer."
    bdef "I don't fully know all the technical detai{nw}"
    hide mir
    show ash camera
    show Ash_Camera_Polaroid
    show bottomi freak
    call flash from _call_flash_7
    bos "AAH!"
    acam "This is absolutely incredible! Real life technopathy!"
    hide Ash_Camera_Polaroid
    apsyched "The occultism forums are going to go wild when they see this!"
    bapology "Good luck. The base is probably gonna confiscate that photo before they let you leave."
    aannoy "Rats..."
    hide ash
    show mir default
    with dissolve
    wthought "And to think, the thing he was dead set on hiding from us was right there the whole time."
    wbase "So, now that the cat is out of the bag..."
    wthink "Are there any other secrets you'd like to share with us?"
    bapology "No, I don't thi-- {nw}"
    show bottomi freak
    bos "No, I don't thi-- {fast}NNNGH!!" with shake
    bremember "Actually, there is, come to think of it."
    bdef "You might have noticed that my recollection of events has been a little shaky..."
    hide mir
    show ash flippant
    aflippant "Yeah, no kidding..."
    bdef "Well, the reason is that I've been lying to you about one important detail."
    bdef "I didn't actually kill Orin Darsha..."
    show ash surprised
    bdef "I made the house do it for me."
    show black with dissolve
    call resetHealth from _call_resetHealth_1
    jump smart_house_act_4_intro
