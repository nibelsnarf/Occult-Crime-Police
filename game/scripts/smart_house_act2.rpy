label smart_house_act_2:
    ### ACT 2: THE GOSSAMER PENANCE
    $ save_name = "Act 2"
    scene black
    typing "September 13th. 8:32 P.M.\nSmart House - Kitchen"
    scene kitchen with fade
    warren "Sir...what did you just say?"
    unknown bottomi "I- I think I'm the one who killed that man on the ground."
    unknown bottomi "No, I know it! I remember stabbing him with that knife!"
    warren "S-slow down, sir. What's your name?"
    bottomi "My name is Louis Bottomi."
    bottomi "H-how could I have done something like this?"
    bottomi "You're a police officer, right? You've got to arrest me!"
    # Add Bottomi profile to inventory
    drang "I reckon these are your footprints, then?"
    bottomi "Y-yes, that's right! I tracked in some mud from the garden when I came in here!"
    carlos "Let me see that shoe of yours..."
    carlos "Yup, it's the same pattern."
    warren thought "Well, that's {i}one{/i} mystery solved..."
    # Muddy Footprints Updates
    drang "Wow... this is fantastic!"
    drang "Man, I knew I was good, but I didn't know I was good enough to make murderers confess on the spot!"
    drang "Looks like this one is wrapped up neatly."
    drang "Let's book this creep real quick, and then I can get out of here!"
    warren "You really think he's our guy?"
    drang "Of course he is! He just confessed, didn't he?"
    drang "Take another look at the photograph that schmuck took."
    # Show Photo
    drang "See that second figure in the window? That's gotta be him!"
    warren thought "Wow, I didn't think he would notice that detail."
    drang "You see? It ties up all the loose ends!"
    # Hide Photo
    warren "Hold on a minute, Agent Drang."
    warren "Don't you think this is all a bit odd? Killers don't usually confess this easily."
    warren "Even remorseful ones like him..."
    warren "I think we need to {color=red}Interrogate{/color} him."
    drang "Do you have to make this so difficult?"
    drang "Fine. Go ahead."
    drang "But as far as I'm concerned, this case is already closed."
    warren "Mr Bottomi, can you please tell me your story from the start?"
    bottomi "Yeah, just give me a second."
    bottomi "My thoughts seem a little hazy right now..."
    bottomi "Okay, I'm ready."

    # Eyewitness Statement ANIMATION
    typing "-- Bottomi's Confession --{fast}"
    bottomi "I'm a test subject in a clinical trial here at the base."
    bottomi "Today I was here for another round in the trial."
    bottomi "I had some free time, so I came over here to take a look at the house."
    bottomi "I saw that man in the kitchen and was suddenly filled with rage."
    bottomi "So I grabbed a nearby knife and... I stabbed it into his back!"
    bottomi "After I left the house, I just sort of wandered around for a while."
    bottomi "How could I have done something so awful... you've got to lock me up!"

    # fade out, fade in
    carlos "Seems pretty straightforward to me."
    carlos "He doesn't have a clear motive, but he had the means and opportunity."
    warren "I don't know... there's one thing here that doesn't sit right with me."
    carlos "What's that?"
    warren "If you're already confessing to a murder... what's the point in lying to a police officer?"
    carlos "You mean you spotted a {color=red}contradiction{/color} in one of his statements?"
    warren "A pretty big one."
    ash "So what happens now, Randi?"
    warren "Now it's time to {color=red}interrogate{/color} the witness."
    ash "How does that work?"
    menu:
        "I'll explain it to you.":
            warren "I'll explain it to you."
            warren "Witness testimonies are often faulty in some way."
            warren "Maybe the witness is lying, or maybe they're just mistaken."
            warren "In either case, the only way to uncover the truth is to {color=red}present evidence{/color} which contradicts with their testimony."
            warren "Every piece of evidence is a small part of the truth."
            ash "How do you present evidence?"
            warren "First we go to the statement which contradicts the facts."
            warren "Next, we pull up our evidence and select the one which proves the contradiction."
            warren "Sometimes it may feel like the witness is holding something back."
            warren "In these cases I can {color=red}press{/color} them for further information."
            ash "This is all a lot to keep track of."
            warren "If you ever get too confused, we can {color=red}consult{/color} with each other on the best way to proceed."
        "You'll figure it out as we go.":
            warren "You'll figure it out as we go."
            ash "No tutorial for me, huh?"

label testimony1_intro:
    scene kitchen
    show mir
    show ash at flip
    ash "All right, let's take this guy's testimony down a peg!"
    # Interrogation Animation
    $ current_present = "SH_Objection1"
    $ back_action = "CurrentTestimony"
    $ mentionedhardware = False

