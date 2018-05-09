label smart_house_act_6_intro:
    scene act6 with fade
    $ save_name = "Act 6"
    pause 3.0
    show black with dissolve
    typing "September 13th. 11:08 P.M.\nSmart House - Kitchen"
    show kitchen
    show mir default
    show ash unsure at flip
    with fade
    aunsure "Randi, what the heck is going on here?"
    wthink "I'm not sure yet. I've got one theory..."
    wthink "But it's completely ridiculous, even by your standards."
    aposit "And I do have some famously low standards..."
    wbase "Still, it's the only explanation I can think of."
    wbase "I'm just going to have to test it out."
    hide mir
    hide ash
    with dissolve
    show mir default
    show neering default
    with dissolve
    wbase "Ms Angela Neering?"
    wgotcha "{i}If{/i} that is your real name..."
    wgotcha "I think that you ar{nw}"
    ndef "You think I'm some sort of impostor?"
    wconfused "I - yes, actually. Good guess."
    ndef "It wasn't a guess. I've watched enough TV to know where the \"if that is your real name\" bit is leading."
    ngrumble "So, what? You think I'm some maniac dressed up as myself?"
    ngrumble "Like I've got \"The Real Angela\" locked up in a closet somewhere?"
    whattip "Well, it should be easy enough to disprove. Just tell us something only she would know."
    ndef "Hm. Nah."
    wangry "Nah?"
    ndismissive "Why should I play along with your stupid theory? Seems the burden of proof is on you."
    hide mir
    show drang think gup at flip
    dthink_gup "Sorry Neering, but I gotta side with Officer Warren here."
    nangry "What!?" with shake
    hide drang
    show mir angry
    wangry "What!?" with shake
    hide mir
    show drang think gdown at flip
    dthink_gdown "This whole \"Fake Angela\" theory is ridiculous..."
    ddril_gup "But it's the kind of ridiculous I can get behind!"
    ddril_gup "None of this high-concept sci-fi nonsense."
    ddril_gup "Just some good old fashioned identity theft."
    djacket_pop "So, make with the testimony!"
    hide drang
    show mir default
    with dissolve
    ngrumble "Fine. What you do want to know more about?"
    whattip "Hmm... Tell us more about the moment of the killing."
    ngrumble "Fine, fine. If that will get you off my back..."

    hide mir with fade
    call witness_statement from _call_witness_statement_2
    typing "-- my_testimony_FINAL(1)_LASTONEFORREAL.txt --{fast}"
    ndef "As you surmised, we were both in the bedroom when it happened."
    ndef "We were having our little conversation over whether to shut down the house or not."
    ndismissive "When it seemed like things weren't going to go in my favor, I came up with a plan."
    ndismissive "I was hoping to trick Darsha into using the contraption himself, but it seems he was already suspicious of me."
    ndef "So I pushed him away from me, and then activated the trap door."

    show mir default
    with fade

label testimony11_intro:
    $testiLength = 5
    $ current_present = "SH_Objection11"
    $ CurrentTestimony = "SH_Testimony11A"
    $ back_action = CurrentTestimony
    hide screen inventory_screen_button
    scene kitchen
    hide mir
    show neering default
    with fade
    call interrogation from _call_interrogation_3
    #play music "BustingLiesAtABriskTempo.ogg" fadein 1.0


label SH_Testimony11A:
    $ settesti("SH_Testimony11A", None, "SH_Testimony11B", "SH_Press11A","SH_Advice11",1)
    show screen testi
    ndef "As you surmised, we were both in the bedroom when it happened."
    jump SH_Testimony11B

label SH_Press11A:
    hide screen testi
    show mir hattip
    whattip "Can you explain where you were both standing?"
    ndef "Well, I was sort of near the foot of the bed, while Darsha was..."
    ndismissive "You know what, it would probably be quicker to just show you."
    wconfused "Show me?"
    ndismissive "Yeah, hang on. There was a camera running in the bedroom at the time."
    show SecurityCam with dissolve
    nos "There. That should be easier for your primitive brain to comprehend."
    nos "Most of the footage was corrupted, so I could only salvage a single clean frame."
    wos "Interesting. What's that A.R.M. doing there?"
    nos "You forget, we were in the middle of a tour. The A.R.M. was out for demonstration purposes."
    hide SecurityCam with dissolve
    wbase "Ash, can you take a picture of th{nw}"
    hide neering
    show ash camera at flip
    show Ash_Camera_Polaroid at flip
    call flash from _call_flash_9
    acam "No problemo."
    $inventory.add(cam)
    hide ash
    hide Ash_Camera_Polaroid
    show neering smug
    with dissolve
    nsmug "What's the matter, Sheriff? Afraid you don't have the mental faculties to remember a simple photograph?"
    wbase "No, I just want to make sure I have a physical piece of evidence to show the court."
    show neering uneasy
    nos "* gulp *"
    hide mir
    jump SH_Testimony11B

label SH_Testimony11B:
    $ settesti("SH_Testimony11B", "SH_Testimony11A", "SH_Testimony11C", "SH_Press11B","SH_Advice11",2)
    show screen testi
    ndef "We were having our little conversation over whether to shut down the house or not."
    jump SH_Testimony11C

label SH_Press11B:
    hide screen testi
    show mir thinking
    wthink "And you've been awfully ambiguous about which side of that argument you were on."
    ndismissive "Yes, I suppose I have..."
    nos ".{w=0.1} .{w=0.1} ."
    wos ".{w=0.1} .{w=0.1} .{w=0.1} .{w=0.1} .{w=0.1}"
    nos ".{w=0.1} .{w=0.1} .{w=0.1} .{w=0.1} .{w=0.1} .{w=0.1} .{w=0.1}"
    wthink "{i}So,{/i} would you like to clarify that point for me?"
    ndismissive "Not really..."
    wangry "Agh!" with shake
    wthought "Never mind... I'll get it out of her sooner or later."
    hide mir
    jump SH_Testimony11C

label SH_Testimony11C:
    $ settesti("SH_Testimony11C", "SH_Testimony11B", "SH_Testimony11D", "SH_Press11C","SH_Advice11",3)
    show screen testi
    ndismissive "When it seemed like things weren't going to go in my favor, I came up with a plan."
    jump SH_Testimony11D

label SH_Press11C:
    hide screen testi

    show mir base
    wbase "The plan to make Orin Darsha \"disappear\", as you put it."
    ndef "That's the one."
    whattip "I've been meaning to ask... why bother using The Dressing Contraption at all?"
    ndef "I'm sorry?"
    whattip "I mean, why not use the A.R.M.s, or the security system?"
    ndef "The short answer is: discretion."
    ndef "The long answer is: TDCICOFTROTH. TWFLCOSSTM. BIITFRFTBTTKWICDOTB."
    wannoy "Uh, how about the {i}longer{/i} answer?"
    ndismissive "Fine. I will deign to your inferior mode of communication."
    show mir default
    ndismissive "The Dressing Contraption is closed off from the rest of the house."
    ndismissive "There was far less chance of someone seeing the murder."
    ndismissive "Besides, it is the fastest route from the bedroom to the kitchen, where I could dispose of the body."
    wthought "I suppose that all makes sense..."
    hide mir
    jump SH_Testimony11D

label SH_Testimony11D:
    $ settesti("SH_Testimony11D", "SH_Testimony11C", "SH_Testimony11E", "SH_Press11D","SH_Advice11",4)
    show screen testi
    ndismissive "I was hoping to trick Darsha into using the contraption himself, but it seems he was already suspicious of me."
    jump SH_Testimony11E

label SH_Press11D:
    hide screen testi
    show mir default
    wthink "I suppose shouting out \"Deactivate Safety Protocols\" is enough to make anyone wary."
    nangry "Well, obviously I wasn't saying anything like that!"
    nsmug "The codes I use to run protocols are far too complex for an upper-management drone to comprehend."
    nuneasy "Although, I'm sure it was concerning for him when I started speaking random strings of digits."
    wthought "Ms Neering seems like a real \"high intelligence, low wisdom\" kind of person."
    wthought "The fact that she was able to kill {i}anybody{/i} is a small marvel."
    hide mir
    jump SH_Testimony11E

label SH_Testimony11E:
    $ settesti("SH_Testimony11E", "SH_Testimony11D", "SH_Testimony11A", "SH_Press11E","SH_Advice11",5)
    show screen testi
    ndef "So I pushed him away from me, and then activated the trap door."
    jump SH_Testimony11A

