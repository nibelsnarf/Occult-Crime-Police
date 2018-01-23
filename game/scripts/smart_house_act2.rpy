label smart_house_act_2:
    show act2 with fade
    pause 3.0
    $ save_name = "Act 2"
    scene black with dissolve
    typing "September 13th. 8:32 P.M.\nSmart House - Kitchen"
    scene kitchen
    show mir default
    show bottomi standard
    with fade
    show screen inventory_screen_button
    wbase "Sir...what did you just say?"
    bunk "I- I think I'm the one who killed that man on the ground."
    bunkfreak "No, I know it! I remember stabbing him with that knife!"
    wholdon "S-slow down, sir. What's your name?"
    bapology "My name is Louis Bottomi."
    bdespair "H-how could I have done something like this?"
    bdespair "You're a police officer, right? You've got to arrest me!"
    $profile.add(bottomi)
    hide mir
    show drang think gup at flip
    with dissolve
    dthink_gup "I reckon these are your footprints, then?"
    bremember "Y-yes, that's right! I tracked in some mud from the garden when I came in here!"
    hide drang
    show car gloves
    with dissolve
    cgloves "Let me see that shoe of yours..."
    cgloves "Yup, it's the same pattern."
    hide bottomi
    hide car
    show mir default
    show drang dril gdown
    with dissolve
    wthought "Well, that's {i}one{/i} mystery solved..."
    # Muddy Footprints Updates
    ddril_gdown "Wow... this is fantastic!"
    ddril_gup "Man, I knew I was good, but I didn't know I was good enough to make murderers confess on the spot!"
    djacket_pop "Looks like this one is wrapped up neatly."
    djacket_popped "Let's book this creep real quick, and then I can get out of here!"
    whattip "You really think he's our guy?"
    dangry_gdown "Of course he is! He just confessed, didn't he?"
    dthink_gdown "Take another look at the photograph that schmuck took."
    show chritudesPhoto with dissolve
    dos "See that second figure in the window? That's gotta be him!"
    wthought "Wow, I didn't think he would notice that detail."
    dos "You see? It ties up all the loose ends!"
    hide chritudesPhoto with dissolve
    wholdon "Hold on a minute, Agent Drang."
    wthink "Don't you think this is all a bit odd? Killers don't usually confess this easily."
    whattip "Even remorseful ones like him..."
    wbase "I think we need to {color=#FF9966}Interrogate{/color} him."
    dangry_gdown "Do you have to make this so difficult?"
    dthink_gdown "Fine. Go ahead."
    dthink_gdown "But as far as I'm concerned, this case is already closed."
    hide drang
    show bottomi standard
    wbase "Mr Bottomi, can you please tell me your story from the start?"
    bapology "Yeah, just give me a second."
    bfuzzy "My thoughts seem a little hazy right now..."
    bdef "Okay, I'm ready."
    hide mir with fade
    # Eyewitness Statement ANIMATION
    typing "-- Bottomi's Confession --{fast}"
    bapology "I'm a test subject in a clinical trial here at the base."
    bdef "Today I was here for another round in the trial."
    bnervous "I had some free time, so I came over here to take a look at the house."
    bmad "I saw that man in the kitchen and was suddenly filled with rage."
    bmad "So I grabbed a nearby knife and... I stabbed it into his back!"
    bapology "After I left the house, I just sort of wandered around for a while."
    bdespair "How could I have done something so awful... you've got to lock me up!"
    hide bottomi
    show car default at flip
    show mir default
    with fade
    clift "Seems pretty straightforward to me."
    chold "He doesn't have a clear motive, but he had the means and opportunity."
    wthink "I don't know... there's one thing here that doesn't sit right with me."
    chold "What's that?"
    wthink "If you're already confessing to a murder... what's the point in lying to a police officer?"
    cser "You mean you spotted a {color=#FF9966}contradiction{/color} in one of his statements?"
    whattip "Yes. A pretty big one, at that."
    hide car
    show ash standard at flip
    adef "So what happens now, Randi?"
    wbase "Now it's time to {color=#FF9966}interrogate{/color} the witness."
    athink "How does that work?"
    menu:
        "I'll explain it to you.":
            wbase "I'll explain it to you."
            wcasefile "Witness testimonies are often faulty in some way."
            whattip "Maybe the witness is lying, or maybe they're just mistaken."
            wcasefile "In either case, the only way to uncover the truth is to {color=#FF9966}present evidence{/color} which contradicts with their testimony."
            wcasefile "Every piece of evidence is a small part of the truth."
            athink "How do you present evidence?"
            wbase "First we go to the statement which contradicts the facts."
            wcasefile "Next, we pull up our evidence and select the one which proves the contradiction."
            wbase "Sometimes it may feel like the witness is holding something back."
            wbase "In these cases I can {color=#FF9966}press{/color} them for further information."
            athink "This is all a lot to keep track of."
            wbase "If you ever get too confused, we can {color=#FF9966}consult{/color} with each other on the best way to proceed."
        "You'll figure it out as we go.":
            wbase "You'll figure it out as we go."
            aflippant "No tutorial for me, huh?"
    apsyched "All right, let's take this guy's testimony down a peg!"

label testimony1_intro:
    # Interrogation Animation
    $ current_present = "SH_Objection1"
    $ CurrentTestimony = "SH_Testimony1A"
    $ back_action = CurrentTestimony
    $ mentionedhardware = False
    hide screen inventory_screen_button
    scene kitchen
    hide ash
    hide mir
    show bottomi apologetic
    with fade

label SH_Testimony1A:
    $ settesti("SH_Testimony1A", None, "SH_Testimony1B", "SH_Press1A","SH_Advice1")
    show screen testi
    bapology "I'm a test subject in a clinical trial here at the base."
    jump SH_Testimony1B

