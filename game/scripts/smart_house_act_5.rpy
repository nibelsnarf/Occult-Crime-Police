label smart_house_act_5_intro:
    scene act5 with fade
    $ save_name = "Act 5"
    $conflictingStories = False
    pause 3.0
    show black with dissolve
    typing "September 13th. 10:24 P.M.\nSmart House - Kitchen"
    show kitchen
    show drang default gup
    show bottomi standard at flip
    with dissolve
    ddef_gup "This is rich. Now you're saying you had nothing to do with this whole thing."
    ddef_gup "And the only reason you confessed is because your brain computer told you to."
    bapology "Uh...basically?"
    ddef_gup "I love this so much."
    dthink_gup "You see, back at the office, me and the boys have this whiteboard where we write the dumbest excuses crooks have told us."
    dangry_gup "\"My twin did it!\" \"I was possessed by a vengeance ghost!\" That kind of thing."
    ddef_gup "Every month we have a little voting party where the worst excuse wins twenty bucks."
    ddril_gup "And buddy, you just won me twenty bucks."
    ddril_gup "I'm gonna get me a fancy steak dinner thanks to you."
    hide bottomi
    show mir default
    wbase "You don't believe him, then."
    dangry_gup "Of course I don't! It's ridiculous!"
    dangry_gup "Consider the two explanations here..."
    dfrown_gup "Either somebody has been counter-programming this man's brain for the past two hours in order to make him falsely confess..."
    dfrown_gup "{i}Or{/i} he killed a guy, fessed up, then got cold feet about going to jail."
    wthink "I agree the whole thing sounds stupid, but it explains a lot of things."
    wthink "The general confusion, the inaccuracies, the way his story kept changing..."
    dfrown_gup "If every guy who couldn't keep his story straight was being mindhacked..."
    dfrown_gup "...then half the guys I've locked up should have a brainchip."
    wholdon "Look, it can't hurt to investigate this."
    wholdon "He said his neural implant was relegated to the base's local network, so the hacker must be somewhere in Base 24."
    dfrown_gup "Great. That narrows the suspects down to, what, a thousand?"
    wbase "Let's start by asking Bottomi some questions. He might be able to clarify some things for us."
    wbase "And if his story still doesn't add up, we can put him right back on the suspect list."
    djacket_pop "Fine. Go ahead."
    ddril_gup "In the meantime, I'm going to call my buddies and get them to put this up on the whiteboard."
    hide drang with dissolve
    "* bleep *"
    dos "Hey! Gordo! Wait until you get a load of {i}this{/i} one!"
    show bottomi standard with dissolve
    wbase "Mr. Bottomi, are you feeling well enough to answer some questions?"
    bsad "S-sure. I'm actually feeling better than I have for a while now..."
    $askingLou = []
    $askingLouCleared = False
    while askingLouCleared == False:
        menu:
            "Did You Do It?":
                wbase "Why don't we get this one out of the way first:"
                wbase "Did you, Louis Bottomi, kill Orin Darsha!"
                bdef "No. I'm certain of that now."
                bapology "I visited the Smart House earlier today, that much is true."
                bsad "But Mr. Darsha was already dead when I arrived."
                whattip "Why did you go there?"
                bapology "I... I don't know, come to think of it."
                bapology "I just suddenly got to thinking that it would be a good idea to check out the kitchen."
                bremember "H-hey, you don't think I was already being controlled at that point, do you?"
                bapology "I {i}did{/i} think it was weird how excited I was to splash around in that mud..."
                wthought ". . . {w=0.5}Hey!"
                wthought "Those footprints..."
                wthought "Could this mystery culprit have been clever enough to fake incriminating evidence against Mr. Bottomi?"
                $askingLou.append("1")
            "Your Confession":
                wbase "So, you think somebody else is responsible for your confession earlier?"
                bsad "Pretty much, yeah..."
                hide mir
                show ash psyched
                call flash from _call_flash_42
                apsyched "Wow! So they, like, mind controlled you!"
                bapology "Uh... not exactly..."
                bapology "It's more like... they gave me fake memories of committing the crime."
                bsad "From my perspective, it really seemed like I had done it."
                hide ash
                show mir default
                with dissolve
                wbase "It's fairly lucky for them that you had the integrity to confess."
                wbase "I suspect most people would have tried to cover up their crime."
                wthink "In fact, it would seem one such person {i}did.{/i}"
                bsad "I guess that was pretty stupid of me, huh?"
                wbase "Not at all. We'd be a lot better off if there were more people like you in the world."
                whattip "Are you now able to tell which of your memories are real and which are false?"
                bapology "Yes, I think so. Now that my connection to the implant is broken, the fake ones are starting to fade."
                bapology "Sort of like how a dream seems so real in the moment, but you start to forget it when you wake up."
                $conflictingStories = True
                $askingLou.append("2")
            "Conflicting Stories" if conflictingStories == True:
                whattip "Why did your story keep changing so much?"
                bdef "Well, my memories kept changing."
                bapology "At the time I thought I had just been remembering things wrong..."
                bdef "But now I think whoever did this was making new memories to counter your arguments."
                bfuzzy "Whenever you pointed out a flaw in my story, it really did hurt my head."
                bfuzzy "From my perspective, it was like you had just proven my own memories false."
                bdespair "It would seem like reality as I knew it was falling apart..."
                bremember "And then, just like that, I would remember something new that explained everything."
                bsad "It was almost a relief, even though it confirmed that I was the killer."
                wbase "I see. But - wait a minute..."
                wthink "If the true culprit was counter-programming you against my arguments..."
                wthink "Doesn't that mean they were listening in on our conversation?"
                bremember "W-well, hey, you're right!"
                bnervous "But wait... it's just us in the house, right? How could someone be listening?"
                wthink "If they had access to your brain, then maybe they were listening through your ears..."
                bnervous "Or maybe they've also got access to the surveillance equipment built into this house."
                $askingLou.append("3")
        if "1" in askingLou and "2" in askingLou and "3" in askingLou:
            $askingLouCleared = True

