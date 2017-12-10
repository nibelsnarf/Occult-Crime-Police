label smart_house_act_4_intro:
    ### ACT 4: DELIVERANCE, THY NAME IS TRUTH
    show black
    typing "September 13th. 9:47 P.M.\nSmart House - Kitchen"
    show kitchen with fade
    warren "All right, run me through this..."
    warren "You still insist that you killed Orin Darsha..."
    warren "But now you claim that you used the Smart House as, what, some sort of weapon?"
    bottomi "Yes, exactly."
    carlos "Oh man, good luck checking this whole thing into evidence."
    ash "Hey, wouldn't that make HARPER sort of like your accomplice?"
    bottomi "I'd say the AI is more like a tool than an accomplice."
    bottomi "It may be advanced, but it's still a machine. It doesn't have the free will to refuse."
    bottomi "At least...I think so..."
    carlos "Hey Chief... are we gonna have to place this thing... under {i}house arrest?{/i}"
    warren "What is wrong with you, Tsukada?"
    carlos "I may have had"
    carlos "One too many of these babies..."
    warren "How do you keep getting more of them, anyways!?"
    drang "Hey bumpkins, if you're going to keep arguing, can I just book this guy and be on my way?"
    warren "Hold on there, Agent. I want to hear Mr Bottomi's new statement first."
    drang "Of course you do. Guess I'll just make myself comfortable over here."
    drang "Hey forensics monkey, do you have any extra margarita glasses on you?"
    carlos "Nope!"
    drang "Perfect. Just perfect."
    carlos "I'm just going to keep doing the autopsy over here if that's cool with everyone."
    warren "Okay, Mr Bottomi. Can you explain to us how exactly you got the Smart House to kill Mr Darsha for you?"
    bottomi "S-sure. I remember it pretty clearly."

    # Eyewitness Statement ANIMATION
    typing "-- Hacking the Smart House --{fast}"
    bottomi "One of the features of the house is an automated security system."
    bottomi "It's meant to keep out home intruders and the like."
    bottomi "It usually just stuns intruders, but there's a lethal option for extreme situations."
    bottomi "All I had to do was reprogram the security system to target Darsha and turn off stun mode."
    bottomi "Anybody could have done it, so long as they knew how."

    # fade out, fade in


    # Interrogation Animation
    $ current_present = "SH_Objection4"
    $ back_action = "CurrentTestimony"

label SH_Testimony4A:
    $ settesti("SH_Testimony4A", None, "SH_Testimony4B", "SH_Press4A","SH_Advice4")
    show screen testi
    bottomi "One of the features of the house is an automated security system."
    jump SH_Testimony4B

label SH_Press4A:
    hide screen testi
    warren "A security system, huh?"
    warren "Do you mind telling us a little more about how that works?"
    drang "HEY WARREN"
    drang "I'M PRETTY SURE"
    drang "HE WAS JUST ABOUT TO TELL US ABOUT THE SECURITY SYSTEM"
    drang "WHY DON'T YOU ZIP IT FOR TWO SECONDS"
    drang "AND LET THE MAN SPEAK"
    warren "Okay, okay..."
    warren thought "Drang's fuse is starting to shrink..."
    warren thought "I'll need to tread lightly around him for the time being..."
    bottomi "Okay, so, the security system..."
    jump SH_Testimony4B

label SH_Testimony4B:
    $ settesti("SH_Testimony4B", "SH_Testimony4A", "SH_Testimony4C", "SH_Press4B","SH_Advice4")
    show screen testi
    bottomi "It's meant to keep out home intruders and the like."
    jump SH_Testimony4C

label SH_Press4B:
    hide screen testi
    warren "How does it know a home intruder from an occupant? Or a visitor?"
    warren "The whole setup seems like an accident waiting to happen."
    bottomi "The house recognizes different people based on a biometric scan."
    bottomi "It creates a profile for each person who enters the house."
    ash "Oh yeah, the house did that for us earlier. Remember, Randi?"
    warren thought "That's right..."
    bottomi "If the person is unfamiliar, or the profile is registered as a threat, it goes into alert mode."
    warren "But still, isn't there a risk of the house hurting a delivery guy or something?"
    bottomi "Even if the house makes some kind of mistake, there's little chance of it harming somebody."
    jump SH_Testimony4C

label SH_Testimony4C:
    $ settesti("SH_Testimony4C", "SH_Testimony4B", "SH_Testimony4D", "SH_Press4C","SH_Advice4")
    show screen testi
    bottomi "It usually just stuns intruders, but there's a lethal option for extreme situations."
    jump SH_Testimony4D

label SH_Press4C:
    hide screen testi
    warren "Why on earth is a lethal option even programmed in there?"
    bottomi "Sometimes people need to be dealt with in a permanent manner."
    bottomi "As a police officer, you should understand this."
    warren "The ending of a life is not something I take lightly, Mr Bottomi."
    warren "The number of situations where I would consider lethal force can be counted on one hand."
    warren "And I would {i}never{/i} give an unfeeling machine the authority to do something like that."
    warren "Besides, look at this place! Every single element of this house can be remotely controlled."
    warren "I can think of five better ways to pacify a threat just off the top of my head!"
    bottomi "I don't know what to tell you, Officer. Maybe you should take it up with the Base."
    jump SH_Testimony4D

label SH_Testimony4D:
    $ settesti("SH_Testimony4D", "SH_Testimony4C", "SH_Testimony4A", "SH_Press4D","SH_Advice4")
    show screen testi
    bottomi "All I had to do was reprogram the security system to target Darsha and turn off stun mode."
    jump SH_Testimony4A

label SH_Press4D:
    hide screen testi
    warren "And how exactly did you do that?"
    bottomi "Well, I had to connect to the house's mainframe somehow..."
    bottomi "In my case, I just used my neural implant."
    warren "You were able to connect to the houe using that {i}thing{/i} on your head?"
    bottomi "That's right. They both use the base's private network for communications, so it was pretty easy to find."
    bottomi "Anyway, all I needed to do to gain control was enter the security codes."
    bottomi "Then I was free to change Darsha's threat level and turn on the lethal option."
    bottomi "The house did all the dirty work for me."
    drang "You're a real scumbag, Bottomi. Getting a robot to kill for you?"
    warren "Are you saying you'd respect him more if he'd killed the man {i}himself?{/i}"
    drang "Well, at least it would be proactive..."
    warren thought "It still seems like a lot of trouble to go through..."
    warren thought "I don't even think it should be possible, given what Bottomi knows..."
    jump SH_Testimony4A