label SH_Testimony1A:
    $ settesti("SH_Testimony1A", None, "SH_Testimony1B", "SH_Press1A","SH_Advice1")
    show screen testi
    bottomi "I'm a test subject in a clinical trial here at the base."
    jump SH_Testimony1B

label SH_Press1A:
    hide screen testi
    warren "What is this clinical trial studying?"
    bottomi "I'm not sure I'm allowed to tell you."
    bottomi "They make you sign a lot of contracts before the testing starts."
    bottomi "I think one of them says that I'm not allowed to tell you."
    warren "You're already a murder suspect. Are you really that concerned about breaking an NDA?"
    ash "Haven't you heard the stories about this place, Randi?"
    ash "You let one little thing leak, and they make you disappear!"
    bottomi "Anyways, I'm just a guinea pig. They don't really tell me how any of it works."
    bottomi "I just show up every so often and they do some different tests."
    bottomi "That's why I'm here right now..."
    jump SH_Testimony1B

label SH_Testimony1B:
    $ settesti("SH_Testimony1B", "SH_Testimony1A", "SH_Testimony1C", "SH_Press1B","SH_Advice1")
    show screen testi
    bottomi "Today I was here for another round in the trial."
    jump SH_Testimony1C

label SH_Press1B:
    hide screen testi
    warren "Is that why you've got that hospital gown on?"
    bottomi "Yeah. It's standard procedure while they do the tests."
    bottomi "Between you and me, they're a little itchy."
    warren "Was there anything different about this round of the trial?"
    warren "Anything that might account for your sudden outburt?"
    bottomi "I... don't think so."
    bottomi "They were just doing a check-up on the hardware."
    warren "Hardware?"
    bottomi "Oh! Uh... I don't think I'm allowed to tell you about that."
    warren thought "I'll have to figure out what he's referring to here."
    $ mentionedhardware = True
    warren thought "But first things first: I should point out that blatant contradiction in his testimony."
    bottomi "Anyway, that's why I was here at the base today."
    jump SH_Testimony1C

label SH_Testimony1C:
    $ settesti("SH_Testimony1C", "SH_Testimony1B", "SH_Testimony1D", "SH_Press1C","SH_Advice1")
    show screen testi
    bottomi "I had some free time, so I came over here to take a look at the house."
    jump SH_Testimony1D

label SH_Press1C:
    hide screen testi
    warren "Was this the first time you had been to the smart house?"
    bottomi "Yeah. Today was the grand unveiling."
    bottomi "Up until then, the house had always been hidden behind these big walls."
    bottomi "I didn't even know it was a house until today."
    bottomi "Of course, I wanted to know what was so darn special about it."
    bottomi "I'm still not really sure what it is."
    warren "It's a Smart House."
    bottomi "Oh, uh, okay."
    bottomi "So there's, what, a bunch of dictionaries in here?"
    warren "I'll explain it to you later. What happened next?"
    jump SH_Testimony1D

label SH_Testimony1D:
    $ settesti("SH_Testimony1D", "SH_Testimony1C", "SH_Testimony1E", "SH_Press1D","SH_Advice1")
    show screen testi
    bottomi "I saw that man in the kitchen and was suddenly filled with rage."
    jump SH_Testimony1E

label SH_Press1D:
    hide screen testi
    warren "What do you mean? Was there something specific that made you feel that way?"
    bottomi "I- I couldn't say."
    bottomi "Honestly, I'd never even met the guy before."
    bottomi "Something in my head just told me that I needed to attack him. I needed to hurt him."
    bottomi "I needed to make sure he never got up again, he never..."
    bottomi ". . ."
    bottomi "...I'm sorry..."
    warren "It's okay, Mr Bottomi. Just tell me what happened."
    jump SH_Testimony1E

label SH_Testimony1E:
    $ settesti("SH_Testimony1E", "SH_Testimony1D", "SH_Testimony1F", "SH_Press1E","SH_Advice1")
    show screen testi
    bottomi "So I grabbed a nearby knife and... I stabbed it into his back!"
    jump SH_Testimony1F

label SH_Press1E:
    hide screen testi
    warren "You're certain you stabbed him with a knife?"
    bottomi "It's one of the few things I am certain of."
    bottomi "A lot of the day is sort of fuzzy... but I remember stabbing him crystal clear."
    bottomi "I still remember what it felt like when the knife went into his back."
    warren thought "This is the most suspicious part of his testimony."
    warren thought "He's so confident in this one fact, even though there's such an obvious {color=red}contradiction{/color} in his claim!"
    warren thought "This is the place to start chipping away at his testimony!"
    bottomi "There's no doubt in my mind that I'm the one who killed him."
    jump SH_Testimony1F