label neeringIntro:
    wbase "Thank you, Lou. This has been very helpful."
    bdef "I'm gonna go walk around and clear my head,{w=0.1} if you don't mind."
    wbase "No problem.{w=0.1} You've been through a lot today."
    hide bottomi with dissolve
    $renpy.stop_predict("sprites/Bottomi*.*")
    $renpy.start_predict("sprites/Neering*.*")
    pause 0.4
    show guard glasses at flip
    gglasses "Excuse me! Sheriff Warren!"
    wannoy "You again?"
    gglasses "Ms Angela Neering wishes to speak with you regarding the murder!"
    whattip "Oh, of course. Where is she?"
    gglasses "Don't worry! I'll bring her to you!"
    hide guard with dissolve
    wbase "Uh, thanks."
    wthought "Wait... \"bring her to you\"?"
    show neering wheelin
    pause 4.0
    wconfused "What in the..."
    noff "Hello, Sheriff."
    noff "I've come because I thought I could - wait, can you see me?"
    wconfused "I'm sorry... what am I supposed to be seeing here?"
    noff "GUARD, GET OVER HERE! YOU SET THE TV TO THE WRONG INPUT, YOU MORON!" with shake
    gos "Sorry! Sorry!"
    gos "I don't get it! I have it set to HDMI 1 and everything..."
    noff "Well keep trying one until it works!"
    show neering default
    call flash from _call_flash_43
    gos "Oh! There we go!"
    nangry "Great. Now get out of my sight!"
    gos "Y-yes, ma'am!"
    ndef "Now, Sheriff. You can see me now, yes?"
    wannoy "I see a mid-2000's A.V. club setup with your face on it, if that's what you mean."
    if concernForZombies == True:
        hide mir
        show ash confident
        aconfident "You've got a lot of explaining to do, Miss Neering."
        aunsure "For starters...{p=0.5} did you know that this house isn't even zombie-proof?"
        ngrumble "What on earth are you talking about?"
        aannoy "The heartbeat monitor! It completely fails to account for instances of the walking dead!"
        aposit "Vampires either, come to think of it."
        aannoy "What kind of ramshackle operation are you running here where any old undead creature can just waltz in and{nw}"
        hide ash
        show mir annoy
        wannoy "Please ignore them. Now..."
    whattip "I was under the impression that you would be coming to speak with me {i}in person{/i}."
    ndismissive "TYM, I suppose!"
    wconfused "TYM?"
    ndismissive "That's Your Mistake."
    ndef "See, as much as I wish to help with your investigation, I'm still incredibly busy fixing this house."
    ndef "I'm sure you understand that my life's work is a little bit more important."
    wbase "Than solving a {i}murder?{/i}"
    nuneasy "Well, see, here's the thing about that..."
    wthought "Oh boy, here we go."
    wbase "Agent Drang, I think you're going to want to hear this."
    hide mir
    show drang dril gup at flip
    ddril_gup "What is it? Are you going to tell me that this Television Woman is the killer?"
    nuneasy "Well... the thing is..."
    nuneasy "I'm... sorta.... the one who hacked that guy's neural implant..."
    dfrazzled "WHAAAAT!?" with shake
    dfrazzled "YOU MEAN HIS ASININE FAKE MEMORIES EXCUSE WAS REAL?" with shake
    nuneasy "Yyyeaaaahhhhhh....."
    dangry_gdown "I need a drink."
    dfrazzled "Hey!{w=0.2} Medicine Man!{w=0.2} Whatshisface!"
    hide neering
    show car agitated at flip
    call flash from _call_flash_44
    chold "Who, me?"
    dfrazzled "Give me that!"
    call flash from _call_flash_45
    cagit "No!{w=0.2} My Marg!"
    dos " * gulp *{w=0.1}  * gulp *{w=0.1}  * gulp *"
    dos " * spfffphhffhhpth * "
    dfrazzled "WHAT THE HELL WAS THAT?" with shake
    cdef "Uh, a margarita. What do you think it was?"
    dfrazzled "B-but there's no tequila in this!"
    dfrazzled "Have... HAVE YOU BEEN DRINKING STRAIGHT MARGARITA MIX THIS ENTIRE TIME!?" with bigshake
    clift "You didn't think I was really drinking on the job, did you?"
    dfrazzled "Somehow... this is worse than if you {i}were{/i}..."
    hide drang
    hide car
    show mir default
    show neering default
    with dissolve
    wthink "Ms Neering... I'm not sure if you understand what you just said..."
    wthink "If you're the one who made Louis Bottomi confess to the murder..."
    wbase "...Wouldn't that make {i}you{/i} the true killer?"
    nsmug "What?{w=0.1} No.{w=0.1} No no no."
    ndef "See, there's something you don't know about Orin Darsha's death."
    ndef "The truth is...{w=0.2} it was {color=#FF9966}an accident.{/color}"
    wannoy "An accident? What, did he fall down the stairs?"
    nuneasy "No, nothing like that. It was... well... it was a malfunctioning piece of tech. Here in the house."
    whattip "Oh, do you mean..."
    menu:
        "...The Grabber Hands?":
            whattip "...The Grabber Hands?"
            nsmug "No. Although, not to brag or anything, they certainly {i}could{/i} kill a man."
            wannoy "That is... an interesting thing to brag about."
            nsmug "What can I say? I'm proud of my children."
            ndef "No, it was The Dressing Contraption where poor Mr. Darsha met his end."
            show mir think
            wthought "That's right... we found that shoe which proved he was in there."
        "...The Dressing Contraption?":
            whattip "...The Dressing Contraption?"
            wcasefile "After all, we found his shoe in there while investigating."
            ndef "Yes, that is the fateful place where Mr. Darsha met his end."
        "... The Security System?":
            whattip "... The Security System?"
            nsmug "No. Although, not to brag or anything, it certainly {i}could{/i} kill a man."
            wannoy "That is... an interesting thing to brag about."
            nsmug "What can I say? I'm proud of my children."
            ndef "No, it was The Dressing Contraption where poor Mr. Darsha met his end."
            show mir think
            wthought "That's right... we found that shoe which proved he was in there."

    wthink "But how is a glorified wardrobe even capable of killing a man?"
    nangry "Hey, any part of a house can be dangerous!"
    nangry "More than a third of household injuries occur in the bathroom, after all!"
    nuneasy "And, as it turns out, a machine which forces clothes onto a human body is also dangerous..."
    nlaugh "But, I mean, it was only a teensy weensy rounding error."
    nlaugh "How was I supposed to know that something like that would be enough to break his neck?"
    wthink "I...see."
    hide neering
    hide mir
    with dissolve
    show mir default with dissolve
    wbase "Carlos, can I talk to you over here for a second?"
    show car serious at flip with dissolve
    cser "Sure, Chief."
    whattip "I don't know if Ms Neering is aware of this, but she's already confessed to several crimes."
    wbase "Maybe she thinks that since Mr. Darsha's death was an accident, she isn't culpable."
    wbase "But since it's her own invention which killed him, it counts as criminally negligent manslaughter."
    wthink "Not to mention the fact that she tampered with a crime scene and obstructed a murder investigation."
    cagit "Shoot, you're right."
    cagit "Well, we can't tell her now. She might bolt before we have a chance to arrest her."
    wbase "Exactly. That's why I need you to go find her."
    cagit "Me?"
    wbase "I've got to stay here and keep her talking so that you can track her down."
    clift "You mean I get to place her under citizen's arrest?"
    wannoy "Uh, you don't need to do that."
    wannoy "You work for the Sheriff's Department. You're already authorized to do the regular kind of arrests."
    cthink "I know, but citizen's arrest always sounded so cool!"
    show car agitated at flip
    wangry "Focus, Tsukada! You're the only one I can trust with this." with shake
    show mir default
    cser ". . . I won't let you down, Chief."
    hide car with dissolve
    pause 0.7
    cos "BOY DO I HAVE TO GO TO THE BATHROOM" with shake
    show mir annoy anim
    cos "LET ME JUST DUCK OUT AND MAKE MY WAY THERE" with shake
    cos "TO THE BATHROOM, THAT IS" with shake
    cos "WHICH IS WHERE I'M GOING" with shake
    wannoy "* sigh *"
    show neering default with dissolve
    ndef "He better not go in any of the Smart House bathrooms..."
    ndef "The pipes aren't actually connected to anything yet."
    hide mir
    show drang frazzled at flip
    dfrazzled "THEY AREN'T!?" with shake
    ndef "No, they're not. Why do you ask?"
    dfrazzled ".{w=0.2} .{w=0.2} .{w=0.2} .{w=0.2}{nw}"
    ddef_gdown ". . . . {fast}No reason."
    hide drang
    show mir base
    wbase "Ms Neering, can you tell me more about this accident?"
    ndismissive "WYS."
    menu:
        "Where's Your Sovereignty?":
            wconfused "Where's Your Sovereignty?"
            nangry "What? No! What would that even mean?"
            whattip "You know, like, what's your authority here?"
            wbase "I thought maybe you were asking if I was in charge here."
            ndismissive "No. Obviously it was \"Whatever You Say\"."
            wthink "Fine. Sheesh."
            ndismissive "You plebeians need to get on my level."

        "Whatever You Say?":
            wconfused "Whatever You Say?"
            nsmug "Yes! Thank you!"
            nsmug "Finally someone here speaks plain English!"
            wthought "Honestly, that was a complete shot in the dark."
            wthought "Glad it worked out, I guess."

        "Cram it with the acronyms already!":
            wangry "Cram it with the acronyms already!" with shake
            ndismissive "I'm not going to let some mouth-breather lower my language to their level."
            ndismissive "Either figure out what I'm saying on your own, or let me explain it to you."
            ndismissive "And by the way, it was \"Whatever You Say\"."
            wthought "See, how on earth was I supposed to guess that?"

    hide mir
    call witness_statement from _call_witness_statement_7
    typing "-- my_testimony.txt --{fast}"
    ndef "After the tour, Darsha came to ask me a few questions about the Smart House."
    ndef "He, of his own volition, decided to test out The Dressing Contraption."
    ndismissive "Needless to say, it didn't go so well for him."
    ndef "I knew that an accident on the day of the Smart House's unveiling would be bad press."
    nsmug "So I framed that buffoon with the neural implant and tricked him into confessing."


    hide neering
    show ash thinking at flip
    show mir default
    with fade
    athink "All right, what's our M.O. right now?"
    wbase "We just need to keep her talking long enough that Carlos can figure out where she's holed up."
    whattip "And, if possible, find any holes in her story."
    athink "But shouldn't Ms Neering's statement here be \"the truth\", so to speak?"
    wthink "See, I thought so too... but something in her story doesn't line up for me."
    apsyched "Okay, let's see if we can figure out what that is!"
    hide ash
    show drang frazzled
    dfrazzled "WARREN!" with shake
    dfrazzled "YOU BETTER FIX THIS, QUICK!"
    wholdon "F-fix what?"
    dfrazzled "This...{w=0.7} this whole case!"
    dangry_gdown "We had everything wrapped up all neat and tidy!"
    dangry_gdown "But then you just had to go picking at every little scab you saw..."
    dangry_gdown "And now we got computer women and mind control and all this other crap!"
    dfrazzled "DO YOU KNOW HOW MUCH PAPERWORK I'M GOING TO HAVE TO DO NOW?"
    dfrazzled "I HAVE TO FILL OUT THREE EXTRA FORMS ALONE, JUST FOR THE MIND CONTROL!"
    wconfused "Your office has specific paperwork related to mind control?"
    dfrazzled "OF COURSE WE DO!" with shake
    dfrazzled "IT'S THE FBI, ISN'T IT?" with shake
    dfrazzled "NOW BRING ME SOMEONE TO ARREST BEFORE I JUST PICK ONE AT RANDOM!"
    wthought "Boy, I'll bet internal affairs would have a field day with this guy..."