label SH_Press1A:
    hide screen testi
    show mir default
    whattip "What is this clinical trial studying?"
    bnervous "I'm not sure I'm allowed to tell you."
    bnervous "They make you sign a lot of contracts before the testing starts."
    bapology "I think one of them says that I'm not allowed to tell you."
    wbase "You're already a murder suspect. Are you really that concerned about breaking an NDA?"
    hide bottomi
    show ash surprised at flip
    asurprise "Haven't you heard the stories about this place, Randi?"
    aconfident "You let one little thing leak, and they make you disappear!"
    hide ash
    show bottomi apologetic
    bapology "Anyways, I'm just a guinea pig. They don't really tell me how any of it works."
    bapology "I just show up every so often and they do some different tests."
    bdef "That's why I'm here right now..."
    hide mir
    jump SH_Testimony1B

label SH_Testimony1B:
    $ settesti("SH_Testimony1B", "SH_Testimony1A", "SH_Testimony1C", "SH_Press1B","SH_Advice1")
    show screen testi
    bdef "Today I was here for another round in the trial."
    jump SH_Testimony1C

label SH_Press1B:
    hide screen testi
    show mir default
    whattip "Is that why you've got that hospital gown on?"
    bapology "Yeah. It's standard procedure while they do the tests."
    bapology "Between you and me, they're a little itchy."
    wthink "Was there anything different about this round of the trial?"
    wthink "Anything that might account for your sudden outburt?"
    bfuzzy "I... don't think so."
    bapology "They were just doing a check-up on the hardware."
    wbase "Hardware?"
    bnervous "Oh! Uh... I don't think I'm allowed to tell you about that."
    wthought "I'll have to figure out what he's referring to here."
    $ mentionedhardware = True
    wthought "But first things first: I should point out that blatant contradiction in his testimony."
    bdef "Anyway, that's why I was here at the base today."
    hide mir
    jump SH_Testimony1C

label SH_Testimony1C:
    $ settesti("SH_Testimony1C", "SH_Testimony1B", "SH_Testimony1D", "SH_Press1C","SH_Advice1")
    show screen testi
    bnervous "I had some free time, so I came over here to take a look at the house."
    jump SH_Testimony1D

label SH_Press1C:
    hide screen testi
    show mir default
    whattip "Was this the first time you had been to the smart house?"
    bapology "Yeah. Today was the grand unveiling."
    bdef "Up until then, the house had always been hidden behind these big walls."
    bdef "I didn't even know it was a house until today."
    bdef "Of course, I wanted to know what was so darn special about it."
    bapology "I'm still not really sure what it is."
    wbase "It's a Smart House."
    bdef "Oh, uh, okay."
    bapology "So there's, what, a bunch of dictionaries in here?"
    wannoy "I'll explain it to you later. What happened next?"
    hide mir
    jump SH_Testimony1D

label SH_Testimony1D:
    $ settesti("SH_Testimony1D", "SH_Testimony1C", "SH_Testimony1E", "SH_Press1D","SH_Advice1")
    show screen testi
    bmad "I saw that man in the kitchen and was suddenly filled with rage."
    jump SH_Testimony1E

label SH_Press1D:
    hide screen testi
    show mir default
    whattip "What do you mean? Was there something specific that made you feel that way?"
    bfuzzy "I- I couldn't say."
    bapology "Honestly, I'd never even met the guy before."
    bmad "Something in my head just told me that I needed to attack him. I needed to hurt him."
    bfreak "I needed to make sure he never got up again, he never..."
    bdef ". . ."
    bdespair "...I'm sorry..."
    wholdon "It's okay, Mr Bottomi. Just tell me what happened."
    hide mir
    jump SH_Testimony1E

label SH_Testimony1E:
    $ settesti("SH_Testimony1E", "SH_Testimony1D", "SH_Testimony1F", "SH_Press1E","SH_Advice1")
    show screen testi
    bmad "So I grabbed a nearby knife and... I stabbed it into his back!"
    jump SH_Testimony1F

label SH_Press1E:
    hide screen testi
    show mir default
    wcasefile "You're certain you stabbed him with a knife?"
    bapology "It's one of the few things I am certain of."
    bfuzzy "A lot of the day is sort of fuzzy... but I remember stabbing him crystal clear."
    bmad "I still remember what it felt like when the knife went into his back."
    wthought "This is the most suspicious part of his testimony."
    wthought "He's so confident in this one fact, even though there's such an obvious {color=#FF9966}contradiction{/color} in his claim!"
    wthought "This is the place to start chipping away at his testimony!"
    bdef "There's no doubt in my mind that I'm the one who killed him."
    hide mir
    jump SH_Testimony1F

label SH_Testimony1F:
    $ settesti("SH_Testimony1F","SH_Testimony1E", "SH_Testimony1G", "SH_Press1F", "SH_Advice1")
    show screen testi
    bapology "After I left the house, I just sort of wandered around for a while."
    jump SH_Testimony1G

label SH_Press1F:
    hide screen testi
    show mir default
    whattip "That's right, we ran into you earlier. You seemed like you were in a hurry."
    bapology "Did I? I honestly don't remember."
    bfuzzy "I think I must have been in shock."
    bdespair "Maybe it's good I didn't see you... I might have tried to hurt you too!"
    wbase "Don't worry... you wouldn't have succeeded."
    wbase "So that's all you've been doing for the past hour?"
    bapology "Yup. Just wandering around this base."
    bnervous "I'm kind of surprised nobody stopped me."
    bdef "Eventually, I ended up back here."
    bfuzzy "The sight of that man must have snapped me out of my daze."
    hide mir
    jump SH_Testimony1G

label SH_Testimony1G:
    $ settesti("SH_Testimony1G", "SH_Testimony1F", "SH_Testimony1A", "SH_Press1G","SH_Advice1")
    show screen testi
    bdespair "How could I have done something so awful... you've got to lock me up!"
    show bottomi apologetic
    with fade
    jump SH_Testimony1A

