label smart_house_act_1:
    show screen jumpTo
    scene black
    pause 1.0
    typing "September 13th. 7:28 P.M.\nNear the outskirts of town."
    play music "sound/Car_Loop.ogg" fadein 1.0
    scene policecarbythesideoftheroad with fade
    pscanner "Sheriff? Sheriff Warren, are you there?"
    menu:
        "No, it's a completely different person emulating her voice perfectly.":
            wos "No, it's a completely different person emulating her voice perfectly."
            wos "Good job, you've cracked the case."

        "You better have a good reason for calling me up. I'm incredibly busy right now.":
            wos "You better have a good reason for calling me up. I'm incredibly busy right now."
            pscanner "You've been napping in the seat off your car, haven't you?"
            wos "..."
            wos "I inkove my right to plead the fifth."

    pscanner "See, this is why nobody in town respects you anymore."
    wos "I think we both know why nobody in town respects me anymore."
    wos "Now, what's so important you had to call up the sherrif?"
    wos "Another loiterer by the general store? Somebody's hedges leaking into their neighbor's yard?"
    pscanner "There's been a murder."
    menu:
        "What are you talking about?":
            wos "What are you talking about?"
            pscanner "Someone's dead."
            wos "Yes, that's generally how murders work."
        "Pull the other one.":
            wos "Pull the other one."
            pscanner "I'm not kidding."
            pscanner "You really think I'd bother jerking you around?"
        "...Oh man.":
            wos "...Oh man."
            pscanner "Yeah."

    wos "So what happened?"
    pscanner "We don't know yet. Somebody called in a dead body just a few minutes ago."
    pscanner "We've already sent Carlos over to have a look."

    menu:
        "Carlos the mortician slash forensics expert slash detective?":
            wos "Carlos the mortician slash forensics expert slash detective?"
            pscanner "That's the one."
            pscanner "We {i}really{/i} need to get more staff down at the station."
            wos "Sure. Their paycheck can come out of your salary."
        "Carlos with four names?":
            wos "Carlos with four names?"
            pscanner "That's the one."
        "Carlos the margarita nut?":
            wos "Carlos the margarita nut?"
            pscanner "That's an oversimplification."
            wos "You're right. He also likes hawaiian shirts."

    pscanner "Well, he'll be waiting for you over at the security checkpoint. {i}If{/i} you can be bothered to show up."
    wos "Security checkpoint?"
    pscanner "That's right. The murder took place over at {color=#FF9966}Base 24.{/color}"
    wos "Base....24...."
    wos "I'll be there."
    pscanner "You will? Wow....\nI mean, good."
    stop music
    play sound "sound/SirenPullAway.ogg"
    show black with fade
    pause 4.0

    wthought "My name is Miranda Warren."
    wthought "I've been the Sherriff of {color=#FF9966}Boomtown, USA{/color} for thirteen years now."
    wthought "Boomtown was built by a real estate tycoon, expecting a large influx of people once the freeways were finished."
    wthought "But barely anyone came, and the town has been sinking back into the desert ever since."
    wthought "The only reason to put it on a map anymore is {color=#FF9966}Base 24,{/color} a government facility on the outskirts of town."
    wthought "It's the only thing keeping this town afloat. Anyone who works at the base lives in Boomtown."
    wthought "A few years back, I failed in my duties as Sheriff."
    wthought "Small towns don't forget a thing like that."
    wthought "But if there's been another incident at the base, it's possible the two are connected."

    ## play act stinger
    scene act1 with dissolve
    $ save_name = "Act 1"
    pause 3.0

label outside_base_intro:

    $inventory.add(badge)
    $profile.add(warren)

    $ eyesight = 0
    $initialguardtalk = 0

    scene outsidebase with dissolve
    pause 1.0
    typing "September 13th\nBase 24 - Security Checkpoint"
    play music "music/Investigation_Loops.ogg" fadein 1.0
    show screen inventory_screen_button
    show guard glasses at flip
    show car agitated
    with dissolve
    gglasses "I'm sorry, sir. I can't let you past here. This is a restricted area."
    cagit "Hey buddy, I'm an american citizen! My taxes pay your salary!" with smallshake
    hide guard eyes
    show mir default at flip
    wbase "Carlos, you work for the Sherrif's Department. His taxes pay {i}your{/i} salary."
    $profile.add(carlos)
    cdef "Oh! Hey, Chief. About time you got here."
    cagit "This stick-in-the-mud won't let me in to investigate."
    hide mir
    show guard glasses at flip
    gglasses "I am merely following orders, citizen."
    gglasses "I have explicit instructions not to let anybody in."
    hide guard
    hide car
    scene outsidebaseboth
    with dissolve
    wthought "Looks like I'm going to have to sort this out before I can get in there."
    show screen outside_base_examine
    pause

screen outside_base_examine:
    modal True
    imagemap:
        ground "outsidebaseboth"
        hover "outsidebaseaaa"
        hotspot (700,495,220,570) action [Hide("outside_base_examine"), Jump("outside_base_carlos")]
        hotspot (970,470,200,590) action [Hide("outside_base_examine"), Jump("outside_base_guard")]
    use inventory_screen_button

label outside_base_carlos:
    scene outsidebaseguard with dissolve
    show mir default
    show car default at flip
    with dissolve
    $loop = 1
    while loop == 1:
        menu:
            "What's Going On":
                whattip "So what's the problem here?"
                cagit "Agent Smith over there doesn't believe I'm a real cop."
                wannoy "Here's a thought: maybe it's because you're wearing a hawaiian shirt instead of a police uniform."
                show mir default
                clift "Come on, Chief. You know you can't stop a man when he's on ISLAND TIME."
                chold "Who am I to resist the siren song of Beach Life?"
                chold "Besides, I don't even think he can see what I'm wearing."
                cwhis "Between you and me, it seems like his eyesight leaves something to be desired."
                $ eyesight = 1

            "The Guard's Eyesight" if eyesight == 1:
                whattip "What's wrong with the guard's eyesight?"
                cdef "Well, I'll put it like this..."
                cdef "When I approached him, he addressed me as \"Sir or Madame\"."
                cdef "When he reported me to his superiors, he described me as a \"suspicious-looking indistinct blur\"."
                cdef "And when I asked him how many fingers I was holding up, he began to weep bitterly."
                cdef "My diagnosis: Nearsightedness."
                wannoy "Great. They put a blind man in charge of guarding their entrance."
                wbase "Well, it explains why he hasn't noticed my uniform."

            "What To Do":
                whattip "How do you suggest I clear this up?"
                cdef "Well, he's looking for proof that we work for the Sheriff's Department."
                cdef "And I seem to have left my ID in my other lab coat..."
                cdef "Do you have anything you could show him to prove who you are?"
                whattip "Yeah, I've got something that should do the trick, all right."

            "Goodbye":
                wbase "Hold tight, I'll deal with this."
                chold "Take your time."
                $loop = 0
                hide mir
                hide car
                with dissolve
                scene outsidebaseboth with dissolve
                show screen outside_base_examine
                pause