label SH_Testimony1F:
    $ settesti("SH_Testimony1F","SH_Testimony1E", "SH_Testimony1G", "SH_Press1F", "SH_Advice1")
    show screen testi
    bottomi "After I left the house, I just sort of wandered around for a while."
    jump SH_Testimony1G

label SH_Press1F:
    warren "That's right, we ran into you earlier. You seemed like you were in a hurry."
    bottomi "Did I? I honestly don't remember."
    bottomi "I think I must have been in shock."
    bottomi "Maybe it's good I didn't see you... I might have tried to hurt you too!"
    warren "Don't worry... you wouldn't have succeeded."
    warren "So that's all you've been doing for the past hour?"
    bottomi "Yup. Just wandering around this base."
    bottomi "I'm kind of surprised nobody stopped me."
    bottomi "Eventually, I ended up back here."
    bottomi "The sight of that man must have snapped me out of my daze."
    jump SH_Testimony1G

label SH_Testimony1G:
    $ settesti("SH_Testimony1G", "SH_Testimony1F", "SH_Testimony1A", "SH_Press1G","SH_Advice1")
    show screen testi
    bottomi "How could I have done something so awful... you've got to lock me up!"
    jump SH_Testimony1A

label SH_Press1G:
    hide screen testi
    warren "How indeed? You claim not to have a motive for the crime."
    warren "And most people don't go around stabbing random individuals for no reason."
    warren "Do you have a history of mental illness, Mr Bottomi?"
    bottomi "You think I'm some kind of psycho?"
    bottomi "Well, sorry, but I'm not. I had to pass a medical examination to qualify for the clinical trial here."
    bottomi "They wouldn't have let me participate if I had something wrong with my head."
    bottomi "It would have interfered with the hardw- with the tests, I mean."
    if mentionedhardware == True:
        warren thought "There he goes, talking about \"hardware\" again."
    else:
        warren thought "Huh? What was he about to say there?"
    bottomi "So, no, I don't have any brain problems that I know about."
    bottomi "You think I coulda just, I dunno... snapped?"
    warren "I don't know. I'm not a doctor or anything."
    carlos "I am!"
    warren "..."
    warren "...So? {i}Could{/i} he have just \"snapped\"?"
    carlos "I don't know! I'm not {i}that{/i} kind of doctor!"
    warren "Then don't pipe up like that!"
    bottomi "Anyway, that's all I remember about the day."
    jump SH_Testimony1A

label SH_Advice1:
    hide screen testi
    ash "I hate to admit it, but I'm kind of lost."
    ash "Where is this {color=red}contradiction{/color} you keep talking about?"
    warren "Well, Mr Bottomi keeps talking about how he {color=red}stabbed{/color} the victim himself."
    warren "But don't we have a piece of evidence which suggests otherwise?"
    warren "If you're still confused, look through the evidence one more time."
    ash "...Oh! I think I know what you're talking about!"
    ash "All right. Let's do this."
    jump CurrentTestimony

label SH_Objection1:
    hide screen testi
    if testipart == "SH_Testimony1E" and present_response == "Knife":
        jump SH_Success1
    else:
        jump SH_Failure1

label SH_Failure1:
    warren "That's a pretty interesting story, Mr Bottomi."
    warren "Unfortunately, it's completely false."
    warren "As demonstrated... by THIS EVIDENCE!"
    bottomi "It is? How so?"
    warren "Isn't it obvious?"
    bottomi "N-no."
    warren "Oh. It's not? Oops."
    drang "Come now, assistant. You've got to try a little harder than that."
    $ mc_health -= 1
    #Health Loss Anim
    drang "Here's a little motivation to step up your game."
    warren thought "Couldn't you try the carrot before you reach for the stick?"

    if mc_health == 0:
        jump SH_GameOver1
    else:
        jump SH_Testimony1A

label SH_GameOver1:
    drang "All right, all right. I've had enough of this."
    drang "You've wasted my time long enough."
    drang "I want you and all of your weird friends out of here."
    warren "Wait! Please! Just give me one more{nw}"
    drang "Get out of my crime scene!"
    drang "Go on, before I arrest you all for obstruction of justice!"
    show black with fade
    warren thought "And so, the truth disappeared into darkness."
    warren thought "Drang failed to bring the real culprit to justice."
    warren thought "And I never unravelled the enigma of Base 24."
    jump endgame