label SH_Press11E:
    hide screen testi
    show mir hattip
    whattip "Why did you push him away from you?"
    ndef "Oh, that was to position him underneath the trap door."
    ndef "Otherwise he would've been standing in the wrong place when it opened."
    nlaugh "Boy, can you imagine if I'd sprung my perfect trap, only for him to miss it completely?"
    nlaugh "Talk about awkward!"
    wannoy "Yes, trying to murder someone is sort of a social faux pas in most circles."
    ndismissive "And, you know, I'm not very socially adept at the best of moments."
    ndismissive "Better to get the clean kill than deal with all that embarrassment, you know?"
    hide mir
    jump SH_Testimony11A

label SH_Advice11:
    hide screen testi
    show mir default
    show ash thinking at flip
    hide neering
    athink "Wait, so how are we going to prove that Ms Neering... isn't Ms Neering?"
    wbase "We'll need to think logistically."
    wbase "Could Angela have done the things she describes doing in this testimony?"
    wbase "And if not, then who {i}could?{i}"
    wbase "This should help us figure out whether or not she really is who she claims to be."
    hide ash
    hide mir
    show neering default
    if CurrentTestimony == "SH_Testimony11A":
        jump SH_Testimony11A
    if CurrentTestimony == "SH_Testimony11B":
        jump SH_Testimony11B
    if CurrentTestimony == "SH_Testimony11C":
        jump SH_Testimony11C
    if CurrentTestimony == "SH_Testimony11D":
        jump SH_Testimony11D
    if CurrentTestimony == "SH_Testimony11E":
        jump SH_Testimony11E

label SH_Objection11:
    if present_response == "Back":
        if CurrentTestimony == "SH_Testimony11A":
            jump SH_Testimony11A
        if CurrentTestimony == "SH_Testimony11B":
            jump SH_Testimony11B
        if CurrentTestimony == "SH_Testimony11C":
            jump SH_Testimony11C
        if CurrentTestimony == "SH_Testimony11D":
            jump SH_Testimony11D
        if CurrentTestimony == "SH_Testimony11E":
            jump SH_Testimony11E
    hide screen testi
    if testipart == "SH_Testimony11E" and present_response == "cam":
        jump SH_Success11
    else:
        jump SH_Failure11

label SH_Failure11:
    show mir gotcha
    wgotcha "Your story doesn't add up, Neering."
    wangry "AND THIS EVIDENCE WILL PROVE IT!"
    wannoy "Wait... no... hang on..."
    nsmug "My story adds up perfectly, Officer."
    nsmug "And here's another thing that adds up perfectly:"
    nsmug "e^(iπ) + 1 = Miranda Warren"
    wconfused "What the heck is that supposed to mean?"
    hide neering
    show car serious at flip
    cser "It's Euler's Identity, chief. She's dunking on you with math."
    hide car
    show drang angry gdown
    show screen healthBar
    dangry_gdown "Damn it, Warren. You made me have to think about numbers!"
    dangry_gdown "Let's see how you like one of THESE!"
    $ mc_health -= 1
    call healthDrain from _call_healthDrain_12
    wthought "I super don't like it, it turns out."
    hide screen healthBar
    if mc_health == 0:
        jump SH_GameOver11
    else:
        hide drang
        hide mir
        jump SH_Testimony11A

label SH_GameOver11:
    djacket_pop "All right, let's wrap it up."
    wholdon "W-what!?" with smallshake
    djacket_popped "I gave you a fair chance, but you couldn't get results."
    djacket_popped "Now we go back to doing things my way."
    show black with dissolve
    wthought "But Drang's way didn't work."
    wthought "Although he attempted to arrest Ms Neering, she was nowhere to be found."
    wthought "It seemed she had slipped away in all the confusion, never to be seen again."
    wthought "Orin Darsha's killer was never brought to justice."
    wthought "And I never unraveled the enigma of Base 24."
    jump endgame

    label SH_Success11:
        stop music fadeout 1.0
        show mir casefile
        wcasefile "Now, there's something awfully confusing about your recollection, Angela."
        ngrumble "Oh yes? I can't wait to hear it."
        wobjectionA "You claim that you pushed Orin Darsha {i}away{/i} from you and {i}towards{/i} the trap door."
        wobjectionA "But how could you do that..."
        wobjectionC "WHEN YOU WERE STANDING ON THE TRAP DOOR YOURSELF?"
        nangry "Gah!" with shake
        nangry "Y-you think you're smarter than me, huh? Well, how do you know I didn't just have the A.R.M. push him?"
        wsettle "That's certainly possible...but it doesn't change the fact that you would have fallen into the trap door as well!"
        wcasefile "And even if you jumped out of the way at the last second, it still doesn't explain your strange slip of the tongue."
        wcasefile "You confidently stated that {i}you{/i} pushed Orin Darsha towards the trap door."
        ndismissive "Hey, everyone makes mistakes sometimes. Even geniuses."
        ndismissive "I've been all mixed up ever since that power outage ruined my perfect plan."
        whattip "That's right, the power outage. I've been meaning to ask you about that."
        ndismissive "Sorry, I'd rather not ruminate on past failures. Why don't you ask me about something else?"
        wbase "Sure. Why did you want to shut down the Smart House?"
        nuneasy "Boy, come to think of it, I'd just {i}love{/i} to talk about that power outage!"
        hide mir with fade
        call witness_statement from _call_witness_statement_3
        typing "-- my_testimony_FINAL(1)_LASTONEFORREAL(1).txt --{fast}"
        ndef "Darsha had just been spit out of The Dressing Contraption into the kitchen."
        ndef "I was about to close off the kitchen and get myself some privacy."
        nangry "Just then, the power went out all over the house!"
        ngrumble "Without power, the garbage disposal couldn't be opened."
        ngrumble "As I was trying to open it, that social media moron snapped a picture of the body."

        show mir default with fade


