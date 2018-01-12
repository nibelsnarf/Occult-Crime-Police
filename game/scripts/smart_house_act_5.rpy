label smart_house_act_5_intro:
    ### ACT 5: THE OSTENSIBLE CALAMITY
    $ save_name = "Act 5"
    show black
    typing "September 13th. 10:24 P.M.\nSmart House - Kitchen"
    show kitchen with fade
    drang "This is rich. Now you're saying you had nothing to do with this whole thing."
    drang "And the only reason you confessed is because your brain computer told you to."
    bottomi "Uh...basically?"
    drang "I love this so much."
    drang "You see, back at the office, me and the boys have this whiteboard where we write the dumbest excuses crooks have told us."
    drang "\"My twin did it!\" \"I was possessed by a vengeance ghost!\" That kind of thing."
    drang "Every month we have a little voting party where the worst excuse wins twenty bucks."
    drang "And buddy, you just won me twenty bucks."
    drang "I'm gonna get me a nice fancy dinner thanks to you."
    warren "You don't believe him, then."
    drang "Of course I don't! It's ridiculous!"
    drang "Consider the two explainations here..."
    drang "Either somebody has been hacking this man's brain for the past two hours in order to make him falsely confess..."
    drang "{i}Or{/i} he killed a guy, fessed up, then got cold feet about going to jail."
    warren "I agree the whole thing sounds stupid, but it explains a lot of things."
    warren "The general confusion, the innacuracies, the way his story kept changing..."
    drang "If every guy who couldn't keep his story straight was being mindhacked, then half the guys I've locked up should have a brainchip."
    warren "Look, it can't hurt to investigate this."
    warren "He said his neural implant was relegated to the base's local network, so the hacker must be somewhere in Base 24."
    drang "Great. That narrows the suspects down to, what, a thousand?"
    warren "Let's start by asking Bottomi some questions. He might be able to clarify some things for us."
    warren "And if his story still doesn't add up, we can put him right back on the suspect list."
    drang "Fine. Go ahead."
    drang "In the meantime, I'm going to call my buddies and get them to put this up on the whiteboard."
    "* bleep *"
    drang "Hey! Gordo! Wait until you get a load of {i}this{/i} one!"
    warren "Mr Bottomi, are you feeling well enough to answer some questions?"
    bottomi "S-sure. I'm actually feeling better than I have for a while now..."
    menu:
        "Did You Do It?":
            warren "Why don't we get this one out of the way first:"
            warren "Did you, Louis Bottomi, kill Orin Darsha!"
            bottomi "No. I'm certain of that now."
            bottomi "I visited the Smart House earlier today, that much is true."
            bottomi "But Mr Darsha was already dead when I arrived."
            warren "Why did you go there?"
            bottomi "I... I don't know, come to think of it."
            bottomi "I just suddenly got to thinking that it would be a good idea to check out the kitchen."
            bottomi "H-hey, you don't think I was already being controlled at that point, do you?"
            bottomi "I {i}did{i/} think it was weird how excited I was to splash around in that mud..."
            warren thought "!"
            warren thought "Those footprints..."
            warren thought "Could this mystery culprit have been clever enough to fake incriminating evidence against Mr Bottomi?"
        "Your Confession":
            warren "So, you think somebody else is responsible for your confession earlier?"
            bottomi "Pretty much, yeah..."
            ash "Wow! So they, like, mind controlled you!"
            bottomi "Uh... not exactly..."
            bottomi "It's more like... they gave me fake memories of committing the crime."
            bottomi "From my perspective, it really seemed like I had done it."
            warren "It's fairly lucky for them that you had the integrity to confess."
            warren "I suspect most people would have tried to cover up their crime."
            warren "In fact, it would seem one such person {i}did.{/i}"
            bottomi "I guess that was pretty stupid of me, huh?"
            warren "Not at all. We'd be a lot better off if there were more people like you in the world."
            warren "Are you now able to tell which of your memories are real and which are false?"
            bottomi "Yes, I think so. Now that my connection to the implant is broken, the fake ones are starting to fade."
            bottomi "Sort of like how a dream seems so real in the moment, but you start to forget it when you wake up."
            ### Unlock Conflicting Stories
        "Conflicting Stories":
            warren "Why did your story keep changing so much?"
            bottomi "Well, my memories kept changing."
            bottomi "At the time I thought I had just been remembering things wrong..."
            bottomi "But now I think whoever did this was making new memories to counter your arguments."
            bottomi "Whenever you pointed out a flaw in my story, it genuinely hurt my head."
            bottomi "From my perspective, it was like you had just proven my own memories false."
            bottomi "It would seem like reality as I knew it was falling apart..."
            bottomi "And then, just like that, I would remember something new that explained everything."
            bottomi "It was almost a relief, even though it confirmed that I was the killer."
            warren "I see. But - wait a minute..."
            warren "If the true culprit was counter-programming you against my arguments..."
            warren "Doesn't that mean they were listening in on our conversation?"
            bottomi "W-well, hey, you're right!"
            bottomi "But wait... it's just us in the house, right? How could someone be listening?"
            warren "If they had access to your brain, then maybe they were listening through your ears..."
            ash "Or maybe they've also got access to the surveilance equipment built into this house."

    warren "Thank you, Lou. This has been very helpful."
    guard "Excuse me! Sheriff Warren!"
    warren "You again?"
    guard "Ms Angela Neering wishes to speak with you regarding the murder!"
    warren "Oh, of course. Where is she?"
    guard "Don't worry! I'll bring her to you!"
    warren "Uh, thanks."
    warren thought "Wait... \"bring her to you\"?"
    # Guard wheels in TV
    warren "What in the..."
    # TV turns on, no picture
    neering "Hello, Sherrif."
    neering "I've come because I thought I could - wait, can you see me?"
    warren "I'm sorry... what am I supposed to be seeing here?"
    neering "GUARD, GET OVER HERE! YOU SET THE TV TO THE WRONG INPUT, YOU MORON!"
    guard "Sorry! Sorry!"
    guard "I don't get it! I have it set to HDMI 1 and everything..."
    neering "Well keep trying one until it works!"
    guard "Oh! There we go!"
    neering "Great. Now get out of my sight!"
    guard "Y-yes, ma'am!"
    neering "Now, Sherrif. You can see me now, yes?"
    warren "I see a mid-2000's av club setup with your face on it, if that's what you mean."
    warren "I was under the impression that you would be coming to speak with me {i}in person{/i}."
    neering "TYM, I suppose!"
    warren "TYM?"
    neering "That's Your Mistake."
    neering "See, as much as I wish to help with your investigation, I'm still incredibly busy fixing this house."
    neering "I'm sure you understand that my life's work is a little bit more important."
    warren "Than solving a {i}murder?{/i}"
    neering "Well, see, here's the thing about that..."
    warren thought "Oh boy, here we go."
    warren "Agent Drang, I think you're going to want to hear this."
    drang "What is it? Are you going to tell me that this Television Woman is the killer?"
    neering "Well... the thing is..."
    neering "I'm... sorta.... the one who hacked that guy's neural implant..."
    drang "WHAAAAT!?"
    drang "YOU MEAN HIS ASININE FAKE MEMORIES EXCUSE WAS REAL?"
    neering "Yyyeaaaahhhhhh....."
    drang "I need a drink."
    drang "Hey! Medicine Man! Whatshisface!"
    carlos "Who, me?"
    drang "Give me that!"
    carlos "No! My Marg!"
    drang " * gulp *  * gulp *  * gulp *"
    drang " * spfffphhffhhpth * "
    drang "WHAT THE HELL WAS THAT?"
    carlos "Uh, a margarita. What do you think it was?"
    drang "B-but there's no tequila in this!"
    drang "Have... HAVE YOU BEEN DRINKING STRAIGHT MARGARITA MIX THIS ENTIRE TIME!?"
    carlos "You didn't think I was really drinking on the job, did you?"
    drang "Somehow... this is actually worse than if you {i}were{/i}..."
    warren "Ms Neering... I'm not sure if you understand what you just said..."
    warren "If you're the one who made Louis Bottomi confess to the murder..."
    warren "...Wouldn't that make {i}you{/i} the true killer?"
    neering "What? No. No no no no."
    neering "See, there's something you don't know about Orin Darsha's death."
    neering "The truth is... it was {color=red}an accident.{/color}"
    warren "An accident? What, did he fall down the stairs?"
    neering "No, nothing like that. It was... well... it was a malfunctioning piece of tech. Here in the house."
    warren "Oh, do you mean..."
    menu:
        "...The Grabber Hands?":
            warren "...The Grabber Hands?"
            neering "No. Although, not to brag or anything, they certainly {i}could{/i} kill a man."
            warren "That is... an interesting thing to brag about."
            neering "What can I say? I'm proud of my children."
            neering "No, it was The Dressing Contraption where poor Mr Darsha met his end."
            warren thought "That's right... we found that shoe which proved he was in there."
        "...The Dressing Contraption?":
            warren "...The Dressing Contraption?"
            warren "After all, we found his shoe in there while investigating."
            neering "Yes, that is the fateful place where poor Mr Darsha met his end."
        "... The Security System?":
            warren "... The Security System?"
            neering "No. Although, not to brag or anything, it certainly {i}could{/i} kill a man."
            warren "That is... an interesting thing to brag about."
            neering "What can I say? I'm proud of my children."
            neering "No, it was The Dressing Contraption where poor Mr Darsha met his end."
            warren thought "That's right... we found that shoe which proved he was in there."

    warren "But how is a glorified wardrobe even capable of killing a man?"
    neering "Hey, any part of a house can be dangerous!"
    neering "And, as it turns out, a machine which forces clothes onto a human body is also dangerous..."
    neering "But, I mean, it was only a teensy weensy rounding error."
    neering "How was I supposed to know that something like that would be enough to make it break his neck?"
    warren "I...see."
    warren "Carlos, can I talk to you over here for a second?"
    carlos "Sure, Chief."
    neering "?"
    warren "I don't know if Ms Neering is aware of this, but she's already confessed to several crimes."
    warren "Maybe she thinks that since Mr Darsha's death was an accident, she isn't culpable."
    warren "But since it's her own invention which killed him, it counts as criminally negligent manslaughter."
    warren "Not to mention the fact that she tampered with a crime scene and obstructed a murder investigation."
    carlos "Shoot, you're right."
    carlos "Well, we can't tell her now. She might bolt before we have a chance to arrest her."
    warren "Exactly. That's why I need you to go find her."
    carlos "Me?"
    warren "I've got to stay here and keep her talking so that you can track her down."
    carlos "You mean I get to place her under citizen's arrest?"
    warren "Uh, you don't need to do that."
    warren "You work for the Sheriff's Department. You're already authorized to do the regular kind of arrests."
    carlos "I know, but citizen's arrest always sounded so cool!"
    warren "Focus, Tsukada! You're the only one I can trust with this."
    carlos ". . . I won't let you down, Chief."
    carlos os "BOY DO I HAVE TO GO TO THE BATHROOM"
    carlos os "LET ME JUST DUCK OUT AND MAKE MY WAY THERE"
    carlos os "TO THE BATHROOM, THAT IS"
    carlos os "WHICH IS WHERE I'M GOING"
    warren "* sigh *"
    neering "He better not go in any of the Smart House bathrooms..."
    neering "The pipes aren't actually connected to anything yet."
    drang "THEY AREN'T!?"
    neering "No, they're not. Why do you ask?"
    drang ". . . . No reason."
    warren "Ms Neering, can you tell me more about this accident?"
    neering "WYS."
    menu:
        "Where's Your Soviergnity?":
            warren "Where's Your Soviergnity?"
            neering "What? No! What would that even mean?"
            warren "You know, like, what's your authority here?"
            warren "I thought maybe you were asking if I was in charge here."
            neering "No. Obviously it was \"Whatever You Say\"."
            warren "Fine. Sheesh."
            neering "You all need to get on my level."

        "Whatever You Say?":
            warren "Whatever You Say?"
            neering "Yes! Thank you!"
            neering "Finally someone here speaks plain english!"
            warren thought "Honestly, that was a complete shot in the dark."
            warren thought "Glad it worked out, I guess."

        "Cram it with the acronyms already!":
            warren "Cram it with the acronyms already!"
            neering "I'm not going to let some mouth-breather lower my language to their level."
            neering "Either figure out what I'm saying on your own, or let me explain it to you."
            neering "And by the way, it was \"Whatever You Say\"."
            warren thought "See, how on earth was I supposed to guess that?"

    # Eyewitness Statement ANIMATION
    typing "-- my_testimony.txt --{fast}"
    neering "After the tour, Darsha came to ash me a few questions about the Smart House."
    neering "He, of his own volition, decided to test out The Dressing Contraption."
    neering "Needless to say, it didn't go so well for him."
    neering "I knew that an accident on the day of the Smart House's unveiling would be bad press."
    neering "So I framed that buffoon with the neural implant and tricked him into confessing."

    #fade out, fade in
    ash "All right, what's our M.O. right now?"
    warren "We just need to keep her talking long enough that Carlos can figure out where she's holed up."
    warren "And, if possible, find any holes in her story."
    ash "But shouldn't Ms Neering's statement here be \"the truth\", so to speak?"
    warren "See, I thought so too... but something in her story doesn't line up for me."
    ash "Okay, let's see if we can figure out what that is!"
    drang "WARREN!"
    drang "YOU BETTER FIX THIS, QUICK!"
    warren "F-fix what?"
    drang "This... this whole case!"
    drang "We had everything wrapped up all neat and tidy!"
    drang "But then you just had to go picking at every little scab you saw..."
    drang "And now we got computer women and mind control and all this other crap!"
    drang "DO YOU KNOW HOW MUCH PAPERWORK I'M GOING TO HAVE TO DO NOW?"
    drang "I HAVE TO FILL OUT THREE EXTRA FORMS ALONE, JUST FOR THE MIND CONTROL!"
    warren "Your office has specific paperwork related to mind control?"
    drang "OF COURSE WE DO!"
    drang "IT'S THE FBI, ISN'T IT?"
    drang "NOW BRING ME SOMEONE TO ARREST BEFORE I JUST PICK ONE AT RANDOM!"
    warren thought "Boy, I'll bet internal affairs would have a field day with this guy..."