label SH_Advice4:
    hide screen testi
    warren "Hmm..."
    warren "Doesn't it seem strange he knows so much about the house?"
    warren "I mean, he himself said that he'd never even seen the thing until today."
    ash "I think that part of his story checks out..."
    ash "Everything he said about how the house works was in the pamphlet we got."
    ash "He'd only need to skim it for a couple of minutes."
    warren "You may be right in that regard..."
    warren "But there's something related to his actions which he couldn't possibly have known."
    ash "There is?"
    warren "Don't worry, you'll see soon enough..."
    ash "Man, why are you always so vague about these things?"
    ash "\"All in due time, my young apprentice.\" That's what you sound like."
    warren thought "Cut me some slack. I'm just trying to keep this interesting..."
    jump CurrentTestimony

label SH_Objection4:
    hide screen testi
    if testipart == "SH_Testimony4D" and present_response == "SecurityLog":
        jump SH_Success4
    else:
        jump SH_Failure4

label SH_Failure4:
    warren "Mr Bottomi, I believe you've been lying to me..."
    bottomi "What? How are you so sure?"
    warren "I'm {i}not{/i} sure. But I {i}believe{/i} it."
    warren "Like, in my gut."
    warren "Just a hunch, really."
    drang "So... you don't have any proof."
    warren "Nah."
    warren "I mean, I thought I did, but looking at the evidence again it's not super convincing."
    warren "Still got that gut feeling, though."
    drang ".  .  .  .  ."
    warren "I'm not getting out of this unscathed, am I?"
    drang "Nope!"
    $ mc_health -= 1
    warren thought "Rats. Looks like I need to be more careful."
    if mc_health == 0:
        jump SH_GameOver4
    else:
        jump SH_Testimony4A

label SH_GameOver4:
    drang "Well, you've been very helpful, Ms Warren."
    drang "You found me the means, the motive, and the opportunity."
    drang "But it looks like your usefulness has finally run out."
    drang "You and your little friends have one minute to get out of here before I arrest you all."
    warren "But I'm so cl{nw}"
    drang "Fifty nine! Fifty eight! Fifty seven!"
    show black with fade
    warren thought "And so, the truth disappeared into darkness."
    warren thought "Drang failed to bring the real culprit to justice."
    warren thought "And I never unravelled the enigma of Base 24."
    jump endgame

label SH_Success4:
    warren "I gotta say, Bottomi. Your story lines up."
    bottomi "Huh?"
    warren "The murder method, the access point, it all lines up..."
    warren "All except for the part where you actually reprogram the house."
    bottomi "S...sorry?"
    warren "See, I've got a printout here from the smart house's data logs."
    warren "It shows a the moment 'Tour Mode' ended, it shows a disabling of the safety protocols..."
    warren "But nowhere does it say that somebody altered the security system."
    bottomi "w-www-wh-w-wha-wh-what?"
    warren "Doesn't that strike you as odd?"
    warren "Every other minute detail recorded, but this massive change to the security system goes unmentioned."
    warren "It's almost as if..."
    warren "YOU NEVER TOUCHED THOSE SYSTEMS AT ALL!"
    bottomi "GGGGUAAAAAAAAAAAAAAGHHH!!!!!"
    bottomi "STOP ATTACKING MY MEMORIIIIIEEEEEEES!"
    warren "How about you start telling us the truth?"
    bottomi "You wanna know the truth?!"
    bottomi "I... I... I hacked the data output too!"
    warren "WHAT!?"
    bottomi "It makes sense, right? If I got into the security system, I could have gotten into the data logs too!"
    bottomi "Of course I would delete the evidence of my infiltration... I would want to cover my tracks!"
    bottomi "You see, there was never any contradiction at all..."
    warren thought "Why is he using the tone of voice people use when they're trying to reassure themselves?"
    bottomi "So, does that answer all of your questions?"
    warren "Not so fast. I still want to know how you faked the crime scene in the kitchen."
    bottomi "Okay, okay. Let me remember exactly what I did..."
    warren thought "How hard is it to remember? Didn't this happen only a couple of hours ago?"

    # Eyewitness Statement ANIMATION
    typing "-- Faking a Crime Scene in 5 Easy Steps --{fast}"

    bottomi "The security system uses a blade hidden in its retractor arms for lethal neutralizations."
    bottomi "The house can't distinguish a dead body from any other inanimate objects."
    bottomi "So I told it that I needed something moved into the kitchen for me."
    bottomi "I had the body dropped on the floor, then asked the house to stab it with a knife."
    bottomi "I never even had to enter the kitchen myself."

    #fade out, fade in
    warren "I see."
    warren "And the purpose of this whole undertaking was to obfuscate your role as the killer?"
    bottomi "That's right. Though eventually I felt guilty and came back here to confess."
    warren "How ethical of you."
    drang "Are you done with this exercise in futility yet?"
    drang "We've already gone so late the I'm going to need to stay the night in this godforsaken town."
    warren "I'm sorry, Agent Drang. I won't stop until this man's testimony lines up with the facts."
    warren "I can reccomend you a nice hotel when I'm finished here."
    drang "If it's reccomended by you, I'll probably have to answer a five-part questionaire before they let me go to bed."

$ current_present = "SH_Objection5"
$ back_action = "CurrentTestimony"
$ concernForZombies = False

label SH_Testimony5A:
    $ settesti("SH_Testimony5A", None, "SH_Testimony5B", "SH_Press5A","SH_Advice5")
    show screen testi
    bottomi "The security system uses a blade hidden in its retractor arms for lethal neutralizations."
    jump SH_Testimony5B

label SH_Press5A:
    hide screen testi
    warren "A hidden blade? This place is sounding more and more ridiculous."
    warren "The US Consumer Product Safety Commission is going to have a field day in here."
    ash "Come on, Randi. You gotta admit it sounds pretty cool."
    ash "I mean, it's knife arms! Haven't you ever wanted knife arms?"
    warren "I can say with a great deal of certainty that I have never wanted anything of the sort."
    ash "I'll bet they spring out of those arms all like SHINK! YAH! STAB STAB!"
    ash "Plus, I'll bet they're pretty useful for chopping vegetables."
    ash "Do you think it can do knife tricks like at those fancy restaurants?"
    warren "Honestly, I'd rather not find out."
    bottomi "Uh, sorry, do you still need me here or..."
    warren "Right! Sorry. Go ahead, Mr Bottomi."
    bottomi "Well, as I was saying..."
    jump SH_Testimony5B

label SH_Testimony5B:
    $ settesti("SH_Testimony5B", "SH_Testimony5A", "SH_Testimony5C", "SH_Press5B","SH_Advice5")
    show screen testi
    bottomi "The house can't distinguish a dead body from any other inanimate objects."
    jump SH_Testimony5C