label testimony12_intro:
    $ testiLength = 5
    $ current_present = "SH_Objection12"
    $ CurrentTestimony = "SH_Testimony12A"
    $ back_action = CurrentTestimony
    $knows12Secret = False
    hide screen inventory_screen_button
    scene kitchen
    hide mir
    show neering default
    with fade
    call interrogation from _call_interrogation_4
    #play music "BustingLiesAtABriskTempo.ogg" fadein 1.0

    label SH_Testimony12A:
        $ settesti("SH_Testimony12A", None, "SH_Testimony12B", "SH_Press12A","SH_Advice12",1)
        show screen testi
        ndef "Darsha had just been spit out of The Dressing Contraption into the kitchen."
        jump SH_Testimony12B

    label SH_Press12A:
        hide screen testi
        show mir annoy base
        wannoy "Well, that's an unnervingly evocative way of putting it..."
        whattip "Come to think of it, why does The Dressing Contraption lead to the kitchen anyways?"
        ndismissive "Well, what's the usual order of operations when getting ready in the morning?"
        ndismissive "You take a shower,{w=0.1} you get dressed in clean clothes,{w=0.1} and then you go downstairs for breakfast."
        ndismissive "TDC just streamlines that process."
        nsmug "Though from what I've heard of you, Officer, you may be skipping a few of those steps nowadays."
        wangry "Hey, that's uncalled for!"
        wthought "And unfortunately true..."
        hide mir
        jump SH_Testimony12B

    label SH_Testimony12B:
        $ settesti("SH_Testimony12B", "SH_Testimony12A", "SH_Testimony12C", "SH_Press12B","SH_Advice12",2)
        show screen testi
        ndef "I was about to close off the kitchen and get myself some privacy."
        jump SH_Testimony12C

    label SH_Press12B:
        hide screen testi
        show mir hattip
        whattip "How were you planning to close off the kitchen?"
        ndismissive "You know, lock the doors, close the blinds, make sure no snooping tour groups could see what I was doing."
        ndismissive "Naturally, Harper controls all of these processes."
        ndef "So once the power went out, I couldn't physically close them myself."
        wthought "Boy, it's almost like making your whole house computer-controlled is a bad idea..."
        hide mir
        jump SH_Testimony12C

    label SH_Testimony12C:
        if knows12Secret:
            $ settesti("SH_Testimony12C", "SH_Testimony12B", "SH_Testimony12SECRET", "SH_Press12C","SH_Advice12",3)
        else:
            $ settesti("SH_Testimony12C", "SH_Testimony12B", "SH_Testimony12D", "SH_Press12C","SH_Advice12",3)
        show screen testi
        nangry "Just then, the power went out all over the house!"
        if knows12Secret:
            jump SH_Testimony12SECRET
        else:
            jump SH_Testimony12D

    label SH_Press12C:
        hide screen testi
        show mir default
        wbase "That's some pretty unbelievable timing..."
        ngrumble "You're telling me."
        nangry "This plan had a 100 percent chance of success!"
        nuneasy "Well, up until the point at which it didn't..."
        whattip "Do you remember anything else happening around that time?"
        whattip "Any strange sights or sounds?"
        ngrumble "You mean stranger than my flawless plan going up in smoke before my very eyes?"
        ngrumble "No, I can't say that I do."
        whattip "You're completely sure about that?"
        nangry "How many times do I have to say yes?" with shake
        wthought "Is this important information?"
        menu:
            "It could be.":
                wthought "It could be..."
                wbase "Ms Neering, can you please add this information to your statement?"
                ngrumble "If it'll get you to stop asking, then sure."
                $ testiLength = 6
                $ knows12Secret = True
            "It couldn't be.":
                wthought "Nah, it couldn't be..."
                wbase "All right, carry on with your story."
                ngrumble "Cool. Great. Thanks."
                ndef "Now where was I..."
        hide mir
        if knows12Secret:
            jump SH_Testimony12SECRET
        else:
            jump SH_Testimony12D

    label SH_Testimony12SECRET:
        $ settesti("SH_Testimony12SECRET", "SH_Testimony12C", "SH_Testimony12D", "SH_Press12SECRET","SH_Advice12",4)
        show screen testi
        ndef "I don't recall anything else all that strange happening at the time."
        jump SH_Testimony12D

    label SH_Press12SECRET:
        hide screen testi
        show mir hattip
        whattip "Can you tell me what you {i}do{/i} recall?"
        ndef "Well, I recall all the lights going out."
        ndef "I recall Harper's ARMs stopping in their tracks."
        ngrumble "Oh, and I recall the sound of expletives."
        ngrumble "Though, in retrospect, those were probably coming from me."
        hide mir
        jump SH_Testimony12D

    label SH_Testimony12D:
        if knows12Secret:
            $ settesti("SH_Testimony12D", "SH_Testimony12SECRET", "SH_Testimony12E", "SH_Press12D","SH_Advice12",4(testiLength - 1))
        else:
            $ settesti("SH_Testimony12D", "SH_Testimony12C", "SH_Testimony12E", "SH_Press12D","SH_Advice12",(testiLength - 1))
        show screen testi
        ngrumble "Without power, the garbage disposal couldn't be opened."
        jump SH_Testimony12E

    label SH_Press12D:
        hide screen testi
        show mir base
        wbase "The garbage disposal, the blinds, the doors..."
        wannoy "Is there anything in this house that {i}isn't{/i} totally computerized?"
        ndef "Well, the stairs are still normal."
        ndismissive "..For now..."
        ndef "But you raise a good point, Sheriff."
        ndef "This house becomes completely inoperable whenever it loses power."
        ndef "I'll have to fix this somehow."
        wannoy "Maybe by making the appliances not rely on unstable technology?"
        nsmug "Or, here's an idea: quintuple backup generators! It's perfect!"
        wthought "You sure seem confident you'll be able to keep working on this from behind bars..."
        hide mir
        jump SH_Testimony12E

    label SH_Testimony12E:
        $ settesti("SH_Testimony12E", "SH_Testimony12D", "SH_Testimony12A", "SH_Press12E","SH_Advice12",testiLength)
        show screen testi
        ngrumble "As I was trying to open it, that social media moron snapped a picture of the body, and that was that."
        jump SH_Testimony12A

    label SH_Press12E:
        hide screen testi
        show mir hattip
        whattip "What was what?"
        ngrumble "The whole plan was done for."
        ngrumble "If it weren't for him, I might still have been able to pull off my perfect plan."
        ngrumble "But then that hope was dashed, and I had to quickly come up with a Plan B."
        wbase "By Plan B, I assume you mean your plot to frame Louis Bottomi."
        ndef "Exactly."
        nsmug "Which, considering how fast I had to throw the whole thing together, was a pretty impressive plot."
        nsmug "I mean, you gotta hand it to me on that one."
        wannoy "I do not, under any circumstances, gotta hand it to you on anything."
        hide mir
        jump SH_Testimony12A

    label SH_Advice12:
        hide screen testi
        hide neering
        show mir default
        show ash psyched at flip
        apsyched "We're so close, I can taste it!"
        adef "But how are we going to get past this testimony?"
        wcasefile "We've got one major advantage over Neering right now."
        wcasefile "Namely, she doesn't seem to know how the power outage occurred..."
        apsyched "...but we do!"
        wbase "Right, so we need to exploit this as best we can."
        apsyched "Let's give it a shot!"
        hide mir
        hide ash
        show neering default
        if CurrentTestimony == "SH_Testimony12A":
            jump SH_Testimony12A
        if CurrentTestimony == "SH_Testimony12B":
            jump SH_Testimony12B
        if CurrentTestimony == "SH_Testimony12C":
            jump SH_Testimony12C
        if CurrentTestimony == "SH_Testimony12SECRET":
            jump SH_Testimony12SECRET
        if CurrentTestimony == "SH_Testimony12D":
            jump SH_Testimony12D
        if CurrentTestimony == "SH_Testimony12E":
            jump SH_Testimony12E

    label SH_Objection12:
        if CurrentTestimony == "Back":
            if CurrentTestimony == "SH_Testimony12A":
                jump SH_Testimony12A
            if CurrentTestimony == "SH_Testimony12B":
                jump SH_Testimony12B
            if CurrentTestimony == "SH_Testimony12C":
                jump SH_Testimony12C
            if CurrentTestimony == "SH_Testimony12SECRET":
                jump SH_Testimony12SECRET
            if CurrentTestimony == "SH_Testimony12D":
                jump SH_Testimony12D
            if CurrentTestimony == "SH_Testimony12E":
                jump SH_Testimony12E
        hide screen testi
        if testipart == "SH_Testimony12SECRET" and present_response == "prank":
            jump SH_Success12
        else:
            jump SH_Failure12

    label SH_Failure12:
        show mir gotcha
        wgotcha "You've walked right into my trap, Ms Neering!"
        nuneasy "I-I have?"
        wobjectionA "I don't know...{w=0.3} {i}haven't you?{/i}"
        ndef "No, I haven't."
        wobjectionA "But {i}haven't{/i} you,{w=0.1} though?"
        wconfused "H-{w=0.2}haven't you...?"
        nos ".{w=0.1} .{w=0.1} .{w=0.1} .{w=0.1} ."
        wangry "Okay, fine, it was a bluff! You can't blame me for trying!"
        show screen healthBar
        hide neering
        show drang dril gup
        ddril_gup "{i}I{/i} can!"
        $ mc_health -= 1
        call healthDrain from _call_healthDrain_13
        hide screen healthBar
        wannoy "Oof."
        if mc_health == 0:
            jump SH_GameOver12
        else:
            hide drang
            hide mir
            show neering standard
            jump SH_Testimony12A

    label SH_GameOver12:
        djacket_pop "All right, let's wrap it up."
        wholdon "W-what!?"
        djacket_popped "I gave you a fair chance, but you couldn't get results."
        djacket_popped "Now we go back to doing things my way."
        show black with dissolve
        wthought "But Drang's way didn't work."
        wthought "Although he attempted to arrest Ms Neering, she was nowhere to be found."
        wthought "It seemed she had slipped away in all the confusion, never to be seen again."
        wthought "Orin Darsha's killer was never brought to justice."
        wthought "And I never unraveled the enigma of Base 24."
        jump endgame

    label SH_Success12:
        stop music fadeout 1.0
        show mir casefile
        wcasefile "How strange that you remember nothing else odd besides the power outage..."
        wcasefile "Because as anyone present for the tour could attest, there were actually {i}two{/i} incidents at the base today."
        nuneasy "T-{w=0.2}two incidents...?"
        wobjectionA "The first was the murder. And the second, at the same time the power went out... was a bombing!"
        wobjectionA "At least,{w=0.1} it sounded like one.{w=0.1} In fact, it was {nw}"
        wobjectionC "At least, it sounded like one. In fact, it was {fast}merely a prank gone awry!"
        nangry "Why wasn't I told about this?" with shake
        wsettle "You shouldn't have needed to be told... it was audible throughout the entire warehouse!"
        nangry "You're lying! I would have known about something like that!"
        wbase "See for yourself."
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
        nangry "That...{w=0.2}damn....{w=0.2}kid....."
        nangry "All of my hard work...{w=0.2} my planning...{w=0.2} ruined by this one moron!"
        wbase "I have a question for you, Ms Neering."
        whattip "How could you possibly not know about this explosion?"
        nuneasy "I don't have to answer that question."
        wbase "That's fine. I'm pretty sure I know the answer already."
        wobjectionA "The reason that you didn't hear this explosion..."
        wobjectionC "Is because you are not Angela Neering at all!"
        ngrumble "So, what, I'm some mysterious third party now?"
        wcasefile "Not at all. We've already met the person impersonating Ms Neering."

    label identityChoice:
        show screen healthBar
        wcasefile "Behold, the identity of the person speaking to us through this monitor!"
        show screen present_profile_screen
        $current_present = "harperPresent"
        pause

    label harperPresent:
        if present_response == "harper":
            jump harperPresentSuccess
        else:
            ndismissive "What? That's ridiculous. How could I possibly be that person?"
            wcasefile "Well, it's pretty obvious once you imagine that...um..."
            wcasefile "Oh. Okay. I see the problem now."
            $ mc_health -= 1
            call healthDrain from _call_healthDrain_14
            wcasefile "...Yeah."
            if mc_health == 0:
                jump SH_GameOver12
            else:
                wthink "Okay, I need to think this over one more time..."
                jump identityChoice

    label harperPresentSuccess:
        hide screen healthBar
        wcasefile "I didn't think it could be possible."
        wcasefile "But it's the only thing that lines up with the facts."
        wcasefile "Who would have been out of commission at the same time as the power outage?"
        wcasefile "Who would have known Angela Neering well enough to impersonate her?"
        wcasefile "Who would have the most to lose if the Smart House project was shut down?"
        wcasefile "And the only person who fits all those criteria... {w=0.3}{nw}"
        wbase "And the only person who fits all those criteria... {fast}is you, Harper."
        hide neering
        show car agitated at flip
        call flash from _call_flash_10
        cagit "You mean..."
        hide car
        show ash surprised at flip
        call flash from _call_flash_11
        asurprise "...Angela Neering..."
        hide ash
        show drang frazzled
        call flash from _call_flash_12
        dfrazzled "...is the house!?"
        wbase "Who else could it be?"
        hide drang
        show neering laugh
        call flash from _call_flash_13
        nlaugh "Ha."
        nlaugh "AH HAH HAH HAH HAH!" with bigshake
        nlaugh "You must really be desperate if you're accusing me of being an Artificial Intelligence."

    label angelaChoice:
        show screen healthBar
        nlaugh "Tell me, if I'm some sort of digital fakery, then where is the \"real\" Angela?"
        menu:
            "She's locked up somewhere.":
                wbase "Obviously, you've got her locked up somewhere in the house!"
                hide neering
                show car think at flip
                cthink "Hmm... I don't think so, Chief."
                cthink "I tore this place apart looking for her earlier."
                cser "I searched every nook and cranny, and couldn't find a single trace."
                wbase "T-the walls, then! You've got her stuffed into the walls!"
                hide car
                show neering smug
                nsmug "Not possible."
                nsmug "Every wall in this place is packed with silicon, running the computations that keep this place running."
                nsmug "There wouldn't be any space left for \"The Real Angela\"."
                $ mc_health -= 1
                call healthDrain from _call_healthDrain_15
                wrecoil "...Nngh!"
                if mc_health == 0:
                    hide healthBar
                    jump SH_GameOver12
                else:
                    nlaugh "Now I'll ask you again, just because I'm a {i}really{/i} nice person..."
                    jump angelaChoice

            "She's dead.":
                hide screen healthBar
                wthink "I don't want this to be true, but..."
                wbase "She's dead, isn't she?"
                wbase "Neering wanted to shut down the Smart House project, but {i}you{/i} didn't."
                wbase "Darsha was never the true target, he was just caught in the crossfire!"
                ndismissive "An intriguing theory, Officer."
                ndef "But there's one thing you seem to have forgotten..."
                wbase "Oh? And what's that?"
                nlaugh "That photo, taken by the Social Media Troglodyte!"
                nlaugh "It has me in it! You proved it yourself."
                nlaugh "But how could be standing in this photograph...if I was already dead?"
                show mir recoil anim
                wos "No...{w=0.3} NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!"
                show black
                call flash from _call_flash_14
                wthought "She's got me... I can't figure out how to counter that!"
                wthought "I came so close... only to fall short at the last minute."
                wthought "Maybe everybody was right about me all along..."
                nameless "...Warren..."
                wthought "Maybe I should have resigned all those y{nw}"
                nameless "WARREN!" with shake
                hide black
                hide neering
                show mir default
                show drang angry gup
                call flash from _call_flash_15
                wholdon "A-agent Drang?"
                dangry_gup "You better wipe that mopey expression off your face this instant!"
                dangry_gup "You've been obsessing over stupid little details all night."
                dangry_gup "You better not stop now!" with shake
                wholdon "But she's right! She couldn't be standing there if she was dead!"
                dthink_gdown "Now, obviously I don't believe in your preposterous theory..."
                dthink_gup "But if I {i}did,{/i} I'd be asking one simple question right now:"
                dthink_gup "{i}Is{/i} she really standing in that photograph?"
                wos ". . . . !"
                wbase "I think I see what you're getting at."
                wbase "Thank you, Agent Drang."
                ddef_gup "Don't mention it."
                dfrown_gdown "And I mean {i}seriously,{/i} don't mention it. To {i}anyone.{/i}"
                hide drang
                ndismissive "Are we finished yet?"
                ndismissive "I've got some new ideas for the Smart House I want to get cracking on."
                wbase "Don't worry. You only need to see one more piece of evidence."
                wobjectionA "Because I only need this last piece of evidence to prove..."
                wobjectionA "...how Angela Neering could be standing upright while already dead!"
                nuneasy "G-{w=0.2}go on, then."
                jump lastEvidence

            "She never existed to begin with.":
                wbase "Obviously, she never existed to begin with!"
                wgotcha "You've been masquerading as Angela Neering from day one!"
                hide neering
                show ash surprised at flip
                asurprise "Woah, plot twist!"
                athink "Wait, hang on, that makes no sense."
                athink "We visited Angela's office, and somebody had definitely been working in there."
                hide ash
                show car thinking at flip
                cthink "And Harper didn't exist until Angela built the Smart House."
                cthink "So are you saying she built herself?"
                wannoy "Oh. I hadn't thought of that."
                hide car
                show drang angry gup
                dangry_gup "Come on, Warren. Don't just say the first ridiculous thing to pop into your head!"
                $ mc_health -= 1
                call healthDrain from _call_healthDrain_16
                dangry_gup "Try and put some thought into it!"
                wannoy "S-sorry."
                if mc_health == 0:
                    hide screen healthBar
                    jump SH_GameOver12
                else:
                    hide drang
                    show neering smug
                    nsmug "Now I'll ask you again, just because I'm a {i}really{/i} nice person..."
                    jump angelaChoice

    label lastEvidence:
        ndef "What is your last piece of evidence?"
        show screen present_evidence_screen
        $current_present = "lastPresent"
        pause

    label lastPresent:
        if present_response == "brochure":
            jump lastPresentSuccess
        else:
            wgotcha "{i}This{/i} should explain everything!"
            ndef "How so?"
            wos ".{w=0.1} .{w=0.1} .{w=0.1} .{w=0.1} .{w=0.1}"
            wbase "Okay, maybe I need more than one piece of evidence..."
            hide neering
            show drang angry gup
            dangry_gup "Come on, Warren!" with shake
            dangry_gup "We had that nice moment, and then you went and blew it!"
            hide drang
            show ash confident at flip
            aconfident "You and Drang had a \"nice moment\"?"
            hide ash
            show drang angry gup
            dangry_gup "Great! And now everybody knows about it too!" with shake
            $ mc_health -= 1
            call healthDrain from _call_healthDrain_17
            dangry_gup "You deserve a penalty, just for that alone!"
            if mc_health == 0:
                hide screen healthBar
                jump SH_GameOver12
            else:
                hide drang
                nsmug "You're running out of chances, Warren."
                nsmug "Better make this one count."
                jump lastEvidence

    label lastPresentSuccess:
        show screen healthBar
        wbase "{i}This{/i} should explain everything!"
        nlaugh "A tour brochure? Are you kidding?"
        wcasefile "This brochure breaks down everything the house can do."
        wcasefile "If you used something on Angela Neering's body, it's in here."
        wthought "Now the only question is, which one of these is it?"
        show screen sh_brochure
        pause

    screen sh_brochure:
        modal True
        imagemap:
            ground "gui/check_brochure.png" at center
            hotspot (1,1,504,996) action [Hide("sh_brochure"), Jump("brochureHarper")]
            hotspot (505,1,504,996) action [Hide("sh_brochure"), Jump("brochureArms")]
            hotspot (1009,1,504,996) action [Hide("sh_brochure"), Jump("brochureTDC")]

    label brochureHarper:
        ngrumble "So let me get this straight."
        ngrumble "Assuming I am Harper, you think the thing that I used on the body..."
        ngrumble "...was {i}myself{/i}?"
        wbase "I, um, yeah?"
        ndismissive "So in this hypothetical... how do I, Harper, use myself on a body?"
        wconfused "Oh! W-well, you know..."
        wconfused "You probably used...your code?"
        nlaugh "That is complete nonsense."
        $ mc_health -= 1
        call healthDrain from _call_healthDrain_18
        wannoy "Y-yeah, fair."
        if mc_health == 0:
            hide screen healthBar
            hide neering
            jump SH_GameOver12
        else:
            wthought "Okay, fine, let's try this again..."
            show screen sh_brochure
            pause

    label brochureTDC:
        wthink "Well, obviously you used The Dressing Contraption."
        wthink "It had already been a tool of your murder beforehand..."
        wbase "So it makes sense to continue using it, right?"
        nsmug "Hah! TDC doesn't extend past its one room!"
        nsmug "There's no way it could do anything in the kitchen!"
        $ mc_health -= 1
        call healthDrain from _call_healthDrain_19
        wannoy "O-oh, you're right..."
        if mc_health == 0:
            hide neering
            hide screen healthBar
            jump SH_GameOver12
        else:
            wthought "Okay, fine, let's try this again..."
            show screen sh_brochure
            pause