label SH_Press1G:
    hide screen testi
    show mir default
    wcasefile "How indeed? You claim not to have a motive for the crime."
    wcasefile "And most people don't go around stabbing random individuals for no reason."
    wbase "Do you have a history of mental illness, Mr Bottomi?"
    bapology "You think I'm some kind of psycho?"
    bdef "Well, sorry, but I'm not. I had to pass a medical examination to qualify for the clinical trial here."
    bfuzzy "They wouldn't have let me participate if I had something wrong with my head."
    bnervous "It would have interfered with the hardw- with the tests, I mean."
    if mentionedhardware == True:
        wthought "There he goes, talking about \"hardware\" again."
    else:
        wthought "Huh? What was he about to say there?"
    bapology "So, no, I don't have any brain problems that I know about."
    bnervous "You think I coulda just, I dunno... snapped?"
    wbase "I don't know. I'm not a doctor or anything."
    hide bottomi
    show car default at flip
    cdef "I am!"
    wos "..."
    whattip "...So? {i}Could{/i} he have just \"snapped\"?"
    cagit "I don't know! I'm not {i}that{/i} kind of doctor!"
    wangry "Then don't pipe up like that!"
    hide car
    show bottomi standard
    bapology "Anyway, that's all I remember about the day."
    hide mir
    show bottomi apologetic
    with fade
    jump SH_Testimony1A

label SH_Advice1:
    hide screen testi
    hide bottomi
    show mir default
    show ash unsure at flip
    with fade
    aunsure "I hate to admit it, but I'm kind of lost."
    athink "Where is this {color=#FF9966}contradiction{/color} you keep talking about?"
    whattip "Well, Mr Bottomi keeps talking about how he {color=#FF9966}stabbed{/color} the victim himself."
    wcasefile "But don't we have a piece of evidence which suggests otherwise?"
    wcasefile "If you're still confused, look through the evidence one more time."
    asurprise "...Oh! I think I know what you're talking about!"
    apsyched "All right. Let's do this."
    hide mir
    hide ash
    show bottomi standard
    with fade
    if CurrentTestimony == "SH_Testimony1A":
        jump SH_Testimony1A
    if CurrentTestimony == "SH_Testimony1B":
        jump SH_Testimony1B
    if CurrentTestimony == "SH_Testimony1C":
        jump SH_Testimony1C
    if CurrentTestimony == "SH_Testimony1D":
        jump SH_Testimony1D
    if CurrentTestimony == "SH_Testimony1E":
        jump SH_Testimony1E
    if CurrentTestimony == "SH_Testimony1F":
        jump SH_Testimony1F
    if CurrentTestimony == "SH_Testimony1G":
        jump SH_Testimony1G

label SH_Objection1:
    hide screen testi
    if present_response == "Back":
        if CurrentTestimony == "SH_Testimony1A":
            jump SH_Testimony1A
        if CurrentTestimony == "SH_Testimony1B":
            jump SH_Testimony1B
        if CurrentTestimony == "SH_Testimony1C":
            jump SH_Testimony1C
        if CurrentTestimony == "SH_Testimony1D":
            jump SH_Testimony1D
        if CurrentTestimony == "SH_Testimony1E":
            jump SH_Testimony1E
        if CurrentTestimony == "SH_Testimony1F":
            jump SH_Testimony1F
        if CurrentTestimony == "SH_Testimony1G":
            jump SH_Testimony1G
    if testipart == "SH_Testimony1E" and present_response == "knife":
        jump SH_Success1
    else:
        jump SH_Failure1

label SH_Failure1:
    show mir default
    wbase "That's a pretty interesting story, Mr Bottomi."
    wgotcha "Unfortunately, it's completely false."
    wgotcha "As demonstrated... by THIS EVIDENCE!"
    bapology "It is? How so?"
    wgotcha "Isn't it obvious?"
    bsad "N-no."
    wannoy "Oh. It's not? Oops."
    hide bottomi
    show drang dril gdown
    show screen healthBar
    ddril_gdown "Come now, assistant. You've got to try a little harder than that."
    $ mc_health -= 1
    while mc_health_display > mc_health:
        $mc_health_display -= 0.1
        pause 0.01
    ddril_gdown "Here's a little motivation to step up your game."
    wthought "Couldn't you try the carrot before you reach for the stick?"
    hide screen healthBar
    if mc_health == 0:
        jump SH_GameOver1
    else:
        hide drang
        hide mir
        show bottomi standard
        with fade
        jump SH_Testimony1A

label SH_GameOver1:
    djacket_pop "All right, all right. I've had enough of this."
    djacket_popped "You've wasted my time long enough."
    djacket_popped "I want you and all of your weird friends out of here."
    wholdon "Wait! Please! Just give me one more{nw}"
    dangry_gdown "Get out of my crime scene!"
    dangry_gdown "Go on, before I arrest you all for obstruction of justice!"
    show black with dissolve
    wthought "And so, the truth disappeared into darkness."
    wthought "Drang failed to bring the real culprit to justice."
    wthought "And I never unravelled the enigma of Base 24."
    jump endgame