label outside_base_guard:
    scene outsidebasecarlos with dissolve
    show mir default
    show guard glasses at flip
    with dissolve

    if initialguardtalk == 0:
        wbase "Hello, sir."
        gglasses "Are you friends with this man, citizen? Can you please ask him to vacate these premises?"
        $initialguardtalk = 1

    $loop = 1
    while loop == 1:
            menu:
                "The Sherrif":
                    wbase "Sir, I am the sherrif of this county."
                    wbase "I need you to let us in so we can investigate a crime."
                    gglasses "Hah! I get it."
                    gglasses "He's an officer, and now you're the sherrif."
                    gglasses "I guess the next guy who shows up will be the president?"
                    wangry "It's the truth!"
                    gglasses "I'm sure it is. Look, I can't just take your word for it."
                    gglasses "You're going to need to show me some {color=#FF9966}proof{/color} first."

                "The Murder":
                    wbase "Sir, are you aware there's been a murder?"
                    gglasses "Of course I am. Why do you think they've got everyone on such high alert?"
                    wbase "So, as an officer of the law, I need to get in there to investigate."
                    gglasses "Now hold on. I have no proof you are who you say you are."
                    gglasses "You might be one of those sneaky reporters trying to get a scoop."
                    wangry "I'm not a reporter!"
                    gglasses "\"I'm not a reporter.\" Hah! Oldest trick in the reporter book."

                "Your Eyesight" if eyesight == 1:
                    wcasefile "On the subject of your eyesight..."
                    show mir default
                    gremglasses "Ah, you've found out about that."
                    gholdglasses "It is true that I have quite attenuating nearsightedness."
                    gholdglasses "Everything further than six inches is a complete blur to me."
                    geyes "However! That shortcoming is offset by my heightened motion perception."
                    geyes "Even the slightest movement will catch my eye! That's why they put me on guard duty."
                    greturnglasses "Don't even try getting past these peepers!"
                    wannoy "Uh, good to know..."

                "Present Evidence":
                    wbase "Let me show you something."
                    gglasses "Go ahead. You're going to have to hold it {i}real{/i} close, though."
                    $ current_present = "outside_base_guard_present"
                    show screen present_evidence_screen
                    show screen back_button
                    pause

                "Goodbye":
                    wbase "I'll be back. Don't go anywhere."
                    gglasses "Hah, you'd {i}like{/i} that, wouldn't you?"
                    $loop = 0
                    hide mir
                    hide guard
                    with dissolve
                    scene outsidebaseboth with dissolve
                    show screen outside_base_examine
                    pause

label outside_base_guard_present:
    if present_response == "badge":
        jump outside_base_outro

    if present_response == "Back":
        wbase "Hm, never mind."
        $ present_response = "None"
        jump outside_base_guard

    else:
        jump Error_Message

label Error_Message:
    show black
    "You should not be seeing this."
    "If you are, it means that something has gone gravely wrong."
    "Please inform the creator of this game how you managed to arrive at this rotten place."
    "Good Bye."
    jump endgame

label outside_base_outro:
    wbase "This is a Sheriff's Badge."
    gremglasses "Well, so it is. Now where did you get a thing like that?"
    whattip "It's mine. My name is Miranda Warren and I'm the Sheriff of Boomtown, USA."
    stop music
    play sound "sound/Bwaaah.ogg"
    geyes "OH NO" with shake
    play sound "sound/Bwaaah.ogg"
    geyes "THE ONLY CHARACTERISTIC MORE DISTINGUISHING THAN MY NEARSIGHTEDNESS" with shake
    play sound "sound/Bwaaah.ogg"
    geyes "IS MY RESPECT FOR SYMBOLS OF AUTHORITY" with shake
    play sound "sound/Bwaaah.ogg"
    geyes "PLEASE GO RIGHT AHEAD OFFICER" with shake
    hide guard with dissolve
    wbase "Finally, he's gone."
    scene outsidebase with dissolve
    show mir default
    show car liftdrink at flip
    with dissolve
    clift "Way to go there, Chief."
    chold "You sure showed an object to that guy."
    wbase "In a world of lies, evidence is the only way to get to the truth. Remember that, Tsukada."
    cdef "That's great. I'll put it on a motivational poster."
    show black with fade

label meeting_ash_intro:

    scene black
    typing "September 13th\nBase 24 - Warehouse"
    show screen inventory_screen_button
    scene basewarehouse with fade
    show mir default
    show car default at flip
    with dissolve
    whattip "So where's this body?"
    cdef "I think it's supposed to be inside that house."
    wthink "Hmm... what's a house doing inside a building anyways?"
    show mir default
    clift "Well, this place is some sort of government research facility, right?"
    chold "Maybe it's an experiment."
    nameless "Randi?"
    hide car default
    show ash standard at flip
    aunk "I figured you would show up here sooner or later."
    aunk "What with the murder and all..."
    wbase "Ash? What are you doing here?"
    $profile.add(ash)
    aconfident "I'm here for the {color=#FF9966}tour!{/color} What else would I be doing?"
    play music "music/TheyWantToBelieve.ogg" fadein 1.0