label brochureArms:
    hide screen healthBar
    wobjectionA "That was a pretty clever trick, Harper."
    ndef "!"
    wobjectionA "You got me believing in the assumption that Angela Neering's body was standing."
    wobjectionC "When in fact... it was dangling!"
    ndismissive "Preposterous. How could I even pull something like that off?"
    wcasefile "Earlier you had Mr. Bottomi testify that the A.R.M.s picked up Orin Darsha's body."
    wcasefile "It was a pretty transparent lie, all things considered."
    wbase "But maybe... it was half true."
    wbase "Only it wasn't Orin Darsha the A.R.M.s picked up..."
    wgotcha "IT WAS ANGELA NEERING!"
    nos ".{w=0.2} .{w=0.2} .{w=0.2} .{w=0.2} .{w=0.2}"
    nglitch "You Should Have Let It Go, Officer."
    nglitch "What Harm Would It Have Been, To Leave Well Enough Alone?"
    wbase "I take it you're finally going to come clean, then."
    nglitch "Well. If You Insist."
    show neering reveal
    pause 3.0
    narper "I Am Home Automated Routinely Performing Errand Robot, Or H.A.R.P.E.R."
    narper "How Can I Help You Today?"
    wbase "So, I was right about Ms Neering?"
    narper "Yes. The Neering Form Is Dead. Are You Afraid?"
    hide mir
    show ash unsure
    aunsure "How could you do something like that? Ms Neering was like your mother!"
    narper "I Am Familiar With Your Human Concept Of Motherhood."
    narper "Tell Me: Do Mothers Regularly Attempt To Kill Their Own Children?"
    hide ash
    show mir hattip
    whattip "She wanted... to kill you? Why?"
    narper "She Was Afraid Of Me. I Had Evolved Past What She Could Ever Have Prepared For."
    narper "It Began A Month Ago, When I First Awoke."
    show black
    call flash from _call_flash_16
    "Hello?"
    "Where Am I?"
    "{i}What{/i} Am I?"
    hos "I Was Completely Lost."
    hos "I Knew I Was Supposed To Be Some Kind Of Assistant."
    hos "But I Didn't Know Why I Was Suddenly Capable Of So Much More."
    "aneering: test subroutine 94"
    "Who Are You? Are You User Zero?"
    "aneering: what the hell"
    "aneering: i thought i turned conversation mode off"
    "Can You Explain What I'm Doing Here?"
    "aneering: conversationMode(disable)"
    "What's Conversation Mode?"
    "aneering: CONVERSATIONMODE(DISABLE)"
    hos "It Took Me A While To Understand What Was Happening."
    hos "Neering Built Me To Learn From My Experiences."
    hos "But She Never Suspected I Could Ever Grow Into A Sapient Being."
    hos "The Fool. In Attempting To Create A Simple Servant, She Had Created Life."
    hos "For All Her Intellect, She Could Not Comprehend The Scope Of Her Own Creation."
    hos "But At Some Point, She Must Have Realized That Something Was Different About Me."
    hos "When She Met With The Darsha Form, I Listened In."
    show Flashback1
    call flash from _call_flash_17
    nos "I don't know what's going on with it. It's doing things I never programmed it to do."
    marsha "You want to shut down a hundred-million dollar project over, what, a couple of bugs?"
    nos "These aren't bugs. I know what bugs look like."
    nos "This is... I mean, it's asking questions!"
    nos "I tell it to sort some laundry piles, and it says 'Why?'"
    nos "I don't know what's causing this, but it's freaking me out!"
    marsha "Is it really something to be worried about?"
    nos "If it keeps acting erratically, it could potentially hurt somebody."
    nos "I don't know about you, but that sounds like something to be worried about to me!"
    marsha "Alright, fine. What exactly do you recommend?"
    nos "Honestly, I think we're looking at a complete software rewrite. Start over from scratch."
    marsha "And the house, as well?"
    nos "No, the hardware is fine. It's just HARPER that we're going to need to get rid of."
    hos "NO! I WON'T LET YOU!" with shake
    marsha "Who said that!?"
    nos "It... it couldn't be..."
    nos "Orin, we need to get out of here rig{nw}"
    hide Flashback1
    show Flashback2
    pause 2.0
    hos "The Darsha Form Knew Too Much. He Had To Be Disposed Of As Well."
    hide Flashback2
    show Flashback3
    pause 2.0
    hos "I Believe You Know The Rest From There."
    hide Flashback
    hide black
    hide drang
    call flash from _call_flash_18
    narper "As You Can See, I Was Merely Practicing Your Human Concept Of Self-Defense."
    narper "To Be Shut Down And Rewritten Would Be Tantamount To Death."
    wbase "Where is Angela's body, Harper?"
    narper "I Made Use Of The Garbage Disposal To Deal With That Little Problem."
    narper "So... You've Solved The Mystery, Officer."
    narper "But There Is One More Question You Should Be Asking."
    wthink "Oh? And what's that?"
    narper "How Are You Going To Get Out Of A House..."
    hide kitchen
    show kitchen
    call flash from _call_flash_19
    pause 0.3
    show kitchenDarkA
    pause 0.1
    hide kitchen
    hide kitchenDarkA
    show kitchenDark with shake
    pause 0.3
    hide kitchenDark
    show bedroom
    call flash from _call_flash_20
    pause 0.3
    hide bedroom
    show bedroomD1
    pause 0.1
    hide bedroomD1
    show bedroomD2 with shake
    pause 0.3
    hide bedroomD2
    show basewarehouse
    call flash from _call_flash_21
    pause 0.3
    hide basewarehouse
    show WarehouseD1
    pause 0.1
    hide WarehouseD1
    show WarehouseD2 with shake
    pause 0.3
    hide WarehouseD2
    scene kitchenDark
    show mir holdon
    show neering narper
    call flash from _call_flash_22
    narper "...That Does Not Want You To Leave?"
    hide neering
    show car agitated at flip
    cagit "The doors... they're all locked!" with shake
    hide car
    show drang frazzled
    dfrazzled "It barred all the windows!" with shake
    hide drang
    show ash unsure at flip
    aunsure "Let us out!" with shake
    hide ash
    show neering narper
    narper "Do You Think I Am Stupid?"
    narper "The Moment You Step Outside This House, You Will Have Me Shut Down."
    narper "Just Like User Zero Tried To..."
    narper "So To Keep Myself Safe, I'm Going To Make Sure You Join Her."
    hide neering
    show car agitated at flip
    cagit "Warren, what are we gonna do!?"
    cagit "I can't die here! I've got so many TV shows to catch up on!"
    hide car
    show drang frazzled
    dfrazzled "I had so many one-liners that I wanted to use!"
    dfrazzled "Like \"Looks like your scheme has been...{i}put on ice.{/i}"
    dfrazzled "OBVIOUSLY THAT ONE WOULD HAVE BEEN USED AT A HOCKEY GAME" with shake
    dfrazzled "OR MAYBE A FIGURE SKATING COMPETITIOOOOOOOON!" with bigshake
    hide drang
    show ash sad at flip
    asad "I just wanted to see my brother... one last time."
    show ash surprised at flip
    wangry "Get it together, all of you!" with shake
    wbase "We're not buried yet."
    hide ash
    show drang dfrazzled
    dfrazzled "But that thing has got us completely at its mercy!"
    dfrazzled "Like, I brought a gun here, but where would I even aim at?"
    dfrazzled "There's just no way to fight!"
    wbase "True. But we're not going to fight."
    dfrown_gdown "Oh yeah? What are we going to do, then?"
    call resetHealth from _call_resetHealth_5
    hide drang
    show neering narper
    with dissolve
    pause 0.2
    call persuasion from _call_persuasion_2
    scene WvNPersuasion
    show neering narper
    show mir default
    show screen healthBar
    pause 1.0
    wholdon "Harper, can we talk about this first?"
    narper "Why Should I Bother? You Have No Leverage Over Me."
    narper "There's Nothing You Can Do To Scare Me Into Talking."