$ current_present = "SH_Testimony8B"
$ back_action = "CurrentTestimony"

label SH_Testimony8A:
    $ settesti("SH_Testimony8A", None, "SH_Testimony8B", "SH_Press8A","SH_Advice8")
    show screen testi
    neering "After the tour, Darsha came to ash me a few questions about the Smart House."
    jump SH_Testimony8B

label SH_Press8A:
    hide screen testi
    warren "Shouldn't the tour have told him everything he needed to know?"
    neering "That tour was more geared towards... pedestrians."
    neering "A lot of concepts were dumbed down so that your average simpleton could understand them."
    neering "It's a dreary yet neccesary process when selling to... {i}the common masses.{/i}"
    warren thought "You didn't need to shudder like that when you said \"the common masses\"."
    warren thought "As a common mass myself, I take offense to that."
    warren "What kind of things was Mr Darsha asking about?"
    neering "Money, of course."
    neering "How much does each A.R.M. cost? What's the price-to-benefit ratio for each feature?"
    neering "It's exhausting!"
    neering "I build that man a revolution in home living and he wants to know where we can cut costs."
    neering "Would you cut costs... on a sunset?"
    warren thought "I swear I must have run into the annual narcissist convention or something..."
    jump SH_Testimony8B

label SH_Testimony8B:
    $ settesti("SH_Testimony8B", "SH_Testimony8A", "SH_Testimony8C", "SH_Press8B","SH_Advice8")
    show screen testi
    neering "He, of his own volition, decided to test out The Dressing Contraption."
    jump SH_Testimony8C