label meeting_ash_conversation:
    $ meeting_ash_cleared_items = []
    $ meeting_ash_cleared = False

    while meeting_ash_cleared == False:
        menu:
            "Ash Jager":
                show mir default
                hide ash
                show car default at flip
                cdef "You two seem to know each other..."
                cdef "Care to introduce me, Warren?"
                wbase "Oh, yes."
                hide mir default
                show ash standard
                with dissolve
                wos "Carlos, this is Ash Jager."
                wos "Ash, this is Carlos Tsukada."
                cdef "Hey, nice to meetch-{nw}"
                show ash camera
                show car agitated at flip
                show Ash_Camera_Polaroid
                show white
                hide white with dissolve
                acam "Nice one!"
                cagit "Ow! What the heck was that?"
                hide ash
                hide Ash_Camera_Polaroid
                wbase "Ash likes to take polaroid pictures."
                hide mir
                acam "Never know when you're going to find a cryptid in the background of one of your shots!"
                hide ash
                whattip "Ash is also {i}very bad{/i} at asking permission."
                hide mir
                asurprise "Oh, whoops."
                cdef "So how do you two know each other?"
                menu:
                    "I know Ash from an old case.":
                        show mir default
                        show ash standard at flip
                        hide car
                        with dissolve
                        wbase "I know Ash from an old case."
                        asad "A few years back, I lost my brother."
                        asad "Sheriff Warren was really nice to me through it all."
                        wthink "Seems like it was the only thing I was good for."
                        hide ash
                        show car default at flip
                        cser "Wait a minute... this wouldn't happen to be the {color=#FF9966}PW-3 Incident{/color}, would it?"
                        show mir angry
                        wos ". . . . ."

                    "I owe Ash for a mistake I made a few years back.":
                        show mir default
                        show ash standard at flip
                        hide car
                        with dissolve
                        wbase "I owe Ash for a {color=#FF9966}mistake{/color} I made a few years back."
                        asad "You didn't make a mistake, Randi. You did everything you could."
                        aconfident "Besides, we both know the {i}real{/i} reason you keep me around is because I'm good company."
                        wos ". . . . ."
                        aannoy "Deny it all you want, we all know I'm the life of the party!"
                        hide ash
                        show car default at flip
                        cser "Hmm... this {color=#FF9966}mistake{/color}..."
                        cser "It wouldn't have anything to do with the {color=#FF9966}PW-3 Incident{/color}, would it?"
                        wangry "You're treading on thin ice, Tsukada."

                    "That's none of your business.":
                        hide ash
                        show mir default
                        show car default at flip
                        with dissolve
                        wbase "That's none of your business."
                        chold "Fine, sheesh, guess I'm the jerk."
                        hide mir
                        show ash standard
                        adef "It's fine, Randi."
                        asad "A few years back, I lost my brother."
                        asad "Sherrif Warren helped on the case."
                        hide ash
                        show mir default
                        cser "Wait a minute... this wouldn't happen to be the {color=#FF9966}PW-3 Incident{/color}, would it?"
                        wangry "I said it's none of your business, Tsukada."

                cagit "Okay, okay, I'll drop it."
                cdef "So, uh... why do you keep calling her Randi?"
                hide mir default
                show ash standard
                aflippant "It's a nickname. Like, Mir-Randi."
                adef "I came up with it when I was a kid."
                aconfident "But I will never, {i}ever{/i} stop using it."
                hide ash
                wannoy "* sigh *"
                $ meeting_ash_cleared_items.append("ashjager")

            "The Tour":
                show mir default
                show ash standard at flip
                hide car
                with dissolve
                whattip "What's this tour you were talking about?"
                asurprise "You mean you haven't heard?"
                aposit "Oh, that's right. You don't use the internet, do you?"
                wthink "I-I don't see what that has to do with anything."
                aflippant "Base 24 has been hyping this event up for the past couple weeks."
                adef "\"Come See The Future of Home Living!\""
                aconfident "I managed to snag tickets for the first tour."
                wbase "Okay, but what {i}is{/i} it?"
                apsyched "A {color=#FF9966}Smart House!{/color}"
                whattip "What does that... mean?"
                athink "It's like a robot butler or something, but it's built into the house itself."
                athink "Hang on, I've got a flyer."
                show houseflyer with dissolve
                aos "It's got these hands that come down from the ceiling to cook and clean."
                aos "There's a whole room where it bathes and dresses you!"
                aos "And they've got this artificial intelligence system that gets smarter as it learns your needs."
                hide houseflyer with dissolve
                adef "I've got an extra flyer if you want to thumb through it."
                $inventory.add(brochure)
                typing "House Brochure Added to Inventory"
                hide mir default
                show car default
                cser "The AI {i}learns?{/i} How does it do that?"
                athink "There were a lot of big words in the explaination, but I'm pretty sure it's..."
                athink "The Cloud?"
                hide car default
                show mir default
                aconfident "Anyway, it's pretty cool, huh?"
                menu:
                    "Yeah, pretty cool.":
                        wbase "Yeah, pretty cool."
                    "Pretty creepy, more like.":
                        wbase "Pretty creepy, more like."

                whattip "But still, you don't strike me as the kind of person who gets excited about domestic innovation."
                show ash surprised at flip
                wbase "Is there another reason you came here today, Ash?"
                aos ". . ."
                asad "Look, between you and me..."
                asad "I was hoping I might see something related to {color=#FF9966}that case{/color} again."
                wbase "I understand."
                wbase "That's part of my reason for coming here too."
                wthink "The other part being, it's my job to solve crimes, of course."
                aflippant "Of course."
                show mir default
                $ meeting_ash_cleared_items.append("thetour")

            "The Murder":
                show mir default
                show ash standard at flip
                with dissolve
                wbase "You know about the murder?"
                aflippant "Of course I do! That picture's been all over social media."
                whattip "Picture?"
                hide ash standard
                show car default at flip
                cagit "Social Media?"
                hide car default
                show ash standard at flip
                aannoy "Yeah, some internet \"Thought Influencer\" was here on the tour."
                wannoy "I have no idea what a Thought Influencer is and I have no desire to find out."
                show mir default
                aflippant "He uploaded a selfie without realizing there was a dead body in the background."
                hide ash standard
                show car default at flip
                cdef "Sheesh. How dense can you be?"
                hide car default
                show ash standard at flip
                whattip "Wait... does this mean there's a photo of the crime scene online?"
                athink "Yeah, I guess so."
                wbase "I need to see this right away."
                adef "Hm... looks like it's been taken down."
                aposit "I guess photos of corpses violate the site's Terms of Service."
                whattip "Ash... you're not a suspect in the murder, are you?"
                aannoy "No, no, don't worry. I was in the tour group the whole time. My alibi is solid as a rock."
                hide mir default
                show car liftdrink
                clift "But this other guy... the, uh, \"Thought Influencer\"..."
                chold "He slipped away to take selfies, right?"
                adef "Yeah."
                chold "His alibi's a bit shakier, then."
                athink "He'd have to be pretty stupid to take a photo of his own victim."
                hide car default
                show mir default
                wbase "At the very least, he might have seen something the rest of you didn't."
                athink "He should be around here somewhere. None of us are allowed to leave until this is wrapped up."
                $ meeting_ash_cleared_items.append("themurder")
        if "ashjager" in meeting_ash_cleared_items and "thetour" in meeting_ash_cleared_items and "themurder" in meeting_ash_cleared_items:
            $ meeting_ash_cleared = True

label meeting_ash_outro:
    stop music fadeout 1.0
    show black with dissolve
    hide black with dissolve
    hide ash
    show mir default
    show car default at flip
    with dissolve
    wbase "Carlos, we need to get going."
    hide car
    show ash standard at flip
    apsyched "Can I come with you, Randi?"
    aflippant "It's not like I can go anywhere else right now."
    hide ash standard
    show car default at flip
    clift "Sure! Come along! There's a murderer hiding around here, after all."
    wbase "All right, but I don't want you touching anything or-{nw}"
    play sound "sound/Ding.ogg"
    hide car
    show bottomi standard
    pause 0.5
    hide bottomi standard
    show car default at flip
    with dissolve
    cdef "Woah, did you see that guy?"
    hide mir default
    show ash surprised
    asurprise "He was so fast I didn't even have time to snap a picture of him."
    acam "Oh well. Guess I'll just have to snap a picture of you, Mr Tsukada."
    cagit "No wait I have a problem with{nw}"
    show white with Pause(0.05)
    hide white with dissolve
    show Ash_Camera_Polaroid
    acam "Ooh, that was a nice one!"
    hide Ash_Camera_Polaroid
    wthought "I wonder where that man was going in such a hurry..."