label testimony8_intro:
    $ current_present = "SH_Objection8"
    $ CurrentTestimony = "SH_Testimony8A"
    $ back_action = CurrentTestimony
    $ testiLength = 5
    hide screen inventory_screen_button
    scene kitchen
    hide drang
    hide mir
    show neering default
    with fade
    call interrogation from _call_interrogation_9
    play music "music/BustingLiesAtAModerateTempo.ogg" fadein 1.0

label SH_Testimony8A:
    $ settesti("SH_Testimony8A", None, "SH_Testimony8B", "SH_Press8A","SH_Advice8",1)
    show screen testi
    ndef "After the tour, Darsha came to ask me a few questions about the Smart House."
    jump SH_Testimony8B

label SH_Press8A:
    hide screen testi
    show mir default
    wbase "Shouldn't the tour have told him everything he needed to know?"
    ndismissive "That tour was more geared towards... pedestrians."
    ndismissive "A lot of concepts were dumbed down so that your average simpleton could understand them."
    ngrumble "It's a dreary yet necessary process when selling to...{w=0.7}\n {i}the common masses.{/i}"
    wthought "You didn't need to shudder like that when you said \"the common masses\"."
    wthought "As a common mass myself, I take offense to that."
    whattip "What kind of things was Mr. Darsha asking about?"
    ndef "Money, of course."
    ndef "How much does each A.R.M. cost? What's the price-to-benefit ratio for each feature?"
    ngrumble "It's exhausting!"
    ngrumble "I build that man a revolution in home living and he wants to know where we can cut costs."
    ndismissive "Would you cut costs... on a sunset?"
    wthought "I swear I must have run into the annual narcissist convention or something..."
    hide mir default
    jump SH_Testimony8B

label SH_Testimony8B:
    $ settesti("SH_Testimony8B", "SH_Testimony8A", "SH_Testimony8C", "SH_Press8B","SH_Advice8",2)
    show screen testi
    ndef "He, of his own volition, decided to test out The Dressing Contraption."
    jump SH_Testimony8C

label SH_Press8B:
    hide screen testi
    show mir default
    wbase "You sure seem, uh, {i}insistent{/i} that it was Darsha's own decision to use the contraption."
    whattip "Why is that?"
    ndef "I just don't want anyone here thinking that I {i}made{/i} Darsha do anything."
    ndef "Otherwise I just know some clown at the insurance agency is gonna be like,"
    ndef "\"Oh, you were the one who made him try it out, so it's your fault that he died!\""
    ngrumble "So let's just set the record straight, here and now: Darsha {i}wanted{/i} to test it."
    ngrumble "He was all riled up about how he didn't get to try it during the tour, so he made me run him through it."
    ngrumble "If I'd had time beforehand, I could have noticed the bug in the contraption and fixed it."
    ndismissive "This is only a prototype, after all. It's not fully polished."
    ndismissive "So really it's on him that he died, not me."
    wthought "That is... {i}super{/i} not how culpability works."
    wthought "And besides, did Darsha {i}really{/i} intend to go through with that test?"
    hide mir default
    jump SH_Testimony8C

label SH_Testimony8C:
    $ settesti("SH_Testimony8C", "SH_Testimony8B", "SH_Testimony8D", "SH_Press8C","SH_Advice8",3)
    show screen testi
    ndismissive "Needless to say, it didn't go so well for him."
    jump SH_Testimony8D

label SH_Press8C:
    hide screen testi
    show mir default
    wannoy "Uh, care to elaborate on that point?"
    ndef "Sure, but it's very technical... and graphic."
    show mir default
    ndismissive "Basically what happened is there was a slight rounding error in the contraption's algorithm."
    nsmug "An easily repairable mistake, if I'd just been given time to troubleshoot."
    ndef "As a result, it mistook Mr. Darsha's skull for a nightcap which needed to be removed."
    ndef "I didn't see any of this, mind you."
    ndef "This is all extrapolated from the state of his body, as well as my own knowledge of the algorithm."
    ndismissive "It's just as well I didn't see any of it, because this next bit gets a little grisly."
    ndismissive "Essentially, in attempting to remove this \"nightcap\", the contraption dislocated his cervical vertebrae."
    nsmug "That means it broke his neck, by the way."
    wannoy "I know what a cervical vertebrae is."
    ndef "Now, you already know that the house's sensors can't recognize a human after they've died."
    ndef "So when the house realized it was holding unfamiliar matter, it executed its error routine..."
    ndef "Which, in this case, is to drop the foreign matter through the exit hatch."
    wbase "Well, that certainly explains the broken neck and the bruises..."
    whattip "But what about the victim's stab wound?"
    nangry "I'm getting to that!"
    hide mir default
    jump SH_Testimony8D

label SH_Testimony8D:
    $ settesti("SH_Testimony8D", "SH_Testimony8C", "SH_Testimony8E", "SH_Press8D","SH_Advice8",4)
    show screen testi
    ndef "I knew that an accident on the day of the Smart House's unveiling would be bad press."
    jump SH_Testimony8E

label SH_Press8D:
    hide screen testi
    show mir default
    wangry "That's all it was to you? Bad press?"
    ndef "Well, think about it from my perspective."
    show mir default
    ndismissive "This house... is my life's work."
    ndismissive "It is the culmination of all of my studies in machine learning, bionic engineering, and interior design."
    ndismissive "And today was the day where I would finally unveil the fruits of my labor to the world."
    ndismissive "How could I let something so trivial as an accidental fatality ruin this moment?"
    ndef "If the press finds a dead body in the kitchen of my invention, what's the headline going to be tomorrow?"
    ndismissive "Is it going to be \"Amazing Genius Improves Everyone's Lives With Great Invention\"?"
    ngrumble "Or is it going to be \"Dangerous House Does A Murder, Is Broken\"?"
    nuneasy "I just {i}tweaked{/i} the headline to \"Crazy Guy Kills Boss Inside Super Cool House\"."
    ndismissive "This is what we in the business like to call \"Public Relations\"."
    wthought "I'll be sure to write \"Wanted for Public Relations\" on the arrest warrant, then."
    hide mir default
    jump SH_Testimony8E

label SH_Testimony8E:
    $ settesti("SH_Testimony8E", "SH_Testimony8D", "SH_Testimony8A", "SH_Press8E","SH_Advice8",5)
    show screen testi
    nsmug "So I framed that buffoon with the neural implant and tricked him into confessing."
    jump SH_Testimony8A