label SH_Press5B:
    hide screen testi
    warren "What about that biometric thingy you mentioned earlier? The one that registers profiles?"
    bottomi "The scanner uses people's heartbeats to recognize people."
    bottomi "Once the heart stops, the house loses 'sight' of them."
    ash "The heartbeat, huh?"
    ash "So if a zombie came in here, it could walk right by and the house wouldn't even notice!"
    bottomi "I... guess not?"
    ash "That seems like a pretty glaring design flaw! Somebody should talk to Miss Neering about that!"
    warren "I doubt that would rank very high on her to-do list..."
    ash "* sigh * Some people just don't have their priorities straight."
    $ concernForZombies = True
    jump SH_Testimony5C

label SH_Testimony5C:
    $ settesti("SH_Testimony5C", "SH_Testimony5B", "SH_Testimony5D", "SH_Press5C","SH_Advice5")
    show screen testi
    bottomi "So I told it that I needed something moved into the kitchen for me."
    jump SH_Testimony5D

label SH_Press5C:
    hide screen testi
    warren "So it picked the body up using those... weird snaking arms?"
    bottomi "That's right."
    warren "Could those things even lift something like that?"
    bottomi "Why don't you ask it?"
    warren "Huh? Oh, right...."
    warren "Hey, HARPER!"
    harper "Hello There, User 'Miranda'."
    warren "Exactly how much can those arms of yours lift?"
    harper "Each Of My Actuated Robotic Manipulators, Or A.R{nw}"
    warren "A.R.Ms, yeah, I get it."
    harper "Each One Is Capable Of Lifiting Over One Thousand Pounds."
    harper "This Makes Me Perfect For Moving Heavy Furniture Around The House."
    bottomi "Still have any doubts?"
    warren "No, no, I got it."
    harper "Is There Anything In Particular You Need Lifting?"
    warren thought "Maybe my spirits..."
    warren "No, thank you HARPER."
    harper "If You Need Anything Else, Just Ask."
    harper "I Am Literally Always Listening!"
    warren thought "That still hasn't gotten any less creepy..."
    warren "Okay, Mr Bottomi. What did you do next?"
    jump SH_Testimony5D

label SH_Testimony5D:
    $ settesti("SH_Testimony5D", "SH_Testimony5C", "SH_Testimony5E", "SH_Press5D","SH_Advice5")
    show screen testi
    bottomi "I had the body dropped on the floor, then asked the house to stab it with a knife."
    jump SH_Testimony5E

label SH_Press5D:
    hide screen testi
    warren "So the kitchen knife we found in the victim's back..."
    bottomi "It wasn't the real murder weapon. It was a ruse, a distraction."
    warren "That still doesn't explain -"
    bottomi "The bruises? I have an explaination for those, too."
    bottomi "The smart house didn't know it was holding a body, so it handled the thing pretty clumsily."
    bottomi "It kept bumping the body into walls and dropping it on the ground."
    warren "How...darkly comical."
    warren "Did you ever think to help the smart house out?"
    warren thought "And perhaps begin some sort of two-man slapstick routine?"
    bottomi "There was never any need to. In fact..."
    jump SH_Testimony5E

label SH_Testimony5E:
    $ settesti("SH_Testimony5E", "SH_Testimony5D", "SH_Testimony5A", "SH_Press5E","SH_Advice5")
    show screen testi
    bottomi "I never even had to enter the kitchen myself."
    jump SH_Testimony5A

label SH_Press5E:
    hide screen testi
    warren "What do you mean by that?"
    bottomi "Well, I had him killed in the downstairs hallway..."
    bottomi "I had the house move the body and clean up the blood..."
    bottomi "And then I just left through the front door."
    bottomi "It was so simple that I never had a reason to go in the kitchen myself."
    warren thought "He never went in the kitchen himself..."
    warren thought "Does that really check out?"
    jump SH_Testimony5A

label SH_Advice5:
    hide screen testi
    warren "didnt get his hands dirty but maybe got his FEET dirty lol"
    jump CurrentTestimony

label SH_Objection5:
    hide screen testi
    if testipart == "SH_Testimony5E" and present_response == "Footprints":
        jump SH_Success5
    else:
        jump SH_Failure5

label SH_Failure5:
    warren "Wait just a minute, Mr Bottomi!"
    bottomi "What? Why?"
    warren "Because I'm having trouble finding a contradiction in any of your statements."
    warren "So if you could just wait a minute while I think this over..."
    warren ". . . . . . ."
    warren "Yeah, I got nothing. Sorry, everybody."
    warren "Go ahead and give me that penalty, Agent Drang."
    $ mc_health -= 1
    warren "Thank you."
    if mc_health == 0:
        jump SH_GameOver5
    else:
        jump SH_Testimony5A

label SH_GameOver5:
    drang "Well, you've been very helpful, Ms Warren."
    drang "You found me the means, the motive, and the opportunity."
    drang "But it looks like your usefulness has finally run out."
    drang "You and your little friends have one minute to get out of here before I arrest you all."
    warren "But I'm so cl{nw}"
    drang "Fifty nine! Fifty eight! Fifty seven!"
    show black with fade
    warren thought "And so, the truth disappeared into darkness."
    warren thought "Drang failed to bring the real culprit to justice."
    warren thought "And I never unravelled the enigma of Base 24."
    jump endgame

label SH_Success5:
    warren "Just to get things straight, you're now telling me you never entered the kitchen?"
    bottomi "That's right. There was simply no need."
    warren "Well, that's real interesting..."
    warren "Because if you never entered the kitchen yourself..."
    warren "THEN WHO IS RESPONSIBLE FOR THESE MUDDY FOOTPRINTS?"
    bottomi "GHWARK!"
    bottomi "But! But! But wait a minute!"
    bottomi "Who's to say those footprints are mine?"
    bottomi "LOTS OF PEOPLE HAVE FEET, RIGHT?"
    warren "Maybe so, but not everyone's footprints have the same pattern as YOUR OWN SHOES!"
    bottomi "But wait... I'm wearing medical slippers!"
    bottomi "These are provided by the base for everyone who volunteers in a clinical trial!"
    bottomi "THERE ARE HUNDREDS OF PAIRS OF SHOES JUST LIKE THESE WITHIN A SQUARE MILE OF THE HOUSE!"
    warren "Wh-WHAAAAAAAAAAT!?"
    warren thought "This is bad... my perfect contradiction!"
    drang "You've reached the end of your rope, Warren."
    drang "I'm feeling pretty confident in the facts of the case as we know them."
    drang "It's time to pack it all up and take this guy into custody."
    warren "W-wait! What if I can still prove that Louis Bottomi was in the kitchen?"
    drang "How? You've already used up your ace in the hole and it turned out to be a dud."
    drang "Unless you're saying you've got another way to prove where Bottomi was?"
    warren thought "Hmm... that's a good point..."