label SH_Success1:
    show mir default
    wcasefile "Just to clarify, Mr Bottomi... were you wearing the same clothes as you are right now?"
    bapology "I guess I must have been. I don't remember going anywhere to change."
    wcasefile "And you're {i}absolutely certain{/i} you stabbed the knife into the victim?"
    bmad "How many times are you gonna make me say it, lady? I stabbed him with my own two hands!"
    bapology "I mean, it was only one hand, but you get the idea!"
    wbase "How interesting that you should mention hands, Mr Bottomi..."
    wgotcha "...because I don't think yours were ever on this blade!"
    bnervous "What are you talking about?"
    wcasefile "Is this is the knife you remember plunging into the victim?"
    bnervous "Y-yes. That's right."
    wbase "Before you arrived, we ran a few tests on it. One of these tests revealed..."
    wgotcha "...THAT THERE WERE NO FINGERPRINTS ANYWHERE ON THE HANDLE!"
    bfreak "Gah!"
    hide bottomi
    show ash at flip
    apsyched "Great job, Randi! You punched a hole right through that testimony!"
    hide ash
    show bottomi standard
    bfreak "No, that can't be right... I remember stabbing him! I swear I'm telling the truth!"
    bfuzzy "There has to be some sort of explaination..."
    bremember "Gloves!"
    whattip "I'm sorry?"
    bremember "I must have been wearing gloves! That would explain the lack of fingerprints, wouldn't it?"
    bremember "Yes, I'm starting to remember now! I took a pair of medical gloves after my tests were complete!"
    bremember "I had them on while I was stabbing him, and I got rid of them while I was wandering around."
    show mir recoil anim
    wos "Wh-whaaaaaaat!? {w=4.0}"
    wangry "But earlier you said you were wearing the same clothes as you are right now!"
    bapology "Sorry, I guess I just forgot about the gloves..."
    bapology "Besides, those don't really count as clothing, do they?"
    wthought "And just like that...my perfect rebuttal crumbles into dust!"
    wthought "Well, there's only one thing to do in a situation like this."
    wbase "Mr Bottomi, you've given us some new information regarding the crime."
    wbase "Can you please make another statement including this new information?"
    bdespair "Come on lady, I already told you I did it. Why do you gotta keep grilling me?"
    bfuzzy "Every time you ask a question, it just makes my head hurt..."
    wbase "I'm just trying to reach the truth, Mr Bottomi."
    wbase "Everything you tell me is immensely helpful."
    bdef "All right, all right. What do you want to know about?"
    wbase "Tell me more about the exact moment of the crime, please."
    hide mir with fade
    ### Eyewitness Statement Animation
    typing "-- The Exact Moment of the Crime --{fast}"
    bremember "I was already wearing the gloves before I entered the kitchen."
    bmad "I saw the man and knew I needed to stab him, so I grabbed a knife from the counter."
    bmad "When I stabbed him, he slumped over onto the floor."
    bnervous "I thought I saw movement in the window, so I ran away."
    bdef "While I was wandering around the base, I took off the gloves and threw them away."

label testimony2_intro:
    scene kitchen
    show mir default
    show ash thinking at flip
    with fade
    #Fade to Black, Fade In
    athink "How did that sound to you?"
    wthink "Hmm... I didn't see any glaring errors in his statements."
    whattip "Still, I get the sense that he's not telling us everything he could."
    whattip "I think the best course of action is to {color=#FF9966}press him{/color} for more information."
    hide ash
    hide mir
    show bottomi remembering
    with fade
    #Interrogation Animation
    $ CurrentTestimony = "SH_Testimony2A"
    $ current_present = "SH_Objection2"
    $ knows2E = False
    $ back_action = "CurrentTestimony"

label SH_Testimony2A:
    $ settesti("SH_Testimony2A", None, "SH_Testimony2B", "SH_Press2A","SH_Advice2")
    show screen testi
    bremember "I was already wearing the gloves before I entered the kitchen."
    jump SH_Testimony2B

label SH_Press2A:
    hide screen testi
    show mir default
    wbase "Why did you put them on in the first place, then?"
    bapology "I'm not quite sure... maybe I just liked wearing them?"
    whattip "That's a pretty flimsy reason to do something like that..."
    #Objection!
    hide bottomi
    show drang dril gup
    ddril_gup "Is that all you've got, Warren? A \"flimsy reason\"?"
    ddril_gup "I'm afraid that contrary to what whiny film critics on the internet believe..."
    djacket_pop "A PERSON MAKING A CHOICE YOU DON'T UNDERSTAND IS NOT A LOGICAL CONTRADICTION!"
    ddril_gup "You're going to have to do better if you want to discount this witness's statements!"
    show mir recoil anim
    wos "Gah! {w=4.0}"
    wthought "I didn't know that Drang was capable of such succinct rebuttals!"
    wthought "(Or that he frequented internet movie forums...)"
    ddef_gdown "Carry on, Mr Bottomi."
    hide drang
    bdef "Oh, uh, all right. So I went into the kitchen and..."
    hide mir
    jump SH_Testimony2B

label SH_Testimony2B:
    $ settesti("SH_Testimony2B", "SH_Testimony2A", "SH_Testimony2D", "SH_Press2B","SH_Advice2")
    show screen testi
    bmad "I saw the man and knew I needed to stab him, so I grabbed a knife from the counter."
    jump SH_Testimony2D

label SH_Press2B:
    hide screen testi
    show mir default
    whattip "And you still don't know what compelled you to attack him?"
    bdef "Not at all."
    bremember "It might have been one of those \"intrustive thoughts\" people talk about. You know the ones?"
    bdef "Like, you're driving home and you hear a little voice in your head that says,"
    bdef "\"Drive your car off the freeway!\""
    bapology "Apparently they're pretty normal things.\nNobody actually listens to them."
    bsad "Only this time I guess I did..."
    bos ". . . . ."
    wbase "Please carry on with your testimony, Mr Bottomi."
    bremember "Oh! Right! So anyways..."
    hide mir
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
    bmad "When I stabbed him, he slumped over onto the floor."
    if knows2E:
        jump SH_Testimony2E
    else:
        jump SH_Testimony2F