label SH_Press8E:
    hide screen testi
    show mir default
    whattip "So you're the one that stuck the knife in the victim's back?"
    nlaugh "No, no, of course not."
    ndismissive "I had the house do it."
    wcasefile "But what about the footprints made by Louis Bottomi?"
    ndismissive "Easy. I splashed some mud around outside the house..."
    nlaugh "Then I \"convinced\" that stooge to take a stroll around."
    nlaugh "It was child's play, really."
    wthink "But why such an elaborate ruse?"
    wthink "Why bother with all of this if your deception was so full of contradictions?"
    ngrumble "Well, to be honest, I didn't figure you cops would be quite so inquiring."
    ndismissive "I figured if you saw a knife in someone's back and a guy saying \"I did it\"..."
    ndismissive "Then you wouldn't bother yourself with anything that didn't quite line up."
    wbase "I'm afraid that while your technique might have worked on {i}some people...{/i}"
    hide neering
    show drang frown gup
    with dissolve
    dfrown_gup ".{w=0.4} .{w=0.4} .{w=0.4} {nw}"
    dangry_gup ". . . {fast}Hey!{w=0.7} What are you looking at me for!?" with shake
    hide drang
    show neering dismissive
    with dissolve
    wbase "...it didn't quite work on me."
    ngrumble "I'll keep that in mind for the next time I need to fabricate a crime scene. I guess."
    hide mir default
    jump SH_Testimony8A

label SH_Advice8:
    hide screen testi
    hide neering
    show ash annoy at flip
    show mir default
    aannoy "Okay, shoot. I'm stumped."
    athink "I feel like we should be looking for some flaw in her description of Mr. Darsha's death."
    athink "Or maybe something with her cover-up of the whole thing."
    wbase "It's much simpler than that, really."
    wbase "We don't need to destroy Ms Neering's entire story. Not yet, at least."
    wcasefile "All we need to do is answer one central question:"
    wcasefile "{color=#FF9966}Did Orin Darsha really intend to use the contraption?{/color}"
    wbase "If we can figure that out, we should be able to find the chink in the armor we need."
    adef "Got it!"
    hide ash
    hide mir
    show neering default
    if CurrentTestimony == "SH_Testimony8A":
        jump SH_Testimony8A
    if CurrentTestimony == "SH_Testimony8B":
        jump SH_Testimony8B
    if CurrentTestimony == "SH_Testimony8C":
        jump SH_Testimony8C
    if CurrentTestimony == "SH_Testimony8D":
        jump SH_Testimony8D
    if CurrentTestimony == "SH_Testimony8E":
        jump SH_Testimony8E

label SH_Objection8:
    if present_response == "Back":
        if CurrentTestimony == "SH_Testimony8A":
            jump SH_Testimony8A
        if CurrentTestimony == "SH_Testimony8B":
            jump SH_Testimony8B
        if CurrentTestimony == "SH_Testimony8C":
            jump SH_Testimony8C
        if CurrentTestimony == "SH_Testimony8D":
            jump SH_Testimony8D
        if CurrentTestimony == "SH_Testimony8E":
            jump SH_Testimony8E
    hide screen testi
    if testipart == "SH_Testimony8B" and present_response == "trapdoor":
        jump SH_Success8
    else:
        jump SH_Failure8

label SH_Failure8:
    wgotcha "I've got a piece of evidence here that's gonn{nw}"
    ndef "Let me see that."
    nos ". . . ."
    nsmug "Using a complex detection algorithm, I've managed to find 16 flaws in your so-called piece of evidence."
    nsmug "Mathematically speaking, there is no way this has any bearing on my testimony whatsoever."
    show screen healthBar
    nsmug "Why don't you just put that thing away? You're only embarrassing yourself."
    show mir recoil anim
    nos "ggghhhhAAAAAHHH!"
    $ mc_health -= 1
    call healthDrain from _call_healthDrain_34
    wthought "I can feel Drang's glare on me from halfway across the room."
    hide screen healthBar
    if mc_health == 0:
        jump SH_GameOver8
    else:
        jump SH_Testimony8A

label SH_GameOver8:
    hide neering
    show drang think gdown
    dthink_gdown "Aaaaand it looks like we're finished here."
    dthink_gdown "I've been about as patient as one could reasonably expect from a man such as myself."
    ddef_gdown "But now I'm just going to pick somebody at random and arrest them for something."
    dfrown_gup "Eenie meenie miney mo..."
    hide drang
    show ash surprised
    asurprise "Aah! Let's get out of here!" with shake
    wholdon "B-but we still haven't found out the truth here!"
    aunsure "Hey, I'm big on the truth too, but I don't know if getting locked up by this guy is worth it."
    wholdon "What about Mr. Bottomi? Heck, what about Carlos?"
    hide ash
    show drang frown gup
    dfrown_gup "...my mother said to pick the very best one..."
    wbase "Okay, let's go."
    show black with dissolve
    wthought "And so, the truth disappeared into darkness."
    wthought "Drang failed to bring the real culprit to justice."
    wthought "And I never unraveled the enigma of Base 24."
    jump endgame

label SH_Success8:
    stop music fadeout 1.0
    show mir default
    wbase "You know, Ms Neering, I'd really hoped that breaking Mr. Bottomi out of his trance would resolve this whole affair."
    wbase "But it seems you are determined to draw this out as much as possible."
    ngrumble "What are you babbling on about?"
    wcasefile "You claim that Mister Darsha was fully willing to test out The Dressing Contraption."
    wcasefile "Not just that, but that he himself was the one who insisted on trying it."
    wcasefile "But why would a willing participant leave scratch marks on the carpet leading to the trap door?"
    nuneasy "W-what's this now?"
    wbase "While searching the bedroom, I found scratch marks leading up to the point where the floor opens up."
    wobjectionA "Now, the only way I can think to explain something like that..."
    wobjectionC "Is if someone were desperately attempting to avoid falling into The Dressing Contraption!"
    nuneasy "Yipes!" with shake
    show mir default
    wthought "Wow. I didn't know that Ms Neering was {i}capable{/i} of being caught off guard."
    wthought "Or that anybody could unironically say \"Yipes\"."
    wbase "So, Angela... care to explain how those scratch marks got there?"
    nangry "H-hah! Hah! You think you've made some brilliant deduction?"
    nangry "Who's to say those scratch marks are from today?"
    wthink "Huh?"
    nsmug "The Smart House project has been in development for years now."
    nsmug "That's hundreds of days during which somebody could have scratched up the carpeting."
    nsmug "You couldn't possibly have proof that those marks are recent."
    wgotcha "As a matter of fact... I do."
    nangry "IMPOSSIBLE!" with shake
    ndismissive "Well, I'm a woman of science. I should never call anything \"impossible\"."
    nangry "STATISTICALLY IMPROBABLE!" with shake
    wobjectionA "That may be, but the odds are in my favor tonight."

label scratchesProof:
    show screen healthBar
    wcasefile "Here is the proof that the scratches in the carpet are from today."
    $current_present = "scratchesProofPresent"
    show screen present_evidence_screen
    pause

label scratchesProofPresent:
    if present_response == "email":
        jump scratchesProofSuccess
    else:
        ndef "What is this. This is nothing. This is a clown's mistake."
        wholdon "No...you see... it proves that.{w=0.2} .{w=0.2} .{w=0.2} .{w=0.2} .{w=0.2} .{w=0.2} .{w=0.2} {nw}"
        $ mc_health -= 1
        show mir recoil anim with shake
        call healthDrain from _call_healthDrain_35
        wos "GWAAAAH!"
        nsmug "It seems the laws of statistics are on my side after all!"
        wthought "Drat. I really thought I had that one."
        if mc_health == 0:
            hide screen healthBar
            jump SH_GameOver8
        else:
            wcasefile "Let's give this one more shot."
            jump scratchesProof

