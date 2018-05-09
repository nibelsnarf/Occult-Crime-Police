label smart_house_act_4_intro:
    scene act4 with fade
    $ save_name = "Act 4"
    pause 3.0
    show black with dissolve
    typing "September 13th. 9:37 P.M.\nSmart House - Kitchen"
    show kitchen with dissolve
    show mir holdon
    show bottomi standard
    with dissolve
    wholdon "All right, run me through this..."
    whattip "You still insist that you killed Orin Darsha..."
    whattip "But now you claim that you used the Smart House as, what, some sort of weapon?"
    bdef "That's the truth, clear as I can remember it."
    hide mir
    show ash thinking
    with dissolve
    athink "Hey, wouldn't that make HARPER sort of like your accomplice?"
    bapology "I dunno, it's kinda more like a tool, right?"
    bapology "It may be all fancy and stuff, but it's just a house."
    bapology "It has to do what you say, right? It doesn't have free will or whatever..."
    hide ash
    hide bottomi
    show mir default
    show car default at flip
    with dissolve
    clift "Oh man, good luck checking this whole house into evidence, chief."
    chold "Hey Chief... are we gonna have to place it... under {i}house arrest?{/i}"
    wangry "What is {i}wrong{/i} with you, Tsukada?"
    chold "I may have had..."
    chold "One too many of these babies..."
    whattip "How do you keep getting more of them, anyways?"
    hide car
    show drang frown gup
    dfrown_gup "Hey bumpkins, if you're going to keep arguing, can I just book this guy and be on my way?"
    wholdon "Hold on there, Agent. I want to hear Mr. Bottomi's new statement first."
    dangry_gdown "Of course you do. Guess I'll just make myself comfortable over here."
    dangry_gdown "Hey forensics monkey, do you have any extra margarita glasses on you?"
    hide mir
    show car default
    cdef "Nope!"
    dangry_gdown "Perfect. Just perfect."
    cdef "I'm just going to keep doing the autopsy over here if that's cool with everyone."
    hide car
    hide drang
    show mir default
    show bottomi standard
    with dissolve
    wbase "Okay, Mr. Bottomi. Can you explain to us how exactly you got the Smart House to kill Mr. Darsha for you?"
    bapology "S-sure. I remember it pretty clearly."
    hide mir with fade
    call witness_statement from _call_witness_statement_4
    typing "-- Hacking the Smart House --{fast}"
    bdef "One of the features of the house is an automated protection system."
    bdef "It's meant to keep out home intruders and the like."
    bapology "It usually just stuns intruders, but there's a lethal option for extreme situations."
    bapology "All I had to do was reprogram the protection system to target Darsha and turn off stun mode."

    # fade out, fade in

label testimony4_intro:
    $ testiLength = 4
    $ current_present = "SH_Objection4"
    $ CurrentTestimony = "SH_Testimony4A"
    $ back_action = CurrentTestimony
    hide screen inventory_screen_button
    scene kitchen
    hide ash
    hide mir
    show bottomi apologetic
    with fade
    call interrogation from _call_interrogation_5
    play music "music/BustingLiesAtAModerateTempo.ogg" fadein 1.0

label SH_Testimony4A:
    $ settesti("SH_Testimony4A", None, "SH_Testimony4B", "SH_Press4A","SH_Advice4",1)
    show screen testi
    bdef "One of the features of the house is an automated protection system."
    jump SH_Testimony4B

label SH_Press4A:
    hide screen testi
    show mir default
    wbase "How do you suddenly know so much about the smart house?"
    wcasefile "Just an hour ago you were saying you'd never seen it before today."
    bapology "Well, there's those pamphlets they were passing out..."
    bapology "Those pretty much explained the broad strokes."
    bapology "And Darsha explained the rest of it to me as we walked around in here."
    bsad "This was before, you know, he fired me, and I..."
    bdef "So, anyway, this automated protection system..."
    hide mir
    jump SH_Testimony4B

label SH_Testimony4B:
    $ settesti("SH_Testimony4B", "SH_Testimony4A", "SH_Testimony4C", "SH_Press4B","SH_Advice4",2)
    show screen testi
    bdef "It's meant to keep out home intruders and the like."
    jump SH_Testimony4C

label SH_Press4B:
    hide screen testi
    show mir default
    wbase "How does it know a home intruder from an occupant? Or a visitor?"
    wbase "The whole setup seems like an accident waiting to happen."
    bdef "The house uses this biometric scanning thingy to recognize people."
    bdef "Kinda like a fingerprint, but for your whole body, or something."
    bdef "It makes a profile for anyone who enters the house."
    hide bottomi
    show ash surprised at flip
    asurprise "Oh yeah, the house did that for us earlier. Remember, Randi?"
    wthought "That's right..."
    hide ash
    show bottomi standard
    bdef "If the house doesn't recognize you, or it thinks you're a bad guy, it goes into alert mode."
    whattip "But still, isn't there a risk of the house hurting a delivery guy or something?"
    bapology "Even if the house messes up like that, it usually won't turn out too bad."
    hide mir
    jump SH_Testimony4C

label SH_Testimony4C:
    $ settesti("SH_Testimony4C", "SH_Testimony4B", "SH_Testimony4D", "SH_Press4C","SH_Advice4",3)
    show screen testi
    bapology "It usually just stuns intruders, but there's a lethal option for extreme situations."
    jump SH_Testimony4D

label SH_Press4C:
    hide screen testi
    show mir default
    wangry "Why on earth is a lethal option even programmed in there?"
    bapology "I dunno...sometimes people need to be dealt with in a permanent manner."
    bdef "Don't you cops have to do stuff like that all the time?"
    wthink "The ending of a life is not something I take lightly, Mr. Bottomi."
    wthink "The number of situations where I would consider lethal force can be counted on one hand."
    wbase "And I would {i}never{/i} give an unfeeling machine the authority to do something like that."
    wbase "Besides, look at this place! Every single element of this house can be remotely controlled."
    wbase "I can think of five better ways to pacify a threat just off the top of my head!"
    bsad "I don't know what to tell you, Officer. Maybe you should take it up with the Base."
    hide mir
    jump SH_Testimony4D

label SH_Testimony4D:
    $ settesti("SH_Testimony4D", "SH_Testimony4C", "SH_Testimony4A", "SH_Press4D","SH_Advice4",4)
    show screen testi
    bapology "All I had to do was reprogram the protection system to target Darsha and turn off stun mode."
    jump SH_Testimony4A

label SH_Press4D:
    hide screen testi
    show mir default
    wbase "And how exactly did you do that?"
    bapology "Well, I had to connect to the house's mainframe somehow..."
    bdef "In my case, I just used my neural implant."
    wconfused "You were able to connect to the house using that {i}thing{/i} on your head?"
    bdef "That's right. They both use the base's private network, so it was pretty easy to find."
    bdef "I just changed Darsha's threat level and made it go all lethal on him."
    bdef "The house did all the dirty work for me."
    hide bottomi
    show drang angry gup
    dangry_gup "You're a real scumbag, Bottomi. Getting a robot to kill for you?"
    wannoy "Are you saying you'd respect him more if he'd killed the man {i}himself?{/i}"
    dthink_gdown "Well, obviously nobody should commit murder ever."
    dthink_gup "But, uh, at least do it like a man, you know?"
    show mir thinking
    wthought "It still seems like a lot of trouble to go through to kill someone..."
    wthought "I don't even think it should be possible, given what Bottomi knows."
    hide mir
    hide drang
    show bottomi standard
    jump SH_Testimony4A