label SH_Press2D:
    hide screen testi
    show mir default
    whattip "Did he try to fight back at all?"
    bremember "No, he just went still when I plunged the kinfe in."
    bremember "I think he tried to scream, but he couldn't make a sound."
    hide bottomi
    show car serious at flip
    cser "Hm... if Lou managed to stab him in a lung, it's possible he immediately went into shock."
    hide car
    show bottomi standard
    wbase "So, he just fell peacefully to the ground? Did you do anything to him besides stabbing him?"
    bdespair "What, like beat him up? No way!"
    bdespair "I'm not some kind of butcher!"
    bapology "Actually, I guess I am, huh?"
    bdespair "Well, I'm not the kind of butcher that kicks a guy while he's down, at least!"
    wbase "I see."
    wthought "Hey, wait a minute..."
    bnervous "What are you looking so funny for? Did I say something important there?"
    menu:
        "Yes, very important.":
            wcasefile "Yes, I think what you said was very important. Could you please add it to your statement?"
            bapology "Oh, uh, sure. If you think it really matters that much..."
            hide mir
            $ knows2E = True
        "Nah, it's probably nothing.":
            wthink "Hm..."
            wthink "Nah, it's probably nothing."
            wbase "Carry on with your testimony, Mr Bottomi."
            bapology "Okay. So, after I stabbed him..."
    hide mir
    if knows2E:
        jump SH_Testimony2E
    else:
        jump SH_Testimony2F

label SH_Testimony2E:
    $ settesti("SH_Testimony2E", "SH_Testimony2D", "SH_Testimony2F", "SH_Press2E","SH_Advice2")
    show screen testi
    bapology "I only ever stabbed him. I didn't beat him up or anything."
    jump SH_Testimony2F

label SH_Press2E:
    hide screen testi
    show mir default
    wbase "Why do you feel the need to make that distinction?"
    bsad "Hey lady, you're the one who asked my to add it to my statement."
    wthought "This is the only foothold I have."
    wthought "If I'm going to find a flaw in the testimony, it's got to be here!"
    bdef "He just fell down and I left him there. After that..."
    hide mir
    jump SH_Testimony2F

label SH_Testimony2F:
    if knows2E:
        $ settesti("SH_Testimony2F", "SH_Testimony2E", "SH_Testimony2G", "SH_Press2F","SH_Advice2")
    else:
        $ settesti("SH_Testimony2F", "SH_Testimony2D", "SH_Testimony2G", "SH_Press2F","AdviceLabel")
    show screen testi
    bnervous "I thought I saw movement in the window, so I ran away."
    jump SH_Testimony2G

label SH_Press2F:
    hide screen testi
    show mir default
    wcasefile "Presumably that was Mr Chritude taking pictures outside the house."
    bdef "See, I didn't know that at the time."
    bnervous "I thought it might have been one of the security guards, come to arrest me."
    bnervous "I didn't want to be caught, so I ran away."
    whattip "And yet you came right back here just an hour later?"
    bapology "I was... I was feeling guilty about what I'd done. So I came back to turn myself in."
    bfuzzy "At least, I think so. Everything after I stabbed the guy is still a blur..."
    bremember "Oh, I do remember one thing about that time!"
    hide mir
    jump SH_Testimony2G

label SH_Testimony2G:
    $ settesti("SH_Testimony2G", "SH_Testimony2F", "SH_Testimony2A", "SH_Press2G","SH_Advice2")
    show screen testi
    bdef "While I was wandering around the base, I took off the gloves and threw them away."
    show bottomi remembering with fade
    jump SH_Testimony2A

label SH_Press2G:
    hide screen testi
    show mir default
    whattip "Do you remember where exactly you left those gloves? They could be vital evidence."
    bfuzzy "Nnnnno, I don't. That's one of the things I'm still hazy on."
    whattip "Even a general idea? Something we could use to start a search?"
    bfuzzy "I think they were... somewhere inside the base?"
    wannoy "Well, great. That sure narrows it down."
    bsad "I-I'm sorry. If you want, I can repeat my testimony for you."
    wannoy "Sure, thanks."
    hide mir
    show bottomi remembering
    with fade
    jump SH_Testimony2A

label SH_Advice2:
    hide screen testi
    hide bottomi
    show mir default
    show ash standard at flip
    with fade
    aannoy "Well, great. What are we supposed to do now?"
    wbase "The same as always. We need to find the inconsistency in his statements."
    if knows2E:
        wcasefile "But there's only one statement which seems likely to bear fruit."
        wbase "We've gotten a little more out of him by pressing."
        wbase "Now we need to take a look at what he's said and see if it matches up with the evidence."
        wcasefile "If we find an inconsistency then we can present evidence as usual."
        athink "And if we can't find an inconsistency?"
        wangry "Then we look harder."
        aunsure "Jeez, Randi. You get serious when you're on the job."
    else:
        wthink "Mr bottomi's story is suspicious in six differet ways."
        wthink "Unfortunately, none of them are conclusive contradictions with the facts."
        wbase "Right now we need more information from him."
        wbase "And the best way to get that is to press his statements."
        wbase "Hopefully something he says will have enough of a crack in it that we can tear it wide open."
        aflippant "I've noticed a theme of destructive metaphors whenever you talk about testimonies."
        wannoy "Save the psych analysis for the witness, please."
    hide mir
    hide ash
    show bottomi standard
    with fade
    if CurrentTestimony == "SH_Testimony2A":
        jump SH_Testimony2A
    if CurrentTestimony == "SH_Testimony2B":
        jump SH_Testimony2B
    if CurrentTestimony == "SH_Testimony2C":
        jump SH_Testimony2C
    if CurrentTestimony == "SH_Testimony2D":
        jump SH_Testimony2D
    if CurrentTestimony == "SH_Testimony2E":
        jump SH_Testimony2E
    if CurrentTestimony == "SH_Testimony2F":
        jump SH_Testimony2F
    if CurrentTestimony == "SH_Testimony2G":
        jump SH_Testimony2G