label SH_Press8B:
    hide screen testi
    warren "You sure seem, uh, {i}insistent{/i} that it was Darsha's own decision to use the contraption."
    warren "Why is that?"
    neering "I just don't want anyone here thinking that I {i}made{/i} Darsha do anything."
    neering "Otherwise I just know some clown at the insurance agency is gonna be like,"
    neering "\"Oh, you were the one who made him try it out, so it's your fault that he died!\""
    neering "So let's just set the record straight, here and now: Darsha {i}wanted{/i} to test it."
    neering "He was all riled up about how he didn't get to try it during the tour, so he made me run him through it."
    neering "If I'd had time beforehand, I could have noticed the bug in the contraption and fixed it."
    neering "This is only a prototype, after all. It's not fully polished."
    neering "So really it's on him that he died, not me."
    warren thought "That is... {i}super{/i} not how culpability works."
    warren thought "And besides, did Darsha {i}really{/i} intend to go through with that test?"

    jump SH_Testimony8C

label SH_Testimony8C:
    $ settesti("SH_Testimony8C", "SH_Testimony8B", "SH_Testimony8D", "SH_Press8C","SH_Advice8")
    show screen testi
    neering "Needless to say, it didn't go so well for him."
    jump SH_Testimony8D

label SH_Press8C:
    hide screen testi
    warren "Uh, care to elaborate on that point?"
    neering "Sure, but it's very technical... and graphic."
    neering "Basically what happened is there was a slight rounding error in the contraption's algorithm."
    neering "An easily repairable mistake, if I'd just been given time to troubleshoot."
    neering "As a result, it mistook Mr Darsha's skull for a nightcap which needed to be removed."
    neering "I didn't see any of this, mind you."
    neering "This is all extrapolated from the state of his body, as well as my own knowledge of the algorithm."
    neering "It's just as well I didn't see any of it, because this next bit gets a little grisly."
    neering "Essentially, in attempting to remove this \"nightcap\", the contraption dislocated his cervical vertebrae."
    neering "That means it broke his neck, by the way."
    warren "I know what a cervical vertebrae is."
    neering "Now, you already know that the house's sensors can't recognize a human after they've died."
    neering "So when the house realized it was holding unfamiliar matter, it executed its error routine..."
    neering "Which, in this case, is to drop the foriegn matter through the exit hatch."
    warren "Well, that certainly explains the bruises and the broken neck..."
    warren "But what about the victim's stab wound?"
    neering "I'm getting to that!"
    jump SH_Testimony8D

label SH_Testimony8D:
    $ settesti("SH_Testimony8D", "SH_Testimony8C", "SH_Testimony8E", "SH_Press8D","SH_Advice8")
    show screen testi
    neering "I knew that an accident on the day of the Smart House's unveiling would be bad press."
    jump SH_Testimony8E

label SH_Press8D:
    hide screen testi
    warren "That's all it was to you? Bad press?"
    neering "Well, think about it from my perspective."
    neering "This house... is my life's work."
    neering "It is the culmination of all of my studies in machine learning, bionic engineering, and interior design."
    neering "And today was the day where I would finally unveil the fruits of my labor to the world."
    neering "How could I let something so trivial as an accidental fatality ruin this moment?"
    neering "If the press finds a dead body in the kitchen of my invention, what's the headline going to be tomorrow?"
    neering "Is it going to be \"Amazing Genius Improves Everyone's Lives With Great Invention\"?"
    neering "Or is it going to be \"Dangerous House Does A Murder, Is Broken\"?"
    neering "I just {i}tweaked{/i} the headline to \"Crazy Guy Kills Boss In Super Cool House\"."
    neering "This is what we in the business like to call \"Public Relations\"."
    warren thought "I'll be sure to write \"Wanted for Public Relations\" on the arrest warrent, then."
    jump SH_Testimony8E