label scratchesProofSuccess:
    hide screen healthBar
    wbase "You must have been very busy the past few days, Ms Neering."
    ndismissive "Why, yes. I have bee- {nw}"
    ngrumble "Why, yes. I have bee- {fast}oh, wait. This is a lead-in to whatever your point is."
    wgotcha "Busy enough, it seems, to forget about this email exchange between you and Orin Darsha."
    nangry "You went through my emails? You can't do that!"
    wbase "We'll talk about what I can and cannot do later on."
    wcasefile "For now, let's take a look at this particular section."
    wcasefile "\"The new carpets will be ready in time for the tours. I've got contractors coming in the day before the event.\""
    nuneasy "!"
    wobjectionA "As you can see, the scratch marks on the carpet must be from today..."
    wobjectionC "BECAUSE THE CARPETING WASN'T EVEN HERE BEFORE YESTERDAY!"
    nangry "Noooooooooo!" with shake
    nangry "This...{w=0.7} this doesn't change anything, you know!"
    nangry "Orin Darsha's death was still an accident!"
    nsmug "And I'll prove it...{w=0.7} with your precious \"testimony\"!"
    hide mir
    call witness_statement from _call_witness_statement_8
    typing "-- my_testimony_FINAL.txt --{fast}"
    # There are many explanations for the scratches in the carpet.
    nsmug "T{w=0.1}A{w=0.1}M{w=0.1}E{w=0.1}F{w=0.1}T{w=0.1}S{w=0.1}I{w=0.1}T{w=0.1}C."
    # Perhaps one of the contractors installing the carpet did it by mistake.
    nsmug "P{w=0.1}O{w=0.1}O{w=0.1}T{w=0.1}C{w=0.1}I{w=0.1}T{w=0.1}C{w=0.1}D{w=0.1}I{w=0.1}B{w=0.1}M."
    # Besides, a couple of scratch marks doesn't prove anything.
    nangry "B{w=0.1}A{w=0.1}C{w=0.1}O{w=0.1}S{w=0.1}M{w=0.1}D{w=0.1}P{w=0.1}A."
    # You want to pin this whole thing on me? Well, it's not gonna happen!
    nangry "Y{w=0.1}W{w=0.1}T{w=0.1}P{w=0.1}T{w=0.1}W{w=0.1}T{w=0.1}O{w=0.1}M?{w=0.2} W{w=0.1}I{w=0.1}N{w=0.1}G{w=0.1}H!"
    # Darsha's death was just an accident caused by a mistake in the AI.
    ndef "D{w=0.1}D{w=0.1}W{w=0.1}J{w=0.1}A{w=0.1}A{w=0.1}C{w=0.1}B{w=0.1}A{w=0.1}M{w=0.1}I{w=0.1}T{w=0.1}AI."

    show warren annoy base with fade
    wos ".{w=0.1} .{w=0.1} .{w=0.1} .{w=0.1} .{w=0.1} .{w=0.1} .{w=0.1} .{w=0.1} .{w=0.1} .{w=0.1}{nw}"
    wangry "WHAT THE HELL WAS THAT?" with bigshake
    ndismissive "My testimony."
    wangry "That wasn't a testimony! That was..."
    menu:
        "...bad dadaist poetry!":
            wangry "...bad dadaist poetry!"
        "...syllable puke!":
            wangry "...syllable puke!"
        "...a malfunctioning junior jumble!":
            wangry "...a malfunctioning junior jumble!"

    nsmug "As a matter of fact, it was a series of acronyms."
    nsmug "You've taken enough of my time as it is. I can't afford to waste time speaking every sentence in full."
    wthought "Again with the acronyms! At this point, she's just doing it to tick me off."

label testimony9_intro:
    $ testiLength = 5
    $ current_present = "SH_Objection9"
    $ CurrentTestimony = "SH_Testimony9A"
    $ back_action = CurrentTestimony
    hide screen inventory_screen_button
    scene kitchen
    hide ash
    hide mir
    show neering smug
    with fade
    call interrogation from _call_interrogation_10
    play music "music/BustingLiesAtAModerateTempo.ogg" fadein 1.0

label SH_Testimony9A:
    $ settesti("SH_Testimony9A", None, "SH_Testimony9B", "SH_Press9A","SH_Advice9",1)
    show screen testi
    nsmug "TAMEFTSITC."
    jump SH_Testimony9B

label SH_Press9A:
    hide screen testi
    show mir hattip
    whattip "I'm going to have to ask you to clarify what that meant."
    ngrumble "What a complete waste of my time."
    ngrumble "Obviously I said, \"There are many explanations for the scratches in the carpet.\""
    nsmug "See, the \"T\" stands for \"There\", the \"A\" stands for \"are\", the-{nw}"
    wannoy "I wasn't confused about the {i}concept{/i} of acronyms!"
    wannoy "Let's just move on..."
    hide mir
    jump SH_Testimony9B

label SH_Testimony9B:
    $ settesti("SH_Testimony9B", "SH_Testimony9A", "SH_Testimony9C", "SH_Press9B","SH_Advice9",2)
    show screen testi
    nsmug "POOTCITCDIBM."
    jump SH_Testimony9C

label SH_Press9B:
    hide screen testi
    show mir annoy talk
    wannoy "You can't really expect me to be able to guess what you're saying, can you?"
    nsmug "Of course not. For a clever enough mind, there should be no guesswork involved."
    nsmug "For example: there are only a certain number of words that begin with the letter P."
    nsmug "From there, only a certain number of letters which begin with O can follow those words."
    nsmug "Following the chain of causality from there, one can logically arrive at the only possible combination."
    ndef "Which, in this case, is \"Perhaps one of the contractors installing the carpet did it by mistake.\""
    whattip "You honestly think the contractor is the one who left those scratches?"
    ndef "Maybe. Maybe not. But there's reasonable doubt, for certain."
    wbase "We could check for DNA traces in the carpet fibers!"
    ndismissive "Perhaps, but HARPER is impressively thorough when it cleans."
    ndismissive "I doubt there would be any traces left behind."
    ndismissive "Not that it matters anyway..."
    hide mir
    jump SH_Testimony9C

label SH_Testimony9C:
    $ settesti("SH_Testimony9C", "SH_Testimony9B", "SH_Testimony9D", "SH_Press9C","SH_Advice9",3)
    show screen testi
    nangry "BACOSMDPA."
    jump SH_Testimony9D

label SH_Press9C:
    hide screen testi
    show mir gotcha
    wobjectionA "Ah, well this one is obvious."
    wobjectionA "You said \"Banana apple cucumber orange salad mango durian pear apricot.\""
    nangry "What? No! How could you possibly come to that conclusion?" with smallshake
    nangry "{i}Clearly{/i} it was \"Besides, a couple of scratch marks doesn't prove anything.\""
    nangry "Honestly, I don't know where you got all those fruit names fro- {w=0.2}{nw}"
    ngrumble "Honestly, I don't know where you got all those fruit names fro- {fast}oh."
    ngrumble "You were messing with me, weren't you?"
    show mir default
    wthought "Actually, I was fishing for the answer to that acronym."
    wthought "And you fell for it hook, line, and sinker."
    hide mir
    jump SH_Testimony9D

label SH_Testimony9D:
    $ settesti("SH_Testimony9D", "SH_Testimony9C", "SH_Testimony9E", "SH_Press9D","SH_Advice9",4)
    show screen testi
    nangry "YWTPTWTOM? WINGH!"
    jump SH_Testimony9E

label SH_Press9D:
    hide screen testi
    show mir default
    wbase "Ms Neering.{w=0.2} Angela.{w=0.2} Am I a dentist?{w=0.2} Because I sure feel like I'm pulling teeth right now."
    wbase "Do you really want to go through the motions for every one of these?"
    wangry "Couldn't you just, for once, tell me what you meant without me prompting?"
    ndismissive "I refuse to deign to lesser minds. If you want to know what I meant, you can ask."
    wannoy "* sigh *"
    wannoy "Could you please explain what you meant by \"YWTPTWTOM? WINGH!\"?"
    nsmug "Hah! Clearly I was saying \"You want to pin this whole thing on me? Well, it's not gonna happen!\""
    wannoy "Great. Good to know. Moving on."
    hide mir
    jump SH_Testimony9E

label SH_Testimony9E:
    $ settesti("SH_Testimony9E", "SH_Testimony9D", "SH_Testimony9A", "SH_Press9E","SH_Advice9",5)
    show screen testi
    ndef "DDWJAACBAMITAI."
    jump SH_Testimony9A

label SH_Press9E:
    hide screen testi
    show mir default
    wbase "So what does this one mea{nw}"
    ndef "It means \"Darsha's death was just an accident caused by a mistake in the A.I.\""
    wthought "Wow, that was fast. Maybe even Ms Neering is getting sick of this charade."
    whattip "So, you still think Mr. Darsha's death was the result of an accident?"
    nsmug "Of course. Not even your precious scratch marks can prove otherwise."
    nsmug "Perhaps Darsha realized early on that something was wrong, and tried to claw his way out of the trap door."
    nsmug "There's just no evidence that this was anything but a machine error."
    hide mir
    jump SH_Testimony9A