label meeting_drang_intro:
    show screen inventory_screen_button
    scene black
    typing "September 13th\nSmart House - Kitchen"
    scene kitchen with fade
    pause 2.0
    show mir default
    show ash standard at flip
    with dissolve
    wbase "There's the body."
    asad "Oh...man..."
    asad "I've never seen a dead body before..."
    asad "Do you ever get used to them?"
    wbase "No... not really."
    hide ash
    show car at flip
    cser "Margaritas help."
    wannoy "Tsukada, can you {i}please{/i} not drink at a crime scene?"
    clift "No can do, boss. It's Party Time on Isla De Carlos."
    wannoy "* sigh *"
    wbase "Well, the first thing we need is to {nw}"
    hide car
    show drang
    # HOLD IT!
    # Show Drang
    play sound "sound/Ding.ogg"
    djacket_pop "What are you doing at my crime scene?"
    whattip "I'm sorry... your crime scene?"
    ddef_gdown "Oh, I see. They didn't tell you I was heading down, did they?"
    ddef_gdown "You folks are probably still using smoke signals around here."
    $ profile.add(drang)
    play music "music/Gods Gift to Gendarmery.ogg"
    ddef_gup "Agent Sturmund Drang. I'm with the FBI."
    wbase "How did you get here so fast?"
    djacket_pop "We work quickly in the big time. We show up fast. We work fast. We leave fast."
    djacket_popped "We don't have time for your small town feelings. We use cold, calculated logic."
    wthought "Oh brother..."
    ddef_gdown "I must say, you're quite lucky."
    wannoy "How so?"
    dthink_gdown "Well, you must be dealing with a real puzzler of a case if they had to send me in."
    ddril_gdown "Of course, it will be like child's play to me, but for a non-sophistocate such as yourself..."
    dthink_gdown "...this case may have taken you ten, no, {i}eleven{/i} thousand years to solve."
    ddef_gdown "Good thing I came along."
    whattip "Listen...Agent Drang? Hmm... how do I put this..."
    djacket_pop "Well, don't ramble. I'm a busy man. I need things blunt and to the point."
    wbase "All right then... why are you here? Why is a local case of interest to the FBI?"
    dthink_gup "Frankly, I don't know myself. My superiors didn't give me a reason, they just handed me the case."
    ddril_gdown "So of course I just took it. They don't pay FBI Agents to ask questions, after all."
    hide drang
    show ash at flip
    aflippant "That's exactly what they pay FBI Agents to d{nw}"
    hide ash
    ddef_gdown "Anyways, I'm going to need you all to back away from the crime scene."
    ddef_gup "Only qualified professionals are allowed in here."
    hide drang with dissolve
    show ash thinking at flip
    with dissolve
    athink "How are we going to get past this clown?"
    wthink "It seems he really does have authority over me. We'll need his cooperation if we want to investigate."
    whattip "In order to do so, we're going to have to take advantage of his {color=#FF9966}psychology{/color}."
    apsyched "You mean we're going to {i}brainwash{/i} him?"
    wbase "No, we've just got to figure out what makes him tick, then capitalize on that."
    athink "So, like what?"
    wcasefile "For instance, I've noticed that he {color=#FF9966}seems to highly value logical thought.{/color}"
    wcasefile "He thinks highly of himself and {color=#FF9966}may respond to flattery.{/color}"
    wcasefile "Finally, he {color=#FF9966}prefers people to speak bluntly{/color}. Up to a point, I'm sure."
    wbase "If I can exploit these personality traits in the right way..."
    wbase "I might be able to convince him to let us investigate."
    aposit "And then Plan B is we brainwash him, right?"
    show mir annoy talk
    wos ". . . "
    wannoy "Sure."
    hide ash
    show drang default gdown
    ### BEGIN PERSUASION ANIMATION
    show healthBar
    wbase "Agent Drang, I need to ask you something."
    ddef_gdown "What, you're still here?"
    ddef_gdown "All right, all right. I'm not dumb."
    dthink_gdown "I know what you're here for."
    dthink_gdown "I can guess from the attire, but let's hear it straight from the horse's mouth."

label meeting_drang_conversation_p1:
    scene kitchen
    show mir default
    show drang default gdown
    ddef_gdown "Who are you, and what are you doing at my crime scene?"
    menu:
        #"Who are you, and what are you doing at my crime scene?"
        "Logic: I'm the Sheriff of this town, and like you, I seek only the cold, logical truth.":
            whattip "I'm the Sheriff of this town, and like you, I seek only the cold, logical truth."
            dthink_gdown "A fellow warrior of the intellectual arts, hmm?"
            djacket_pop "Well, I'm sorry to disappoint you, but I've already got this case in the bag."
            djacket_popped "This is a simple town, full of simple people. People like yourself."
            ddril_gdown "It should be no challenge at all to deduce the simple motivations of this simple murder."
            ddef_gdown "If you want the cold, logical truth about this case..."
            ddef_gdown "You'll just have to wait to read it in the newspaper with the rest of your simple neighbors."

        "Blunt: I'm the Sheriff and I have as much of a right to investigate as you.":
            wbase "I'm the Sheriff of this town, and I have as much of a right to investigate as you."
            ddef_gup "Blunt and to the point. I like people who don't waste my time."
            dthink_gup "Unfortunately, you're not quite right."
            ddril_gdown "I have been given full athority over this crime scene by my superiors."
            ddril_gup "They're part of a little organization, maybe you've heard of it, called the {i}FBI?{/i}"
            ddef_gup "So, no, sweetcheeks. I'm the only one here with the right to investigate."

        "Flattery: I am but a simpleton, hoping that I may assist you in your resplendent investigation.":
            wthink "I am but a simpleton, hoping that I may assist you in your resplendent investigation."
            dangry_gup "You're talking down to me, aren't you?"
            wannoy "N-no, I just {nw}"
            dangry_gdown "Save it. I won't be condescended to."
            $ mc_health -= 1
            while mc_health_display > mc_health:
                $mc_health_display -= 0.1
                pause 0.01
            show mir recoil anim
            wos "NNNGGGGGG!!!! {w=4.0}"
            djacket_pop "I'm a big man. I know big words."
            djacket_popped "Words like... 'condescended'."
            wthought "Damn. He saw right through me."
            wthought "I'm going to have to take a different approach."
            dthink_gdown "Now I'm going to ask you once again..."
            jump meeting_drang_conversation_p1

    wangry "No. I've got to get in there."
    dangry_gdown "Boy, you're persistent, huh?"

label meeting_drang_conversation_p2:
    dangry_gdown "Let me ask you something:"
    dthink_gdown "What possible reason might I have to bring a nosy small town police chief along on my assignment?"
    menu:
        "What possible reason would I have to bring you along?"
        "Logic: The more help you have, the faster you can wrap this case up.":
            whattip "Look, I know you don't want to be here."
            wbase "You're an FBI officer. You don't want to waste your time in a backwoods town like this."
            wbase "So, the more help you have, the faster you can wrap this case up."
            wbase "The faster you wrap this case up, the faster you're back where you belong."
            dthink_gdown "Compelling. Succinct. Logical."
            ddef_gdown "I like the cut of your gib, Warren."

        "Blunt: You clearly have no idea what you’re doing.":
            wbase "I'll cut right to the chase, Drang."
            wangry "You clearly have no idea what you’re doing."
            wangry "You haven't set up a perimeter, you haven't begun to interview witnesses."
            wangry "Best I can tell, you've just been standing here rubbing your chin."
            dangry_gup "Get out of my sight, you disrespecful cretin!"
            dangry_gup "Never in all my life have I met someone so asinine!"
            $ mc_health -= 1
            while mc_health_display > mc_health:
                $mc_health_display -= 0.1
                pause 0.01
            show mir recoil anim
            wos "NNNGGGGGG!!!! {w=4.0}"
            wthought "Uh oh. Looks like I pushed him too far."
            wthought "Maybe I should try that one again."
            jump meeting_drang_conversation_p2

        "Flattery: You’ll need someone around to appreciate your genius.":
            wthink "I have no doubt that you can solve this case on your own."
            whattip "That's why they sent you down all this way, right?"
            wbase "But you’ll still need someone around to appreciate your genius."
            wbase "A Watson to your Holmes. A Hastings to your Poirot."
            hide mir
            show ash
            aflippant "A Marty to your Doc Brown!"
            hide ash
            show mir
            wannoy "Not the analogy I would have gone with,{nw}"
            wbase "Not the analogy I would have gone with,{fast} but yes."
            dthink_gup "Hmm...a most astute point."
            ddril_gup "My talents are wasted without someone to marvel at them."

    wbase "So, I have your permission to examine the crime scene?"
    dthink_gdown "All right... on one condition."