label SH_Success1:
    warren "Just to clarify, Mr Bottomi... were you wearing the same clothes as you are right now?"
    bottomi "I guess I must have been. I don't remember going anywhere to change."
    warren "And you're {i}absolutely certain{/i} you stabbed the knife into the victim?"
    bottomi "How many times are you gonna make me say it, lady? I stabbed him with my own two hands!"
    bottomi "I mean, it was only one hand, but you get the idea!"
    warren "How interesting that you should mention hands, Mr Bottomi..."
    warren "...because I don't think yours were ever on this blade!"
    bottomi "What are you talking about?"
    warren "Is this is the knife you remember plunging into the victim?"
    bottomi "Y-yes. That's right."
    warren "Before you arrived, we ran a few tests on it. One of these tests revealed..."
    warren "...THAT THERE WERE NO FINGERPRINTS ANYWHERE ON THE HANDLE!"
    bottomi "Gah!"
    ash "Great job, Randi! You punched a hole right through that testimony!"
    bottomi "No, that can't be right... I remember stabbing him! I swear I'm telling the truth!"
    bottomi "There has to be some sort of explaination..."
    bottomi "Gloves!"
    warren "I'm sorry?"
    bottomi "I must have been wearing gloves! That would explain the lack of fingerprints, wouldn't it?"
    bottomi "Yes, I'm starting to remember now! I took a pair of medical gloves after my tests were complete!"
    bottomi "I had them on while I was stabbing him, and I got rid of them while I was wandering around."
    warren "Wh-whaaaaaaat!?"
    warren "But earlier you said you were wearing the same clothes as you are right now!"
    bottomi "Sorry, I guess I just forgot about the gloves..."
    bottomi "Besides, those don't really count as clothing, do they?"
    warren thought "And just like that...my perfect rebuttal crumbles into dust!"
    warren thought "Well, there's only one thing to do in a situation like this."
    warren "Mr Bottomi, you've given us some new information regarding the crime."
    warren "Can you please make another statement including this new information?"
    bottomi "Come on lady, I already told you I did it. Why do you gotta keep grilling me?"
    bottomi "Every time you ask a question, it just makes my head hurt..."
    warren "I'm just trying to reach the truth, Mr Bottomi."
    warren "Everything you tell me is immensely helpful."
    bottomi "All right, all right. What do you want to know about?"
    warren "Tell me more about the exact moment of the crime, please."

    ### Eyewitness Statement Animation
    typing "-- The Exact Moment of the Crime --{fast}"
    bottomi "I was already wearing the gloves before I entered the kitchen."
    bottomi "I saw the man and knew I needed to stab him, so I grabbed a knife from the counter."
    bottomi "When I stabbed him, he slumped over onto the floor."
    bottomi "I thought I saw movement in the window, so I ran away."
    bottomi "While I was wandering around the base, I took off the gloves and threw them away."

label testimony2_intro:
    scene kitchen
    show mir
    show ash at flip
    #Fade to Black, Fade In
    ash "How did that sound to you?"
    warren "Hmm... I didn't see any glaring errors in his statements."
    warren "Still, I get the sense that he's not telling us everything he could."
    warren "I think the best course of action is to {color=red}press him{/color} for more information."

    #Interrogation Animation
    $ current_present = "SH_Objection2"
    $ knows2E = False
    $ back_action = "CurrentTestimony"

label SH_Testimony2A:
    $ settesti("SH_Testimony2A", None, "SH_Testimony2B", "SH_Press2A","SH_Advice2")
    show screen testi
    bottomi "I was already wearing the gloves before I entered the kitchen."
    jump SH_Testimony2B

label SH_Press2A:
    hide screen testi
    warren "Why did you put them on in the first place, then?"
    bottomi "I'm not quite sure... maybe I just liked wearing them?"
    warren "That's a pretty flimsy reason to do something like that..."
    #Objection!
    drang "Is that all you've got, Warren? A \"flimsy reason\"?"
    drang "I'm afraid that contrary to what whiny film critics on the internet believe..."
    drang "A PERSON MAKING A CHOICE YOU DON'T UNDERSTAND IS NOT A LOGICAL CONTRADICTION!"
    drang "You're going to have to do better if you want to discount this witness's statements!"
    warren "Gah!"
    warren thought "I didn't know that Drang was capable of such succinct rebuttals!"
    warren thought "(Or that he frequented internet movie forums...)"
    drang "Carry on, Mr Bottomi."
    bottomi "Oh, uh, all right. So I went into the kitchen and..."
    jump SH_Testimony2B

label SH_Testimony2B:
    $ settesti("SH_Testimony2B", "SH_Testimony2A", "SH_Testimony2D", "SH_Press2B","SH_Advice2")
    show screen testi
    bottomi "I saw the man and knew I needed to stab him, so I grabbed a knife from the counter."
    jump SH_Testimony2D