label kitchenProof:
    warren thought "{color=red}Do I Have Any Other Proof That Bottomi Was In The Kitchen?{/color}"
    menu:
        "Yes, I do.":
            warren "Yes, I do."
            drang "Great, then let's see it?"
            drang "{color=red}What Else Do You Have Which Proves The Suspect Entered The Kitchen?{/color}"
            $current_present = "kitchenProofPresent"
            show screen present_evidence_screen
            pause

        "No, I don't.":
            warren "No, I don't think I do."
            drang "Then that's it. This case is closed."
            ash "Randi, what are you doing?"
            ash "You've gotta have something else you can use as proof!"
            ash "Otherwise, Mr Bottomi is done for!"
            warren "Wait! Hold on! I've changed my mind."
            drang "You've wated my time is what you've done."
            drang "Let this penalty be a lesson for you."
            $ mc_health -= 1
            warren thought "Okay, I kind of deserved that..."
            if mc_health == 0:
                jump SH_GameOver5
            else:
                warren thought "So, let's ask the question again..."
                jump kitchenProof

label kitchenProofPresent:
    if present_response == "EyewitnessPhoto":
        jump kitchenProofSuccess
    else:
        drang "I don't see how that piece of evidence proves anything."
        drang "Other than your own incompetence, perhaps!"
        $ mc_health -= 1
        warren "Gaaah! That wasn't the proof I was looking for!."
        if mc_health == 0:
            jump SH_GameOver5
        else:
            warren "Okay, I need to think this over one more time..."
            jump kitchenProof

label kitchenProofSuccess:
    warren "How soon you forget, Agent Drang."
    warren "Little more than an hour ago you brought up {color=red}this photo{/color} when making your case for Mr Bottomi's guilt."
    ### Flashback Filter with white flash
    warren "You really think he's our guy?"
    drang "Of course he is! He just confessed, didn't he?"
    drang "Take another look at the photograph that schmuck took."
    # Show Photo
    drang "See that second figure in the window? That's gotta be him!"
    # Hide Photo
    ### Flashback Filter with white flash
    drang "Hah, well, is that so? It, uh, completely slipped my, uh, mind...."
    warren "I'm sure you already realize what this means."
    warren "If Mr Bottomi is visible in this photograph..."
    warren "Then he must have entered the kitchen at some point!"
    drang "Well, ah, you see, the thing about that is..."
    drang "Who...uh.....cares?"
    warren "I'm sorry?"
    drang "He went in the kitchen, he didn't go to the kitchen, what's the difference?"
    warren "The difference is that he explicitly told us tha{nw}"
    drang "The guy made a mistake. It happens to the best of us."
    drang "Poor sucker's been lying on the ground unconscious for half an hour. He's probably still woozy."
    bottomi "That's...uh... that's right."
    bottomi "Of course I went into the kitchen. I just got confused for a little while there."
    bottomi "I'm sorry for the uncertainty this caused. Do you wish to hear more about how I killed Mr Darsha?"
    warren thought "Great... they're working together to patch up holes in his story now."
    warren thought "I've gotta come up with some damning evidence fast or these two are going to cover the whole thing up."
    warren "Go ahead with your testimony, Mr Bottomi."

    # Eyewitness Statement ANIMATION
    typing "-- The Where, When and How of the Murder --{fast}"
    bottomi "Mr Darsha and I were in the smart house. He had just fired me."
    #bottomi "We were in the downstairs hallway at the time."
    bottomi "Using my implant, I noticed that somebody had left the access point to the house open."
    bottomi "So I hacked my way in while we were still talking, and forced the house to kill him."
    bottomi "The house stabbed him in the back, killing him instantly."

    # fade out, fade in
    bottomi "And that's it. That's the whole story."
    warren "Well, hold on. What about-"
    drang "Nope, that's all you're getting, Warren."
    drang "Your incessant questioning has been leading us in circles for hours now."
    drang "If you can't completely discount the suspect's story using this one testimony, then this case is closed."
    warren "What? But there's so much here which hasn't been explained."
    drang "So what? Unexplainable stuff happens all the time!"
    drang "Why, just the other week I purchased a marvellous diamond ring for my mother."
    drang "But when my geologist friend examined it, he told me that it was made out of glass!"
    drang "Now how does diamond transform into glass overnight? It's just a mystery of the universe."
    warren thought "Uh, it sounds like you just got ripped off."
    drang "So! I'm giving you this one testimony, because I'm a real nice guy."
    drang "But after that, I'm arresting this man and heading back to the agency."
    drang "I have an appointment with a local alchemist tomorrow that I simply {i}can not{/i} reschedule!"
    warren thought "Great. This is my last chance to get to the bottom of things."
    warren thought "Better make it count."

$ current_present = "SH_Objection6"
$ unlockedTestimony = "None"
$ back_action = "CurrentTestimony"

label SH_Testimony6A:
    $ settesti("SH_Testimony6A", None, "unlockedTestimony", "SH_Press6A","SH_Advice6")
    show screen testi
    bottomi "Mr Darsha and I were in the smart house. He had just fired me."
    if unlockedTestimony == "6B":
        jump SH_Testimony6B
    if unlockedTestimony == "6C":
        jump SH_Testimony6C
    if unlockedTestimony == "None":
        jump SH_Testimony6D