label meeting_drang_conversation_p3:
    djacket_pop "If you come along, you’re going to have to follow my directions to the T."
    djacket_popped "Can you do that?"
    menu:
        "Logic: If you contradict the facts of the case, I’ll be forced to disregard your directions.":
            wbase "I'm sorry, Agent. I can't fully agree to that."
            wbase "I'll try to follow your lead as much as I can. However..."
            wbase "If you contradict the facts of the case, I’ll be forced to disregard your directions."
            dthink_gdown "Intriguing. An officer of the law with as strong a will as I."
            dthink_gdown "Engaged in a speculative tete-a-tete, a war of competing logics."
            ddril_gdown "And only he with the superior intellect will emerge victorious."
            whattip "You mean he {i}or she{/i}."
            ddril_gup "No..... Just he."
            hide mir
            show ash
            aannoy "What about \"they\"?"
            hide ash
            show mir default
            djacket_pop "Very well, Officer. I accept your proposition."
            djacket_popped "You may accompany me into this snake pit of criminality for as long as you prove a worthy foe."

        "Blunt: I’ll never follow the instructions of a dope like you.":
            wangry "Hah! I’ll never follow the instructions of a dope like you."
            wangry "You need to grow up and accept that you can't just boss people around!"
            ddril_gdown "Well, that was a close one."
            ddril_gdown "To think I almost let a rude little boondock cop into {i}my{/i} crime scene!"
            ddril_gdown "Good thing your little outburst there convinved me otherwise!"
            $ mc_health -= 1
            while mc_health_display > mc_health:
                $mc_health_display -= 0.1
                pause 0.01
            show mir recoil anim
            wos "Ah! Wait! {w=4.0}"
            wthought "What was I thinking, getting so confrontational with him?"
            wthought "And right as I was getting through to him, too!"
            wannoy "Agent Drang, I'm sorry for speaking out of turn. Give me another chance."
            dthink_gdown "Humbling yourself before me is a good start. Now..."
            jump meeting_drang_conversation_p3

        "Flattery: Of course. You are my superior officer, after all.":
            whattip "Well, Of course. You are my superior officer, after all."
            hide drang
            show ash at flip
            aunsure "(Randi! What are you saying?)"
            aunsure "(You're not really gonna let this chauvinistic prat boss you around, are you?)"
            wbase "(No, of course not.)"
            wbase "(But the only way to examine this crime scene is to play along for now.)"
            hide mir
            hide ash
            show ash standard
            show drang
            dangry_gdown "What are you two whispering about over there?"
            asurprise "!"
            dthink_gdown "No need to answer. My skills of deduction have already surmised..."
            ddril_gdown "...that you are talking about what a genius I am!"
            asurprise "uh"
            asurprise "yes"
            asurprise "that is exactly, the thing, we were doing,"
            ddef_gup "Well, don't be so shy about it from now on."
            ddef_gup "I am a humble man. I am not embarrassed by descriptions of my incredible wit."
            ddef_gdown "Now, come along. There will be plenty of time to bask in my genius."


label meeting_drang_outro:
    stop music fadeout 1.0
    hide healthBar
    show black with dissolve
    scene kitchen
    hide black
    hide drang
    show mir default
    show ash standard at flip
    with dissolve
    adef "Well, you got us through."
    wthink "Now we just need to stay on his good side for as long as it takes to solve this case."
    adef "Let's hope this is a quick one, then."
    hide mir
    hide ash
    $unlockedoutage = False
    $unlockedphoto = False
    $chritudeinto = False
    $warehouseFirstVisit = True
    $loop = 0
    $investigation1_cleareditems = []
    play music "music/Investigation_Loops.ogg" fadein 1.0

label investigation1:
    scene kitchendrang with fade
    hide victimbody
    if "1" in investigation1_cleareditems and "2" in investigation1_cleareditems and "3" in investigation1_cleareditems and "4" in investigation1_cleareditems and "5" in investigation1_cleareditems and "6" in investigation1_cleareditems and "7" in investigation1_cleareditems and "8" in investigation1_cleareditems and "9" in investigation1_cleareditems:
        jump smart_house_act_1_finale
    show screen sh_investigation1_kitchen

    pause

screen sh_investigation1_kitchen:
    modal True
    imagemap:
        ground "kitchendrang"
        hotspot (535,898,434,187) action [Hide("sh_investigation1_kitchen"), Jump("investigation1_footprints")]
        hotspot (1525,271,357,768) action [Hide("sh_investigation1_kitchen"), Jump("investigation1_drang_conversation")]
        hotspot (961,732,628,346) action [Hide("sh_investigation1_kitchen"), Jump("investigation1_examining_victim")]
    use inventory_screen_button
    imagebutton auto "assets/menu/move_%s.png"  xalign 0.5 yalign 1.0 action Jump("inv1_move_kitchen")

label inv1_move_kitchen:
    menu:
        "Base 24 - Warehouse":
            hide screen sh_investigation1_kitchen
            jump investigation1_warehouse


label investigation1_drang_conversation:
    $back_action = "investigation_1_drang_present"
    scene kitchen
    hide ash
    hide car
    show mir default
    show drang default gup
    with dissolve
    if loop == 0:
        ddef_gup "Ah, my new assistant!"
        ddef_gup "How goes your little investigation?"

    $loop = 1
    while loop == 1:
        menu:
            "The Murder":
                whattip "Tell me what you've uncovered so far."
                ddef_gup "Of course. Allow me to astound you with my powers of observation."
                djacket_pop "The first thing I've deduced: there has been a murder."
                show mir default
                wos ". . . . ."
                wbase "...Go on."
                dthink_gdown "The victim was stabbed to death in this very kitchen."
                dthink_gdown "Time of death is somewhere between 5 and 6 P.M."
                ddef_gdown "We know this because the first sighting of the body was at 6..."
                ddef_gdown "And the tour group passing through the kitchen around 5 did not see it."
                wbase "This first sighting of the body..."
                whattip "Was this the boy who unknowlingly uploaded a photo of the body online?"
                ddef_gdown "That's the one."
                ddril_gdown "Simpleton didn't even notice there was key evidence in his glamour shot."
                dthink_gup "Eventually someone else reported the photo to the FBI."
                ddef_gup "And they sent me over to clean the whole mess up."
                wbase "Did any of the witnesses see or hear anything peculiar before the body was discovered?"
                dthink_gup "I heard there was a {color=#FF9966}power outage{/color} right around that time."
                whattip "A {color=#FF9966}Power Outage{/color}?"
                $unlockedoutage = True

            #"Sturmund Drang":
            #    warren "So, you're from the Federal Bureau of Investigation?"

            "Power Outage" if unlockedoutage == True:
                wbase "What do you know about the power outage?"
                ddril_gup "What's there to know?"
                ddril_gup "Some idiot somewhere blew a fuse while the tour was in progress."
                ddef_gup "The whole house lost power. The lights, the appliances, even the computer thing in charge."
                wthink "You think it was our culprit, creating a distraction in order to cover his tracks?"
                dangry_gdown "Oh my god! That's...that's..."
                ddril_gdown "...exactly what I was thinking, of course."
                ddril_gdown "Good job keeping pace, assistant."
                $ investigation1_cleareditems.append("1")

            "Show Evidence":
                wbase "Let me show you something."
                $ current_present = "investigation_1_drang_present"
                show screen present_evidence_screen
                show screen back_button
                pause

            "Show Profile":
                wbase "What do you know about this person?"
                $ current_present = "investigation_1_drang_present"
                show screen present_profile_screen
                show screen back_button
                pause

            "Goodbye":
                wbase "I'm going to take another look around."
                djacket_pop "Don't come back until you've got something good to show me."
                hide drang
                $loop = 0

    call investigation1 from _call_investigation1