label SH_Testimony8E:
    $ settesti("SH_Testimony8E", "SH_Testimony8D", "SH_Testimony8A", "SH_Press8E","SH_Advice8")
    show screen testi
    neering "So I framed that buffoon with the neural implant and tricked him into confessing."
    jump SH_Testimony8A

label SH_Press8E:
    hide screen testi
    warren "So you're the one that stuck the knife in the victim's back?"
    neering "No, no, of course not."
    neering "I had the house do it."
    warren "But what about the footprints made by Louis Bottomi?"
    neering "Easy. I splashed some mud around outside the house..."
    neering "Then I \"convinced\" the stooge to take a stroll around."
    neering "It was child's play, really."
    warren "But why such an elaborate ruse?"
    warren "Why bother with all of this if your deception was so full of contradictions?"
    neering "Well, to be honest, I didn't figure you cops would be quite so inquiring."
    neering "I figured if you saw a knife in someone's back and a guy saying \"I did it\"..."
    neering "Then you wouldn't bother yourself with anything that didn't quite line up."
    warren "I'm afraid that while your technique might have worked on {i}some people...{/i}"
    drang ". . . Hey! What are you looking at me for!?"
    warren "...it didn't quite work on me."
    neering "I'll keep that in mind for the next time I need to fabricate a crime scene. I guess."
    jump SH_Testimony8A

label SH_Advice8:
    hide screen testi
    ash "Okay, shoot. I'm stumped."
    ash "I feel like we should be looking for some flaw in her description of Mr Darsha's death."
    ash "Or maybe something with her cover-up of the whole thing."
    warren "It's much simpler than that, really."
    warren "We don't need to destroy Ms Neering's entire story. Not yet, at least."
    warren "All we need to do is answer one central question: {color=red}Did Orin Darsha really intend to use the contraption?{/color}"
    warren "If we can figure that out, we should be able to find the chink in the armor we need."
    ash "Got it!"
    jump CurrentTestimony

label SH_Objection8:
    hide screen testi
    if testipart == "SH_Testimony8B" and present_response == "Scratch Marks":
        jump SH_Success8
    else:
        jump SH_Failure8

label SH_Failure8:
    warren "I've got a piece of evidence here that's gonn{nw}"
    neering "Let me see that."
    neering ". . . ."
    neering "Using a complex detection algorithm, I've managed to find 16 flaws in your so-called piece of evidence."
    neering "Mathematically speaking, there is no way this has any bearing on my testimony whatsoever."
    neering "Why don't you just put that thing away? You're only embarrasing yourself."
    warren "ggghhhhAAAAAHHH!"
    $ mc_health -= 1
    warren "I can feel Drang's glare on me from halfway across the room."
    if mc_health == 0:
        jump SH_GameOver8
    else:
        jump SH_Testimony8A

label SH_GameOver8:
    drang "Aaaaand it looks like we're finished here."
    drang "I've been about as patient as one could reasonably expect from a man such as myself."
    drang "But now I'm just going to pick somebody at random and arrest them for something."
    drang "Eenie meenie miney mo..."
    ash "Aah! Let's get out of here!"
    warren "B-but we still haven't found out the truth here!"
    ash "Hey, I'm big on the truth too, but I don't know if getting locked up by this guy is worth it."
    warren "What about Mr Bottomi? Heck, what about Carlos?"
    drang "...my mother said to pick the very best one..."
    warren "Okay, let's go."
    show black with fade
    warren thought "And so, the truth disappeared into darkness."
    warren thought "Drang failed to bring the real culprit to justice."
    warren thought "And I never unravelled the enigma of Base 24."
    jump endgame

label SH_Success8:
    warren "You know, Ms Neering, I'd really hoped that breaking Mr Bottomi out of his trance would resolve this whole affair."
    warren "But it seems you are determined to draw this out as much as possible."
    neering "What are you babbling on about?"
    warren "You claim that Mister Darsha was fully willing to test out The Dressing Contraption."
    warren "Not just that, but that he himself was the one who insisted on trying it."
    warren "But why would a willing participant leave scratch marks on the carpet leading to the trap door?"
    neering "W-what's this now?"
    warren "Scratch marks. Bloody scratch marks leading up to the point where the floor opens up."
    warren "Now, the only way I can think to explain something like that..."
    warren "Is if someone were desperately attempting to avoid falling into The Dressing Contraption!"
    neering "Yipes!"
    warren "Woah. I didn't know that Ms Neering was {i}capable{/i} of being caught off guard."
    ash "Or that anybody could unironically say \"Yipes\"."
    warren "So, Angela... care to explain how those scratch marks got there?"
    neering "H-hah! Hah! You think you've made some brilliant deduction?"
    neering "Who's to say those scratch marks are from today?"
    warren "Huh?"
    neering "The Smart House project has been in development for years now."
    neering "That's hundreds of days during which somebody could have scratched up the carpeting."
    neering "You couldn't possibly have proof that those marks are recent."
    warren "As a matter of fact... I do."
    neering "IMPOSSIBLE!"
    neering "Well, I'm a woman of science. I should never call anything \"impossible\"."
    neering "STATISTICALLY IMPROBABLE!"
    warren "That may be, but the odds are in my favor tonight."

label scratchesProof:
    warren "Here is the proof that the scratches in the carpet are from today."
    $current_present = "scratchesProofPresent"
    show screen present_evidence_screen

label scratchesProofPresent:
    if present_response == "NeeringsEmail":
        jump scratchesProofSuccess
    else:
        neering "What is this. This is nothing. This is a clown's mistake."
        warren "No...you see... it proves that.......{nw}"
        $ mc_health -= 1
        warren "GWAAAAH!"
        neering "It seems the laws of statistics are on my side after all!"
        warren thought "Drat. I really thought I had that one."
        if mc_health == 0:
            jump SH_GameOver8
        else:
            warren "Let's give this one more shot."
            jump scratchesProof