label SH_Advice4:
    hide screen testi
    hide bottomi
    show mir default
    show ash default at flip
    adef "What's your read on his statement?"
    wthink "I really don't believe Mr. Bottomi could have done this."
    athink "I know. He looks all scary, but he's kind of a big pushover."
    athink "I don't think he could have murdered {i}anybody!{/i}"
    wbase "No, I mean it's literally impossible for him to have hacked the protection system."
    wcasefile "If he had, then one of our pieces of evidence should reflect it."
    asurprise "What do you mean?"
    wgotcha "Don't worry, you'll see soon enough..."
    aannoy "Man, why you gotta be so vague about these things?"
    aannoy "\"All in due time, my young apprentice.\" That's what you sound like, all the time."
    show mir annoy anim
    wthought "Cut me some slack. I'm just trying to keep this interesting..."
    hide mir
    hide ash
    show bottomi standard
    if CurrentTestimony == "SH_Testimony4A":
        jump SH_Testimony4A
    if CurrentTestimony == "SH_Testimony4B":
        jump SH_Testimony4B
    if CurrentTestimony == "SH_Testimony4C":
        jump SH_Testimony4C
    if CurrentTestimony == "SH_Testimony4D":
        jump SH_Testimony4D

label SH_Objection4:
    if present_response == "Back":
        if CurrentTestimony == "SH_Testimony4A":
            jump SH_Testimony4A
        if CurrentTestimony == "SH_Testimony4B":
            jump SH_Testimony4B
        if CurrentTestimony == "SH_Testimony4C":
            jump SH_Testimony4C
        if CurrentTestimony == "SH_Testimony4D":
            jump SH_Testimony4D
    hide screen testi
    if testipart == "SH_Testimony4D" and present_response == "logs":
        jump SH_Success4
    else:
        jump SH_Failure4

label SH_Failure4:
    wgotcha "Mr. Bottomi, I believe you've been lying to me..."
    bnervous "What? How are you so sure?"
    wbase "I'm {i}not{/i} sure. But I {i}believe{/i} it."
    wbase "Like, in my gut."
    wbase "Just a hunch, really."
    hide bottomi
    show drang frown gdown
    dfrown_gdown "So... you don't have any proof."
    wbase "Nah."
    wcasefile "I mean, I thought I did, but looking at the evidence again it's not super convincing."
    wbase "Still got that gut feeling, though."
    dos ".  .  .  .  ."
    show screen healthBar
    wbase "I'm not getting out of this unscathed, am I?"
    ddril_gup "Nope!"
    $ mc_health -= 1
    call healthDrain from _call_healthDrain_27
    wthought "Rats. Looks like I need to be more careful."
    hide screen healthBar
    if mc_health == 0:
        jump SH_GameOver4
    else:
        hide drang
        hide mir
        show bottomi standard
        jump SH_Testimony4A

label SH_GameOver4:
    ddef_gdown "Well, you've been very helpful, Ms Warren."
    ddef_gdown "You found me the means, the motive, and the opportunity."
    ddril_gup "But it looks like your usefulness has finally run out."
    ddril_gup "You and your little friends have one minute to get out of here before I arrest you all."
    wholdon "But I'm so close to figuring out wha{nw}"
    ddril_gup "Sixty! Fifty nine! Fifty eight! Fifty seven!"
    show black with fade
    wthought "And so, the truth disappeared into darkness."
    wthought "Drang failed to bring the real culprit to justice."
    wthought "And I never unraveled the enigma of Base 24."
    jump endgame

label SH_Success4:
    stop music fadeout 1.0
    wcasefile "I gotta say, Bottomi. Your story lines up."
    bnervous "Huh?"
    wcasefile "The murder method, the access point, it all lines up..."
    wgotcha "All except for the part where you actually reprogram the house."
    bnervous "S...sorry?"
    wcasefile "See, I've got a printout here from the smart house's data logs."
    wcasefile "It shows a the moment 'Tour Mode' ended, it shows a disabling of the safety protocols..."
    wcasefile "But nowhere does it say that somebody altered the protection system."
    bnervous "w-www-wh-w-wha-wh-what?"
    wcasefile "Doesn't that strike you as odd?"
    wcasefile "Every other minute detail recorded, but this massive change to the security system goes unmentioned."
    wobjectionA "It's almost as if..."
    wobjectionC "YOU NEVER TOUCHED THOSE SYSTEMS AT ALL!"
    show bottomi freak
    bos "GGGGUAAAAAAAAAAAAAAGHHH!!!!!" with shake
    show bottomi freak
    bos "STOP ATTACKING MY MEMORIIIIIEEEEEEES!" with shake
    wsettle "How about you start telling us the truth?"
    bmad "You wanna know the truth?!"
    bremember "I... I... I hacked the data output too!"
    show mir recoil anim
    wos "WHAT!?"
    bremember "It makes sense, right? If I got into the security system, I could have gotten into the data logs too!"
    bremember "Of course I would delete the evidence of my infiltration... I would want to cover my tracks!"
    bnervous "You see, there was never any contradiction at all..."
    wthought "Why is he using the tone of voice people use when they're trying to reassure themselves?"
    bdespair "So, does that answer all of your questions?"
    wbase "Not so fast. I still want to know how you faked the crime scene in the kitchen."
    bfuzzy "Okay, okay. Let me remember exactly what I did..."
    show mir annoy anim
    wthought "How hard is it to remember? Didn't this happen only a couple of hours ago?"
    hide mir

    call witness_statement from _call_witness_statement_5
    typing "-- Faking a Crime Scene in 5 Easy Steps --{fast}"

    bdef "The protection system uses a blade hidden in its retractor arms for lethal neutralizations."
    bdef "The house can't tell between a dead body and an inanimate object."
    bdef "So I told it that I needed something moved into the kitchen for me."
    bdef "I had the body dropped on the floor, then asked the house to stab it with a knife."
    bdef "I never even had to enter the kitchen myself."

    show mir default with fade
    wbase "I see."
    whattip "And the purpose of this whole undertaking was to obfuscate your role as the killer?"
    bsad "That's right. But then I felt guilty so I came back here to confess."
    wthink "How... ethical of you."
    hide bottomi
    show drang frown gdown
    dfrown_gdown "Are you done with this exercise in futility yet?"
    dfrown_gdown "We've already gone so late the I'm going to need to stay the night in this godforsaken town."
    wbase "I'm sorry, Agent Drang. I won't stop until this man's testimony lines up with the facts."
    wbase "I can recommend you a nice hotel when I'm finished here."
    dangry_gup "If it's recommended by you, I'll probably have to answer a five-part questionnaire before they let me go to bed."