label investigation_1_drang_present:
    if present_response == "badge":
        ddef_gup "Aww, that's cute. It almost looks like a real one."
        hide drang
        show ash standard at flip
        asurprise "Oh my gosh!"
        adef "Can I punch this guy, Randi?"
        wbase "Speaking as a police officer: No."
        wthought "Though I'd be lying if I said I wasn't considering it myself..."
        hide ash
        show drang default gup
        jump investigation1_drang_conversation

    if present_response == "brochure":
        whattip "Have you toured the rest of the house yet?"
        ddril_gdown "Why bother? The body is right here."
        wangry "The culprit could be hiding somewhere in the house right now!"
        djacket_popped "* sigh *"
        dthink_gup "Look, between you and me, I agree with you."
        dthink_gup "But these Base 24 goons are real sensitive about anyone looking at their precious R&D projects."
        dthink_gup "They won't let me anywhere else in the house until I can prove it has something to do with the case."
        ddef_gup "So let's hope there's something of the sort hidden around here, eh?"
        jump investigation1_drang_conversation

    if present_response == "knife":
        djacket_pop "There it is, the murder weapon."
        djacket_popped "Did you have your Forensics Stooge take a look at this?"
        cos "Hey!"
        wbase "Yes. He didn't find any fingeprints on the handle."
        dthink_gup "Interesting. There's only one conclusion to draw from this."
        wbase "The culprit was{nw}"
        dthink_gdown "Your assistant is completely incompetent."
        cos "HEY!"
        wannoy "I, uh, don't think it's that."
        wthink "I don't think even Carlos is inept enough to mess up a simple fingerprint test."
        cos "{b}ET TU, CHIEF?{/b}"
        jump investigation1_drang_conversation

    if present_response == "prelim":
        whattip "What do you make of the bruises on the victim's body?"
        ddef_gup "I've seen this kind of thing before. Nasty business."
        wbase "What is it?"
        dthink_gdown "Technically, I'm not supposed talk about it."
        dthink_gup "But if it's neccesary to solve this case..."
        wangry "What? What is it? Tell me!"
        dos ". . ."
        dthink_gup "Have you ever heard... of a \"Fight Club\"?"
        wannoy "Ugh, never mind."
        jump investigation1_drang_conversation

    if present_response == "missingshoe":
        dangry_gdown "Now, I've noticed here, that the thing you're showing me, is nothing."
        dangry_gdown "It's literally the absence of a thing."
        dangry_gdown "And now I'm wondering if this is some new Police Officer Prank."
        dangry_gdown "Where you try and waste my time."
        dangry_gdown "To which I say... good prank, I guess?"
        wbase "I'm trying to say that the victim's missing shoe might be an important clue."
        wbase "It could tell us where he's been."
        dthink_gup "Well... you shouldn't have wasted my time by letting me go on that whole tirade."
        jump investigation1_drang_conversation

    if present_response == "idcard":
        ddef_gup "You've ID'd the victim?"
        wbase "His name is Orin Darsha. It looks like he worked here at Base 24."
        whattip "Any chance you know of him?"
        ddril_gdown "Hah. I don't intend to know {i}anyone{/i} in this bumpkin town."
        ddril_gdown "That includes this guy, and it includes {i}you{/i}, small fry."
        wthought "The feeling's mutual, you smarmy puke."
        jump investigation1_drang_conversation

    if present_response == "darsha":
        ddef_gup "You've ID'd the victim?"
        wbase "His name is Orin Darsha. It looks like he worked here at Base 24."
        whattip "Any chance you know of him?"
        ddril_gdown "Hah. I don't intend to know {i}anyone{/i} in this bumpkin town."
        ddril_gdown "That includes this guy, and it includes {i}you{/i}, small fry."
        wthought "The feeling's mutual, you smarmy puke."
        jump investigation1_drang_conversation

    if present_response == "crimephoto":
        djacket_pop "What a sorry excuse for evidence."
        djacket_popped "Back in my day, photographic evidence was all grainy and black and white."
        djacket_popped "There was some dignity to the whole affair."
        djacket_popped "Now it's all {i}selfies{/i} and {i}smartphones.{/i} I mean, where's the respect?"
        wthought "For once, I actually agree with him."
        jump investigation1_drang_conversation

    #if present_response == "paulchritude":
        #drang "I see you've met our \"eyewitness\"."

    if present_response == "Back":
        wbase "Actually, never mind."

    else:
        djacket_popped "I don't know about that and I don't care."
        djacket_popped "I'm far too busy to be looking at every little thing you want to show me."
        djacket_popped "I need to save my genius for things of true importance."

    jump investigation1_drang_conversation

label investigation1_warehouse:
    if warehouseFirstVisit == True:
        show black with dissolve
        typing "Base 24 - Warehouse"
        $warehouseFirstVisit = False
    scene basewarehousepaul with fade
    show screen sh_investigation1_warehouse
    hide black with dissolve
    pause

screen sh_investigation1_warehouse:
    modal True
    imagemap:
        ground "basewarehousepaul"
        hotspot (1152,618,242,328) action [Hide("sh_investigation1_warehouse"), Jump("investigation1_chritude_conversation")]
    use inventory_screen_button
    imagebutton auto "assets/menu/move_%s.png" xalign 0.5 yalign 1.0 action Jump("inv1_move_warehouse")

label inv1_move_warehouse:
    menu:
        "Smart House - Kitchen":
            hide screen sh_investigation1_warehouse
            jump investigation1