label scratchesProofSuccess:
    warren "You must have been very busy the past few days, Ms Neering."
    neering "Why, yes. I have bee- oh, wait. This is a lead-in to whatever your point is."
    warren "Busy enough, it seems, to forget about this email exchange between you and Orin Darsha."
    neering "You went through my emails? You can't do that!"
    warren "We'll talk about what I can and cannot do later on."
    warren "For now, let's take a look at this particular section."
    warren "\"The new carpets will be ready in time for the tours. I've got contractors coming in the day before the event.\""
    neering "!"
    warren "As you can see, the scratch marks on the carpet must be from today..."
    warren "BECAUSE THE CARPETING WASN'T EVEN HERE BEFORE YESTERDAY!"
    neering "Noooooooooo!"
    neering "This... this doesn't change anything, you know!"
    neering "Orin Darsha's death was still an accident!"
    neering "And I'll prove it... with your precious \"testimony\"!"

    # Eyewitness Statement ANIMATION
    typing "-- my_testimony_FINAL.txt --{fast}"
    # There are many explainations for the scratches in the carpet.
    neering "TAMEFTSITC."
    # Perhaps one of the contractors installing the carpet did it by mistake.
    neering "POOTCITCDIBM."
    # Besides, a couple of scratch marks doesn't prove anything.
    neering "BACOSMDPA."
    # You want to pin this whole thing on me? Well, it's not gonna happen!
    neering "YWTPTWTOM? WINGH!"
    # Darsha's death was just an accident caused by a mistake in the AI.
    neering "DDWJAACBAMITAI."

    # fade out, fade in
    warren ". . . . . . . . . ."
    warren "WHAT THE HELL WAS THAT?"
    neering "My testimony."
    warren "That wasn't a testimony! That was..."
    menu:
        "...bad dadaist poetry!":
            warren "...bad dadaist poetry!"
        "...syllable puke!":
            warren "...syllable puke!"
        "...a malfunctioning junior jumble!":
            warren "...a malfunctioning junior jumble!"

    neering "As a matter of fact, it was a series of acronyms."
    neering "You've taken enough of my time as it is. I can't afford to waste time speaking every sentence."
    warren thought "Again with the acronyms! At this point, I think she's just doing it to tick me off."

    # Interrogation Animation
$ current_present = "ObjectionLabel"
$ back_action = "CurrentTestimony"

label SH_Testimony9A:
    $ settesti("SH_Testimony9A", None, "SH_Testimony9B", "SH_Press9A","SH_Advice9")
    show screen testi
    neering "TAMEFTSITC."
    jump NextTestimony

label SH_Press9A:
    hide screen testi
    warren "I'm going to have to ask you to clarify what that meant."
    neering "What a complete waste of my time."
    neering "Obviously I said, \"There are many explainations for the scratches in the carpet.\""
    neering "See, the \"T\" stands for \"There\", the \"A\" stands for \"are\", the-{nw}"
    warren "I wasn't confused about the {i}concept{/i} of acronyms!"
    warren "Let's just move on..."
    jump NextTestimony

label SH_Testimony9B:
    $ settesti("SH_Testimony9B", "SH_Testimony9A", "SH_Testimony9C", "SH_Press9B","SH_Advice9")
    show screen testi
    neering "POOTCITCDIBM."
    jump NextTestimony

label SH_Press9B:
    hide screen testi
    warren "You can't really expect me to be able to guess what you're saying, can you?"
    neering "Of course not. For a clever enough mind, there should be no guesswork involved."
    neering "For example: there are only a certain number of words that begin with the letter P."
    neering "From there, only a certain number of letters which begin with O can follow those words."
    neering "Following the chain of causality from there, one can logically arive at the only possible combination."
    neering "Which, in this case, is \"Perhaps one of the contractors installing the carpet did it by mistake.\""
    warren "You honestly think the contractor is the one who left those scratches?"
    neering "Maybe. Maybe not. But there's reasonable doubt, for certain."
    warren "We could check for DNA traces in the carpet fibers!"
    neering "Perhaps, but HARPER is impressively thorough when it cleans."
    neering "I doubt there would be any traces left behind."
    neering "Not that it matters anyway..."

    jump NextTestimony

label SH_Testimony9C:
    $ settesti("SH_Testimony9C", "SH_Testimony9B", "SH_Testimony9D", "SH_Press9C","SH_Advice9")
    show screen testi
    neering "BACOSMDPA."
    jump NextTestimony

label SH_Press9C:
    hide screen testi
    warren "Ah, well this one is obvious."
    warren "You said \"Banana apple cucumber orange salad mango durian pear apricot.\""
    neering "What? No! How could you possibly come to that conclusion?"
    neering "{i}Clearly{/i} it was \"Besides, a couple of scratch marks doesn't prove anything.\""
    neering "Honestly, I don't know where you got all those fruit names fro- oh."
    neering "You were messing with me, weren't you?"
    warren thought "Actually, I was fishing for the answer to that acronym."
    warren thought "And you fell for it hook, line, and sinker."
    jump NextTestimony

label SH_Testimony9D:
    $ settesti("SH_Testimony9D", "SH_Testimony9C", "SH_Testimony9E", "SH_Press9D","SH_Advice9")
    show screen testi
    neering "YWTPTWTOM? WINGH!"
    jump NextTestimony

label SH_Press9D:
    hide screen testi
    warren "Ms Neering. Angela. Am I a dentist? Because I sure feel like I'm pulling teeth right now."
    warren "Do you really want to go through the motions for every one of these?"
    warren "Couldn't you just, for once, tell me what you meant without me prompting?"
    neering "I refuse to deign to lesser minds. If you want to know what I meant, you can ask."
    warren "* sigh *"
    warren "Could you please explain what you meant by \"YWTPTWTOM? WINGH!\"?"
    neering "Hah! Clearly I was saying \"You want to pin this whole thing on me? Well, it's not gonna happen!\""
    warren "Great. Good to know. Moving on."
    jump NextTestimony

label SH_Testimony9E:
    $ settesti("SH_Testimony9E", "SH_Testimony9D", "SH_Testimony9A", "SH_Press9E","SH_Advice9")
    show screen testi
    neering "DDWJAACBAMITAI."
    jump NextTestimony

label SH_Press9E:
    hide screen testi
    warren "So what does this one mea{nw}"
    neering "It means \"Darsha's death was just an accident caused by a mistake in the AI.\""
    warren thought "Wow, that was fast. Maybe even Ms Neering is getting sick of this charade."
    warren "So, you still think Mr Darsha's death was the result of an accident?"
    neering "Of course. Not even your precious scratch marks can prove otherwise."
    neering "Perhaps Darsha realized early on that something was wrong, and tried to claw his way out of the trap door."
    neering "There's just no evidence that this was anything but a machine error."
    jump NextTestimony