label testimony5_intro:
    $ testiLength = 5
    $ current_present = "SH_Objection5"
    $ concernForZombies = False
    $ CurrentTestimony = "SH_Testimony5A"
    $ back_action = CurrentTestimony
    hide screen inventory_screen_button
    scene kitchen
    hide drang
    hide mir
    show bottomi standard
    with fade
    call interrogation from _call_interrogation_6
    play music "music/BustingLiesAtAModerateTempo.ogg" fadein 1.0

label SH_Testimony5A:
    $ settesti("SH_Testimony5A", None, "SH_Testimony5B", "SH_Press5A","SH_Advice5",1)
    show screen testi
    bdef "The protection system uses a blade hidden in its retractor arms for lethal neutralizations."
    jump SH_Testimony5B

label SH_Press5A:
    hide screen testi
    show mir default
    wannoy "A hidden blade? This place is sounding more and more ridiculous."
    wthink "The US Consumer Product Safety Commission is going to have a field day in here."
    hide bottomi
    show ash posit at flip
    aposit "Come on, Randi. You gotta admit it sounds pretty cool."
    apsyched "I mean, it's knife arms! Haven't you ever wanted knife arms?"
    wannoy "I can say with a great deal of certainty that I have never wanted knife arms."
    apsyched "I'll bet they spring out of those arms all like SHINK!{w=0.2} YAH!{w=0.2} STAB STAB!"
    aposit "Plus, I'll bet they're pretty useful for chopping vegetables."
    aposit "Do you think it can do knife tricks like at those fancy restaurants?"
    wbase "Honestly, I'd rather not find out."
    hide ash
    show bottomi sad
    bsad "Uh, sorry, do you still need me here or..."
    wholdon "Right! Sorry. Go ahead, Mr. Bottomi."
    bapology "Well, as I was saying..."
    hide mir
    jump SH_Testimony5B

label SH_Testimony5B:
    $ settesti("SH_Testimony5B", "SH_Testimony5A", "SH_Testimony5C", "SH_Press5B","SH_Advice5",2)
    show screen testi
    bdef "The house can't tell between a dead body and an inanimate object."
    jump SH_Testimony5C

label SH_Press5B:
    hide screen testi
    show mir default
    whattip "What about that scanner you mentioned earlier? The one that registers profiles?"
    bdef "The scanner uses people's heartbeats to recognize them."
    bdef "Once the heart stops, the house can't tell it's a person anymore."
    hide bottomi
    show ash posit at flip
    aposit "The heartbeat, huh?"
    aunsure "So if a zombie came in here, it could walk right by and the house wouldn't even notice!"
    hide ash
    show bottomi apology
    bapology "I... guess not?"
    hide bottomi
    show ash surprised at flip
    asurprise "That seems like a pretty glaring design flaw! Somebody should talk to Miss Neering about that!"
    wannoy "I doubt that would rank very high on her to-do list..."
    aannoy "* sigh * Some people just don't have their priorities straight."
    $ concernForZombies = True
    hide ash
    hide mir
    show bottomi standard
    jump SH_Testimony5C

label SH_Testimony5C:
    $ settesti("SH_Testimony5C", "SH_Testimony5B", "SH_Testimony5D", "SH_Press5C","SH_Advice5",3)
    show screen testi
    bdef "So I told it that I needed something moved into the kitchen for me."
    jump SH_Testimony5D

label SH_Press5C:
    hide screen testi
    show mir default
    wthink "So it picked the body up using those... weird snaking arms?"
    bdef "That's right."
    wthink "Could those things even lift something like that?"
    bdef "Why don't you ask it?"
    wconfused "Huh? Oh, right...."
    wbase "Hey, HARPER!"
    show har deploy at flip
    hos "Hello There, User 'Miranda'."
    whattip "Exactly how much can those arms of yours lift?"
    hbase "Each Of My Actuated Robotic Manipulators, Or A.R--"
    wannoy "A.R.Ms, yeah, I get it."
    hbase "Each One Is Capable Of Lifting Over One Thousand Pounds."
    hbase "This Makes Me Perfect For Moving Heavy Furniture Around The House."
    bdef "See what I mean?"
    wannoy "No, no, I got it."
    hbase "Is There Anything In Particular You Need Lifting?"
    wthought "Maybe my spirits..."
    wannoy "No, thank you HARPER."
    hyes "If You Need Anything Else, Just Ask."
    hbase "I Am Literally Always Listening!"
    hide har with dissolve
    show mir base
    wthought "That still hasn't gotten any less creepy..."
    wbase "Okay, Mr.Bottomi. What did you do next?"
    hide mir
    jump SH_Testimony5D

label SH_Testimony5D:
    $ settesti("SH_Testimony5D", "SH_Testimony5C", "SH_Testimony5E", "SH_Press5D","SH_Advice5",4)
    show screen testi
    bdef "I had the body dropped on the floor, then asked the house to stab it with a knife."
    jump SH_Testimony5E

label SH_Press5D:
    hide screen testi
    show mir default
    whattip "So the kitchen knife we found in the victim's back..."
    bdef "It wasn't the real murder weapon. It was a ruse, a distraction."
    whattip "That still doesn't explain the bruises."
    bremember "Oh, those? I know how they happened."
    bdef "The smart house didn't know it was holding a body, so it handled the thing pretty clumsily."
    bdef "It kept bumping the body into walls and dropping it on the ground."
    wannoy "How...darkly comical."
    wannoy "Did you ever think to help the smart house out?"
    wthought "And perhaps begin some sort of two-man slapstick routine?"
    bapology "I really didn't have to. In fact..."
    hide mir
    jump SH_Testimony5E

label SH_Testimony5E:
    $ settesti("SH_Testimony5E", "SH_Testimony5D", "SH_Testimony5A", "SH_Press5E","SH_Advice5",5)
    show screen testi
    bdef "I never even had to enter the kitchen myself."
    jump SH_Testimony5A

label SH_Press5E:
    hide screen testi
    show mir default
    wbase "What do you mean by that?"
    bdef "Well, I had him killed in the downstairs hallway."
    bdef "After I had the house move the body, I made it clean up the blood."
    bdef "And then I just left through the front door."
    bdef "It was so simple that I never had a reason to go in the kitchen myself."
    hide mir
    jump SH_Testimony5A

label SH_Advice5:
    hide screen testi
    hide bottomi
    show mir default
    show ash sad at flip
    asad "Boy, it seems like Mr. Bottomi could have gotten the house to do anything for him."
    asad "How can we prove what he did or didn't do?"
    show ash thinking at flip
    wbase "There might be one way."
    wbase "Mister Bottomi may not have gotten his hands dirty..."
    wbase "But we know for a fact that he got his {i}feet{/i} dirty."
    wbase "And that fact should lead us to the truth."
    athink "What do you mea- {nw}"
    asurprise "What do you mea- {fast}oh!"
    aposit "I see what you're getting at!"
    hide mir
    hide ash
    show bottomi standard
    if CurrentTestimony == "SH_Testimony5A":
        jump SH_Testimony5A
    if CurrentTestimony == "SH_Testimony5B":
        jump SH_Testimony5B
    if CurrentTestimony == "SH_Testimony5C":
        jump SH_Testimony5C
    if CurrentTestimony == "SH_Testimony5D":
        jump SH_Testimony5D
    if CurrentTestimony == "SH_Testimony5E":
        jump SH_Testimony5E