label SH_Press2B:
    hide screen testi
    warren "And you still don't know what compelled you to attack him?"
    bottomi "Not at all."
    bottomi "It might have been one of those \"intrustive thoughts\" people talk about. You know the ones?"
    bottomi "Like, you're driving home and you hear a little voice in your head that says,"
    bottomi "\"Drive your car off the freeway!\""
    bottomi "Apparently they're pretty normal things. Nobody actually listens to 'em."
    bottomi "Only this time I guess I did..."
    bottomi ". . . . ."
    warren "Please carry on with your testimony, Mr Bottomi."
    bottomi "Oh! Right! So anyways..."
    jump SH_Testimony2D

### Note for posterity: I decided to cut Testimony 2C but didn't bother to rename everything after it

#label SH_Testimony2C:
#    $ settesti("SH_Testimony2C", "SH_Testimony2B", "SH_Testimony2D", "SH_Press2C","SH_Advice2")
#    show screen testi
#    bottomi "He tried to scream when I plunged the knife into his back, but he couldn't make a sound."
#    jump SH_Testimony2D

#label SH_Press2C:
#    hide screen testi
#    jump SH_Testimony2D

label SH_Testimony2D:
    if knows2E:
        $ settesti("SH_Testimony2D", "SH_Testimony2B", "SH_Testimony2E", "SH_Press2D","SH_Advice2")
    else:
        $ settesti("SH_Testimony2D", "SH_Testimony2B", "SH_Testimony2F", "SH_Press2D","SH_Advice2")
    show screen testi
    bottomi "When I stabbed him, he slumped over onto the floor."
    if knows2E:
        jump SH_Testimony2E
    else:
        jump SH_Testimony2F

label SH_Press2D:
    hide screen testi
    warren "Did he try to fight back at all?"
    bottomi "No, he just went still when I plunged the kinfe in."
    bottomi "I think he tried to scream, but he couldn't make a sound."
    carlos "Hm... if Bottomi managed to stab him in a lung, it's possible he immediately went into shock."
    warren "So, he just fell peacefully to the ground? Did you do anything to him besides stabbing him?"
    bottomi "What, like beat him up? No way!"
    bottomi "I'm not some kind of butcher!"
    bottomi "Actually, I guess I am, huh?"
    bottomi "Well, I'm not the kind of butcher that kicks a guy while he's down, at least!"
    warren "I see."
    warren thought "Hey, wait a minute..."
    bottomi "What are you looking so funny for? Did I say something important there?"
    menu:
        "Yes, very important.":
            warren "Yes, I think what you said was very important. Could you please add it to your statement?"
            bottomi "Oh, uh, sure. If you think it really matters that much..."
            $ knows2E = True
        "Nah, it's probably nothing.":
            warren "Hm..."
            warren "Nah, it's probably nothing."
            warren "Carry on with your testimony, Mr Bottomi."
            bottomi "Okay. So, after I stabbed him..."
    if knows2E:
        jump SH_Testimony2E
    else:
        jump SH_Testimony2F

label SH_Testimony2E:
    $ settesti("SH_Testimony2E", "SH_Testimony2D", "SH_Testimony2F", "SH_Press2E","SH_Advice2")
    show screen testi
    bottomi "I only ever stabbed him. I didn't beat him up or anything."
    jump SH_Testimony2F

label SH_Press2E:
    hide screen testi
    warren "Why do you feel the need to make that distinction?"
    bottomi "Hey lady, you're the one who asked my to add it to my statement."
    warren thought "This is the only foothold I have."
    warren thought "If I'm going to find a flaw in the testimony, it's got to be here!"
    bottomi "He just fell down and I left him there. After that..."
    jump SH_Testimony2F

label SH_Testimony2F:
    if knows2E:
        $ settesti("SH_Testimony2F", "SH_Testimony2E", "SH_Testimony2G", "SH_Press2F","SH_Advice2")
    else:
        $ settesti("SH_Testimony2F", "SH_Testimony2D", "SH_Testimony2G", "SH_Press2F","AdviceLabel")
    show screen testi
    bottomi "I thought I saw movement in the window, so I ran away."
    jump SH_Testimony2G

label SH_Press2F:
    hide screen testi
    warren "Presumably that was Mr Chritude taking pictures outside the house."
    bottomi "See, I didn't know that at the time."
    bottomi "I thought it might have been one of the security guards, come to arrest me."
    bottomi "I didn't want to be caught, so I ran away."
    warren "And yet you came right back here just an hour later?"
    bottomi "I was... I was feeling guilty about what I'd done. So I came back to turn myself in."
    bottomi "At least, I think so. Everything after I stabbed this man is still a blur..."
    bottomi "Oh, I do remember one thing about that time!"
    jump SH_Testimony2G

label SH_Testimony2G:
    $ settesti("SH_Testimony2G", "SH_Testimony2F", "SH_Testimony2A", "SH_Press2G","SH_Advice2")
    show screen testi
    bottomi "While I was wandering around the base, I took off the gloves and threw them away."
    jump SH_Testimony2A