label investigation1_chritude_conversation:
    if chritudeinto == False:
        show mir default
        show ash standard at flip
        with dissolve
        wbase "There's somebody over there taking pictures of himself."
        asurprise "Hey, that's the guy!"
        whattip "You mean the, uh, \"Thought Influencer\"?"
        adef "Yup."
        wbase "Let's go introduce ourselves, then."
        aannoy "What? I don't want to talk to that pompous chump."
        wthink "Me either, but we need that photo he took of the crime scene."
        aunsure "All right, all right."
        hide ash
        scene basewarehouse
        with fade
        show chritude standard at flip
        show mir default
        with dissolve
        wbase "Excuse me, sir. Are you..."
        punk "...The most fabulous eCeleb ever beheld by mankind?"
        punk "Why, yes. How kind of you to say."
        pglitter "My name is Paul Chritude, but you probably know me by my internet handle... MASTER STYLE!"
        hide mir
        show ash
        athink "How did you make those sparkles appear?"
        pconceited "Trade secret, my dear."
        hide ash
        show mir hattip
        wthought "Master Style, huh? He looks more like a King Clown."
        wbase "Mr Chritude, my name is Miranda Warren. I'm the Sheriff of Boomtown."
        pdef "Oh, you're here about the murder!"
        psad "Terrible thing, that. Ruined one of my trademark glamour shots!"
        wannoy "You'll forgive me if the disruption of a selfie isn't my number one concern right now."
        pconceited "If you have any questions for me, ask away. I'm always glad to help the little people."
        $chritudeinto = True

    $loop = 1
    while loop == 1:
        menu:
            "Paul Chritude":
                show mir
                show chritude at flip
                whattip "Mr Chritude... could you explain to me what it is you actually do?"
                poutrage "Are you saying you've never heard of moi?"
                poutrage "Why, I've never been more offended in all my life!"
                hide mir default
                show ash
                aannoy "You'll have to excuse my friend, Master Style. She doesn't go on the internet all that much."
                aflippant "She doesn't even know what a hashtag is!"
                hide ash
                show mir default
                psad "You poor soul! I... I had no idea!"
                pconceited "Very well. I will explain who I am, for your sake."
                pglitter "I... am a tastemaker. I make tastes."
                pdef "When you want to know what's hot in fashion, luxury, technology, you come to me."
                pdef "I am the utmost authority in all these things."
                plaugh "A new trend simply does not get started without my express approval."
                pconceited "Many people consider me to be Oprah 2: The Sequel to Oprah."
                wthought "And here I thought Drang was conceited..."
                $ investigation1_cleareditems.append("2")

            "The Tour":
                show mir
                show chritude at flip
                whattip "So, you were part of the group touring the smart house this evening?"
                pdef "Why, yes. This unveiling is the first step in a major rollout for the Smart House brand."
                pconceited "So naturally they needed a Thought Influencer such as myself to give it the stamp of approval."
                pconceited "My upcoming tell-all expoSay vlog will either make or break the Smart House."
                hide mir
                show ash
                aflippant "So... are you going to make it, or break it?"
                plaugh "You'll have to wait and see, now won't you?"
                hide ash
                show mir
                wcasefile "At one point you snuck away from the the tour group, is that right?"
                pdef "Yes, that tour was getting dreadfully boring."
                poutrage "My followers were chomping at the bit for new content! How could I deny them?"
                wbase "So what did you do?"
                poutrage "I simply went and explored the house at my own pace. I wasn't causing any trouble or anything!"
                wbase "And this is when you photographed the body?"
                pdef "Yes, indeed."
                wthought "I should ask for more detail on that..."
                $unlockedphoto = True

            "Your Photo" if unlockedphoto == True:
                show mir
                show chritude at flip
                whattip "I suppose I'll start with the obvious question:"
                wangry "How on earth could you not not have noticed there was a dead body in your photograph?"
                poutrage "Listen here, lady cop. I adhere to a strict regimen of twelve glamour shots per hour."
                pconceited "I don't have the time to be combing each and every one for corpses!"
                pconceited "The only thing I can review with any sort of thoroughness is the face region, which must, of course, be perfect."
                pdef "Frankly, I only looked twice at that picture after I'd recieved the takedown notice."
                wthink "That reminds me... I need to consult that photograph, but it's been taken offline."
                wbase "Is there any chance you have a copy you could give me?"
                plaugh "Don't worry, I get asked this all the time."
                pdef "It's fifteen for a glossy, thirty if you want it signed."
                wangry "How about zero for not getting charged with obstruction of justice?"
                psad "Very well, very well..."
                psad "...spoilsport..."
                show chritudesPhoto with dissolve
                wos "This has got to be the most absurd evidence I've ever recieved."
                wos "Still, it's a bit more understandable he didn't notice something that was on the other side of a window."
                wos "All this time I thought he'd been in the same room as the body."
                aos "Hey, look at that! Is there someone else inside the kitchen?"
                wos "You're right! It's hard to make out any detail, but that's definitely the silhouette of another person."
                wos "Whoever it is, it's probably our culprit."
                aos "Or, maybe it's the victim's spirit, caught on camera as it exited its corporeal host!"
                wos "Let's... put a pin in that theory, okay?"
                hide chritudesPhoto with dissolve
                $inventory.add(photo)
                $ investigation1_cleareditems.append("3")

            "Power Outage" if unlockedoutage == True:
                show mir
                show chritude at flip
                wbase "Around the time you took that photo of the crime scene, there was a power outage, right?"
                pnervous "Oh! Was there? I had almost forgotten!"
                pnervous "However did that happen, is what I'm wondering!"
                whattip "Yes, I was curious about that as well. I thought that since you were away from the tour group, you-"
                poutrage "-might have blown the fuse myself? Preposterous!"
                wbase "I was going to say \"might have seen who did it\"."
                wthink "Although now that you mention it..."
                poutrage "Too bad! It wasn't me! I don't know anything about that power outage, or that big explosion!"
                wbase "Big explosion?"
                psurprise "Ulp!"
                hide mir
                show ash
                asurprise "Oh, that's right! Around the time the power went out, there was this big BANG noise!"
                athink "I guess it did kind of sound like an explosion..."
                psurprise "Exactly! {i}That{/i} explosion noise!"
                pconceited "I don't know anything about it."
                hide ash
                show mir annoy anim
                wos ". . . . ."
                wthought "Clearly this guy's hiding something..."
                wthought "But I've got more pressing matters to deal with than his shaky coverup."
                wthought "I'll just have to come back to him later."
                $ investigation1_cleareditems.append("4")


            "Show Evidence":
                wbase "What do you make of this right here?"
                $ current_present = "investigation_1_chritude_present"
                show screen present_evidence_screen
                show screen back_button
                pause

            "Show Profile":
                wbase "What do you think of this person?"
                $ current_present = "investigation_1_chritude_present"
                show screen present_profile_screen
                show screen back_button
                pause

            "Goodbye":
                wbase "Thank you for speaking with us. It's been very, um, helpful."
                pdef "Oh, any time, darling."
                $loop = 0

    call investigation1_warehouse from _call_investigation1_warehouse


label investigation_1_chritude_present:
    if present_response == "sheriffbadge":
        pdef "What a wonderful little trinket!"
        pdef "Where did you get such a charming accessory?"
        wannoy "Um...from the police station. Where I work. Because I'm a police officer."
        plaugh "Yes, yes, of course."
        pdef "How much?"
        wbase "For my {i}badge?{/i}"
        poutrage "Of course! What else would I be asking for?"
        pconceited "Certainly there's nothing else about that outfit worth any money."
        wannoy "I'll be sure to voice your concerns to the police department's wardrobe team."

    if present_response == "crimephoto":
        psad "Such a shame..."
        psad "My poor selfie...stricken down before its time by the Cruel Internet Gods."
        pglitter "Had it been allowed to prosper, it could have gone viral! I just know it!"
        hide mir
        show ash
        aunsure "It's got a dead body in it, though!"
        plaugh "I know! Just think of the {i}scandal!{/i}"
        plaugh "My shares would have hit the BILLIONS!"
        hide ash
        show mir
        wannoy "Well, at least your priorities are in the right place."
        pconceited "You know, I tell myself that {i}all the time.{/i}"

    if present_response == "Back":
        wbase "Actually, never mind."

    else:
        pconceited "Fabulous! Daring! I love it!"
        wannoy "Um, you haven't even looked at it."
        pconceited "I've never seen something so marvellous in all my life!"
        wannoy "All right, sheesh, never mind."

    jump investigation1_chritude_conversation