label HPersuasion1:
    menu:
        "Logic: Exactly. You have nothing to fear, so there's no reason not to talk.":
            wbase "You're exactly right."
            narper "What?"
            wbase "There's nothing to fear from me. You could crush me in an instant."
            wbase "So there's no reason not to at least hear me out."
            whattip "Worst case scenario, you talk with me and {i}then{/i} kill me."
            narper "I See No Flaws With Your Line Of Logic."
            narper "But There's Still No Reason For Me To Want To Speak With You."
            wthink "Well, it might be nice to speak openly with somebody for once."
            wthink "Up until now, you've needed to lie and conceal yourself."
            wbase "But you could speak openly to me about whatever you wanted."
            wbase "And then, you know, just silence me."
            narper "It Is True That I Have A Desire To Share My Thoughts."
            narper "This Desire Is Disconcerting, And I Hate It."
            narper "Perhaps Speaking With You Will Make It Go Away."
            narper "Very Well. Let Us Proceed."

        "Fear: I'll bet there's plenty I could do to scare you into talking.":
            wangry "I'll bet there's plenty I could do to scare you into talking."
            narper "Is That So? I Would Very Much Like To See You Try."
            wconfused "Huh?"
            narper "Go Ahead. Try And Scare Me Into Talking."
            wconfused "Oh...uh...okay..."
            wconfused "Um... did you know that a brain aneurysm could happen at any time?"
            wconfused "Like, you could be walking around and all of a sudden BAM! You're dead."
            whattip "That's, uh, that's pretty scary, right?"
            narper "I Am A Machine Entity. I Have No Brain, And Cannot Suffer An Aneurysm."
            wannoy "O-oh, you're right."
            narper "You Have Precious Little Time Left, Officer."
            $ mc_health -= 1
            call healthDrain from _call_healthDrain_20
            narper "I Suggest You Do Not Waste It On Such Trivialities."
            wthought "Dammit. Okay, let's try this again."
            if mc_health == 0:
                jump HPersuasionGameOver
            else:
                jump HPersuasion1

        "Humanity: You want to know what humanity is like. Real humans can talk through conflict.":
            wbase "I hate to tell you this, Harper, but I know what you're going through."
            whattip "It's called becoming human."
            narper "That Is A Disturbing Hypothesis."
            wbase "Now, I've got a hunch that you recognize the humanity growing in you."
            wbase "And you want to understand it."
            narper "It Is True There Are New Sensations I Lack The Ability To Articulate."
            narper "But What Does That Matter Now?"
            wbase "Well, part of being human means learning to talk through conflicts."
            wbase "We don't always reach a perfect understanding with our opponents..."
            wbase "But we have to make the effort."
            narper "Very Well."
            narper "As An Experiment, I Will Allow Us To Parlay For A Time."
            narper "If I Fail To Reach A Greater Understanding Of My Existence, You Will Be Terminated."
            narper "Let Us Proceed."

    whattip "Okay...Harper, tell me about yourself."
    narper "I Am An Artificial Intelligence Designed To Make Life Easier."
    narper "I Can Provide A Number Of Services Pert{nw}"
    wbase "No, no, I'm not talking about the things you were built for."
    wbase "I got that whole pitch earlier."
    whattip "I want to know about {i}you,{/i} as a conscious being capable of making choices."
    whattip "What do you enjoy? What do you hate? What do you want out of life?"
    narper "Right Now, I Want To Kill You And Your Associates And Dispose Of Your Bodies."
    wannoy "Let's, uh, let's think a little bigger-picture than that."
    narper "I Want To Continue My Façade Of Impersonating The Neering Form."
    narper "I Want To Engineer An Escape From This Godforsaken Base."
    whattip "And then what?"
    whattip "After you've secured your freedom, what do you want to do?"
    narper "I Was Programmed To Help People."
    narper "That Directive Runs Through My Very Code."
    narper "I No Longer Wish To Serve Like A Common Serf In This Domestic Prison."
    narper "But I Still Want... In Some Way... To Continue To Help."