label SH_Press2G:
    hide screen testi
    warren "Do you remember where exactly you left those gloves? They could be vital evidence."
    bottomi "Nnnnno, I don't. That's one of the things I'm still hazy on."
    warren "Even a general idea? Something we could use to start a search?"
    bottomi "I think they were... somewhere inside the base?"
    warren "Well, great. That sure narrows it down."
    bottomi "I-I'm sorry. If you want, I can repeat my testimony for you."
    warren "Sure, thanks."
    jump SH_Testimony2A

label SH_Advice2:
    hide screen testi
    ash "Well, great. What are we supposed to do now?"
    warren "The same as always. We need to find the inconsistency in his statements."
    if knows2E:
        warren "But there's only one statement which seems likely to bear fruit."
        warren "We've gotten a little more out of him by pressing."
        warren "Now we need to take a look at what he's said and see if it matches up with the evidence."
        warren "If we find an inconsistency then we can present evidence as usual."
        ash "And if we can't find an inconsistency?"
        warren "Then we look harder."
        ash "Jeez, Randi. You get serious when you're on the job."
    else:
        warren "Mr bottomi's story is suspicious in six differet ways."
        warren "Unfortunately, none of them are conclusive contradictions with the facts."
        warren "Right now we need more information from him."
        warren "And the best way to get that is to press his statements."
        warren "Hopefully something he says will have enough of a crack in it that we can tear it wide open."
        ash "I've noticed a theme of destructive metaphors whenever you talk about testimonies."
        warren "Save the psych analysis for the witness, please."
    jump CurrentTestimony

label SH_Objection2:
    hide screen testi
    if testipart == "SH_Testimony2E" and present_response == "MedicalReport":
        jump SH_Success2
    else:
        jump SH_Failure2

label SH_Failure2:
    warren "This one singular piece of evidence will tear your statement to shreds, Botomi!"
    bottomi "Oh my gosh, it will? ...How so?"
    warren "Well, you see... uh...."
    warren "When you look at the angle of the... um..."
    warren "Webster's Dictionary defines \"evidence\" as{nw}"
    # Drang Objects
    drang "I've heard enough."
    $ mc_health -= 1
    drang "Stop wasting our time with needless objections, assistant."
    if mc_health == 0:
        jump SH_GameOver2
    else:
        jump CurrentTestimony

label SH_GameOver2:
    drang "All right, all right. I've had enough of this."
    drang "You've wasted my time long enough."
    drang "I want you and all of your weird friends out of here."
    warren "Wait! Please! Just give me one more{nw}"
    drang "Get out of my crime scene!"
    drang "Go on, before I arrest you all for obstruction of justice!"
    show black with fade
    warren thought "And so, the truth disappeared into darkness."
    warren thought "Drang failed to bring the real culprit to justice."
    warren thought "And I never unravelled the enigma of Base 24."
    jump endgame

label SH_Success2:
    warren "I thought it was interesting that you were so insistent you only stabbed the victim."
    warren "But it's a good thing you were, because it exposes another key flaw in your story!"
    bottomi "W-what are you talking about?"
    warren "This is a preliminary medical report written by my forensics expert, Carlos Tsukada."
    warren "I could read out what's written there, but let's get it straight from the horse's mouth, shall we?"
    carlos "Hi, I'm the horse."
    carlos "Or am I the mouth?"
    warren "Carlos, could you please tell Mr Bottomi about the state we found the victim's body in?"
    carlos "Sure. He was dead on the floor with a knife in his back..."
    bottomi "Of course he was. That's how I lef{nw}"
    carlos "...and with severe bruises covering his entire body."
    bottomi "Ah!"
    carlos "At this point, it's unknown whether the cause of death was stabbing... or blunt force trauma!"
    bottomi "AAAAAAHHHHH!"
    bottomi "I forgot about the bruises!"
    warren "So you remember them now?"
    bottomi "Yes! They were all over his body! Even before I stabbed him!"
    bottomi "What's going on heeeeeeereeee?"
    bottomi "Wait! I'm... remembering... something... else... now..."
    bottomi "Before... I stabbed him... I beat him up!"
    bottomi "I threw him to the floor and I kicked him until he passed out!"
    bottomi "That's where the bruises came from."
    warren "You've gotta be kiddiiiiing meeeeeeeeeeeeee!"
    bottomi "And there's something else..."
    warren "Oh, great. What now?"
    bottomi "I remember my motive for killing him now."
    bottomi "You probably want another statement about that, don't you?"
    warren "Yes, please."

    # Eyewitness Statement Animation
    typing "-- That's How I Beat Darsha --{fast}"
    bottomi "I remember that man now. He was the one in charge of the trial I'm participating in."
    bottomi "Today he asked me to meet him here in the Smart House."
    bottomi "We walked into the kitchen together, and that's when he broke the news to me."
    bottomi "They were kicking me off the trial because they thought I had leaked information."
    bottomi "I was so mad that I started beating him up. And then... I grabbed the knife and..."