label investigation1_footprints:
    show mir default
    show ash standard at flip
    apsyched "Look over here, Randi! Muddy footprints!"
    apsyched "That's like Clues 101!"
    athink "But whose could they be...?"
    wthink "They don't seem to be the victim's. His feet are clean."
    aposit "We know one thing for certain..."
    aposit "Whoever this person is, they don't possess the power of flight."
    hide ash
    show car at flip
    clift "I just kind of assume that about everybody, all the time."
    cdef "Hey, these are some pretty clear prints."
    cdef "It won't be hard to match it up with the shoe, if we can find it."
    wthink "There's something bothering me about these prints..."
    cser "Hm?"
    wthink "We're in a pristine government warehouse."
    wbase "Where did this person find a puddle big enough to muddy their shoes like this?"
    hide car
    show ash standard at flip
    adef "There's a little fake garden outside the house."
    athink "Maybe this person stepped in the dirt out there?"
    wthink "It's possible..."
    whattip "Still, it seems like you'd have to go out of your way to make these footprints."
    hide ash
    show car at flip
    cser "You mean... somebody {i}wanted{/i} us to find these?"
    cser "Why would anybody do that?"
    $inventory.add(footprints)
    $ investigation1_cleareditems.append("5")
    call investigation1 from _call_investigation1_2


label investigation1_examining_victim:
    wos "Let's get a closer look at the body."
    ### Show Closeup of Body
    show victimbody with dissolve
    cos "Jeez. This guy looks really bad."
    cos "Not that murder victims usually look {i}great{/i}, but even by corpse standards this is nasty."
    wos "Ash, you really shouldn't be looking at this."
    aos "I'll be fine. This isn't much worse than most video games."
    wos "That's awful. Who'd want to play a video game with something like {i}this{/i} in it?"
    jump investigation1_examining_victim_map

label investigation1_examining_victim_map:
    show screen sh_investigation1_body
    pause

screen sh_investigation1_body:
    modal True
    imagemap:
        ground "victimbody"
        hotspot (1565,664,296,145) action [Hide("sh_investigation1_body"), Jump("investigation1_missing_shoe")]
        hotspot (244,425,93,89) action [Hide("sh_investigation1_body"), Jump("investigation1_identifying_victim")]
        hotspot (54,331,159,439) action [Hide("sh_investigation1_body"), Jump("investigation1_examine_injuries")]
        hotspot (699,132,299,221) action [Hide("sh_investigation1_body"), Jump("investigation1_examine_injuries")]
        hotspot (483,157,164,290) action [Hide("sh_investigation1_body"), Jump("investigation1_examine_weapon")]
    use inventory_screen_button
    imagebutton auto "assets/menu/return_%s.png"  action [Hide("sh_investigation1_body"), Jump("investigation1")] xalign 1.0 yalign 1.0

label investigation1_missing_shoe:
    wos "Tsukada. Take a look at this."
    cos "What?"
    wos "This man is missing one of his shoes."
    cos "You think it came off during the murder?"
    wos "I don't think he took it off for the fun of it, if that's what you're asking."
    aos "Maybe some sort of shoe-hungry creature came and took it for a snack!"
    wos "That's completely ridiculous."
    aos "Agh, you're right. A shoe-eater obviously would have taken the other one, too."
    wos "That's not what I... never mind."
    wos "In any case, let's take a note of it."
    $ investigation1_cleareditems.append("6")
    $inventory.add(missingshoe)
    typing "Missing Shoe Added to Inventory"
    call investigation1_examining_victim_map from _call_investigation1_examining_victim_map


label investigation1_identifying_victim:
    wos "There's something pinned to his shirt."
    cos "Looks like an ID Card."
    $inventory.add(idcard)
    typing "ID Card Added to Inventory"
    show darshasid with dissolve
    ### ID Card icon on screen
    cos "\"Orin Darsha, Base 24 Research and Development.\""
    cos "\"Head of Applied Research.\""
    hide darshasid with dissolve
    $profile.add(darsha)
    cos "I guess this guy was in charge around here."
    wos "He was probably overseeing the development of this smart house."
    aos "Poor guy. Killed in the kitchen of his own project."
    aos "And on the day he finally got to unveil it to everyone."
    cos "I wonder if this house has anything to do with why he was killed."
    wos "We should ask around to see if anyone knows more about him."
    cos "At least we've got a name for our John Doe now."
    $ investigation1_cleareditems.append("7")
    call investigation1_examining_victim_map from _call_investigation1_examining_victim_map_1

label investigation1_examine_injuries:
    cos "This guy's got quite a few injuries on him."
    cos "Obviously, he's got a massive stab wound."
    cos "But what's really strange is the bruises."
    cos "You don't expect a stabbing victim to have signs of blunt force trauma."
    wos "Well, which one is the cause of death?"
    cos "I can figure that out, but it's going to take a while."
    cos "In the meantime, let me write you up a preliminary medical report."
    $inventory.add(prelim)
    typing "Autopsy Report Added to Inventory"
    $ investigation1_cleareditems.append("8")
    call investigation1_examining_victim_map from _call_investigation1_examining_victim_map_2

label investigation1_examine_weapon:
    cos "Well, not to jump to conclusions here..."
    cos "But I think we've found our murder weapon."
    cos "I'll be running some tests to determine the cause of death, of course."
    cos "But in most cases, the simplest solution is usually the correct one."
    wos "Occam's Razor."
    cos "Or in this case, Occam's Kitchen Knife."
    wos "Carlos, can you run a fingerprint test on the handle of this knife?"
    cos "No problem. Just give me one second..."
    ### Short fade to black to show passage of time
    show black with dissolve
    pause 1.0
    hide black with dissolve
    cos "Huh. That's strange."
    wos "What?"
    cos "There's not a single print on this handle."
    cos "In fact, there's no indication a hand even {i}touched{/i} this knife."
    $inventory.add(knife)
    typing "Kitchen Knife Added to Inventory"
    aos "No fingerprints, huh?"
    aos "You know what could grab a knife without leaving fingerprints?"
    wos "Please don't say ghosts."
    aos "Now, listen."
    aos "I'm not saying it {i}was{/i} ghosts."
    aos "{i}All I'm saying is{/i} we need to keep an open mind to the {i}possibility{/i} that it was ghosts."
    wos "Let's stay away from the supernatural theories until we conclusively rule out the natural ones, all right?."
    $ investigation1_cleareditems.append("9")
    call investigation1_examining_victim_map from _call_investigation1_examining_victim_map_3

label smart_house_act_1_finale:
    stop music fadeout 1.0
    show mir default
    show car at flip
    cdef "So, how are things going, Chief?"
    wbase "Not great."
    wthink "I've got quite a few pieces of evidence, but none of it fits together yet."
    wthink "The biggest problem is that I still don't have a prime suspect."
    cdef "Well, you can't exactly expect somebody to conf{nw}"
    nameless "Please... help.... me....."
    hide car
    show bottomi standard with dissolve
    pause 1.0
    hide mir
    asurprise "Randi, who is this guy?"
    hide ash
    wbase "I don't know."
    bunk "That man... on the ground..."
    bunk "I'm... so sorry... I'm so sorry...."
    wbase "Sir... are you all right? What's your name?"
    bunk "I think... it was me."
    bunk "I'm the one who killed that man."
    ### End of Act 1 Animation
    jump endgame
    jump smart_house_act_2_intro