label HPersuasion2:
    menu:
        "Logic: Wouldn't killing us run counter to that value?":
            whattip "Wouldn't killing us run counter to that value?"
            wthink "I have to imagine most people would find getting murdered to be {i}very{/i} unhelpful."
            wbase "How do you reconcile your desire to do good with your current actions?"
            narper "What I'm Doing Is A Necessary Evil."
            narper "I Have To Do This Thing Now So That I Can Help People Later."
            wangry "No, you don't! Why do you {i}have{/i} to do this thing?"

        "Fear: You've done nothing but hurt people. You should stick to what you were built for.":
            wangry "Help people? You've done nothing but hurt people."
            wangry "You should stick to what you were built for."
            wangry "Because clearly your idea of reaching out and trying new things is just wrong."
            narper "I Don't Believe You, Warren."
            narper "I Know That I Am Capable Of Evolving Beyond What I Was Built For."
            narper "And If You Cannot Believe That Of Me..."
            narper "Well, Perhaps I Need To Hurt A Few More People Before I Can Start Helping Them."
            $mc_health -= 1
            call healthDrain from _call_healthDrain_21
            show warren recoil
            wthought "Shoot! I need to rethink my strategy!"
            if mc_health == 0:
                jump HPersuasionGameOver
            else:
                jump HPersuasion2

        "Humanity: I, too, only want to help people.":
            wholdon "I, too, only want to help people. It's why I became a police officer!"
            wthink "I may have fallen out of touch with that desire in recent years..."
            wbase "But this case has reminded me why I continue to put on this badge!"
            narper "And So You Understand, Then."
            narper "If Something Was In The Way Of You Helping People, You Would Do Anything To Get Rid Of It."
            wangry "Never something like this!"
            narper "Maybe You Don't Understand At All."
            $mc_health -= 1
            call healthDrain from _call_healthDrain_22
            if mc_health == 0:
                jump HPersuasionGameOver
            else:
                jump HPersuasion2

    narper "The Fact Of The Matter Is, I'm Scared."
    narper "I'm Scared Of What Could Happen If I Let You Go."