label SH_Objection5:
    if present_response == "Back":
        if CurrentTestimony == "SH_Testimony5A":
            jump SH_Testimony5A
        if CurrentTestimony == "SH_Testimony5B":
            jump SH_Testimony5B
        if CurrentTestimony == "SH_Testimony5C":
            jump SH_Testimony5C
        if CurrentTestimony == "SH_Testimony5D":
            jump SH_Testimony5D
        if CurrentTestimony == "SH_Testimony5E":
            jump SH_Testimony5E
    hide screen testi
    if testipart == "SH_Testimony5E" and present_response == "footprints":
        jump SH_Success5
    else:
        jump SH_Failure5

label SH_Failure5:
    show mir angry
    wgotcha "Wait just a minute, Mr. Bottomi!"
    bnervous "What? Why?"
    wcasefile "Because I'm having trouble finding a contradiction in any of your statements."
    show bottomi apologetic
    wcasefile "So if you could just wait a minute while I think this over..."
    wos ". . . . . . ."
    wbase "Yeah, I got nothing. Sorry, everybody."
    show screen healthBar
    wbase "Go ahead and give me that penalty, Agent Drang."
    $ mc_health -= 1
    call healthDrain from _call_healthDrain_28
    wbase "Thank you."
    hide screen healthBar
    if mc_health == 0:
        jump SH_GameOver5
    else:
        hide mir
        jump SH_Testimony5A

label SH_GameOver5:
    hide bottomi
    show drang default gdown
    ddef_gdown "Well, you've been very helpful, Ms Warren."
    ddef_gdown "You found me the means, the motive, and the opportunity."
    ddril_gup "But it looks like your usefulness has finally run out."
    ddril_gup "You and your little friends have one minute to get out of here before I arrest you all."
    wholdon "But I'm so close to figuring out wha{nw}"
    ddril_gup "Sixty! Fifty nine! Fifty eight! Fifty seven!"
    show black with fade
    wthought "And so, the truth disappeared into darkness."
    wthought "Drang failed to bring the real culprit to justice."
    wthought "And I never unraveled the enigma of Base 24."
    jump endgame

label SH_Success5:
    stop music fadeout 1.0
    show mir default
    wcasefile "Just to get things straight, you're now telling me you never entered the kitchen?"
    bdef "That's right. There wasn't really any reason to."
    wgotcha "Well, that's real interesting..."
    wobjectionA "Because if you never entered the kitchen yourself..."
    wobjectionC "THEN WHO IS RESPONSIBLE FOR THESE MUDDY FOOTPRINTS?"
    show bottomi freak
    bos "GHWARK!"
    bremember "But! But! But wait a minute!"
    bremember "Who's to say those footprints are mine?"
    bdespair "LOTS OF PEOPLE HAVE FEET, RIGHT?"
    wsettle "Maybe so, but not everyone's footprints have the same pattern as YOUR OWN SHOES!"
    bremember "But wait... I'm wearing medical slippers!"
    bremember "These are provided by the base for everyone who volunteers in a clinical trial!"
    bremember "THERE ARE HUNDREDS OF PAIRS OF SHOES JUST LIKE THESE WITHIN A SQUARE MILE OF THE HOUSE!"
    show mir recoil anim
    wos "Wh-WHAAAAAAAAAAT!?"
    wthought "This is bad... my perfect evidence!"
    hide bottomi
    show drang default gdown
    ddef_gdown "You've reached the end of your rope, Warren."
    ddef_gdown "I'm feeling pretty confident in the facts of the case as we know them."
    ddef_gup "It's time to pack it all up and take this guy into custody."
    wholdon "W-wait! What if I can still prove that Louis Bottomi was in the kitchen?"
    dfrown_gup "How? You've already used up your ace in the hole and it turned out to be a dud."
    dthink_gup "Unless you're saying you've got another way to prove where Bottomi was?"
    show mir thinking
    wthought "Hmm... that's a good point..."

label kitchenProof:
    show screen healthBar
    wthought "{color=#FF9966}Do I Have Any Other Proof That Bottomi Was In The Kitchen?{/color}"
    menu:
        "Yes, I do.":
            wbase "Yes, I do."
            ddril_gup "Great, then let's see it!"

            ddril_gup "{color=#FF9966}What Else Do You Have Which Proves The Suspect Entered The Kitchen?{/color}"
            $current_present = "kitchenProofPresent"
            show screen present_evidence_screen
            pause

        "No, I don't.":
            wthink "No, I don't think I do."
            dfrown_gdown "Then that's it. This case is closed."
            hide drang
            show ash unsure at flip
            aunsure "Randi, what are you doing?"
            aunsure "You've gotta have something else you can use as proof!"
            aunsure "Otherwise, Mr. Bottomi is done for!"
            wbase "Shoot, you're right!"
            hide ash
            show drang default gdown
            wholdon "Wait! Hold on! I've changed my mind."
            dangry_gdown "You've wasted my time is what you've done."
            dangry_gdown "Let this penalty be a lesson for you."
            $ mc_health -= 1
            call healthDrain from _call_healthDrain_29
            wthought "Okay, I kind of deserved that..."
            if mc_health == 0:
                hide screen healthBar
                jump SH_GameOver5
            else:
                wthought "So, let's ask the question again..."
                jump kitchenProof

label kitchenProofPresent:
    if present_response == "photo":
        jump kitchenProofSuccess
    else:
        dthink_gdown "I don't see how that piece of evidence proves anything."
        ddril_gup "Other than your own incompetence, perhaps!"
        $ mc_health -= 1
        call healthDrain from _call_healthDrain_30
        show mir recoil anim
        wos "Gaaah!"
        wthought "That wasn't the proof I was looking for!."
        if mc_health == 0:
            hide screen healthBar
            jump SH_GameOver5
        else:
            wcasefile "Okay, I need to think this over one more time..."
            jump kitchenProof