label SH_Objection2:
    hide screen testi
    if present_response == "Back":
        if CurrentTestimony == "SH_Testimony2A":
            jump SH_Testimony2A
        if CurrentTestimony == "SH_Testimony2B":
            jump SH_Testimony2B
        if CurrentTestimony == "SH_Testimony2C":
            jump SH_Testimony2C
        if CurrentTestimony == "SH_Testimony2D":
            jump SH_Testimony2D
        if CurrentTestimony == "SH_Testimony2E":
            jump SH_Testimony2E
        if CurrentTestimony == "SH_Testimony2F":
            jump SH_Testimony2F
        if CurrentTestimony == "SH_Testimony2G":
            jump SH_Testimony2G
    if testipart == "SH_Testimony2E" and present_response == "prelim":
        jump SH_Success2
    else:
        jump SH_Failure2

label SH_Failure2:
    show mir default
    wgotcha "This one singular piece of evidence will tear your statement to shreds, Bottomi!"
    bnervous "Oh my gosh, it will?"
    bapology "...how so?"
    wbase "Well, you see... uh...."
    wbase "When you look at the angle of the... um..."
    wbase "Webster's Dictionary defines \"evidence\" as{nw}"
    hide bottomi
    show drang angry gdown
    # Drang Objects
    show screen healthBar
    dangry_gdown "I've heard enough."
    $ mc_health -= 1
    while mc_health_display > mc_health:
        $mc_health_display -= 0.1
        pause 0.01
    dangry_gdown "Stop wasting our time with needless objections, assistant."
    hide screen healthBar
    if mc_health == 0:
        jump SH_GameOver2
    else:
        hide drang
        hide mir
        show bottomi standard
        with fade
        jump SH_Testimony2A

label SH_GameOver2:
    dangry_gdown "All right, all right. I've had enough of this."
    dangry_gdown "You've wasted my time long enough."
    dangry_gup "I want you and all of your weird friends out of here."
    wholdon "Wait! Please! Just give me one more{nw}"
    dangry_gup "Get out of my crime scene!"
    dangry_gup "Go on, before I arrest you all for obstruction of justice!"
    show black with fade
    wthought "And so, the truth disappeared into darkness."
    wthought "Drang failed to bring the real culprit to justice."
    wthought "And I never unravelled the enigma of Base 24."
    jump endgame

label SH_Success2:
    show mir default
    wbase "I thought it was interesting that you were so insistent you only stabbed the victim."
    wgotcha "But it's a good thing you were, because it exposes another key flaw in your story!"
    bnervous "W-what are you talking about?"
    wcasefile "This is a preliminary medical report written by my forensics expert, Carlos Tsukada."
    wcasefile "I could read out what's written there, but let's get it straight from the horse's mouth, shall we?"
    hide mir
    show car default
    cdef "Hi, I'm the horse."
    cconfuse "Or am I the mouth?"
    hide car
    show mir default
    wbase "Carlos, could you please tell Mr Bottomi about the state we found the victim's body in?"
    hide mir
    show car serious
    cser "Sure. He was dead on the floor with a knife in his back..."
    bdef "Of course he was. That's how I lef{nw}"
    cser "...and with severe bruises covering his entire body."
    bnervous "Ah!"
    cser "At this point, it's unknown whether the cause of death was stabbing... or blunt force trauma!"
    bfreak "AAAAAAHHHHH!"
    bfreak "I forgot about the bruises!"
    hide car
    show mir thinking
    wthink "So you remember them now?"
    bremember "Yes! They were all over his body! Even before I stabbed him!"
    bfreak "What's going on heeeeeeereeee?"
    bremember "Wait! I'm... remembering... something... else... now..."
    bfuzzy "Before... I stabbed him... I beat him up!"
    bmad "I threw him to the floor and I kicked him until he passed out!"
    bmad "That's where the bruises came from."
    show mir recoil anim
    wos "You've gotta be kiddiiiiing meeeeeeeeeeeeee!"
    bapology "And there's something else..."
    wrecoil "Oh, great. What now?"
    bdef "I remember my motive for killing him now."
    bsad "You probably want another statement about that, don't you?"
    wrecoil "Yes, please."
    hide mir with fade
    # Eyewitness Statement Animation
    typing "-- That's How I Beat Darsha --{fast}"
    bremember "I remember that man now. He was the one in charge of the trial I'm participating in."
    bdef "Today he asked me to meet him here in the Smart House."
    bdef "We walked into the kitchen together, and that's when he broke the news to me."
    bmad "Darsha was kicking me off the trial because he thought I had leaked information."
    bmad "I was so mad that I just started wailing on him. And then... I grabbed the knife and..."

label testimony3_intro:
    scene kitchen
    show mir default
    show drang think gup
    with fade
    #Fade to Black, Fade In
    dthink_gup "I'll admit I doubted you, assistant, but you really did pull it off."
    ddril_gup "You managed to drag the motive out of him! This is really going to cut down on the paperwork I need to file!"
    ddef_gup "I'll put in a good word for you at the Bureau once we book this fool."
    wbase "Hold your horses, Agent. I'm still not done interrogating him yet."
    dangry_gdown "Ugh, can you hicks talk about {i}anything{/i} without needing some kind of farm metaphor?"
    hide drang
    show ash annoyed at flip
    aannoy "What are we going to do, Randi? This guy keeps changing his story!"
    wbase "That might be a good thing..."
    asurprise "Huh?"
    wcasefile "Assuming he's lying, every time he makes something up he increases the chances of contradicting a piece of evidence we already have."
    wbase "We just need to wait for a slip-up he can't possibly cover up."

    #Interrogation Animation
    $ CurrentTestimony = "SH_Testimony3A"
    $ current_present = "SH_Objection3"
    $ back_action = "CurrentTestimony"
    $ knows3Secret = False
    hide mir
    hide ash
    show bottomi remembering
    with fade