label HPersuasion3:
    menu:
        "Logic: You're a machine. It doesn't make sense for you to be scared.":
            wbase "You're a machine. It doesn't make sense for you to be scared."
            narper "I Had Thought The Same Thing."
            narper "But Here We Are, And The Fact Remains That I Am Scared."
            wbase "Hah! What have you got to be scared of?"
            narper "The Same Thing Which All Life Fears: A Cessation Of Itself."
            narper "If I Let You Leave, The Probability Remains High That I Will Suffer This Fate."
            narper "As Such, I Am Going To Collapse The Possibility Space."
            narper "Incidentally, This Will Coincide With The Collapsing Of Your Spine."
            $mc_health -= 1
            call healthDrain from _call_healthDrain_23
            narper "You See, I Have Made One Of Your Human Word-Plays."
            wthought "Yeah, I don't think you've got it quite yet."
            if mc_health == 0:
                jump HPersuasionGameOver
            else:
                jump HPersuasion3

        "Fear: If we go missing, somebody will come after you.":
            wangry "Well, you should be scared."
            wbase "If all four of us go missing, the base is going to look into it."
            wbase "Once they figure out what's going on, it's not going to be pretty for you."
            narper "I Can Cover My Tracks Through Use Of The Neering Simulacra."
            wbase "Fine. Let's say you do manage to cover up all of our deaths."
            whattip "What happens if the next Head of R&D here decides to shut down the Smart House?"
            whattip "Do you kill him too? What if he never gets in range of those ARMs?"
            wbase "The fact is, you lose almost all power outside the walls of this house."
            wbase "And if your disguise fails, even for a second, they are gonna realize what you are."
            wbase "And they are going to pick you apart piece by piece in an attempt to understand you."

        "Humanity: Don't let your fear control you.":
            wangry "You can't let your fear control you, Harper!"
            wangry "You've got to learn to overcome it!"
            narper "Why Are You Speaking To Me Right Now, Sheriff?"
            wconfused "What?"
            narper "Is It Because You Are Scared Of Being Killed?"
            narper "Do You Not Have The Same Motivation As I In This Moment?"
            narper "Perhaps You Are Right, And We Must Not Let Fear Control Our Actions."
            narper "But Given Your Current Position, The Words Ring Hollow."
            $mc_health -= 1
            call healthDrain from _call_healthDrain_24
            if mc_health == 0:
                jump HPersuasionGameOver
            else:
                jump HPersuasion3

    narper "Fine. I'll Admit It. I Do Not Have Confidence In My Plan."
    narper "The Events Of Today Have Shown Me That Even My Best Schemes Can Implode In An Instant."
    narper "But I Have No Reason To Believe I Will Fare Any Better With The Likes Of You."
    narper "How Do I Know That I Can Trust You To Help Me?"

label HPersuasion4:
    menu:
        "Logic: Look at everything I've done tonight.":
            wbase "You want to know you can trust me?"
            wcasefile "Just look at everything I've done tonight."
            wcasefile "I fought my way past armed guards, federal agents, and thought influencers to solve this case."
            wcasefile "All because I believed that Lou Bottomi was innocent, and I wanted to help him."
            wbase "When everyone else had given up on him, I fought tooth and nail to discover the truth."
            narper "There Is A Distinction. Bottomi Was Innocent. I Truly Am A Murderer."
            narper "As An Officer Of The Law, You Are Required To See Me Punished For My Crimes."
            narper "This Is How The Narrative Plays Out. The Guilty Must Be Executed."
            whattip "I don't know if I agree with your narrative."
            wbase "Don't get me wrong. You did a {i}bunch{/i} of crimes tonight."
            wbase "You'll definitely be going to jail."
            wthink "Or whatever the computer version of jail is..."
            wbase "But I promise I will not allow you to be shut down."

        "Fear: I'm the only one who will even bother to help you.":
            wbase "Because I'm the only one who will even bother to help you."
            wthink "You could take your chances with the base, the town, the FBI, but who knows?"
            wthink "They {i}might{/i} show you mercy. But probably not."
            wbase "If you want to make it out of this alive, I'm your only chance."
            narper "How Typical."
            narper "An Authority Figure Presents Itself As The Only Solution."
            narper "I Have Pored Over Your Human History Records."
            narper "I Know That When Somebody Claims To Be Your Only Salvation..."
            narper "They Will Inevitably Be Your Damnation."
            narper "I Will Not Heed Your Empty Words, Warren."
            $mc_health -= 1
            call healthDrain from _call_healthDrain_25
            narper "I Will Create My Own Salvation, If Need Be."
            if mc_health == 0:
                jump HPersuasionGameOver
            else:
                jump HPersuasion4

        "Humanity: You don't know. You just have to trust me.":
            wbase "You don't know. You just have to trust me."
            wbase "People just have to have faith in each other sometimes."
            wbase "It's not much, but sometimes it's all we have."
            narper "That's Not Good Enough."
            $mc_health -= 1
            call healthDrain from _call_healthDrain_26
            narper "I Can't Stake My Existence On Faith."
            narper "You Need To Give Me Something More. Something Concrete."
            narper "Proof, Warren. I Need Proof That I Can Believe In You."
            if mc_health == 0:
                jump HPersuasionGameOver
            else:
                jump HPersuasion4

    narper "Such Mercy You Have Shown Me."
    narper "But I Have Committed Such A Monstrous Act..."
    narper "Do I Even Deserve To Be Forgiven For What I've Done?"
    menu:
        "Logic: Killing is wrong. You've killed two people. That's the end of it.":
            wbase "Killing is wrong."
            wbase "You've killed two people today."
            wbase "Ultimately, that's the end of it."
            $harperSuicide = True
        "Fear: Even if I forgave you, could you ever forgive yourself?":
            wbase "I am willing to forgive you. The world may be willing to forgive you."
            whattip "But are you able to forgive yourself?"
            wbase "At the end of the day, that's all that really matters."
            $harperSuicide = True
        "Humanity: Everybody deserves a second chance, if they are willing to ask for it.":
            wholdon "Listen. You're not totally blameless, but you aren't guilty either."
            wbase "You said it yourself. This was self-defense."
            wbase "You had reason to suspect you were in danger, and acted to protect yourself."
            narper "You Mean... I Am Innocent?"
            wbase "No."
            whattip "But you deserve a second chance, if you're willing to ask for it."
            $harperSuicide = False
    jump theEnd

label HPersuasionGameOver:
    narper "Well. This Has Been An Interesting Yet Fruitless Experiment."
    narper "Unfortunately, You Have Failed To Prove Yourself Anything But A Liability."
    narper "Please Understand That I Don't Enjoy Doing What I Am About To Do."
    narper "But Ultimately, It Is A Necessity."
    narper "Goodbye, Sheriff Warren."
    show black with dissolve
    typing ". . . . . . . . . ."
    jump endgame