label SH_Press6A:
    hide screen testi
    warren "You still maintain that your firing was the motive for killing Mr Darsha?"
    bottomi "Well, of course. Why would that have changed?"
    warren "Well, it's just that so many {i}other{/i} parts of your story have changed, I thought maybe this had too."
    drang "Sheriff Warren, you will refrain from being passive aggressive with the witness."
    warren "Fine, fine."
    warren "Still, it feels like your description of the circumstances is a little lacking."
    warren "Can you please tell me more about..."
    menu:
        "...where this all took place?":
            warren "...where this all took place?"
            bottomi "Of course."
            bottomi "Mr Darsha took me aside to the downstairs hallway to fire me."
            warren "The downstairs hallway?"
            bottomi "It's the one which from the kitchen to the living room."
            bottomi "You can see it through that door over there."
            warren "I see. So that's the room where Mr Bottomi was killed?"
            bottomi "That's right."
            warren thought "Is this information important?"
            menu:
                "Yes, very important.":
                    warren "Mr Bottomi, could you add this information to your testimony?"
                    bottomi "Sure, if you think it's that important."
                    $ unlockedTestimony = "6B"
                "No, not really.":
                    warren "I probably don't need any of this information."
                    warren "Thank you anyways, Mr Bottomi."
                    bottomi "Uh, sure. Anyways..."

        "...when this all took place?":
            warren "...when this all took place?"
            bottomi "Uh, okay."
            bottomi "Mr Darsha had just come back from the tour of the Smart House when he brought me aside."
            bottomi "So it must have been sometime around... 5:30?"
            warren thought "Well, that lines up with when Tour Mode ended in the Smart House's feedback logs..."
            warren "In that case, Mr Darsha would have died sometime around 5:35 or so, is that right?"
            bottomi "Yeah, that sounds correct..."
            warren thought "Is this information important?"
            menu:
                "Yes, very important.":
                    warren "Mr Bottomi, could you add this information to your testimony?"
                    bottomi "Sure, if you think it's that important."
                    $ unlockedTestimony = "6C"
                "No, not really.":
                    warren "I probably don't need any of this information."
                    warren "Thank you anyways, Mr Bottomi."
                    bottomi "Uh, sure. Anyways..."

    if unlockedTestimony == "6B":
        jump SH_Testimony6B
    if unlockedTestimony == "6C":
        jump SH_Testimony6C
    if unlockedTestimony == "None":
        jump SH_Testimony6D

label SH_Testimony6B:
    $ settesti("SH_Testimony6B", "SH_Testimony6A", "SH_Testimony6D", "SH_Press6B","SH_Advice6")
    show screen testi
    bottomi "We were in the downstairs hallway at the time."
    jump SH_Testimony6D

label SH_Press6B:
    hide screen testi
    warren "Why weren't there any bloodstains in the hallway?"
    warren "If that's where he was stabbed, then surely some blood would have splattered onto something."
    bottomi "Well, um, it turns out that one of the things this automated butler house is really good at is, uh, {i}cleaning.{/i}"
    bottomi "After I'd faked the crime scene in the kitchen, I had Harper clean up the hallway."
    bottomi "It did such a good job, I doubt even your friend in the medical coat over there could find a trace of blood."
    carlos "I, uh, don't think that's how bloodstains work."
    carlos "You want me to go sweep the hallway real quick, Chief?"
    warren "Don't worry about it, Tsukada."
    warren thought "I don't think I'm going to need help poking a hole in this claim..."
    jump SH_Testimony6D

label SH_Testimony6C:
    $ settesti("SH_Testimony6C", "SH_Testimony6A", "SH_Testimony6D", "SH_Press6C","SH_Advice6")
    show screen testi
    bottomi "Mr Darsha had just come back from the tour of the Smart House. It was around 5:30."
    jump SH_Testimony6D

label SH_Press6C:
    hide screen testi
    warren "You're sure it was 5:30?"
    bottomi "Pretty sure."
    carlos "Ah, I love five-o-clock."
    carlos "When most people need an excuse to drink, they'll say \"It's five-o-clock somewhere!\""
    carlos "But when it's already five, you don't even need to say it. You can just drink!"
    warren "You, on the other hand, {i}never{/i} need an excuse to drink."
    carlos "That's because Island Time truly is all the time!"
    carlos "Did I ever show you this custom watch I had made?"
    warren "Can we please focus on the c{nw}"
    carlos "Every hour is just replaced with the words 'Island Time'."
    carlos "It's completely useless as a timepiece, but it reminds me of what's important in life."
    warren thought "This line of questioning has yielded nothing but nonsense."
    warren thought "I think I'm barking up the wrong tree here..."
    jump SH_Testimony6D

label SH_Testimony6D:
    $ settesti("SH_Testimony6D", "unlockedTestimony", "SH_Testimony6E", "SH_Press6D","SH_Advice6")
    show screen testi
    bottomi "Using my implant, I noticed that somebody had left the access point to the house open."
    jump SH_Testimony6E

label SH_Press6D:
    hide screen testi
    warren "Why were you using your neural implant at that moment?"
    warren "Did you honestly expect to find a way to access the house?"
    bottomi "No, nothing like that."
    bottomi "I guess I knew that they were going to get rid of it soon, since I was being fired..."
    bottomi "And I wanted to give it one last go before I lost it."
    bottomi "Then I found the access point to the house open, and well..."
    bottomi "I started to get an idea..."
    warren "It was a crime of opportunity, then."
    bottomi "Well, of course. I wasn't planning on killing him {i}before{/i} he'd fired me."
    warren "Fair enough. What did you do next?"
    jump SH_Testimony6E

label SH_Testimony6E:
    $ settesti("SH_Testimony6E", "SH_Testimony6D", "SH_Testimony6F", "SH_Press6E","SH_Advice6")
    show screen testi
    bottomi "So I hacked my way in while we were still talking, and forced the house to kill him."
    jump SH_Testimony6F

label SH_Press6E:
    hide screen testi
    warren "It's pretty impressive you're able to maintain a conversation while doing something like that."
    warren "It seems like you would get distracted with one or the other."
    bottomi "It's not as hard as it sounds, actually."
    bottomi "It's just like browsing the internet while talking with a friend."
    bottomi "Nothing hard about that, right?"
    warren "Ah... um... isn't it, though?"
    ash "Forgive her, Mr Bottomi. You have to remember that Randi is computer illiterate."
    warren "I don't need qualifiers at the end of my sentences, Ash."
    warren "I get the point: talking and hacking isn't that hard."
    warren "Now tell me what happened next."
    bottomi "Okay, so..."
    jump SH_Testimony6F

label SH_Testimony6F:
    $ settesti("SH_Testimony6F", "SH_Testimony6E", "SH_Testimony6A", "SH_Press6F","SH_Advice6")
    show screen testi
    bottomi "The house stabbed him in the back, killing him instantly."
    jump SH_Testimony6A

label SH_Press6F:
    hide screen testi
    warren "How do you know it was instant?"
    bottomi "I guess I don't know for sure..."
    bottomi "But he stopped moving right when the house stuck its blade through him."
    bottomi "It looked pretty instant to me..."
    warren "I'm sorry, Mr Bottomi, but..."
    warren "\"Looked pretty instant\" isn't exactly a confirmation of death!"
    drang "Are you going to stand around arguing semantics, or do you have some proof to back up whatever you're claiming?"
    drang "In the absence of solid evidence, this witness's statment is the best indication we have of what happened here."
    drang "We need to trust it fully unless we have something more concrete which conflicts with it."
    warren thought "Wow, that was an unusually solid point considering it came from Drang."
    jump SH_Testimony6A