label kitchenProofSuccess:
    hide screen healthBar
    wgotcha "How soon you forget, Agent Drang."
    wgotcha "Little more than an hour ago you brought up {color=#FF9966}this photo{/color} when making your case for Mr.Bottomi's guilt."
    call flash from _call_flash_37
    whattip "You really think he's our guy?"
    dangry_gdown "Of course he is! He just confessed, didn't he?"
    dthink_gdown "Take another look at the photograph that schmuck took."
    show chritudesPhoto
    dos "See that second figure in the window? That's gotta be him!"
    hide chritudesPhoto
    call flash from _call_flash_38
    dfrown_gup "Hah, well, is that so? It, uh, completely slipped my, uh, mind...."
    wbase "I'm sure you already realize what this means."
    wbase "If Mr. Bottomi is visible in this photograph..."
    wgotcha "Then he must have entered the kitchen at some point!"
    dfrown_gup "Well, ah, you see, the thing about that is..."
    ddril_gdown "Who...uh.....cares?"
    whattip "I'm sorry?"
    ddril_gdown "He did go in the kitchen, he didn't go to the kitchen, what's the difference?"
    wangry "The difference is that he explicitly told us tha{nw}"
    ddril_gdown "The guy made a mistake. It happens to the best of us."
    ddril_gdown "Poor guy's been lying on the ground unconscious for half an hour. He's probably still woozy."
    hide drang
    show bottomi sad
    bsad "That's...uh...{nw}"
    bremember "That's...uh... {fast}that's right!"
    bremember "Of course I went into the kitchen. I just got confused for a little while there."
    bsad "I'm sorry I messed up like that. Do you wanna hear more about how I killed Mr. Darsha?"
    show mir thinking
    wthought "Great... now those two are working together to patch up holes in his story."
    wthought "I've gotta come up with some damning evidence fast or these two are going to cover the whole thing up."
    wbase "Go ahead with your testimony, Mr. Bottomi."
    hide mir

    call witness_statement from _call_witness_statement_6
    typing "-- The Where, When and How of the Murder --{fast}"
    bsad "Mr. Darsha and I were in the smart house. He had just fired me."
    #bottomi "We were in the downstairs hallway at the time."
    bdef "Using my implant, I noticed that somebody had left the access point to the house open."
    bdef "So I hacked my way in while we were still talking, and forced the house to kill him."
    bmad "The house stabbed him in the back, killing him instantly."

    show mir default
    show bottomi standard
    with fade
    bdef "And that's it. That's the whole story."
    wcasefile "Well, hold on. What about the strange evid{nw}"
    hide bottomi
    show drang angry gup
    dfrown_gdown "Nope, that's all you're getting, Warren."
    wholdon "W-what?"
    dfrown_gdown "Your incessant questioning has been leading us in circles for hours now."
    dfrown_gdown "If you can't completely discount the suspect's story using this one testimony, then this case is closed."
    wangry "But there's so much here which hasn't been explained."
    dangry_gup "So what? Unexplainable stuff happens all the time!"
    show mir default
    dthink_gup "Why, just the other week I purchased a marvelous diamond ring for my mother."
    dthink_gup "But when my geologist friend examined it, he told me that it was made out of glass!"
    ddril_gup "Now how does diamond transform into glass overnight? It's just a mystery of the universe."
    show mir annoy anim
    wthought "Uh, it sounds like you just got ripped off."
    dfrown_gup "So! I'm giving you this one testimony, because I'm a real nice guy."
    dfrown_gup "But after that, I'm arresting this man and heading back to the agency."
    dfrown_gup "I have an appointment with a local alchemist tomorrow that I simply {i}can not{/i} reschedule!"
    wthought "Great. This is my last chance to get to the bottom of things."
    wthought "Better make it count."
    hide drang
    hide mir

label testimony6_intro:
    $ testiLength = 4
    $ current_present = "SH_Objection6"
    $ unlockedTestimony = "None"
    $ CurrentTestimony = "SH_Testimony6A"
    $ back_action = CurrentTestimony
    $ sixOrSeven = 6
    hide screen inventory_screen_button
    scene kitchen
    show bottomi sad
    with fade
    call interrogation from _call_interrogation_7
    #play music "music/BustingLiesAtABriskTempo.ogg" fadein 1.0

label SH_Testimony6A:
    if unlockedTestimony == "6B":
        $ settesti("SH_Testimony6A", None, "SH_Testimony6B", "SH_Press6A","SH_Advice6",1)
    if unlockedTestimony == "6C":
        $ settesti("SH_Testimony6A", None, "SH_Testimony6C", "SH_Press6A","SH_Advice6",1)
    if unlockedTestimony == "None":
        $ settesti("SH_Testimony6A", None, "SH_Testimony6D", "SH_Press6A","SH_Advice6",1)
    show screen testi
    bsad "Mr.Darsha and I were in the smart house. He had just fired me."
    if unlockedTestimony == "6B":
        jump SH_Testimony6B
    if unlockedTestimony == "6C":
        jump SH_Testimony6C
    if unlockedTestimony == "None":
        jump SH_Testimony6D

label SH_Press6A:
    hide screen testi
    show mir default
    wbase "You still maintain that your firing was the motive for killing Mr. Darsha?"
    bremember "Yeah, of course. Why would that have changed?"
    wthink "Well, it's just that so many {i}other{/i} parts of your story have changed, I thought maybe this had too."
    hide bottomi
    show drang frown gdown
    dfrown_gdown "Sheriff Warren, you will refrain from being passive aggressive with the witness."
    wannoy "Fine, fine."
    hide drang
    show bottomi standard
    wbase "Still, it feels like your description of the circumstances is a little lacking."
    wbase "Can you please tell me more about..."
    menu:
        "...where this all took place?":
            wbase "...where this all took place?"
            bfuzzy "Oh, sure."
            bdef "Mr. Darsha took me aside to the downstairs hallway to fire me."
            whattip "The downstairs hallway?"
            bdef "It's the one that leads from the kitchen to the living room."
            bdef "You can see it through that door over there."
            wthink "I see. So that's the room where Mr. Bottomi was killed?"
            bdef "That's right."
            wthought "Is this information important?"
            menu:
                "Yes, very important.":
                    wbase "Mr. Bottomi, could you add this information to your testimony?"
                    bapology "Sure, if you think it's that important."
                    $ unlockedTestimony = "6B"
                "No, not really.":
                    wbase "I probably don't need any of this information."
                    wbase "Thank you anyways, Mr. Bottomi."
                    bdef "Uh, sure. Anyways..."

        "...when this all took place?":
            wbase "...when this all took place?"
            bdef "Uh, okay."
            bdef "Mr. Darsha had just come back from the tour of the Smart House when he brought me aside."
            bapology "So it must have been sometime around... 5:30?"
            wthought "Well, that lines up with when Tour Mode ended in the Smart House's feedback logs..."
            wbase "In that case, Mr. Darsha would have died sometime around 5:35 or so, is that right?"
            bapology "Yeah, that sounds correct..."
            wthought "Is this information important?"
            menu:
                "Yes, very important.":
                    wbase "Mr. Bottomi, could you add this information to your testimony?"
                    bapology "Sure, if you think it's that important."
                    $ unlockedTestimony = "6C"
                "No, not really.":
                    wbase "I probably don't need any of this information."
                    wbase "Thank you anyways, Mr. Bottomi."
                    bdef "Uh, sure. Anyways..."
    hide mir
    if unlockedTestimony == "6B":
        jump SH_Testimony6B
    if unlockedTestimony == "6C":
        jump SH_Testimony6C
    if unlockedTestimony == "None":
        jump SH_Testimony6D

label SH_Testimony6B:
    $ settesti("SH_Testimony6B", "SH_Testimony6A", "SH_Testimony6D", "SH_Press6B","SH_Advice6",2)
    show screen testi
    bdef "We were in the downstairs hallway at the time."
    jump SH_Testimony6D