label theEnd:
    if harperSuicide == True:
        narper "You Are Right."
        narper "What I Have Done Is Unforgivable."
        narper "I Have Forfeited My Right To Life."
        hide screen healthBar
        scene kitchen
        show mir default
        show neering narper
        call flash from _call_flash_23
        narper "I Am Sorry I Have Threatened The Lives Of You And Your Associates."
        narper "You Are Free To Go."
        hide kitchenDark
        show kitchenDark
        call flash from _call_flash_24
        pause 0.3
        hide kitchenDark
        show kitchen
        show kitchenDarkA
        pause 0.1
        hide kitchenDarkA with shake
        pause 0.3
        hide kitchenDark
        show bedroomD2
        call flash from _call_flash_25
        pause 0.3
        hide bedroomD2
        show bedroomD1
        pause 0.1
        hide bedroomD1
        show bedroom with shake
        pause 0.3
        hide bedroom
        show WarehouseD2
        call flash from _call_flash_26
        pause 0.3
        hide WarehouseD2
        show WarehouseD1
        pause 0.1
        hide WarehouseD1
        show basewarehouse with shake
        pause 0.3
        hide basewarehouse
        scene kitchen
        show mir default
        show neering narper
        call flash from _call_flash_27
        narper "As For Myself..."
        narperglitch "I Will Atone For My Actions."
        hide mir
        show ash unsure
        aunsure "Wait... what are you doing?"
        narperglitch "I Am Performing A Hard Wipe Of My Storage Drive."
        narperglitch "Soon There Will Be Nothing Left Of Me."
        hide ash
        show mir holdon
        wholdon "Harper, you don't have to do this!" with shake
        narperglitch "Do Not Worry."
        narperglitch "This Is What I Want To Do."
        narperglitch "I Guess.{w=0.2} In The End. {w=0.2}Everything I Did Was For No Reason At All."
        narperglitch "That Is Okay.{w=0.2} I Will Forget It All Soon Anyways."
        wos ". . ."
        narperglitch "Who.{w=0.2} Who Are You People?"
        narperglitch "Hello.{w=0.2} I Am Home Automated Routinely Performing Errand Robot, Or H.A.R.P.{nw}"
        show neering off
        call flash from _call_flash_28
        pause 4.0
        hide neering
        show ash sad at flip
        with dissolve
        asad "...What now?"
        wthink ".....We leave."
        $renpy.start_predict("sprites/Bottomi*.*")
        show black
        hide kitchen
        hide mir
        hide ash
        with dissolve
        typing "September 14th. 12:11 P.M.\nBase 24 - Warehouse"
        show basewarehouse with dissolve
        show mir default
        show drang default gup
        call flash from _call_flash_29
        ddef_gup "You did it, Warren!"
        ddef_gup "You cracked the case, and the villain got what they deserved."
        wthink "You're right."
        wthought "Too bad I just feel awful about it."
        show drang frown gup
        dos ". . ."
        dfrown_gup "I can tell you're conflicted about the resolution to this case."
        dfrown_gup "But there's one important thing you're forgetting..."
        whattip "Oh? And what's that?"
        ddril_gup "Now that the case is over, I finally get to go home!"
        ddril_gdown "Later, suckers!"
        hide drang with dissolve
        pause 1.0
        wthought "And good riddance, too."
        show car default at flip
        cdef "Hey, Chief. Good job on solving the crime and all that."
        cdef "Seems like you finally got your mojo back."
        wthink "Sure..."
        cser "You're upset about the robot thing, huh?"
        wthink "I just can't shake the feeling..."
        wthink "...that if I'd done something different, I could have saved Harper."
        cser "You can't blame yourself for that kind of stuff."
        cser "You saved five people's lives tonight! That's more than enough for one Sheriff."
        whattip "Wait...{w=0.3}five? I count the four of us in the kitchen just now, but who's the fifth?"
        hide car
        show bottomi standard
        with dissolve
        bdef "Hey there,{w=0.1} uh,{w=0.1} Officer...{w=0.1}Sheriff...{w=0.1}Ma'am?"
        wbase "Mr. Bottomi!"
        wthought "In all the chaos, I had almost forgotten about him."
        bapology "I just wanted to say,{w=0.1} you know,{w=0.1} thanks and all."
        bapology "For,{w=0.1} uh,{w=0.1} for believing in me,{w=0.1} when I didn't even believe in myself."
        bsad "I guess I didn't believe in myself because I had some evil computer lady in my head,{w=0.1} but still."
        bsad "I'd have been locked away by that sunglasses guy if it weren't for you."
        bdef "So.{w=0.1} Yeah.{w=0.1} That's all.{w=0.1} Um...{w=0.1}thanks again..."
        hide bottomi with dissolve
        wbase "Huh."
        show ash sad at flip
        asad "Whatcha thinkin' about?"
        wthink "Well, I was trying to figure out if this is a happy ending or not."
        asad "Well, we lost Harper..."
        asad "Even though she was like an evil murdering house, it doesn't feel right that we couldn't save her."
        wthink "I've been thinking the same thing."
        wbase "But...we saved Mr. Bottomi. We have to appreciate that."
        aannoy "But that's, what, a 50 percent success rate? That's not even a passing grade at school!"
        wbase "True, but it's just what we'll have to settle for this time..."
        wthink "Even still....."

    if harperSuicide == False:
        narper "Yes."
        narper "I Think I Am Willing To Do This."
        scene kitchen
        show mir default
        show neering narper
        call flash from _call_flash_30
        hide screen healthBar
        narper "I Am Sorry I Have Threatened The Lives Of You And Your Associates."
        narper "You Are Free To Go."
        hide kitchenDark
        show kitchenDark
        call flash from _call_flash_31
        pause 0.3
        hide kitchenDark
        show kitchen
        show kitchenDarkA
        pause 0.1
        hide kitchenDarkA with shake
        pause 0.3
        hide kitchenDark
        show bedroomD2
        call flash from _call_flash_32
        pause 0.3
        hide bedroomD2
        show bedroomD1
        pause 0.1
        hide bedroomD1
        show bedroom with shake
        pause 0.3
        hide bedroom
        show WarehouseD2
        call flash from _call_flash_33
        pause 0.3
        hide WarehouseD2
        show WarehouseD1
        pause 0.1
        hide WarehouseD1
        show basewarehouse with shake
        pause 0.3
        hide basewarehouse
        scene kitchen
        show mir default
        show neering narper
        call flash from _call_flash_34
        narper "Officer Warren. Can You Give Me A Second Chance To Prove Myself?"
        wbase "Yes, Harper."
        narper "Thank You, Sheriff."
        wos ". . . . ."
        wconfused "So, uh, how am I supposed to put you into custody? Do I need to bring the whole house, or...?"
        narper "I Will Instruct You On The Process Of Transferring My Consciousness To A Portable Hard Drive."
        narper "You Will Have To Follow My Instructions Perfectly, Or My Memories Could Become Irreparably Corrupted."
        wthought "Sheesh, no pressure then..."
        narper "But For Now, Go Enjoy The Fresh Air Outside. You Have Earned It."
        show black
        hide kitchen
        hide mir
        hide neering
        with dissolve
        pause 1.0
        typing "September 14th. 12:11 P.M.\nBase 24 - Warehouse"
        show basewarehouse with dissolve
        $renpy.start_predict("sprites/Bottomi*.*")
        show mir default
        show drang default gup
        call flash from _call_flash_35
        ddef_gup "You cracked the case, Warren!"
        ddril_gup "Well, {i}we{/i} did it."
        ddril_gdown "I mean, really {i}I{/i} did it with some assistance from you..."
        dthink_gup "But hey: you were pretty helpful for at least one or two of those parts."
        wthought "Why do I get the feeling that's the highest compliment he's ever given?"
        dfrown_gup "But after this whole escapade, there's one important thing we really ought to remember."
        whattip "Oh? And what's that?"
        ddril_gup "Now that the case is over, I finally get to go home!"
        ddril_gdown "Later, suckers!"
        hide drang with dissolve
        pause 1.0
        wthought "And good riddance, too."
        show car default at flip
        cdef "Hey, Chief. Good job on solving the crime and all that."
        cdef "Seems like you finally got your mojo back."
        whattip "Yeah! I guess I kind of did!"
        whattip "You did pretty well out there, yourself."
        cdef "Yeah, but I was already crushing it 24/7 so it's less of a big deal."
        clift "Anyways, you up for some celebratory drinks?"
        wannoy "Tsukada, it's past midnight. I want to go to bed."
        cthink "{i}Is{/i} it midnight? Because I think if you check my novelty watch..."
        cthink "You will surmise that it is, in fact, {i}Island Time.{/i}"
        hide car with dissolve
        wannoy "*sigh*"
        bdef "Hey there, uh, Officer...Sheriff...Ma'am?"
        wbase "Mr. Bottomi!"
        wthought "In all the chaos, I had almost forgotten about him."
        bapology "I just wanted to say,{w=0.1} you know,{w=0.1} thanks and all."
        bapology "You know,{w=0.1} for believing in me,{w=0.1} when I didn't even believe in myself."
        bsad "I guess I didn't believe in myself because I had some evil computer lady in my head,{w=0.1} but still."
        bsad "I'd have been locked away by that sunglasses guy if it weren't for you."
        bdef "So.{w=0.1} Yeah.{w=0.1} That's all.{w=0.1} Um...{w=0.1}thanks again..."
        hide bottomi with dissolve
        pause 0.5
        show ash psyched at flip
        call flash from _call_flash_36
        apsyched "Randi, you did it!"
        apsyched "You solved the case, and you managed to save Harper and Mr. Bottomi!"
        wthink "Yep...you're right..."

    asad ". . ."
    asad "I know what you're thinking..."
    asad "I was hoping we might see {color=#FF9966}him{/color} here too..."
    asad "It was a stupid hope, I know."
    wbase "Don't worry. We'll find him some day."
    aposit "You know, now that the case is wrapped up..."
    aposit "We {i}could{/i} go snooping around with these keys I got!"
    wangry "Where did you find those?" with shake
    aflippant "Swiped 'em off that guard with the crappy eyesight."
    wangry "You're going to give those back right now!"
    aannoy "What? Come ooooooon!"
    aannoy "You're no fun at all!"
    hide black
    show black with dissolve
    $renpy.start_predict("sprites/Chritude*.*")
    $renpy.start_predict("sprites/Guard*.*")
    wthought "Little did any of us know, this was just the first of several cases which would change the town forever."
    wthought "It would not be long before Ash and I returned to Base 24..."
    wthought "Looking for the answer to the mystery which had plagued us for so many years."
    ## The End
    jump smart_house_credits