label SH_Advice6:
    hide screen testi
    ash "Did you hear Special Agent Doofus over there?"
    ash "You've only got this last chance to find the flaw in Mr Bottomi's story!"
    ash "What are we going to do?"
    warren "Don't worry. There's a key contradiction hidden in this testimony."
    warren "We just need to press harder and {color=red}ask the right question{/color} in order to draw it out of Mr Bottomi."
    ash "The right question?"
    ash "But what if you end up asking the {color=red}wrong question?{/color}"
    warren "Well in that case I can always {color=red}ask again.{/color}"
    ash "Okay. Let's give this everything we've got!"
    jump CurrentTestimony

label SH_Objection6:
    hide screen testi
    if testipart == "SH_Testimony6B" and present_response == "Missing Shoe":
        jump SH_Success6
    else:
        jump SH_Failure6

label SH_Failure6:
    warren "Here it is. The evidence that's going to blow this thing wide open."
    warren "What do you think of this, Mr. Bottomi?"
    bottomi "Uh, I dunno. It's kind of nice, I guess..."
    bottomi "Wait, sorry... was that supposed to be your evidence?"
    warren "Rats, I don't think that was the evidence I needed."
    drang "There goes your last chance, Warren. Time to close this case for good."
    warren "Wait! No!"
    warren "Wouldn't you say that I only used up twenty percent or so of my last chance there?"
    drang "Sure, sure... as long as you're fine with taking one hundred percent of a penalty."
    $ mc_health -= 1
    warren thought "Ouch... well, I guess I can't complain..."
    if mc_health == 0:
        jump SH_GameOver6
    else:
        jump SH_Testimony6A

label SH_GameOver6:
    drang "Well, we've put this whole testimony under a microscope and you still haven't found anything."
    drang "Looks like it's time to finally call it a night."
    drang "Louis Bottomi, you're under arrest for the murder of Orin Darsha."
    drang "You have the right to remain silent. Anything you say... oh, hey Warren!"
    warren "W-what?"
    drang "I feel like you should be doing this part."
    drang "These are the {i}Miranda{/i} Rights, after all."
    drang "See, it's a pun, because your name is Miranda, and the thing you say to criminals is called the...{nw}"
    show black with fade
    warren thought "And so, the truth disappeared into darkness."
    warren thought "Drang failed to bring the real culprit to justice."
    warren thought "And I never unravelled the enigma of Base 24."
    jump endgame

label SH_Success6:
    warren "The downstairs hallway, huh?"
    bottomi "That's right..."
    warren "Do you reckon that Mr Darsha lost his shoe during the house's attack?"
    bottomi "That... sounds about right."
    bottomi "Uh, why?"
    warren "Well, it seems we've got a problem here, Mr Bottomi."
    bottomi "* gulp *"
    warren "You see, I managed to find the shoe while I was investigating."
    warren "Only...I didn't find it in the hallway..."
    warren "I FOUND IT UPSTAIRS, IN THE DRESSING CONTRAPTION!"
    bottomi "WHAAAAAAAT!?"
    warren "Ash here confirmed for me that Mr Darsha didn't use the contraption during the tour."
    warren "So: do you mind explaining to me how the victim's shoe ended up in a room he never even visited?"
    warren "The only explaination is: YOUR ENTIRE STORY IS A FABRICATION!"
    bottomi "Th-this isn't right! It doesn't m-m-make any sense! I remember it so clearly, a-and yet... IT'S ALL WRONG!"
    bottomi "NNNNNNNNNNNNNNNNOOOOOOOOOOOOOOOOOOOOOAAAAAAAAA{nw}"
    # Drang HOLD ITs
    drang "Hold your horses, Warren."
    drang "Being a small-town cop, I assume you have several, which you use in place of squad cars."
    warren "What are you on about?"
    drang "Hah! It really is exhausting, having to be the only voice of reason around here."
    drang "But I guess I'm going to have to spell it all out to you:"
    drang "The location of that shoe doesn't {i}prove{/i} anything about how the victim died."
    warren "Of course it does! It proves he wasn't in the downstairs hallway!"
    drang "Does it really, though? Let's consider a few hypotheticals..."
    drang "The Dressing Contraption is basically a glorified closet, right?"
    drang "Who's to say it doesn't stock the same kind of shoe the victim wears?"
    drang "And who's to say one of those shoes didn't fall out of place?"
    warren "We could easily check on that, though..."
    drang "All right, here's another hypothetical:"
    drang "Perhaps the house hid Darsha's shoe up there when it was cleaning up the crime scene."
    drang "We can't confirm or deny that, since the house lost its memory in the blackout."
    drang "Still, it's a completely valid possibility."
    drang "And, my final hypothetical: what if your little sidekick is just lying about Darsha?"
    drang "Perhaps he really did use The Dressing Contraption, and Ash here is covering it up!"
    ash "You really think I would lie to a Federal Officer?"
    drang "In this business, you learn not to trust anyone."
    warren thought "Except for Bottomi, apparently..."
    drang "So, do you have anything to refute my possibilities?"
    warren "I... I..."
    warren "...I don't."
    warren "But if you could just give me a little more time!"
    drang "Did you forget our little agreement? If you couldn't poke a hole in this one last testimony, you were done."
    drang "And, well, it looks like you couldn't do it."
    drang "You know what that means!"
    warren thought "N-no! It can't end like this! Not after I've come so far!"
    warren thought "I really thought I could get to the bottom of things this time... I thought that if I could just solve {i}this{/i} case, then... then..."
    warren thought "Then it would be like I had never failed all those years ago..."
    warren thought "But once again... I couldn't do it..."
    warren thought "I failed the town... I failed Ash...."
    warren thought "Damn it! All I needed was {i}one more{/i} piece of evidence!"
    drang "Louis Bottomi, you're under arrest for the murder of Orin Darsha."
    drang "You have the right to remain silent. Anything you s{nw}"
    # Carlos HOLD ITs
    carlos "Hold it! Hold everything!"
    carlos "Nobody's arresting anybody until I show this to Sheriff Warren!"
    warren "Carlos? What are you doing?"
    carlos "I finally finished up the Autopsy Report, and, well, you're gonna want to see this."
    ### Warren reading
    warren "Hm . . . . . Ah!"
    carlos "You see that?"
    warren "Yeah, I see it all right."
    ### Add Updated Autopsy Report
    warren "Agent Drang, I just need one more testimony out of this witness."
    warren "Just one more, and I guarauntee I can expose the truth."
    drang "Hmm... no."
    warren "WWWHHAT!?"
    drang "I said you only got one last testimony, and I'm sticking by that."
    drang "But... if you think you can find a flaw in the one we just heard, I'd love to see you try."
    drang "So, what do you think?"
    warren thought "Shoot... can I really find another flaw in that last testimony?"
    menu:
        "Of course I can.":
            warren thought "Of course! This last piece of evidence was exactly what I needed."
            warren thought "Carlos has given me a chance to turn this around... I can't waste it!"
        "Probably not, but I have to try anyway.":
            warren thought "Probably not. There's a lot stacked against me."
            warren thought "Still, I can't give up. Not after Carlos has given me this last shot!"
            warren thought "I should probably put on an act of confidence for Drang, though..."
    warren "Of course I can do it!"
    drang "Ooh, things are heating up!"
    drang "All right, Bottomi. Let's hear that testimony one more time, all right?"
    drang "And don't give Miss Confidence any more info than you already have."
    drang "We have to keep things fair, after all."