label SH_Advice9:
    hide screen testi
    hide neering
    show mir default
    show ash annoyed at flip
    aannoy "Okay, what the heck is going on here?"
    wbase "It's an entire testimony of acronyms."
    whattip "Either Neering is trying to slow me down because she's afraid I'm on the right track..."
    wannoy "Or she's just trying to mess with me."
    wbase "In either case, we're just going to have to press each statement just to figure out what they mean."
    wbase "Then we'll have to present evidence which contradicts the erroneous, um, acronym."
    aannoy "What a pain in the neck!"
    aannoy "I sure hope Ms Neering is getting a kick out of all this, because otherwise it's just needlessly complicated!"
    hide mir
    hide ash
    show neering smug
    if CurrentTestimony == "SH_Testimony9A":
        jump SH_Testimony9A
    if CurrentTestimony == "SH_Testimony9B":
        jump SH_Testimony9B
    if CurrentTestimony == "SH_Testimony9C":
        jump SH_Testimony9C
    if CurrentTestimony == "SH_Testimony9D":
        jump SH_Testimony9D
    if CurrentTestimony == "SH_Testimony9E":
        jump SH_Testimony9E

label SH_Objection9:
    if present_response == "Back":
        if CurrentTestimony == "SH_Testimony9A":
            jump SH_Testimony9A
        if CurrentTestimony == "SH_Testimony9B":
            jump SH_Testimony9B
        if CurrentTestimony == "SH_Testimony9C":
            jump SH_Testimony9C
        if CurrentTestimony == "SH_Testimony9D":
            jump SH_Testimony9D
        if CurrentTestimony == "SH_Testimony9E":
            jump SH_Testimony9E
    hide screen testi
    if testipart == "SH_Testimony9E" and present_response == "logs":
        jump SH_Success9
    else:
        jump SH_Failure9

label SH_Failure9:
    wgotcha "Sorry Ms Neering, but your web of lies comes crumbling down now!"
    wcasefile "Oh wait."
    wcasefile "Actually, I'm looking at this evidence, and I don't think it actually disproves anything."
    wcasefile "This is very embarrassing. I must have been confused by all the acronyms."
    wholdon "Can I get a do-over?"
    show screen healthBar
    hide neering
    show drang frown gup
    dfrown_gup "I don't know... let's ask Mister Penalty."
    dfrown_gup "Mister Penalty, can Officer Warren get a do-over?"
    $ mc_health -= 1
    call healthDrain from _call_healthDrain_36
    ddef_gup "Ah, I see. Very succinct, Mister Penalty."
    hide screen healthBar
    wthought "All right, all right, I get it."
    if mc_health == 0:
        jump SH_GameOver9
    else:
        hide drang
        hide mir
        show neering smug
        jump SH_Testimony9A

label SH_GameOver9:
    dfrown_gdown "Mister Penalty says you're done for, Warren."
    dfrown_gdown "He says to get out of my crime scene and not come back."
    dfrown_gdown "I think you better do what he says, Warren. He's got that look in his eye."
    hide drang
    show ash standard at flip
    wannoy "Great. Agent Drang is trying to shoo us away with imaginary characters."
    wannoy "Are we really going to let him push us around like this?"
    aunsure "I dunno. I'm pretty scared of what this Mister Penalty guy could do to us."
    aunsure "I think we should get out of here!"
    show black with dissolve
    wthought "And so, the truth disappeared into darkness."
    wthought "Drang failed to bring the real culprit to justice."
    wthought "And I never unraveled the enigma of Base 24."
    jump endgame

label SH_Success9:
    stop music fadeout 1.0
    show mir gotcha
    wgotcha "Ms Neering."
    ngrumble "Oh great. You've got that look in your eyes like you're about to twist my words around on me."
    wcasefile "You are familiar with the feedback logs in your office, correct?"
    ngrumble "I'm familiar with the fact that those are supposed to be confidential."
    wcasefile "I have here the logs pertaining to the hour of Orin Darsha's death."
    wcasefile "It shows 'Tour Mode' deactivating at 5:30 PM."
    wcasefile "In between then and the moment the body was discovered at 6, there's an interesting note here."
    wcasefile "At 5:51, it seems that the safety protocols were manually disabled."
    wobjectionA "Now, why would somebody do something like that..."
    wobjectionC "...unless they were trying to stage an \"accident\"!"
    nangry "Wh-what!?" with shake
    nangry "You think I turned off the safety protocols so that I could kill Darsha?"
    wgotcha "Who else would have the authority to do so?"
    nsmug "I'm afraid your theory is for the birds, officer."
    nsmug "For you see! Although I am indeed responsible for turning off the protocols..."
    nsmug "...I didn't do so until {i}after{/i} Orin was already dead!"
    wbase "You don't expect me to swallow that story, do you?"
    wbase "What possible reason could you have to turn off a vital function like that?"
    ndef "Simple. It was the first step in figuring out what went wrong with the Contraption."
    ndef "I needed to see why the safety protocols malfunctioned so badly, so I had to turn them off to run some tests."
    ndef "I never got around to the rest of the steps, because right around then the power went out."
    hide neering
    show ash thinking at flip
    with dissolve
    athink "What do you think, Randi?"
    athink "Is it possible that the safety protocols were turned off {i}after{/i} Mr. Darsha's death?"
    wbase "No, it's not possible."
    hide ash
    show neering default
    with dissolve

label atThisTIme:
    show screen healthBar
    wbase "It's clear that Orin Darsha was killed after the house's safety protocol was disabled."
    wcasefile "And the proof can be found within the feedback logs."
    wcasefile "Specifically, the entry at this time:"
    menu:
        "5:30 PM":
            wcasefile "Let's take a look at the entry at 5:30 PM: \"Tour Mode Disabled\"."
            wcasefile "This proves, er, that the tour was not going on after 5:30."
            ndef "That point was never in contention, you double-digit IQ score."
            $ mc_health -= 1
            call healthDrain from _call_healthDrain_37
            ndef "You were supposed to be proving that Darsha was killed after the safety protocol was disabled."
            nsmug "I don't blame you for failing, because it is, in fact, impossible to prove."
            if mc_health == 0:
                nsmug "And now, it looks like your time has run out."
                nsmug "Isn't that right, Agent Drang?"
                hide neering
                show drang default gup
                ddef_gup "Yes indeed, suspicious computer."
                jump SH_GameOver9
            else:
                nsmug "But you're free to keep trying, if you so choose."
                nsmug "I enjoy seeing you flounder like this."
                jump atThisTIme
        "5:51 PM":
            wcasefile "Let's take a look at the entry at 5:51 PM: \"Manual Override: Safety Protocols Deactivate.\""
            ngrumble "Isn't that the same entry you just showed me? What's that going to prove?"
            wcasefile "Well, you see, it proves that...oh. Hm."
            wconfused "It proves that the security system went down at 5:51?"
            ngrumble "We already knew that."
            $ mc_health -= 1
            call healthDrain from _call_healthDrain_38
            wbase "Ulp!"
            nsmug "Lucky for you, I like to see you squirm. So I'm going to give you another shot at proving the impossible."
            if mc_health == 0:
                dangry_gdown "No you're not! This has gone on for too long already. In fact..."
                jump SH_GameOver9
            else:
                wthought "I'm so close to the truth, I just know it! But I have to figure out this question first!"
                jump atThisTIme
        "5:52 PM":
            jump neeringsBreakdown1
        "5:58 PM":
            wcasefile "Let's take a look at the entry at 5:58 PM: \"Communications Error. Check Connection\"."
            wcasefile "It's fair to say that this is when the power outage occurred, correct?"
            ndef "Yes, that's right."
            wbase "Well, that leaves 7 minutes between when the security system went off and when the whole house went off."
            wgotcha "More than enough time to kill Darsha with The Dressing Contraption."
            nangry "The time it would take to kill Darsha wasn't in question here, you troglodyte."
            ndismissive "And besides, there was even more time between the tour ending and the security system going offline. 21 minutes, to be exact."
            $ mc_health -= 1
            call healthDrain from _call_healthDrain_39
            ndismissive "If anything, it makes even more sense for Darsha's death to have happened first."
            show mir recoil anim
            wos "Oh!{w=0.4} Oh no!"
            if mc_health == 0:
                ddef_gdown "Oh no indeed, Officer."
                jump SH_GameOver9
            else:
                wthought "This is bad. I should take another look at the evidence..."
                jump atThisTIme