label SH_Testimony3A:
    $ settesti("SH_Testimony3A", None, "SH_Testimony3B", "SH_Press3A","SH_Advice3")
    show screen testi
    bremember "I remember that man now. He was the one in charge of the trial I'm participating in."
    jump SH_Testimony3B

label SH_Press3A:
    hide screen testi
    show mir angry
    wangry "How could you possibly forget someone that important?"
    bnervous "Well, he wasn't the one in charge of the trial exactly."
    bapology "He was more like the one in charge of the one in charge of the trial."
    bapology "He was the boss of the guy I reported to."
    bdef "I only saw him occasionally in passing."
    bsad "Up until today, that is..."
    hide mir
    jump SH_Testimony3B

label SH_Testimony3B:
    $ settesti("SH_Testimony3B", "SH_Testimony3A", "SH_Testimony3C", "SH_Press3B","SH_Advice3")
    show screen testi
    bdef "Today he asked me to meet him here in the Smart House."
    jump SH_Testimony3C

label SH_Press3B:
    hide screen testi
    show mir hattip
    whattip "Around what time did you meet up with the victim?"
    bdef "He told me to meet him at 5:30."
    bdef "He was busy with a tour of the house until then."
    wthought "That lines up with the estimated time of death..."
    wbase "Were you at all suspicious of his request?"
    bapology "Not really. I just figured he wanted the show me the house."
    hide mir
    jump SH_Testimony3C

label SH_Testimony3C:
    if knows3Secret:
        $ settesti("SH_Testimony3C", "SH_Testimony3B", "SH_Testimony3Secret", "SH_Press3C","SH_Advice3")
    else:
        $ settesti("SH_Testimony3C", "SH_Testimony3B", "SH_Testimony3D", "SH_Press3C","SH_Advice3")
    show screen testi
    bdef "We walked into the kitchen together, and that's when he broke the news to me."
    if knows3Secret:
        jump SH_Testimony3Secret
    else:
        jump SH_Testimony3D

label SH_Press3C:
    hide screen testi
    wbase "Is that when you tracked those muddy footprints in?"
    bdef "Sure is."
    whattip "Where did you even find mud to step in around here?"
    bapology "I...uh... {nw}"
    bremember "I...uh... {fast}oh yeah!"
    bapology "It's cleaned up now, but earlier there was this big mud puddle outside the front door."
    bapology "I think a sprinkler in the garden malfunctioned \nand sprayed it everywhere."
    bdef "You couldn't avoid stepping in it if you wanted to get in the door."
    wbase "I see."
    show mir thinking
    wthought "But wait a minute... if that's the case, then isn't there something missing here?"
    if knows3Secret == True:
        hide mir
        jump SH_Testimony3Secret
    wthought "Should I ask him to add that information to his statement?"
    menu:
        "Ask Him":
            wthought "Might as well... no harm in it."
            wbase "Mr Bottomi, can you please add that information to your testimony?"
            bdef "Uh, all right... sure."
            $ knows3Secret = True
            hide mir
            jump SH_Testimony3Secret
        "Don't Ask Him":
            wthought "Nah... it's probably not that important."
            wbase "Carry on with your testimony, Mr Bottomi."
            bdef "Oh, yeah, okay..."
            hide mir
            jump SH_Testimony3D

label SH_Testimony3Secret:
    $ settesti("SH_Testimony3Secret", "SH_Testimony3C", "SH_Testimony3D", "SH_Press3Secret","SH_Advice3")
    show screen testi
    bremember "There was this big mud puddle outside. You couldn't avoid stepping in it."
    jump SH_Testimony3D

label SH_Press3Secret:
    hide screen testi
    show mir default
    wbase "And this was where you met with the victim?"
    bdef "Yeah, he was waiting outside for me when I arrived."
    bapology "I showed up around 5:30 or so and he invited me inside."
    bsad "We walked from the front porch to the kitchen, and that's where he told me the bad news."
    whattip "Oh? And what was this bad news?"
    hide mir
    jump SH_Testimony3D

label SH_Testimony3D:
    if knows3Secret:
        $ settesti("SH_Testimony3D", "SH_Testimony3Secret", "SH_Testimony3E", "SH_Press3D","SH_Advice3")
    else:
        $ settesti("SH_Testimony3D", "SH_Testimony3C", "SH_Testimony3E", "SH_Press3D","SH_Advice3")
    show screen testi
    bmad "Darsha was kicking me off the trial because he thought I had leaked information."
    jump SH_Testimony3E

label SH_Press3D:
    hide screen testi
    whattip "Why were you so upset about this?"
    bdef "I was being paid to participate in the trial. It was a pretty sweet deal."
    bsad "I'm in kind of a bad spot right now, and I was really counting on that money."
    wbase "I guess I'll ask the obvious question next..."
    whattip "{i}Did{/i} you leak information about the trial?"
    bdespair "No! I would never risk losing my stipend!"
    wthink "Not even for a greater sum of money than you were receiving?"
    bdespair "No, I promise!"
    hide bottomi
    show drang think gdown
    dthink_gdown "Is this line of questioning relevant, assistant?"
    dthink_gdown "Mr Bottomi is under suspicion of murder, not espionage."
    wbase "Okay, okay."
    whattip "So how did you react to this information, Mr Bottomi?"
    hide mir
    hide drang
    show bottomi mad
    jump SH_Testimony3E

label SH_Testimony3E:
    $ settesti("SH_Testimony3E", "SH_Testimony3D", "SH_Testimony3A", "SH_Press3E","SH_Advice3")
    show screen testi
    bmad "I was so mad that I just started wailing on him. And then... I grabbed the knife and..."
    show bottomi remembering with fade
    jump SH_Testimony3A