$ current_present = "SH_Objection7"
$ unlockedTestimony = "7B"
$ back_action = "CurrentTestimony"

label SH_Testimony7A:
    $ settesti("SH_Testimony7A", None, "unlockedTestimony", "SH_Press7A","SH_Advice7")
    show screen testi
    bottomi "Mr Darsha and I were in the smart house. He had just fired me."
    if unlockedTestimony == "7B":
        jump SH_Testimony7B
    if unlockedTestimony == "7C":
        jump SH_Testimony7C
    if unlockedTestimony == "None":
        jump SH_Testimony7D

label SH_Press7A:
    hide screen testi
    warren "You still maintain that your firing was the motive for killing Mr Darsha?"
    bottomi "Well, of course. Why would that have changed?"
    warren "Well, it's just that so many {i}other{/i} parts of your story have changed, I thought maybe this had too."
    drang "Sheriff Warren, you will refrain from being passive aggressive with the witness."
    warren "Fine, fine."
    warren "Still, it feels like your description of the circumstances is a little lacking."
    warren "Can you please tell me more about..."
    menu:
        "...where this all took place?":
            warren "...where this all took place?"
            bottomi "Of course."
            bottomi "Mr Darsha took me aside to the downstairs hallway to fire me."
            warren "The downstairs hallway?"
            bottomi "It's the one which from the kitchen to the living room."
            bottomi "You can see it through that door over there."
            warren "I see. So that's the room where Mr Bottomi was killed?"
            bottomi "That's right."
            warren thought "Is this information important?"
            menu:
                "Yes, very important.":
                    warren "Mr Bottomi, could you add this information to your testimony?"
                    bottomi "Sure, if you think it's that important."
                    $ unlockedTestimony = "7B"
                "No, not really.":
                    warren "I probably don't need any of this information."
                    warren "Thank you anyways, Mr Bottomi."
                    bottomi "Uh, sure. Anyways..."

        "...when this all took place?":
            warren "...when this all took place?"
            bottomi "Uh, okay."
            bottomi "Mr Darsha had just come back from the tour of the Smart House when he brought me aside."
            bottomi "So it must have been sometime around... 5:30?"
            warren thought "Well, that lines up with when Tour Mode ended in the Smart House's feedback logs..."
            warren "In that case, Mr Darsha would have died sometime around 5:35 or so, is that right?"
            bottomi "Yeah, that sounds correct..."
            warren thought "Is this information important?"
            menu:
                "Yes, very important.":
                    warren "Mr Bottomi, could you add this information to your testimony?"
                    bottomi "Sure, if you think it's that important."
                    $ unlockedTestimony = "7C"
                "No, not really.":
                    warren "I probably don't need any of this information."
                    warren "Thank you anyways, Mr Bottomi."
                    bottomi "Uh, sure. Anyways..."

    if unlockedTestimony == "7B":
        jump SH_Testimony7B
    if unlockedTestimony == "7C":
        jump SH_Testimony7C
    if unlockedTestimony == "None":
        jump SH_Testimony7D

label SH_Testimony7B:
    $ settesti("SH_Testimony7B", "SH_Testimony7A", "SH_Testimony7D", "SH_Press7B","SH_Advice7")
    show screen testi
    bottomi "We were in the downstairs hallway at the time."
    jump SH_Testimony7D

label SH_Press7B:
    hide screen testi
    warren "Why weren't there any bloodstains in the hallway?"
    warren "If that's where he was stabbed, then surely some blood would have splattered onto something."
    bottomi "Well, um, it turns out that one of the things this automated butler house is really good at is, uh, {i}cleaning.{/i}"
    bottomi "After I'd faked the crime scene in the kitchen, I had Harper clean up the hallway."
    bottomi "It did such a good job, I doubt even your friend in the medical coat over there could find a trace of blood."
    drang "Now remember, that contradiction you already found won't work this time. That shoe doesn't prove a thing."
    drang "So for your sake, I hope you have another idea."
    jump SH_Testimony7D

label SH_Testimony7C:
    $ settesti("SH_Testimony7C", "SH_Testimony7A", "SH_Testimony7D", "SH_Press7C","SH_Advice7")
    show screen testi
    bottomi "Mr Darsha had just come back from the tour of the Smart House. It was around 5:30."
    jump SH_Testimony7D

label SH_Press7C:
    hide screen testi
    warren "You're sure it was 5:30?"
    bottomi "Pretty sure."
    carlos "Ah, I love five-o-clock."
    carlos "When most people need an excuse to drink, they'll say \"It's five-o-clock somewhere!\""
    carlos "But when it's already five, you don't even need to say it. You can just drink!"
    warren "You, on the other hand, {i}never{/i} need an excuse to drink."
    carlos "That's because Island Time truly is all the time!"
    carlos "Did I ever show you this custom watch I had made?"
    warren "Can we please focus on the c{nw}"
    carlos "Every hour is just replaced with the words 'Island Time'."
    carlos "It's completely useless as a timepiece, but it reminds me of what's important in life."
    warren thought "This line of questioning has yielded nothing but nonsense."
    warren thought "I think I'm barking up the wrong tree here..."
    jump SH_Testimony7D

label SH_Testimony7D:
    $ settesti("SH_Testimony7D", "unlockedTestimony", "SH_Testimony7E", "SH_Press7D","SH_Advice7")
    show screen testi
    bottomi "Using my implant, I noticed that somebody had left the access point to the house open."
    jump SH_Testimony7E

label SH_Press7D:
    hide screen testi
    warren "Why were you using your neural implant at that moment?"
    warren "Did you honestly expect to find a way to access the house?"
    bottomi "No, nothing like that."
    bottomi "I guess I knew that they were going to get rid of it soon, since I was being fired..."
    bottomi "And I wanted to give it one last go before I lost it."
    bottomi "Then I found the access point to the house open, and well..."
    bottomi "I started to get an idea..."
    warren "It was a crime of opportunity, then."
    bottomi "Well, of course. I wasn't planning on killing him {i}before{/i} he'd fired me."
    warren "Fair enough. What did you do next?"
    jump SH_Testimony7E