label neeringsBreakdown1:
    hide screen healthBar
    wcasefile "Let's take a look at the entry at 5:52 PM: \"TDC Subroutine Activated.\""
    wbase "When Ash and I found this, we were unsure what TDC could stand for."
    hide mir
    show ash confident
    aconfident "I still think it was \"Timothy, Don't Creep!\""
    hide ash
    show mir gotcha
    wgotcha "But looking at it now, I think it's pretty obvious that TDC stands for \"The Dressing Contraption.\""
    nuneasy "!"
    wcasefile "This subroutine was only activated {i}after{/i} the security system went down."
    wcasefile "And it's the only instance of \"TDC\" anywhere in the hour's logs."
    wbase "The only possible explanation for this..."
    wobjectionA "...is that your entire debugging story is a fabrication!"
    nlaugh "heh" with smallshake
    nlaugh "eh heh heh" with shake
    nlaugh "heh heh heh heh ha hah ha ha hah" with bigshake
    nsmug "Well done, Officer. My great genius plan, you have foiled it."
    nsmug "But don't be too proud of yourself."
    nsmug "What should have been a perfect plan was in fact ruined by one event I could not have foreseen."
    nsmug "Allow me to explain my masterstroke."
    hide mir
    call witness_statement from _call_witness_statement_9
    typing "-- my_testimony_FINAL(1).txt --{fast}"
    ndef "Darsha was trying to shut down the Smart House project, so I had to get rid of him."
    ndef "I turned off the safety protocols and asked him to test out the dressing contraption."
    ngrumble "Everything would have gone according to plan, were it not for that power outage!"
    ngrumble "The house lost power before it could finish disposing of the body."
    ngrumble "Then that vapid fool made sure everyone knew about the dead body in the Smart House."
    nsmug "So I had to improvise a cover story for the murder. I did pretty well, considering the circumstances."

    hide neering
    show mir default
    show drang default gup
    with fade
    ddef_gup "Well, Warren, you've got some unconventional methods, but you sure do get results."
    wthought "Maybe if by 'unconventional methods', you mean 'actually interrogating suspects'."
    ddef_gup "You've managed to find a culprit, find their motive, prove that both of them were lies..."
    ddef_gup "...and then find the person who manufactured both the fake culprit and the fake motive and get them to confess!"
    ddef_gup "All in the span of about three hours!"
    dthink_gdown "Now, of course, I could usually do all that in about two and a half, but still."
    dfrown_gup "So! Are you ready to tie this all up, or are you going to keep poking and prodding."
    dfrown_gup "Keep in mind, the answer to this question will determine if I continue to like you."
    wholdon "Agent Drang, I want to be done here just as much as you..."
    dangry_gup "Nope.{w=0.2} All right.{w=0.2} Stop right there."
    dangry_gup "Unless the end of that sentence is \"so let's book this sucker then go grab some cold ones\" I don't want to hear it."
    wbase "...but I don't think this case is completely wrapped up yet."
    dfrazzled "AAAAAAAAGGGGHHHH! COME ON!" with shake
    dfrazzled "WHAT ELSE COULD YOU POSSIBLY NEED? SHE CONFESSED TO THE MURDER!"
    wbase "Exactly. She confessed to one of the worst crimes imaginable."
    wbase "There should be no further reason for her to lie."
    wbase "So why is there still a clear contradiction in her statement?"
    dos ".{w=0.1} .{w=0.1} .{w=0.1} .{w=0.1} ."
    dangry_gup "Damn it, Warren, now you've got me curious."
    dfrown_gup "Go ahead. Interrogate her. \nI want to see where you're going with this."
    dfrown_gup "But you better satisfy my curiosity, or else."
    wbase "Can do, Agent Drang."
    wthought "In any case, Carlos should be closing in on Neering's location by now."
    wthought "She'll be under arrest soon enough."