label SH_Advice9:
    hide screen testi
    ash "Okay, what the heck is going on here?"
    warren "It's an entire testimony of acronyms."
    warren "Either Neering is trying to slow me down because she's afraid I'm on the right track..."
    warren "Or she's just trying to mess with me."
    warren "In either case, we're just going to have to press each statement just to figure out what they mean."
    warren "Then we'll have to present evidence which contradicts the erroneous, um, acronym."
    ash "What a pain in the neck!"
    ash "I sure hope Ms Neering is getting a kick out of all this, because otherwise it's just needlessly complicated!"
    jump CurrentTestimony

label SH_Objection9:
    hide screen testi
    if testipart == "SH_Testimony9E" and present_response == "SecurityLogs":
        jump SH_Success9
    else:
        jump SH_Failure9

label SH_Failure9:
    warren "Sorry, Ms Neering, but your web of lies comes crumbling down now!"
    warren "Actually, I'm looking at this evidence, and I don't think it actually disproves anything."
    warren "This is very embarrasing. I must have been confused by all the acronyms."
    warren "Can I get a do-over?"
    drang "I don't know... let's ask Mister Penalty."
    drang "Mister Penalty, can Officer Warren get a do-over?"
    $ mc_health -= 1
    drang "Ah, I see. Very succinct, Mister Penalty."
    warren thought "All right, all right, I get it."
    if mc_health == 0:
        jump SH_GameOver9
    else:
        jump SH_Testimony9A

label SH_GameOver9:
    drang "Mister Penalty says you're done for, Warren."
    drang "He says to get out of my crime scene and not come back."
    drang "I think you better do what he says, Warren. He's got that look in his eye."
    warren "Great. Agent Drang is trying to shoo us away with imaginary characters."
    warren "Are we really going to let him push us around like this?"
    ash "I dunno. I'm pretty scared of what that Mister Penalty guy could do to us."
    ash "I think we should get out of here!"
    show black with fade
    warren thought "And so, the truth disappeared into darkness."
    warren thought "Drang failed to bring the real culprit to justice."
    warren thought "And I never unravelled the enigma of Base 24."
    jump endgame

label SH_Success9:
    warren "Ms Neering."
    neering "Oh great. You've got that look in your eyes like you're about to twist my words around on me."
    warren "You are familiar with the feedback logs in your office, correct?"
    neering "I'm familiar with the fact that those are supposed to be private."
    warren "I have here the logs pertaining to the hour of Orin Darsha's death."
    warren "It shows 'Tour Mode' deactivating at 5:30 PM."
    warren "In between then and the moment the body was discovered at 6, there's an interesting note here."
    warren "At 5:51, it seems that the safety protocols were manually disabled."
    warren "Now, why would somebody do something like that..."
    warren "...unless they were trying to stage an \"accident\"!"
    neering "Wh-what!?"
    neering "You think I turned off the safety protocols so that I could kill Darsha?"
    warren "Who else would have the authority to turn those off?"
    neering "I'm afraid your theory is for the birds, officer."
    neering "For you see! Although I am indeed responsible for turning off the protcols..."
    neering "...I didn't do so until {i}after{/i} Orin was already dead!"
    warren "You don't expect me to swallow that story, do you?"
    warren "What possible reason could you have to turn off a vital function like that?"
    neering "Simple. It was the first step in figuring out what went wrong with the Contraption."
    neering "I needed to see why the safety protocols malfunctioned so badly, so I had to turn them off to run some tests."
    neering "I never got around to the rest of the steps, because right around then the power went out."
    ash "What do you think, Randi?"
    ash "Is it possible that the safety protocols were turned off {i}after{/i} Mr Darsha's death?"
    warren "No, it's not possible."

label atThisTIme:
    warren "It's clear that Orin Darsha was killed after the house's safety protocol was disabled."
    warren "And the proof can be found within the feedback logs."
    warren "Specifically, the entry at this time:"
    menu:
        "5:30 PM":
            warren "Let's take a look at the entry at 5:30 PM: \"Tour Mode Deactivated\"."
            warren "This proves, er, that the tour was not going on after 5:30."
            neering "That point was never in contention, you double-digit IQ score."
            $ mc_health -= 1
            neering "You were supposed to be proving that Darsha was killed after the safety protocol was disabled."
            neering "I don't blame you for failing, because it is, in fact, impossible to prove."
            if mc_health == 0:
                neering "And now, it looks like your time has run out."
                neering "Isn't that right, Agent Drang?"
                drang "Yes indeed, suspicious computer."
                jump SH_GameOver9
            else:
                neering "But you're free to keep trying, if you so choose."
                neering "I enjoy seeing you flounder like this."
                jump atThisTIme
        "5:51 PM":
            warren "Let's take a look at the entry at 5:51 PM: \"Manual Override: Security System Disabled.\""
            neering "Isn't that the same entry you just showed me? What's that going to prove?"
            warren "Well, you see, it proves that...oh. Hm."
            warren "It proves that the security system went down at 5:51?"
            neering "We already knew that."
            warren "Ulp!"
            neering "Lucky for you, I like to see you squirm. So I'm going to give you another shot at proving the impossible."
            if mc_health == 0:
                drang "No you're not! This has gone on for too long already. In fact..."
                jump SH_GameOver9
            else:
                warren thought "I'm so close to the truth, I just know it! But I have to figure out this question first!"
                jump atThisTIme
        "5:52 PM":
            jump neeringsBreakdown1
        "5:58 PM":
            warren "Let's take a look at the entry at 5:58 PM: \"Communication Error. Please Check Connection\"."
            warren "It's fair to say that this is when the power outage occurred, correct?"
            neering "Yes, that's right."
            warren "Well, that leaves 7 minutes between when the security system went off and when the whole house went off."
            warren "More than enough time to kill Darsha with The Dressing Contraption."
            neering "The time it would take to kill Darsha wasn't in question here, you troglodyte."
            neering "And besides, there was even more time between the tour ending and the security sytem going offline. 21 minutes, to be exact."
            $ mc_health -= 1
            neering "If anything, it makes even more sense for Darsha's death to have happened first."
            warren "Oh! Oh no!"
            if mc_health == 0:
                drang "Oh no indeed, Officer."
                jump SH_GameOver9
            else:
                warren thought "This is bad. I take another look at the evidence..."
                jump atThisTIme