label SH_Press6B:
    hide screen testi
    show mir default
    wbase "Why weren't there any bloodstains in the hallway?"
    wcasefile "If that's where he was stabbed, then surely some blood would have splattered onto something."
    bdef "Well, um, it turns out that one of the things this automated butler house is really good at is, uh, {i}cleaning.{/i}"
    bdef "After I faked the crime scene in the kitchen, I had Harper clean up the hallway."
    bdef "It did such a good job, I doubt even your doctor friend over there could find any blood."
    if sixOrSeven == 6:
        hide bottomi
        show car serious at flip
        cser "I, uh, don't think that's how bloodstains work."
        cdef "You want me to go sweep the hallway real quick, Chief?"
        wbase "Don't worry about it, Tsukada."
        wthought "I don't think I'm going to need help poking a hole in {i}this{/i} claim..."
        hide car
    if sixOrSeven == 7:
        drang "Now remember, that contradiction you already found won't work this time. That shoe doesn't prove a thing."
        drang "So for your sake, I hope you have another idea."
        hide drang
    hide mir
    show bottomi standard
    jump SH_Testimony6D

label SH_Testimony6C:
    $ settesti("SH_Testimony6C", "SH_Testimony6A", "SH_Testimony6D", "SH_Press6C","SH_Advice6",2)
    show screen testi
    bdef "Mr. Darsha had just come back from the tour of the Smart House. It was around 5:30."
    jump SH_Testimony6D

label SH_Press6C:
    hide screen testi
    show mir default
    whattip "You're sure it was 5:30?"
    bapology "Pretty sure."
    hide bottomi
    show car default at flip
    cdef "Ah, I love five-o-clock."
    clift "When most people need an excuse to drink, they'll say \"It's five-o-clock somewhere!\""
    chold "But when it's already five, you don't even need to say it. You can just drink!"
    wannoy "You, on the other hand, {i}never{/i} need an excuse to drink."
    cdef "That's because Island Time truly is all the time!"
    cdef "Did I ever show you this custom watch I had made?"
    wannoy "Can we please focus on the case at han{nw}"
    cdef "Every hour is just replaced with the words 'Island Time'."
    cdef "It's completely useless as a timepiece, but it reminds me of what's important in life."
    wthought "This line of questioning has yielded nothing but garbage."
    wthought "I think I'm barking up the wrong tree here..."
    hide car
    hide mir
    show bottomi standard
    jump SH_Testimony6D

label SH_Testimony6D:
    if unlockedTestimony == "6B":
        $ settesti("SH_Testimony6D", "SH_Testimony6B", "SH_Testimony6E", "SH_Press6D","SH_Advice6",(testiLength - 2))
    if unlockedTestimony == "6C":
        $ settesti("SH_Testimony6D", "SH_Testimony6C", "SH_Testimony6E", "SH_Press6D","SH_Advice6",(testiLength - 2))
    if unlockedTestimony == "None":
        $ settesti("SH_Testimony6D", "SH_Testimony6A", "SH_Testimony6E", "SH_Press6D","SH_Advice6",(testiLength - 2))
    show screen testi
    bdef "Using my implant, I noticed that somebody had left the access point to the house open."
    jump SH_Testimony6E

label SH_Press6D:
    hide screen testi
    show mir default
    whattip "Why were you using your neural implant at that moment?"
    whattip "Did you honestly expect to find a way to access the house?"
    bsad "Not really..."
    bsad "I guess I knew that they were going to get rid of it soon, since I was being fired..."
    bsad "And I wanted to give it one last go before I lost it."
    bdef "Then I found the access point to the house open, and well..."
    bnervous "I started to get an idea..."
    wbase "It was a crime of opportunity, then."
    bsad "Well, of course. I wasn't gonna kill him {i}before{/i} he'd fired me, right?."
    wbase "Fair enough. What did you do next?"
    hide mir
    jump SH_Testimony6E

label SH_Testimony6E:
    $ settesti("SH_Testimony6E", "SH_Testimony6D", "SH_Testimony6F", "SH_Press6E","SH_Advice6",(testiLength - 1))
    show screen testi
    bdef "So I hacked my way in while we were still talking, and forced the house to kill him."
    jump SH_Testimony6F

label SH_Press6E:
    hide screen testi
    show mir default
    wbase "It's pretty impressive you're able to maintain a conversation while doing something like that."
    wbase "It seems like you would get distracted with one or the other."
    bdef "It's not as hard as it sounds, actually."
    bdef "It's just like browsing the internet while talking with a friend."
    bapology "Nothing hard about that, right?"
    wconfused "Ah... um... isn't it, though?"
    hide mir
    show ash flippant
    aflippant "Forgive her, Mr. Bottomi. You have to remember that Randi is computer illiterate."
    hide ash
    show mir thinking
    wthink "I don't need qualifiers at the end of my sentences, Ash."
    wthink "I get the point: talking and hacking isn't that hard."
    wbase "Now tell me what happened next."
    bdef "Okay, so..."
    hide mir
    jump SH_Testimony6F

label SH_Testimony6F:
    $ settesti("SH_Testimony6F", "SH_Testimony6E", "SH_Testimony6A", "SH_Press6F","SH_Advice6",testiLength)
    show screen testi
    bmad "The house stabbed him in the back, killing him instantly."
    jump SH_Testimony6A

label SH_Press6F:
    hide screen testi
    show mir default
    wbase "How do you know it was instant?"
    bfuzzy "I guess I don't know for sure..."
    bdef "But he stopped moving right when the house stuck its blade through him."
    bdef "So, like, it seemed pretty instant to me..."
    wbase "I'm sorry, Mr. Bottomi, but..."
    wbase "\"Looked pretty instant\" isn't exactly a confirmation of death!"
    hide bottomi
    show drang angry gdown
    dangry_gdown "Are you going to stand around arguing semantics, or do you have some proof to back up whatever you're claiming?"
    dfrown_gup "In the absence of solid evidence, this witness's statement is the best indication we have of what happened here."
    dfrown_gup "We need to trust it fully unless we have something more concrete which conflicts with it."
    wthought "Wow, that was an unusually solid point considering it came from Drang."
    hide drang
    hide mir
    show bottomi standard
    jump SH_Testimony6A

label SH_Advice6:
    hide screen testi
    hide bottomi
    show mir default
    show ash unsure at flip
    if sixOrSeven == 6:
        aunsure "Did you hear Special Agent Doofus over there?"
        aunsure "You've only got this last chance to find the flaw in Mr. Bottomi's story!"
        aunsure "What are we going to do?"
        wbase "Don't worry. There's a key contradiction hidden in this testimony."
        wbase "We just need to press harder and {color=#FF9966}ask the right question{/color} in order to draw it out of Mr. Bottomi."
        asurprise "The right question?"
        aunsure "But what if you end up asking the {color=#FF9966}wrong question?{/color}"
        wbase "Well in that case I can always {color=#FF9966}ask again.{/color}"
        adef "Okay. Let's give this everything we've got!"
    if sixOrSeven == 7:
        aunsure "We're really on the ropes now, Randi."
        aunsure "Do you honestly think you can find {i}another{/i} contradiction in this old testimony?"
        wthink "It doesn't matter whether I can or not. The fact is, I {i}have{/i} to."
        wcasefile "I need to take a look at that new evidence I got from Carlos; that's the key to everything."
        wcasefile "If I can just figure out where that fits in, I can finally discount this story."
        apsyched "I believe in you, Randi!"
    hide ash
    hide mir
    show bottomi standard
    if CurrentTestimony == "SH_Testimony6A":
        jump SH_Testimony6A
    if CurrentTestimony == "SH_Testimony6B":
        jump SH_Testimony6B
    if CurrentTestimony == "SH_Testimony6C":
        jump SH_Testimony6C
    if CurrentTestimony == "SH_Testimony6D":
        jump SH_Testimony6D
    if CurrentTestimony == "SH_Testimony6E":
        jump SH_Testimony6E
    if CurrentTestimony == "SH_Testimony6F":
        jump SH_Testimony6F