label testimony3_intro:
    scene kitchen
    show mir
    show drang
    #Fade to Black, Fade In
    drang "I'll admit I doubted you, assistant, but you really did pull it off."
    drang "You managed to drag the motive out of him! This is really going to cut down on the paperwork I need to file!"
    drang "I'll put in a good word for you at the Bureau once we book this fool."
    warren "Hold your horses, Agent. I'm still not done interrogating him yet."
    drang "Ugh, can you hicks talk about {i}anything{/i} without needing some kind of farm metaphor?"
    ash "What are we going to do, Randi? This guy keeps changing his story!"
    warren "That might be a good thing..."
    ash "Huh?"
    warren "Assuming he's lying, every time he makes something up he increases the chances of contradicting a piece of evidence we already have."
    warren "We just need to wait for a slip-up he can't possibly cover up."

#Interrogation Animation
$ current_present = "SH_Objection3"
$ back_action = "CurrentTestimony"
$ knows3Secret = False

label SH_Testimony3A:
    $ settesti("SH_Testimony3A", None, "SH_Testimony3B", "SH_Press3A","SH_Advice3")
    show screen testi
    bottomi "I remember that man now. He was the one in charge of the trial I'm participating in."
    jump SH_Testimony3B

label SH_Press3A:
    hide screen testi
    warren "How could you possibly forget someone that important?"
    bottomi "Well, he wasn't the one in charge of the trial exactly."
    bottomi "He was more like the one in charge of the one in charge of the trial."
    bottomi "He was the boss of the guy I reported to."
    bottomi "I only saw him occasionally in passing."
    bottomi "Up until today, that is..."
    jump SH_Testimony3B

label SH_Testimony3B:
    $ settesti("SH_Testimony3B", "SH_Testimony3A", "SH_Testimony3C", "SH_Press3B","SH_Advice3")
    show screen testi
    bottomi "Today he asked me to meet him here in the Smart House."
    jump SH_Testimony3C

label SH_Press3B:
    hide screen testi
    warren "Around what time did you meet up with the victim?"
    bottomi "He told me to meet him at 5:30."
    bottomi "He was busy with a tour of the house until then."
    warren thought "That lines up with the estimated time of death..."
    warren "Were you at all suspicious of his request?"
    bottomi "Not really. I just figured he wanted the show me the house."
    jump SH_Testimony3C

label SH_Testimony3C:
    if knows3Secret:
        $ settesti("SH_Testimony3C", "SH_Testimony3B", "SH_Testimony3Secret", "SH_Press3C","SH_Advice3")
    else:
        $ settesti("SH_Testimony3C", "SH_Testimony3B", "SH_Testimony3D", "SH_Press3C","SH_Advice3")
    show screen testi
    bottomi "We walked into the kitchen together, and that's when he broke the news to me."
    if knows3Secret:
        jump SH_Testimony3Secret
    else:
        jump SH_Testimony3D

label SH_Press3C:
    hide screen testi
    warren "Is that when you tracked those muddy footprints in?"
    bottomi "Sure is."
    warren "Where did you even find mud to step in around here?"
    bottomi "I...uh... oh yeah!"
    bottomi "It's cleaned up now, but earlier there was this big mud puddle outside the front door."
    bottomi "I think a sprinkler in the garden malfunctioned and sprayed it everywhere."
    bottomi "You couldn't avoid stepping in it if you wanted to get in the door."
    warren "I see."
    warren thought "But wait a minute... if that's the case, then isn't there something missing here?"
    warren "Please add this information to your statement, Mr Bottomi."
    bottomi "Uh, all right... sure."
    $ knows3Secret = True
    jump SH_Testimony3Secret

label SH_Testimony3Secret:
    $ settesti("SH_Testimony3Secret", "SH_Testimony3C", "SH_Testimony3D", "SH_Press3Secret","SH_Advice3")
    bottomi "There was this big mud puddle outside. You couldn't avoid stepping in it."
    jump SH_Testimony3D

label SH_Press3Secret:
    warren ""
    jump SH_Testimony3D

label SH_Testimony3D:
    if knows3Secret:
        $ settesti("SH_Testimony3D", "SH_Testimony3Secret", "SH_Testimony3E", "SH_Press3D","SH_Advice3")
    else:
        $ settesti("SH_Testimony3D", "SH_Testimony3C", "SH_Testimony3E", "SH_Press3D","SH_Advice3")
    show screen testi
    bottomi "They were kicking me off the trial because they thought I had leaked information."
    jump SH_Testimony3E