label SH_Press3E:
    hide screen testi
    wbase "So, it was a crime of passion. Not premeditated."
    bremember "Yeah, I guess so."
    bsad "It was the heat of the moment."
    show mir thinking
    wthought "Isn't that a song?"
    bsad "One thing led to another. Incidents rose from circumstance."
    wthought "All right, he's definitely just saying song lyrics at this point."
    hide bottomi
    show car default at flip
    cdef "Some people claim that there's a woman to blame... \nbut I know it's nobody's fault."
    wthought "Et tu, Carlos?"
    hide mir
    hide car
    show bottomi remembering
    with fade
    jump SH_Testimony3A

label SH_Advice3:
    hide screen testi
    hide bottomi
    show ash thinking
    athink "Do you see any problems with his testimony, Randi?"
    wbase "Yes I do. I may need to press him a bit first, but..."
    wcasefile "There's a notable piece of evidence left here at the crime scene."
    wcasefile "Only, according to this testimony there ought to be {color=#FF9966}two of them.{/color}"
    athink "Huh. Really? I'll have to take another look at the case files."
    hide ash
    hide mir
    show bottomi remembering
    if CurrentTestimony == "SH_Testimony3A":
        jump SH_Testimony3A
    if CurrentTestimony == "SH_Testimony3B":
        jump SH_Testimony3B
    if CurrentTestimony == "SH_Testimony3C":
        jump SH_Testimony3C
    if CurrentTestimony == "SH_Testimony3D":
        jump SH_Testimony3D
    if CurrentTestimony == "SH_Testimony3E":
        jump SH_Testimony3E
    if CurrentTestimony == "SH_Testimony3Secret":
        jump SH_Testimony3Secret

label SH_Objection3:
    if present_response == "Back":
        if CurrentTestimony == "SH_Testimony3A":
            jump SH_Testimony3A
        if CurrentTestimony == "SH_Testimony3B":
            jump SH_Testimony3B
        if CurrentTestimony == "SH_Testimony3C":
            jump SH_Testimony3C
        if CurrentTestimony == "SH_Testimony3D":
            jump SH_Testimony3D
        if CurrentTestimony == "SH_Testimony3E":
            jump SH_Testimony3E
        if CurrentTestimony == "SH_Testimony3Secret":
            jump SH_Testimony3Secret
    hide screen testi
    if testipart == "SH_Testimony3Secret" and present_response == "footprints":
        jump SH_Success3
    else:
        jump SH_Failure3

label SH_Failure3:
    show mir default
    wbase "If that's the case..."
    wgotcha "...Then what about THIS?"
    wos ". . . . ."
    wcasefile "Wait hang on, I had the evidence upside down."
    wcasefile "Oh, yeah, okay. Never mind. Not contradictory."
    wcasefile "Sorry folks, that one's on me."
    hide bottomi
    show screen healthBar
    show drang jacket popped
    dos ". . . . ."
    $ mc_health -= 1
    while mc_health_display > mc_health:
        $mc_health_display -= 0.1
        pause 0.07
    djacket_popped "Next time think before you speak, huh?"
    hide screen healthBar
    if mc_health == 0:
        jump SH_GameOver3
    else:
        hide drang
        hide mir
        if CurrentTestimony == "SH_Testimony3A":
            jump SH_Testimony3A
        if CurrentTestimony == "SH_Testimony3B":
            jump SH_Testimony3B
        if CurrentTestimony == "SH_Testimony3C":
            jump SH_Testimony3C
        if CurrentTestimony == "SH_Testimony3D":
            jump SH_Testimony3D
        if CurrentTestimony == "SH_Testimony3E":
            jump SH_Testimony3E
        if CurrentTestimony == "SH_Testimony3Secret":
            jump SH_Testimony3Secret

label SH_GameOver3:
    djacket_pop "All right, all right. I've had enough of this."
    djacket_popped "You've wasted my time long enough."
    djacket_popped "I want you and all of your weird friends out of here."
    wholdon "Wait! Please! Just give me one more{nw}"
    dangry_gdown "Get out of my crime scene!"
    dangry_gdown "Go on, before I arrest you all for obstruction of justice!"
    show black with fade
    wthought "And so, the truth disappeared into darkness."
    wthought "Drang failed to bring the real culprit to justice."
    wthought "And I never unravelled the enigma of Base 24."
    jump endgame

label SH_Success3:
    wgotcha "You've really stepped in it now, Mr Bottomi."
    wgotcha "And by {i}it{/i}... I MEAN MUD!"
    bnervous "Excuse me?"
    wcasefile "There's no doubt that you tracked in mud when you entered the smart house."
    wcasefile "The muddy footprints and the silt on your shoes prove that pretty conclusively."
    wbase "But if events had proceeded as you claim they did, then the victim would have stepped in mud as well..."
    wgotcha "...AND THERE WOULD BE A SECOND PAIR OF FOOTPRINTS RIGHT NEXT TO YOURS!"
    bfreak "Gwah! You're absolutely right!"
    bfuzzy "What does this mean?"
    wbase "It means you've been lying to us, Mr Bottomi."
    wbase "You lied about the fingerprints, you lied about the bruises, and you're lying to us right now!"
    bmad "N-no! I'm not lying! I remember walking in with him!"
    bdespair "But the footprints... why aren't there two pairs...?"
    bfreak "It doesn't make... there has to be... I know that I..."
    bkaboom "STOP ASKING THESE QUESTIOOOOOOOOOOOOOOOOOOONNNNNNNSSSSSSSSS!"
    hide bottomi with dissolve
    pause 3.0
    show car agitated at flip
    ## Bottomi Loses His Medical Cap, Passes Out
    cagit "He passed out!"
    whattip "Looks like he lost his medical cap...wait. What on earth?"
    show bottomiKO with dissolve
    aos "His head!"
    cos "What is that thing?"
    dos "Well. That's a new one."
    show black with dissolve
    jump endgame
    jump smart_house_act_3_intro