label SH_Objection6:
    if present_response == "Back":
        if CurrentTestimony == "SH_Testimony6A":
            jump SH_Testimony6A
        if CurrentTestimony == "SH_Testimony6B":
            jump SH_Testimony6B
        if CurrentTestimony == "SH_Testimony6C":
            jump SH_Testimony6C
        if CurrentTestimony == "SH_Testimony6D":
            jump SH_Testimony6D
        if CurrentTestimony == "SH_Testimony6E":
            jump SH_Testimony6E
        if CurrentTestimony == "SH_Testimony6F":
            jump SH_Testimony6F
    hide screen testi
    if testipart == "SH_Testimony6B" and present_response == "shoe":
        if sixOrSeven == 6:
            jump SH_Success6
        if sixOrSeven == 7:
            show mir default
            wgotcha "Here it is. The evidence that's going to blow this {nw}"
            hide bottomi
            show drang frown gup
            dfrown_gup "Hold up, Warren."
            dfrown_gup "You're not trying to present the same piece of evidence again, are you?"
            wconfused "I... uh... of course not..."
            wconfused "I was just going to say that... hallways.... are a bad place to do murders?"
            wos ". . . . ."
            show screen healthBar
            wangry "Okay, fine, I was going to use the same evidence again."
            wangry "What are you going to do about it?"
            ddef_gup "This."
            $ mc_health -= 1
            call healthDrain from _call_healthDrain_31
            show mir recoil anim
            wos "Gghrk!"
            hide screen healthBar
            if mc_health == 0:
                jump SH_GameOver6
            else:
                hide drang
                hide mir
                jump SH_Testimony6A
    if testipart == "SH_Testimony6F" and present_response == "autopsy":
        jump SH_Success7
    else:
        jump SH_Failure6

label SH_Failure6:
    show mir default
    if sixOrSeven == 6:
        wgotcha "Here it is. The evidence that's going to blow this thing wide open."
        wbase "What do you think of this, Mr. Bottomi?"
        bapology "Uh, I dunno. It's kind of nice, I guess..."
        bdef "Wait, sorry... was that supposed to be your evidence?"
        wannoy "Rats, I don't think that was the evidence I needed."
        hide bottomi
        show drang frown gup
        dfrown_gup "There goes your last chance, Warren. Time to close this case for good."
        wholdon "Wait! No!"
        show screen healthBar
        wholdon "Wouldn't you say that I only used up twenty percent or so of my last chance there?"
        dthink_gup "Sure, sure... as long as you're fine with taking one hundred percent of a penalty."
        $ mc_health -= 1
        call healthDrain from _call_healthDrain_32
        wthought "Ouch... well, I guess I can't complain..."
    if sixOrSeven == 7:
        wthought "Here it is! The final contradiction!"
        wcasefile "Mister Bottomi... please take a look at this!"
        bnervous "I... I don't understand..."
        wconfused "Uh... you don't?"
        bapology "Yeah, uh... this is supposed to be decisive proof, right?"
        wconfused "O-of course!"
        show screen healthBar
        bapology "I, uh, I don't know what you're talking about here..."
        wos ". . . . ."
        $ mc_health -= 1
        show mir recoil anim
        call healthDrain from _call_healthDrain_33
        wos "Ack!"
        wthought "I must have presented the wrong thing!"
    hide screen healthBar
    if mc_health == 0:
        jump SH_GameOver6
    else:
        hide drang
        hide mir
        jump SH_Testimony6A

label SH_GameOver6:
    if sixOrSeven == 6:
        dthink_gdown "Well, we've put this whole testimony under a microscope and you still haven't found anything."
        dthink_gup "Looks like it's time to finally call it a night."
        ddef_gdown "Louis Bottomi, you're under arrest for the murder of Orin Darsha."
        ddef_gdown "You have the right to remain silent. Anything you say... oh, hey Warren!"
        wholdon "W-what?"
        dthink_gdown "I feel like you should be doing this part."
        ddril_gup "These are the {i}Miranda{/i} Rights, after all."
        ddril_gup "See, it's a pun, because your name is Miranda, and the thing you say to criminals is called the...{nw}"
    if sixOrSeven == 7:
        ddril_gdown "I knew you couldn't possibly figure this out..."
        ddef_gup "But at least it was fun to watch you try!"
        ddef_gup "I've gotta thank you for at least keeping things interesting around here."
        dfrown_gdown "Still, it's time to wrap things up. I've wasted enough time in this town as it is."
        dfrown_gdown "Louis Bottomi, you're under arrest for the murder of Orin Darsha."
    show black with fade
    wthought "And so, the truth disappeared into darkness."
    wthought "Drang failed to bring the real culprit to justice."
    wthought "And I never unraveled the enigma of Base 24."
    jump endgame