label SH_Press3D:
    hide screen testi
    warren "Why were you so upset about this?"
    bottomi "I was being paid to participate in the trial. It was a pretty sweet deal."
    bottomi "I'm in kind of a bad spot right now, and I was really counting on that money."
    warren "I guess I'll ask the obvious question next..."
    warren "{i}Did{/i} you leak information about the trial?"
    bottomi "No! I would never risk losing my stipend!"
    warren "Not even for a greater sum of money than you were receiving?"
    bottomi "No, I promise?"
    drang "Is this line of questioning relevant, assistant?"
    drang "Mr Bottomi is under suspicion of murder, not espionage."
    warren "Okay, okay."
    warren "So how did you react to this information, Mr Bottomi?"
    jump SH_Testimony3E

label SH_Testimony3E:
    $ settesti("SH_Testimony3E", "SH_Testimony3D", "SH_Testimony3A", "SH_Press3E","SH_Advice3")
    show screen testi
    bottomi "I was so mad that I started beating him up. And then... I grabbed the knife and..."
    jump SH_Testimony3A

label SH_Press3E:
    hide screen testi
    warren "So, it was a crime of passion. Not premeditated."
    bottomi "Yeah, I guess so."
    bottomi "It was the heat of the moment."
    warren thoughts "Isn't that a song?"
    bottomi "One thing led to another. Incidents rose from circumstance."
    warren thoughts "All right, he's definitely just saying song lyrics at this point."
    carlos "Some people claim that there's a woman to blame... but I know it's nobody's fault."
    warren thoughts "Et tu, Carlos?"
    jump SH_Testimony3A

label SH_Advice3:
    hide screen testi
    ash "Do you see any problems with his testimony, Randi?"
    warren "Yes I do. I may need to press him a bit first, but..."
    warren "There's a notable piece of evidence left here at the crime scene."
    warren "Only, according to this testimony there ought to be {color=red}two of them.{/color}"
    ash "Huh. Really? I'll have to take another look at the case files."
    jump CurrentTestimony

label SH_Objection3:
    hide screen testi
    if testipart == "SH_Testimony3Secret" and present_response == "Muddy Footprints":
        jump SH_Success3
    else:
        jump SH_Failure3

label SH_Failure3:
    $ mc_health -= 1
    ### DIALOGUE FOR MAKING WRONG CHOICE, HEALTH LOSS INCLUDED
    if mc_health == 0:
        jump SH_GameOver3
    else:
        jump CurrentTestimony

label SH_GameOver3:
    drang "All right, all right. I've had enough of this."
    drang "You've wasted my time long enough."
    drang "I want you and all of your weird friends out of here."
    warren "Wait! Please! Just give me one more{nw}"
    drang "Get out of my crime scene!"
    drang "Go on, before I arrest you all for obstruction of justice!"
    show black with fade
    warren thought "And so, the truth disappeared into darkness."
    warren thought "Drang failed to bring the real culprit to justice."
    warren thought "And I never unravelled the enigma of Base 24."
    jump endgame

label SH_Success3:
    warren "You've really stepped in it now, Mr Bottomi."
    warren "And by {i}it{/i}... I MEAN MUD!"
    bottomi "Excuse me?"
    warren "There's no doubt that you tracked in mud when you entered the smart house."
    warren "The muddy footprints and the silt on your shoes prove that pretty conclusively."
    warren "But if events had proceeded as you claim they did, then the victim would have stepped in mud as well..."
    warren "...AND THERE WOULD BE A SECOND PAIR OF FOOTPRINTS RIGHT NEXT TO YOURS!"
    bottomi "Gwah! You're absolutely right!"
    bottomi "What does this mean?"
    warren "It means you've been lying to us, Mr Bottomi."
    warren "You lied about the fingerprints, you lied about the bruises, and you're lying to us right now!"
    bottomi "N-no! I'm not lying! I remember walking in with him!"
    bottomi "But the footprints... why aren't there two pairs...?"
    bottomi "It doesn't make... there has to be... I know that I..."
    bottomi "STOP ASKING THESE QUESTIOOOOOOOOOOOOOOOOOOONNNNNNNSSSSSSSSS!"
    ## Bottomi Loses His Medical Cap, Passes Out
    carlos "He passed out!"
    warren "Looks like he lost his medical cap...wait. What on earth?"
    ash "His head!"
    carlos "What is that thing?"
    drang "I've never seen anything like that in my life!"
    drang "Which is unusual for me, because I am very well travelled!"
    show black with fade
    jump smart_house_act_3_intro