label SH_Testimony7E:
    $ settesti("SH_Testimony7E", "SH_Testimony7D", "SH_Testimony7F", "SH_Press7E","SH_Advice7")
    show screen testi
    bottomi "So I hacked my way in while we were still talking, and forced the house to kill him."
    jump SH_Testimony7F

label SH_Press7E:
    hide screen testi
    warren "It's pretty impressive you're able to maintain a conversation while doing something like that."
    warren "It seems like you would get distracted with one or the other."
    bottomi "It's not as hard as it sounds, actually."
    bottomi "It's just like browsing the internet while talking with a friend."
    bottomi "Nothing hard about that, right?"
    warren "Ah... um... isn't it, though?"
    ash "Forgive her, Mr Bottomi. You have to remember that Randi is computer illiterate."
    warren "I don't need qualifiers at the end of my sentences, Ash."
    warren "I get the point: talking and hacking isn't that hard."
    warren "Now tell me what happened next."
    bottomi "Okay, so..."
    jump SH_Testimony7F

label SH_Testimony7F:
    $ settesti("SH_Testimony7F", "SH_Testimony7E", "SH_Testimony7A", "SH_Press7F","SH_Advice7")
    show screen testi
    bottomi "The house stabbed him in the back, killing him instantly."
    jump SH_Testimony7A

label SH_Press7F:
    hide screen testi
    warren "How do you know it was instant?"
    bottomi "I guess I don't know for sure..."
    bottomi "But he stopped moving right when the house stuck its blade through him."
    bottomi "It looked pretty instant to me..."
    warren "I'm sorry, Mr Bottomi, but..."
    warren "\"Looked pretty instant\" isn't exactly a confirmation of death!"
    drang "Are you going to stand around arguing semantics, or do you have some proof to back up whatever you're claiming?"
    drang "In the absence of solid evidence, this witness's statment is the best indication we have of what happened here."
    drang "We need to trust it fully unless we have something more concrete which conflicts with it."
    warren thought "Wow, that was an unusually solid point considering it came from Drang."
    jump SH_Testimony7A

label SH_Advice7:
    hide screen testi
    ash "We're really on the ropes now, Randi."
    ash "Do you honestly think you can find {i}another{/i} contradiction in this old testimony."
    warren "It doesn't matter whether I can or not. The fact is, I {i}have{/i} to."
    warren "I need to take a look at that new evidence I got from Carlos; that's the key to everything."
    warren "If I can just figure out where that fits in, I can finally discount this story."
    ash "I beleive in you, Randi!"
    jump CurrentTestimony

label SH_Objection7:
    hide screen testi
    if testipart == "SH_Testimony7F" and present_response == "Updated Autopsy Report":
        jump SH_Success7
    else:
        jump SH_Failure7

label SH_Failure7:
    warren thought "Here it is! The final contradiction!"
    warren "Mister Bottomi... please take a look at this!"
    bottomi "I... I don't understand..."
    warren "Uh... you don't?"
    bottomi "Yeah, uh... this is supposed to be decisive proof, right?"
    warren "O-of course!"
    bottomi "I, uh, I don't know what you're talking about here..."
    warren ". . . . ."
    $ mc_health -= 1
    warren "Ack!"
    warren thought "I must have presented the wrong thing!"
    if mc_health == 0:
        jump SH_GameOver7
    else:
        jump SH_Testimony7A

label SH_GameOver7:
    drang "I knew you couldn't possibly figure this out..."
    drang "But at least it was fun to watch you try!"
    drang "I've gotta thank you for at least keeping things interesting around here."
    drang "Still, it's time to wrap things up. I've wasted enough time in this town as it is."
    drang "Louis Bottomi, you're under arrest for the murder of Orin Darsha."
    show black with fade
    warren thought "And so, the truth disappeared into darkness."
    warren thought "Drang failed to bring the real culprit to justice."
    warren thought "And I never unravelled the enigma of Base 24."
    jump endgame

label SH_Success7:
    warren thought "Here it is! The final contradiction!"
    warren "Mister Bottomi... please take a look at this!"
    bottomi "I... I don't understand..."
    warren "Well, then let me explain it to you."
    warren "Your entire story, from the beginning, has been based on one central premise."
    warren "Namely, the fact that Orin Darsha was killed by a stab wound to the back."
    warren "Now, I just got back a finalized autopsy report..."
    bottomi "Y-yes, I was there when that happened!"
    warren "...Right."
    warren "Now, one of the most interesting things this autopsy report reveals..."
    warren "Is that THE ACTUAL CAUSE OF DEATH WAS A BROKEN NECK!"
    bottomi "N-no! That can't be right! The doctor guy must have made a mistake!"
    warren "Not possible. Carlos may be eccentric, but he knows his medicine."
    bottomi "This can't be possible! I... I saw it with my own eyes! He was stabbed!"
    bottomi "Wait... but now I'm starting to remember...the machine breaking his neck?"
    bottomi "No! I know he was stabbed! How can I possibly have two memories of the same event?"
    bottomi "I remember everything...so many different ways...and none of it fits together!"
    bottomi "WHAAAAT IS HAAAPPENIIIIINGG TO MEEEEEEEEEEEEEEEEEEEEEEEEEE"
    # Bottomi's Head Fucking Explodes
    ash "Did his head just explode!?"
    carlos "Medically speaking, that's super bad for you!"
    warren "I think it was just his neuron thing..."
    warren "Carlos, go check on him!"
    carlos "I'm on it!"
    drang "Well, great job, Warren. You confused the witness so hard that he died."
    drang "Do you know how hard it is to prosecute a man with no head!?"
    warren "Wait a minute... do {i}you?{/i}"
    carlos "It's okay, everyone! He's waking up now!"
    bottomi "Oh...man....my head..."
    warren "Mr Bottomi! Are you all right?"
    bottomi "Actually...yes. My thoughts are starting to clear up..."
    bottomi "Wait...w-where's my neural implant?"
    carlos "It kinda short circuted. Nearly took your head off, actually!"
    bottomi "If the neural implant is gone... and I'm starting to think straight again..."
    ash "Oh my gosh! Somebody was using the implant to control your behavior, right?"
    bottomi "Exactly."
    warren "Ash was right!?"
    ash "I was right!?"
    bottomi "I mean, I can't say for sure..."
    bottomi "But I'm starting to think I'm not the one who killed Mister Darsha."
    bottomi "I think that somebody else {i}forced{/i} me to confess..."
    show black with fade
    jump smart_house_act_5_intro