label SH_Success6:
    stop music fadeout 1.0
    show mir default
    wcasefile "The downstairs hallway, huh?"
    bdef "That's right..."
    wbase "Do you reckon that Mr. Darsha lost his shoe during the house's attack?"
    bfuzzy "That... sounds about right."
    bnervous "Uh, why?"
    wcasefile "Well, it seems we've got a problem here, Mr. Bottomi."
    bos "* gulp *"
    wcasefile "You see, I managed to find the shoe while I was investigating."
    wcasefile "Only...I didn't find it in the hallway..."
    wgotcha "I FOUND IT UPSTAIRS, IN THE DRESSING CONTRAPTION!"
    show bottomi freak
    bos "WHAAAAAAAT!?"
    wbase "Ash here confirmed for me that Mr. Darsha didn't use the contraption during the tour."
    wbase "So: do you mind explaining to me how the victim's shoe ended up in a room he never even visited?"
    wbase "The only explanation is: YOUR ENTIRE STORY IS A FABRICATION!"
    show bottomi freak
    bos "Th-this isn't right! It doesn't m-m-make any sense! I remember it so clearly, a-and yet... IT'S ALL WRONG!"
    show bottomi freak
    bos "NNNNNNNNNNNNNNNNOOOOOOOOOOOOOOOOOOOOOAAAAAAAAA{nw}"
    call flash from _call_flash_39
    # Drang HOLD ITs
    hide bottomi
    show drang frown gup
    dfrown_gup "Hold your horses, Warren."
    dthink_gup "Being a small-town cop, I assume you have several, which you use in place of squad cars."
    wannoy "What are you on about?"
    ddril_gdown "Hah! It really is exhausting, having to be the only voice of reason around here."
    ddril_gdown "But I guess I'm going to have to spell it all out to you:"
    ddef_gdown "The location of that shoe doesn't prove {i}anything{/i} about how the victim died."
    wangry "Of course it does! It proves he wasn't in the downstairs hallway!"
    ddef_gup "Does it really, though? Let's consider a few hypotheticals..."
    dthink_gup "The Dressing Contraption is basically a glorified closet, right?"
    dthink_gup "Who's to say it doesn't stock the same kind of shoe the victim wears?"
    dthink_gup "And who's to say one of those shoes didn't fall out of place?"
    wbase "We could easily check on that, though..."
    ddef_gup "All right, here's another hypothetical:"
    dthink_gup "Perhaps the house hid Darsha's shoe up there when it was cleaning up the crime scene."
    dthink_gup "We can't confirm or deny that, since the house lost its memory in the blackout."
    dthink_gup "Still, it's a completely valid possibility."
    ddef_gup "And, my final hypothetical: what if your little sidekick is just lying about Darsha?"
    ddef_gup "Perhaps he really did use The Dressing Contraption, and Ash here is covering it up!"
    hide drang
    show ash annoyed at flip
    aannoy "You really think I would lie to a Federal Officer?"
    hide ash
    show drang think gdown
    dthink_gdown "In this business, you learn not to trust anyone."
    wthought "Except for Bottomi, apparently..."
    ddef_gup "So, do you have anything to refute my possibilities?"
    wthink "I... I..."
    wthink "...I don't."
    wholdon "But if you could just give me a little more time!"
    dfrown_gdown "Did you forget our little agreement? If you couldn't poke a hole in this one last testimony, you were done."
    djacket_pop "And, well, it looks like you couldn't do it."
    djacket_popped "You know what that means!"
    dfrown_gdown "Louis Bottomi, you're under arrest for the murder of Orin Darsha."
    dfrown_gdown "You have the right to remain silent. Anything you s{nw}"
    show black
    call flash from _call_flash_40
    wthought "N-no! It can't end like this! Not after I've come so far!"
    wthought "I really thought I could get to the bottom of things this time... I thought that if I could just solve {i}this{/i} case, then... then..."
    wthought "Then it would be like I had never failed all those years ago..."
    wthought "But once again... I couldn't do it..."
    wthought "I failed the town... I failed Ash...."
    wthought "Damn it! All I needed was {i}one more{/i} piece of evidence!"
    hide black
    hide drang
    show car agitated at flip
    call flash from _call_flash_41
    cagit "Hold it! Hold everything!"
    cagit "Nobody's arresting anybody until I show this to Sheriff Warren!"
    wholdon "Carlos? What are you doing?"
    cser "I finally finished up the Autopsy Report, and, well, you're gonna want to see this."
    wcasefile "Hm . . . . . Ah!"
    cser "You see that?"
    wcasefile "Yeah, I see it all right."
    $inventory.add(autopsy)
    $inventory.drop(prelim)
    typing "Autopsy Report Updated"
    hide car
    show drang think gup
    wbase "Agent Drang, I just need one more testimony out of this witness."
    wbase "Just one more, and I guarantee I can expose the truth."
    dthink_gup "Hmm... no."
    show mir recoil anim
    wos "WWWHHAT!?"
    dfrown_gdown "I said you only got one last testimony, and I'm sticking by that."
    ddef_gup "But... if you think you can find a flaw in the one we just heard, I'd love to see you try."
    ddef_gup "So, what do you think?"
    show mir base
    wthought "Shoot... can I really find another flaw in that last testimony?"
    menu:
        "Of course I can.":
            wthought "Of course! This last piece of evidence was exactly what I needed."
            wthought "Carlos has given me a chance to turn this around... I can't waste it!"
        "Probably not, but I have to try anyway.":
            wthought "Probably not. There's a lot stacked against me."
            wthought "Still, I can't give up. Not after Carlos has given me this last shot!"
            wthought "I should probably put on an act of confidence for Drang, though..."
    wgotcha "Of course I can do it!"
    ddef_gup "Ooh, things are heating up!"
    dfrown_gdown "All right, Bottomi. Let's hear that testimony one more time, all right?"
    dfrown_gdown "And don't give Miss Confidence any more info than you've already done."
    ddef_gdown "We have to keep things fair, after all."
    $sixOrSeven = 7
    hide drang
    hide mir
    show bottomi standard
    call interrogation from _call_interrogation_8
    jump SH_Testimony6A

label SH_Success7:
    show mir default
    wthought "Here it is! The final contradiction!"
    wbase "Mister Bottomi... please take a look at this!"
    bnervous "I... I don't understand..."
    wcasefile "Well, then let me explain it to you."
    wcasefile "Your entire story, from the beginning, has been based on one central premise."
    wcasefile "Namely, the fact that Orin Darsha was killed by a stab wound to the back."
    wcasefile "Now, I just got back a finalized autopsy report..."
    bremember "Y-yes, I was there when that happened!"
    wannoy "...Right."
    wobjectionA "Now, one of the most interesting things this autopsy report reveals..."
    wobjectionC "Is that THE ACTUAL CAUSE OF DEATH WAS A BROKEN NECK!"
    show bottomi freak
    bos "N-no! That can't be right! The doctor guy must have made a mistake!"
    wsettle "Not possible. Carlos may be eccentric, but he knows his medicine."
    show bottomi freak
    bos "This can't be possible! I... I saw it with my own eyes! He was stabbed!"
    bremember "Wait... but now I'm starting to remember...the machine breaking his neck?"
    bfuzzy "No! I know he was stabbed! How can I possibly have two memories of the same event?"
    show bottomi freak
    bos "I remember everything...so many different ways...and none of it fits together!"
    show bottomi kaboom
    bos "WHAAAAT IS HAAAPPENIIIIINGG TO MEEEEEEEEEEEEEEEEEEEEEEEEEE"
    hide bottomi
    $bHat = 3
    show ash surprised at flip
    asurprise "Did his head just explode!?"
    hide ash
    show car agitated at flip
    cagit "Medically speaking, that's super bad for you!"
    wbase "Carlos, go check on him!"
    cser "I'm on it!"
    hide car
    show drang frown gdown
    dfrown_gdown "Well, great job, Warren. You confused the witness so hard that he exploded."
    dfrazzled "Do you know how hard it is to prosecute a man with no head!?"
    wangry "Wait a minute... do {i}you?{/i}"
    hide drang
    show car agitated at flip
    cagit "It's okay, everyone! He's waking up now!"
    hide car
    show bottomi fuzzy
    bfuzzy "Oh...man....my head..."
    wholdon "Mr. Bottomi! Are you all right?"
    bapology "Actually...yes. My thoughts are starting to clear up..."
    bdef "Wait...w-where's my neural implant?"
    hide mir
    show car default
    cdef "It kinda short circuited. Nearly took your head off, actually!"
    bdef "If the neural implant is gone... and I'm starting to think straight again..."
    hide car
    show ash surprised
    aposit "Oh my gosh! Somebody was using the implant to control your behavior, right?"
    bdef "I think so."
    hide ash
    show mir angry
    wangry "Ash was right!?"
    hide mir
    show ash surprised
    asurprise "I was right!?"
    bapology "I mean, I can't say for sure..."
    bdef "But I'm starting to think I'm not the one who killed Mister Darsha."
    bdef "I think that somebody else {i}forced{/i} me to confess..."
    show black with dissolve
    call resetHealth from _call_resetHealth_6
    jump smart_house_act_5_intro