label testimony10_intro:
    $ testiLength = 6
    $ current_present = "SH_Objection10"
    $ CurrentTestimony = "SH_Testimony10A"
    $ back_action = CurrentTestimony
    hide screen inventory_screen_button
    scene kitchen
    hide ash
    hide mir
    show neering default
    with fade
    call interrogation from _call_interrogation_11
    play music "BustingLiesAtABriskTempo.ogg" fadein 1.0

    label SH_Testimony10A:
        $ settesti("SH_Testimony10A", None, "SH_Testimony10B", "SH_Press10A","SH_Advice10",1)
        show screen testi
        ndef "Darsha was trying to shut down the Smart House project, so I had to get rid of him."
        jump SH_Testimony10B

    label SH_Press10A:
        hide screen testi
        show mir default
        wbase "It was worth taking a life, just to protect your little project?"
        ndef "You don't understand."
        ndismissive "This house...was my l{nw}"
        wbase "Let me guess...{w=0.2} it was your life's work?"
        ngrumble "Y-{w=0.1}yes...."
        ndef "Years worth of study and research had gone into it."
        ngrumble "To have it shut down, all because some small-minded bureaucrat didn't understand what I was doing here..."
        ndismissive "Well, it simply {i}could not{/i} happen."
        whattip "But wouldn't a death surrounding the project be even more damning?"
        ndef "Once again, you fail to understand."
        ndef "If everything had gone according to plan, there wouldn't have been a {i}death{/i}..."
        ndismissive "Just a...{w=0.1} let's say...{w=0.2} {i}disappearance.{/i}"
        ndismissive "Darsha would have just never showed up for work tomorrow."
        ndef "People would ask questions, sure, but they'd never be able to trace anything back to me."
        ndef "Meanwhile, I could continue work on the house in peace."
        ngrumble "And it would have gone that way, if it weren't for that accursed--"
        ndef "Well, we'll get around to that."
        hide mir
        jump SH_Testimony10B

    label SH_Testimony10B:
        $ settesti("SH_Testimony10B", "SH_Testimony10A", "SH_Testimony10C", "SH_Press10B","SH_Advice10",2)
        show screen testi
        ndef "I turned off the safety protocols and asked him to test out the Dressing Contraption."
        jump SH_Testimony10C

    label SH_Press10B:
        hide screen testi
        show mir angry
        wangry "How could you allow your own creation to be used for evil?"
        ndef "What are you talking about?"
        whattip "HARPER. It's like your child, metaphorically speaking."
        wangry "How could you force it to do something so immoral?"
        ndismissive "It was an evil, yes, but a necessary evil. \nSelf-defense, you might say."
        ndismissive "You've brought up HARPER, so let's consider things from its perspective."
        ndismissive "If Darsha wasn't gotten rid of, then HARPER would have been shut down, effectively killing it."
        ndismissive "So if you told the machine, \"It's either you or him\", what's it going to pick?"
        whattip "Aren't there laws or something which tell a machine to value a human's life over its own?"
        ndef "Maybe in Science Fiction stories, but this is real life, Officer."
        nsmug "Any sentient creature on earth is going to value its own life above somebody else's. It's just nature."
        nsmug "Besides, there are billions of humans out there, but there's only one HARPER."
        hide mir
        jump SH_Testimony10C

    label SH_Testimony10C:
        $ settesti("SH_Testimony10C", "SH_Testimony10B", "SH_Testimony10D", "SH_Press10C","SH_Advice10",3)
        show screen testi
        ngrumble "Everything would have gone according to plan, were it not for that power outage!"
        jump SH_Testimony10D

    label SH_Press10C:
        hide screen testi
        show mir thinking
        wthink "The power outage..."
        wthink "Is that the 'one event you could not have foreseen' you mentioned earlier?"
        ndef "Precisely."
        ngrumble "The power outage... and that pesky style boy... they were rogue elements."
        wbase "Well, you know what they say. The best laid plans of mice and men..."
        nangry "Do not compare me to filthy rodents! I...{w=0.2} am a genius!"
        ndismissive "My expert knowledge of the house's workings allowed me complete control of everything inside these walls."
        ndismissive "I could see everything and do anything. My four walls and a roof of personal godhood."
        ngrumble "But... there was no way to deal with anything {i}outside{/i} these walls."
        ngrumble "I'll have to keep that in mind for next time..."
        wthought "Next time? Does she plan on doing this again?"
        hide mir
        jump SH_Testimony10D

    label SH_Testimony10D:
        $ settesti("SH_Testimony10D", "SH_Testimony10C", "SH_Testimony10E", "SH_Press10D","SH_Advice10",4)
        show screen testi
        ngrumble "The house lost power before it could finish disposing of the body."
        jump SH_Testimony10E

    label SH_Press10D:
        hide screen testi
        show mir hattip
        whattip "How were you planning on getting rid of Orin Darsha's body before you were interrupted?"
        ndef "The house has a garbage disposal here in the kitchen. That's why I'd brought it in here."
        wbase "You really thought a garbage disposal would be enough to get rid of a body?"
        nsmug "This is no average garbage disposal. This is the garbage disposal... of the future!"
        wthought "She's got that look of motherly pride again..."
        ndef "Every piece of garbage is first run through a trash compactor."
        ndef "Then, it is incinerated in an underground furnace."
        ndef "Finally, the remains are submerged in a heavily corrosive chemical solution."
        nsmug "You don't even need to pay for the garbage collector anymore. It's all completely annihilated!"
        wthought "Sounds like the EPA's worst nightmare..."
        ngrumble "But then the power went out, and my infallible plan...{w=0.2} well,{w=0.1} failed."
        hide mir
        jump SH_Testimony10E

    label SH_Testimony10E:
        $ settesti("SH_Testimony10E", "SH_Testimony10D", "SH_Testimony10F", "SH_Press10E","SH_Advice10",5)
        show screen testi
        ngrumble "Then that vapid fool made sure everyone knew about the dead body in the Smart House."
        jump SH_Testimony10F

    label SH_Press10E:
        hide screen testi
        show mir default
        wbase "Couldn't you have still disposed of the body?"
        ndef "What would be the point anymore?"
        ndef "The point of getting rid of a body is so that nobody knows there is a body."
        ndef "When a photo of the body starts trending online, that element is sort of lost."
        ndef "I knew that no matter what, I would be getting police attention sooner or later."
        hide mir
        jump SH_Testimony10F

    label SH_Testimony10F:
        $ settesti("SH_Testimony10F", "SH_Testimony10E", "SH_Testimony10A", "SH_Press10F","SH_Advice10",6)
        show screen testi
        nsmug "So I had to improvise a cover story for the murder. I did pretty well, considering the circumstances."
        jump SH_Testimony10A

    label SH_Press10F:
        hide screen testi
        show mir thinking
        wthink "If by pretty well, you mean you brainwashed and framed a man for your crime."
        ngrumble "I've already killed one man today, Officer."
        ngrumble "Do you really think I'm going to feel bad about incriminating another?"
        ndismissive "At this point, anything I do to cover things up is just a drop in the bucket."
        wbase "I'll admit, I've never heard the \"Defense by Relative Criminality\" before."
        wannoy "But, uh, I wouldn't count on that strategy at your trial."
        hide mir
        jump SH_Testimony10A

    label SH_Advice10:
        hide screen testi
        hide neering
        show mir default
        show ash standard at flip
        adef "Okay, what are we looking for here?"
        wthink "This is a strange one."
        wthink "What we've got here is an embarrassment of riches, as far as confessions go."
        wbase "Neering has laid out her {color=#FF9966}motive{/color}, her {color=#FF9966}scheme{/color}, and even her {color=#FF9966}fatal mistake{/color}."
        wbase "But for whatever reason, she's lying about one of these."
        whattip "So the question becomes... which one?"
        whattip "Is she lying about her {color=#FF9966}motive{/color}, her {color=#FF9966}scheme{/color}, or her {color=#FF9966}mistake{/color}?"
        wbase "If we can answer that question, we can figure out why she's still lying to us."
        hide ash
        hide mir
        show neering standard
        if CurrentTestimony == "SH_Testimony10A":
            jump SH_Testimony10A
        if CurrentTestimony == "SH_Testimony10B":
            jump SH_Testimony10B
        if CurrentTestimony == "SH_Testimony10C":
            jump SH_Testimony10C
        if CurrentTestimony == "SH_Testimony10D":
            jump SH_Testimony10D
        if CurrentTestimony == "SH_Testimony10E":
            jump SH_Testimony10E
        if CurrentTestimony == "SH_Testimony10F":
            jump SH_Testimony10F

    label SH_Objection10:
        if present_response == "Back":
            if CurrentTestimony == "SH_Testimony10A":
                jump SH_Testimony10A
            if CurrentTestimony == "SH_Testimony10B":
                jump SH_Testimony10B
            if CurrentTestimony == "SH_Testimony10C":
                jump SH_Testimony10C
            if CurrentTestimony == "SH_Testimony10D":
                jump SH_Testimony10D
            if CurrentTestimony == "SH_Testimony10E":
                jump SH_Testimony10E
            if CurrentTestimony == "SH_Testimony10F":
                jump SH_Testimony10F
        hide screen testi
        if testipart == "SH_Testimony10A" and present_response == "email":
            jump SH_Success10
        else:
            jump SH_Failure10

    label SH_Failure10:
        wgotcha "You're lying, Ms Neering."
        wdef "About what?"
        wobjectionA "About... this piece of evidence!"
        ndismissive "We've known each other for little more than a couple hours, Officer."
        ndismissive "And yet, I can already tell when you're bluffing."
        ndismissive "Am I profoundly insightful, or are you just obliviously transparent?"
        nsmug "The answer, obviously, is both."
        wannoy "Drat."
        show screen healthBar
        hide neering
        show drang frown gup
        dfrown_gup "Warren, you piqued my curiosity and then completely failed to follow through!"
        $ mc_health -= 1
        call healthDrain from _call_healthDrain_40
        dfrown_gdown "I'm very, very disappointed in you."
        wthought "Sorry, I guess."
        hide screen healthBar
        if mc_health == 0:
            jump SH_GameOver10
        else:
            hide drang
            show neering default
            jump SH_Testimony10A

    label SH_GameOver10:
        djacket_pop "All right, let's wrap it up."
        wholdon "W-what!?" with shake
        djacket_popped "I gave you a fair chance, but you couldn't get results."
        djacket_popped "Now we go back to doing things my way."
        show black with dissolve
        wthought "But Drang's way didn't work."
        wthought "Although he attempted to arrest Ms Neering, she was nowhere to be found."
        wthought "It seemed she had slipped away in all the confusion, never to be seen again."
        wthought "Orin Darsha's killer was never brought to justice."
        wthought "And I never unraveled the enigma of Base 24."
        jump endgame

    label SH_Success10:
        stop music fadeout 1.0
        show mir default
        wbase "So, you killed Orin Darsha because he wanted to shut down the Smart House project?"
        nangry "Yes! How many times do I have to say it?" with shake
        whattip "That's strange, though."
        ngrumble "What now?"
        wcasefile "Do you remember this email exchange? I showed it to you earlier."
        ngrumble "Are you going to bring up the carpeting again?"
        wcasefile "No, I want you to take a look at another part of this exchange."
        wcasefile "It seems there was an ongoing debate about whether to continue the Smart House project..."
        wobjectionA "But it was {i}you{/i}, Ms Neering, who wanted to shut things down."
        nuneasy "W-what? There were emails about...?"
        wobjectionA "It seems strange that you don't remember your own stance in this argument."
        wobjectionA "Even stranger that you don't even remember sending emails on the subject."
        nuneasy "W-well, it's been a stressful couple of days. A lot has slipped my mind."
        nuneasy "Perhaps I really did want to shut down the Smart House. What of it?"
        whattip "Well, why would you want that?"
        whattip "You said yourself that the Smart House was your life's work. You would protect it at all costs."
        wobjectionA "So why would you suddenly want to shut it down?"
        wobjectionA "And why was it so important that you would kill a man over it?"
        wobjectionC "Can you explain that?"
        nos ".{w=0.1} .{w=0.1} .{w=0.1} .{w=0.1} .{w=0.1}"
        hide neering
        show carlos agit at flip
        cagit "CHIIIIEEEEFFFFF!" with bigshake
        wholdon "Carlos? What are you doing back here?"
        wholdon "You're supposed to be looking for..."
        cagit "That's just the thing, Chief."
        cagit "I've been all over this crazy house. I went in that dressing room place, and inside the walls, and..."
        cagit "Angela Neering... is not anywhere in this house!"
        cagit "In fact, I don't think she's anywhere on this base!"
        hide car
        show guard glasses
        gglasses "That's impossible! I have Ms Neering's television here hooked up to the house's local network!"
        hide guard
        show car serious at flip
        cser "Then... where is she?"
        show black with dissolve
        call resetHealth from _call_resetHealth_7
        jump smart_house_act_6_intro