label neeringsBreakdown1:
    warren "Let's take a look at the entry at 5:52 PM: \"TDC Subroutine Activated.\""
    warren "When Ash and I found this, we were unsure what TDC could stand for."
    ash "I still think it was \"Timothy, Don't Creep!\""
    warren "But looking at it now, I think it's pretty obvious that TDC stands for \"The Dressing Contraption.\""
    neering "!"
    warren "This subroutine was only activated {i}after{/i} the security system went down."
    warren "And it's the only instance of \"TDC\" anywhere in the hour's logs."
    warren "The only possible explaination for this..."
    warren "...is that your entire debugging story is a fabrication!"
    neering "heh"
    neering "eh heh heh"
    neering "heh heh heh heh ha hah ha ha hah"
    neering "HAAAAAAH HAH HAH HAHHHHH HAH HAH HAH HAH"
    neering "HOO HEE HEE HEE HA HAW HOH HEH HA HA HA HA HAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    neering "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    neering "AAAAAAAAAaaaaaaaaaaaaahhhhh......\nhah. hah. hah."
    neering "Well done, Officer. My great genius plan, you have foiled it."
    neering "But don't be too proud of yourself."
    neering "What should have been a perfect plan was in fact ruined by one event I could not have foreseen."
    neering "Allow me to explain my masterstroke."

    #Eyewitness Statement Animation
    typing "-- my_testimony_FINAL(1).txt --{fast}"
    neering "Darsha was trying to shut down the Smart House project, so I had to get rid of him."
    neering "So I turned off the safety protocols and asked him to test out the dressing contraption."
    neering "Everything would have gone according to plan, were it not for that power outage!"
    neering "The house lost power before it could finish disposing of the body."
    neering "Then that vapid fool made sure everyone knew about the dead body in the Smart House."
    neering "So I had to improvise a cover story for the murder. I did pretty well, considering the circumstances."

    # fade out, fade in
    drang "Well, Warren, you've got some unconventional methods, but you sure do get results."
    warren thought "Maybe if by 'unconventional methods', you mean 'actually interrogating suspects'."
    drang "You've managed to find a culprit, find their motive, prove that both of them were lies..."
    drang "...and then find the person who manufactured both the fake culprit and the fake motive and get them to confess!"
    drang "All in the span of about three hours!"
    drang "Now, of course, I could usually do all that in about two and a half, but still."
    drang "So! Are you ready to tie this all up, or are you going to keep poking and prodding."
    drang "Keep in mind, the answer to this question will determine if I continue to like you."
    warren "Agent Drang, I want to be done here just as much as you..."
    drang "Nope. All right. Stop right there."
    drang "Unless the end of that sentence is \"so let's book this sucker then go grab some cold ones\" I don't want to hear it."
    warren "...I don't think this case is completely wrapped up yet."
    drang "AAAAAAAAGGGGHHHH! COME ON!"
    drang "WHAT ELSE COULD YOU POSSIBLY NEED? SHE CONFESSED TO THE MURDER!"
    warren "Exactly. She confessed to one of the worst crimes imaginable."
    warren "There should be no further reason for her to lie."
    warren "So why is there still a clear contradiction in her statement?"
    drang ". . . . ."
    drang "Damn it, Warren, now you've got me curious."
    drang "Go ahead. Interrogate her. I want to see where you're going with this."
    drang "But you better satisfy my curiosity, or else."
    warren thought "In any case, Carlos should be closing in on Neering's location by now."
    warren thought "She'll be under arrest soon enough."

    # Interrogation Animation
    $ current_present = "ObjectionLabel"
    $ back_action = "CurrentTestimony"

    label SH_Testimony10A:
        $ settesti("SH_Testimony10A", None, "SH_Testimony10B", "SH_Press10A","SH_Advice10")
        show screen testi
        neering "Darsha was trying to shut down the Smart House project, so I had to get rid of him."
        jump SH_Testimony10B

    label SH_Press10A:
        hide screen testi
        warren "It was worth taking a life, just to protect your little project?"
        neering "You don't understand."
        neering "This house...was my life's work."
        neering "Years worth of study and research had gone into it."
        neering "To have it shut down, all because some small-minded bureaucrat didn't understand what I was doing here..."
        neering "Well, it simply could not happen."
        warren "But wouldn't a death surrounding the project be even more damning?"
        neering "Once again, you fail to understand."
        neering "If everything had gone according to plan, there wouldn't have been a {i}death{/i}..."
        neering "Just a... let's say... {i}disappearance.{/i}"
        neering "Darsha would have just never showed up for work tomorrow."
        neering "People would ask questions, sure, but they'd never be able to trace anything back to me."
        neering "Meanwhile, I could continue work on the house in peace."
        neering "And it would have gone that way, if it weren't for that accursed--"
        neering "Well, we'll get around to that. Anyways..."
        jump SH_Testimony10B

    label SH_Testimony10B:
        $ settesti("SH_Testimony10B", "SH_Testimony10A", "SH_Testimony10C", "SH_Press10B","SH_Advice10")
        show screen testi
        neering "So I turned off the safety protocols and asked him to test out the Dressing Contraption."
        jump SH_Testimony10C

    label SH_Press10B:
        hide screen testi
        warren "How could you allow your own creation to be used for evil?"
        neering "What are you talking about?"
        warren "HARPER. It's like your child, metaphorically speaking."
        warren "How could you force it to do something so immoral?"
        neering "It was an evil, yes, but a neccesary evil. Self-defense, you might say."
        neering "You've brought up HARPER, so let's consider things from its perspective."
        neering "If Darsha wasn't gotten rid of, then HARPER would have been shut down, effectively killing it."
        neering "So if you told the machine, \"It's either you or him\", what's it going to pick?"
        warren "Aren't there laws or something which tell a machine to value a human's life over its own?"
        neering "Maybe in Science Fiction stories, but this is real life, Officer."
        neering "Any sentient creature on earth is going to value its own life above somebody else's. It's just nature."
        neering "Besides, there are billions of humans out there, but there's only one HARPER."
        jump SH_Testimony10C

    label SH_Testimony10C:
        $ settesti("SH_Testimony10C", "SH_Testimony10B", "SH_Testimony10D", "SH_Press10C","SH_Advice10")
        show screen testi
        neering "Everything would have gone according to plan, were it not for that power outage!"
        jump SH_Testimony10D

    label SH_Press10C:
        hide screen testi
        warren "The power outage..."
        warren "Is that the 'one event you could not have forseen' you mentioned earlier?"
        neering "Precicely."
        neering "The power outage... and that pesky style boy... they were rogue elements."
        warren "Well, you know what they say. The best laid plans of mice and men..."
        neering "Do not compare me to filthy rodents or apes. I... am a genius!"
        neering "My expert knowledge of the house's workings allowed me complete control of everything inside these walls."
        neering "I could see everything and do anything. My four walls and a roof of personal godhood."
        neering "But... there was no way to deal with anything {i}outside{/i} these walls."
        neering "I'll have to keep that in mind for next time..."
        warren thought "Next time? Does she plan on doing this again?"
        jump SH_Testimony10D

    label SH_Testimony10D:
        $ settesti("SH_Testimony10D", "SH_Testimony10C", "SH_Testimony10E", "SH_Press10D","SH_Advice10")
        show screen testi
        neering "The house lost power before it could finish disposing of the body."
        jump SH_Testimony10E

    label SH_Press10D:
        hide screen testi
        warren "How were you planning on getting rid of Orin Darsha's body before you were interrupted?"
        neering "The house has a garbage disposal here in the kitchen. That's why I'd brought it in here."
        warren "You really thought a garbage disposal would be enough to get rid of a body?"
        neering "This is no average garbage disposal. This is the garbage disposal... of the future!"
        warren thought "She's got that look of motherly pride again..."
        neering "Every piece of garbage is first run through a trash compactor."
        neering "Then, it is incinerated in an underground furnace."
        neering "Finally, the remains are submerged in a heavily corrosive chemical solution."
        neering "You don't even need to pay for the garbage collector anymore. It's all completely annihilated!"
        warren thought "Sounds like the EPA's worst nightmare..."
        neering "But then the power went out, and my infallable plan... well, failed."
        jump SH_Testimony10E

    label SH_Testimony10E:
        $ settesti("SH_Testimony10E", "SH_Testimony10D", "SH_Testimony10F", "SH_Press10E","SH_Advice10")
        show screen testi
        neering "Then that vapid fool made sure everyone knew about the dead body in the Smart House."
        jump SH_Testimony10F

    label SH_Press10E:
        hide screen testi
        warren "Couldn't you have still disposed of the body?"
        neering "What would be the point anymore?"
        neering "The point of getting rid of a body is so that nobody knows there is a body."
        neering "When a photo of the body starts trending online, that element is sort of lost."
        neering "I knew that no matter what, I would be getting police attention sooner or later."
        jump SH_Testimony10F

    label SH_Testimony10F:
        $ settesti("SH_Testimony10F", "SH_Testimony10E", "SH_Testimony10A", "SH_Press10F","SH_Advice10")
        show screen testi
        neering "So I had to improvise a cover story for the murder. I did pretty well, considering the circumstances."
        jump SH_Testimony10A

    label SH_Press10F:
        hide screen testi
        warren "If by pretty well, you mean you brainwashed and framed a man for your crime."
        neering "I've already killed one man today, Officer."
        neering "Do you really think I'm going to feel bad about incriminating another?"
        neering "I'm already past any sort of moral threshold."
        neering "At this point, anything I do to cover things up is just a drop in the bucket."
        warren "I'll admit, I've never heard the \"Defense by Relative Criminality\" before."
        warren "But, uh, I wouldn't count on that strategy at your trial."
        jump SH_Testimony10A

    label SH_Advice10:
        hide screen testi
        ash "Okay, what are we looking for here?"
        warren "This is a strange one."
        warren "What we've got here is an embarrassment of riches, as far as confessions go."
        warren "Neering has laid out her {color=red}motive{/color}, her {color=red}scheme{/color}, and even her {color=red}fatal mistake{/color}."
        warren "But for whatever reason, she's lying about one of these."
        warren "So the question becomes... which one?"
        warren "Is she lying about her {color=red}motive{/color}, her {color=red}scheme{/color}, or her {color=red}mistake{/color}?"
        warren "If we can answer that question, we can figure out why she's still lying to us."
        jump CurrentTestimony

    label SH_Objection10:
        hide screen testi
        if testipart == "SH_Testimony10A" and present_response == "DarshasEmail":
            jump SH_Success10
        else:
            jump SH_Failure10

    label SH_Failure10:
        warren "You're lying, Ms Neering."
        neering "About what?"
        warren "About... this piece of evidence!"
        neering "We've known each other for little more than a couple hours, Officer."
        neering "And yet, I can already tell when you're bluffing."
        neering "Am I profoundly insightful, or are you just obliviously transparent?"
        neering "The answer, obviously, is both."
        warren "Drat."
        drang "Warren, you piqued my curiosity and then completely failed to follow through!"
        $ mc_health -= 1
        drang "I'm very, very disappointed in you."
        warren thought "Sorry, I guess."
        if mc_health == 0:
            jump SH_GameOver10
        else:
            jump SH_Testimony10A

    label SH_GameOver10:
        drang "All right, let's wrap it up."
        warren "W-what!?"
        drang "I gave you a fair chance, but you couldn't get results."
        drang "Now we go back to doing things my way."
        show black with fade
        warren thought "But Drang's way didn't work."
        warren thought "Although he attempted to arrest Ms Neering, she was nowhere to be found."
        warren thought "It seemed she had slipped away during the conclusion, never to be seen again."
        warren thought "Orin Darsha's killer was never brought to justice."
        warren thought "And I never unravelled the enigma of Base 24."
        jump endgame

    label SH_Success10:
        warren "So, you killed Orin Darsha because he wanted to shut down the Smart House project?"
        neering "Yes! How many times do I have to say it?"
        warren "That's strange, though."
        neering "What now?"
        warren "Do you remember this email exchange? I showed it to you earlier."
        neering "Are you going to bring up the carpeting again?"
        warren "No, I want you to take a look at another part of this exchange."
        warren "It seems there was an ongoing debate about whether to continue the Smart House project..."
        warren "But it was {i}you{i/}, Ms Neering, who wanted to shut things down."
        neering "W-what? There were emails about...?"
        warren "It seems strange that you don't remember your own stance in this argument."
        warren "Even stranger that you don't even remember sending emails on the subject."
        neering "W-well, it's been a stressful couple of days. A lot has slipped my mind."
        neering "Perhaps I really did want to shut down the Smart House. What of it?"
        warren "Well, why would you want that?"
        warren "You said yourself that the Smart House was your life's work. You would protect it at all costs."
        warren "So why would you suddenly want to shut it down?"
        warren "And why was it so important that you would kill a man over it?"
        warren "Can you explain that?"
        neering ". . . . ."
        carlos "CHIIIIEEEEFFFFF!"
        warren "Carlos? What are you doing back here?"
        warren "You're suppossed to be looking for..."
        carlos "That's just the thing, Chief."
        carlos "I've been all over this crazy house. I went in that dressing room place, and inside the walls, and..."
        carlos "Angela Neering... is not anywhere in this house!"
        carlos "In fact, I don't think she's anywhere on this base!"
        guard "That's impossible! I have Ms Neering's television here hooked up to the house's local network!"
        carlos "Then... where is she?"
        show black with fade
        jump smart_house_act_6
