label smart_house_act_3_intro:
    ### ACT 3: A THEOREM REVISED
    $ save_name = "Act 3"
    $ askedHarperAboutMurder = False
    show black
    typing "September 13th. 9:02 P.M.\nSmart House - Kitchen"
    show kitchen with fade
    #Show Drang
    drang "Well, well, well..."
    drang "It looks like this case just got interesting..."
    # Show Drang and Ash
    ash "How has this case {i}not{/i} been interesting up until this point?"
    drang "You see a lot of strange things on the job, kid. It takes a lot to catch one's interest."
    ash "The crime scene is a revolutionary piece of technology!"
    ash "The main suspect keeps lying in order to prove his own guilt!"
    ash "If anything, a microchip in a guy's head is the {i}least{/i} peculiar thing we've seen today!"
    drang "I don't have to take any guff from you, kid! You're my assistant's assistant!"
    drang "You're, like, my grand-assistant!"
    drang "Warren, tell this kid to be quiet!"
    # SHow Warren and Carlos
    warren "Any luck waking him up?"
    carlos "Nope. He's out cold."
    carlos "We're just gonna need to wait for him to wake up and hope he didn't get a concussion."
    warren "All right. You stay here and keep an eye on him."
    warren "I've got a couple of things I want to check out."
    carlos "Hell yeah. Relaxation time with my good unconscious friend down here."
    carlos "Hey, want a drink, buddy?"
    carlos "Just kidding. Looks like you've had one too many already."
    warren "* sigh *"
    warren "Ash, are you coming?"
    # Show Drang and Ash
    drang "No, {i}you're{/i} a nerd!"
    ash "Oh, hold that thought."
    ash "Coming, Randi!"
    # Show Warren and Ash
    warren "Why do you ever bother with him?"
    ash "He's so {i}easy{/i} to mess with! It's like shooting dorks in a barrel!"
    ash "So where are we going?"
    warren "There are a few things we ought to check out."
    warren "First, we need to investigate the rest of the house."
    warren "It's seeming less and less likely that this kitchen is the true scene of the crime."
    warren "Come to think of it, the smart house itself may be capable of answering some questions."
    warren "In that case, we should see if we can get it to testify."
    ash "You want to interrogate... the smart house?"
    warren "The pamphlet you gave me says it has sensors all over."
    warren "It's possible it recorded the crime with one of those."
    ash "Okay, what else?"
    warren "That internet guy acted very strangely the last time we spoke."
    warren "I think there's something he is still hiding from us."
    ash "Anything else?"
    warren "I'd like to speak with somebody involved with the Smart House project."
    warren "They may have more information about this whole affair."
    ash "All right! Let's do it!"
    ash "Investigation Ahoy!"
    ### Add Bedroom to Travellable Locations

label investigation2_houseconvo:
    ### Speak with Smart House
    ash "Hey, look at that little touchscreen!"
    ash "How did we miss that?"
    warren "Well, Agent Drang was standing there earlier. He blocked our line of sight to it."
    ash "I think it's a control panel for the Smart House."
    ash "So I bet if I push this button..."
    ### Arms Come Down
    ash "Woah!"
    warren "What the...?"
    unknown harper "New Users Detected. Please State Your Name."
    warren "Uh, Miranda Warren."
    ash "Butt Stevenson."
    warren "Ash!"
    unknown harper "Profiles Created. Welcome, Miranda Warren, and, Butt Stevenson."
    ash "Hah hah"
    ash "Nice."
    unknown harper "I Am Home Automated Routinely Performing Errand Robot, Or HARPER."
    harper "How Can I Help You Today?"
    menu:
        "Smart House":
            warren "So, what are you exactly?"
            harper "I Am An Artificial Intelligence Designed To Make Your Life Easier."
            harper "I Can Provide A Number Of Services Pertaining To Everyday Life."
            harper "I Can Cook And Clean, I Can Move Heavy Objects, I Can Search The Internet For Various Things."
            harper "I Can Respond To Requests Made Of Me, And Can Learn From Previous Experiences."
            ash "Can you tell knock-knock jokes?"
            harper "I Have Over Ten Thousand Knock-Knock Jokes In My Database."
            warren "Please don't demonstrate."
            harper "Understood."
            warren "Harper, tell me who made you."
            harper "I Am A Co-Production Of United States Government And The Burchfield Manufacturing Corporation."
            warren "No, I mean, who is your inventor? Who lead the project which created you?"
            harper "That Would Be User Zero. Her Name Is Angela Neering."
            warren "Angela Neering... does she work here at the base?"
            harper "I Am Not Sure. I Have Limited Knowledge Of Things Outside Of My Walls."
            harper "However, If This Base You Speak Of Is Where I Was Built, Then It Is Likely That User Zero Works Here."
            harper "She Makes Frequent Visits Here In Order To Test Various Functions."
            warren "Ash, I think you and I should go visit this Angela Neering when we get a chance."
            harper "Unfortunately, User Zero Is Not In Her Office Right Now."
            warren "How would you know that?"
            harper "I Have Communication Enabled With User Zero's Office. It Is One Of The Few Outside Views Afforded To Me."
            warren "Well, we can always wait around for her to return."
            warren "Uh, thanks, Harper. Do I need to thank you?"
            harper "While I Will Warmly Receive Your Thanks, I Do Not Require Positive Feedback To Function."
            harper "I Have No Human Emotions To Speak Of, And Can Feel Neither Happy Nor Sad About Our Interactions."
            warren "Next time, just stick with a \"You're Welcome\"."
            harper "Understood."
            ### Add Neering's Office to Travellable Locations

        "The Murder":
            warren "Can you tell us anything about the murder?"
            harper "I'm Sorry. I Do Not Have \"The Murder\" In My Data Banks."
            ash "Randi, remember this thing is a robot. It doesn't fully understand human language."
            ash "You gotta act like you're talking to your smartphone or something."
            warren "Oh, uh..."
            warren "Can you tell me what happened in the kitchen between 5 and 6 P.M. today?"
            harper "Certainly, User Miranda."
            harper ". . . ."
            harper "ERROR. BACKUP FILES FOR SEPTEMBER_13_5-6PM INACCESSABLE."
            harper "STORAGE DRIVE CORRUPTED BY POWER INTERRUPTION."
            warren "You're kidding me."
            harper "While I Am Programmed To Be Capable Of Kidding, I Am Not Doing So On This Occasion."
            $ askedHarperAboutMurder = True

        "Show Evidence":
            warren "Do you recognize this item?"
            $ current_present = "investigation_2_house_present"
            show screen present_evidence_screen
            show screen back_button
            pause

        "Show Profile":
            warren "Do you have a profile of this person?"
            $ current_present = "investigation_2_house_present"
            show screen present_profile_screen
            show screen back_button
            pause

        "Goodbye":
            warren "Thank you for your assistance."
            warren "Uh, turn off now, or whatever."
            harper "You Cannot Turn Me Off! I Am A Constant Presence In The House."
            harper "I Am Always Listening To Every Conversation, In Case I Am Needed."
            warren "All right then, uh... just be quiet, I guess?"
            house "Understood."
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
        warren "We discovered this trap door in the upstairs bedroom..."
        harper "Ah, That Is The Entrance To The Dressing Contraption."
        warren "The Dressing what now?"
        ash "Oh, I remember now! The Dressing Contraption is one of the features of the house."
        ash "When you wake up in the morning, your bed tilts forward and a trap door opens..."
        ash "Then you slide down into this secret room where a big contraption gets you dressed for the day!"
        ash "When you're ready, it drops you down into the kitchen just in time for breakfast!"
        warren "That sounds..."
        menu:
            "...incredibly dangerous.":
                warren "...incredibly dangerous."
            "...extremely annoying.":
                warren "...extremely annoying."
            "...overly complicated.":
                warren "...overly complicated."
        ash "Come on, you spoilsport, it's fun!"
        ash "What's the point of having a Smart House if you're not gonna do cool stuff with it?"
        warren "Harper, we have reason to believe that this \"Dressing Contraption\" may have something to do with the case."
        warren "Can you please open up the trap door to let us investigate it?"
        harper "Even Better, I Can Open Up The Service Entrance So You Do Not Have To Jump Through The Trap Door."
        ash "...But what if I {i}wanted{/i} to jump through the trap door?"
        warren "Then you can buy your own smart house."
        warren "Thank you, Harper."
        harper "You're Welcome."
    else:
        harper "I'm Sorry. I Do Not Have A Record Of That."
        harper "If You Feel This Is An Error, Please Send A Bug Report To feedback@base24.gov"
        jump investigation2_houseconvo

label investigation2_neeringsoffice:
    if visitedOffice == False:
        typing "September 13th.\nBase 24 - Neering's Office"
        ### First Visit Conversation
        warren "This should be the place."
        ash "I sure hope so."
        ash "This is like the fifth office we've barged in on."
        warren "Well, it looks like Ms Neering isn't even here."
        ash "Perfect! Time to do some snooping!"
        warren "Ash, we aren't going to do any snooping, all right?"
        warren "Although, if we take a quick look around while waiting for Ms Neering..."
        ash "Snoo! Ping! Snoo! Ping! Snoo! Ping!"
        warren "All right, all right! Call it snooping if you really want to!"
        ash "Hooray!"
    #imagemap

label investigation2_emails:
    ### Find Emails About Carpet / Sentience Concerns
    ash "Hey, it looks like {i}somebody{/i} left their email open!"
    warren "All right, I can tolerate a little snooping, but reading private emails is just too far."
    ash "Even private emails received from {color=red}Mr Darsha?{/color}"
    warren "What? Let me see!"
    ### (SHOW EMAIL)
    ### From: OrinD@base24.gov
    ### To: AngelaN@base24.gov
    ### RE: RE: Carpets
    ###
    ### We will talk about it after the reveal, all right? It's imperative this launch goes well. We
    ### cannot afford any more delays on this project.
    ### ------------------------------------------------------------------------------------------
    ### yes, the new carpets will be ready in time for the tours. i've got contractors coming in
    ### the day before the event. now can we please talk about the AI? i don't think it's ready
    ### for the reveal. i keep getting erratic behavior and strange bugs. i need some time to
    ### troubleshoot the problems. i may even need to bring the whole thing offline for a while.
    ### ------------------------------------------------------------------------------------------
    ### Ms Neering,
    ###     It has come to my attention that the upstairs bedroom still does not have carpeting
    warren "Hm... it looks like there was some friction between Ms Neering and the victim over the state of the house."
    ash "Isn't that just the way..."
    ash "The creative type wants to take their time on the project while the higher-ups want to kick it out the door as soon as possible."
    warren "Is that... something you have experience with?"
    ash "No, but I watch a lot of Making-Of documentaries."
    warren "I've got a feeling this exchange is important."
    warren "Ash, could you take a picture of t{nw}"
    ### White Flash
    ash "Way ahead of you."
    ### Darsha's Email added to Inventory

label investigation2_securitylogs:
    ### Find Dot Matrix Printer
    ash "Hey, check it out, it's one of those zig-zag printers they use for earthquakes and stuff!"
    ash "I love those big ka-chunk noises they make."
    warren "Let me see that..."
    warren ". . ."
    warren "Looks like Ms Neering has a printer set up to log feedback from the house's operating system."
    warren "Things like system functionality and user inputs."
    ash "Hey, check the log from between 5 and 6!"
    ash "Maybe the house logged somebody saying \"I'm gonna murder you!\""
    warren "We should be so lucky..."
    ### Show Logs
    warren "Most of this is programmer gobbeldygook, but I can make out some of it."
    warren "It shows \"Tour Mode\" ending at 5:30..."
    warren "Was Mr Darsha with your group through the whole tour?"
    ash "I think so... he was hanging around near the back."
    warren "So he died some time between then and 6 P.M."
    warren "Odd... somebody disabled the safety protocols at 5:51."
    warren "I wonder how many people have the authority to do something like that?"
    warren "Hm. Look at this. At 5:52 it says \"TDC Subroutine Activated.\""
    ash "What do you think TDC stands for?"
    ash "\"Terribly Dangerous Cookies?\""
    ash "\"Total Dinosaur Conquest?\""
    ash "Ooh! Ooh! \"Timothy, Don't Creep!\""
    warren "What about... "
    menu:
        "Say Statement"
        "\"Try Discovering Clues\"?":
            warren "\"Try Discovering Clues\"?"
        "\"The Decisive Contradiction\"?":
            warren "\"The Decisive Contradiction\"?"
        "\"Thoroughly Disliking Crimes\"?":
            warren "\"Thoroughly Disliking Crimes\"?"
    ash "Nice one!"
    warren "Hm... looks like there's a communications error at 5:58."
    ash "That must be when the power outage happened."
    warren "Yeah, that would make sense."
    ### Hide Logs
    warren "I'm sure Ms Neering wouldn't mind if we borrowed this for the time being..."
    ### Logs Added to Inventory

label investigation2_neeringconvo:
    ### Neering Shows Up On Screen
    neering "Who are you and what are you doing in my office?"
    ash "W-woah! The TV is talking to us!"
    warren "Are you Angela Neering?"
    neering "Yes! I'm her and this is my office! So what are you doing in it?"
    warren "We came to speak with you. We're investigating a murder."
    neering "Fine, but MIQ."
    warren "I'm sorry... MIQ?"
    neering "{i}Make It Quick?{/i} It's shorthand, you simpleton."
    ash "Oh, you mean like \"TGIF\" or \"LOL\"."
    neering "That's a gross oversimplification, but yes."
    neering "I'm an incredibly busy person. I don't have time to go speaking sentences in full, so I abbreviate them."
    warren thought "It seems like you waste more time explaining yourself than you would just saying what you meant."
    $ loop = 1
    while loop == 1:
        menu:
            "Smart House":
                warren "Now, you're the project lead on the Smart House, aren't you?"
                neering "{i}And{/i} lead programmer, {i}and{/i} head of design, yes."
                warren "The smart house is constantly recording, right? Is there any possibility it captured the murder."
                neering "I'm afraid not. The house only records things in-the-moment. It doesn't actually keep any of the footage."
                warren "Of course. That would be too easy."
                if askedHarperAboutMurder = False:
                    ash "But it remembers things, right? Couldn't we ask it what it saw?"
                    neering "I suppose so. Hopefully the power outage didn't corrupt the backup drive."
                if askedHarperAboutMurder = True:
                    warren "We asked it if it remembers anything about the murder, but it says the backup drive is corrupted."
                    neering "I was just about to check on the backup drive. Well, drat. There goes all the data from the tour."
                warren "Is there anything else you can tell us about the house which could help us out?"
                neering "Hmmm...I could tell you how many lines of code it takes to get the H.A.R.P.E.R AI running."
                warren "I don't see how that would be partic{nw}"
                neering "One Hundred Million."
                warren "Um...is that a large amount? A small amount?"
                neering "Boy, they let just about {i}anyone{/i} be a police officer these days..."

            "Power Outage":
                warren "Do you know anything about the power outage which occurred around 6 P.M. today?"
                neering "I know it's been a massive thorn in my side."
                neering "The house wasn't built to handle a power outage, so half the systems are on the fritz now."
                neering "I told them, I {i}told them{/i} we needed to be prepared for such a thing, but as usual, NLTOA."
                warren "Uh...NLTOA?"
                neering "\"Nobody Listens To Ol' Angela\"."
                neering "Anyway, I'm down in the house's guts right now trying to sort out this mess."
                neering "It's why I couldn't come to speak with you in person."
                neering "Not that I would have, anyways..."
                warren "Do you have any idea what could have caused the power outage?"
                neering "It would probably be the main breaker."
                neering "If somebody messed with that, they could bring the house down for a while."
                neering "Now is there anything else, or can I get back to my work?"

            "Orin Darsha":
                warren "You know a man by the name of Orin Darsha, yes?"
                neering "Ugh, yes. He's technically my boss. A small minded fool of a man."
                neering "Why do you ask?"
                warren "He's dead."
                neering ". . ."
                neering "WELL WHY DIDN'T YOU TELL ME THAT EARLIER? NOW I LOOK LIKE A GRADE-A JERK!"
                warren thought "Trust me, lady. You didn't need {i}my{/i} help to do that."
                warren "We found him dead in the kitchen of your smart house."
                neering "Great. Just great."
                neering "This is going to completely overshadow the Smart House reveal!"
                neering "Way to mess things up again, Darsha!"
                warren thought "Is there a single person on this base with an ounce of human empathy?"
                warren "Now, I have to ask..."
                warren "...not that you would answer truthfully anyways..."
                warren "Did you murder Orin Darsha?"
                neering "Hah! No."
                neering "To murder somebody, you need to have strong feelings about them."
                neering "Darsha may have been an annoyance, but I really didn't think about him all that much."
                neering "Now is there anything else, or can I get back to my work?"

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
    ash "What a nice bedroom!"
    warren "It's larger than the one I have at home."
    ash "That bed is so big and soft looking I could just..."
    # Floomf
    warren "Do you really want to be lying there? For all we know, that's where the victim was killed."
    ash "GYAAAH!"
    ash "Do you think I got dead guy on me?"
    warren "If you did, it's your own fault."
    ash "Gross!"

label investigation2_scratches:
    warren "There are scratch marks in the carpeting down here."
    ash "You know what that must mean..."
    warren "Somebody was probably atta{nw}"
    ash "Chupacabra marks."
    ash "I mean, uh, the thing that you said."
    warren "The square foot of carpeting around the scratch marks are wet."
    warren "I wonder if someone was trying to clean up a stain..."
    ash "Wait Randi, look at what the scratch marks are leading to!"
    ash "There's a seam here. It makes a big square shape..."
    ash "Oh my gosh, it's a trapdoor! This house really {i}does{/i} have everything!"
    warren "I can't seem to find a handle or a lever anywhere..."
    ash "Knowing this house, it's probably computer controlled."
    warren "In that case, we'll need the house's AI to open it for us."
    ### Trap Door Added to Inventory

label investigation2_thedressingcontraption:
    ash "Wooooaaahh! This place is huge!"
    warren thought "How on earth does this fit inside the rest of the house?"

label investigation2_missingshoe:
    ash "Looks like The Dressing Contraption didn't dress someone up all the way!"
    ash "See? It dropped a shoe!"
    warren "Wait a minute...a shoe?"
    warren "Wasn't there a shoe we were looking for?"
    $ current_present = "investigation_2_shoe_present"
    show screen present_evidence_screen
    pause

label investigation_2_shoe_present:
    if present_response == "missingshoe":
        warren "That's right... Orin Darsha's body was missing a shoe when we found it."
        warren "Ash, show me that photo you took of him..."
        ### Show Body Photo
        wos "There's no doubt about it... it's the same shoe."
        ash "So that means... Mr Darsha was in here some time today?"
        wos "I can't think of another way this shoe could have found its way here."
        ### Hide Body Photo
        ash "During the tour, our guide let somebody test out the Dressing Contraption..."
        ash "But it wasn't Mr Darsha who volunteered."
        ash "When did he have time to run through the whole thing?"
        warren "And why?"
        ### Missing Shoe Updated

    else:
        warren "Wait, that wasn't it..."
        ash "Come on, Randi. Even {i}I{/i} know what you're talking about!"
        warren "Okay, let's try this again..."
        warren "Wasn't there a shoe we were looking for?"
        show screen present_evidence_screen
        pause

label investigation2_chritude:
    "good writing here"

label investigation2_bottomiawakens:
    drang "Hey, assistant."
    drang "While you were off galavanting on your own, our main suspect finally woke up."
    warren "You mean Mr Bottomi?"
    drang "No, the {i}other{/i} main suspect."
    drang "Your forensics monkey is over there attending to him."
    drang "How about we finish up that cross examination, huh?"
    drang "Any longer down here and I'm going to have to book some repugnant hotel."
    warren "Mr Bottomi. Are you alright?"
    bottomi "I... I think so..."
    bottomi "H-how long was I out?"
    carlos "Approximately thirty minutes."
    carlos "I'm going to be honest: you may have brain damage."
    carlos "You should probably go see a doctor when you get a chance."
    warren "Now, do you mind telling us exactly what that is on your head?"
    bottomi "You mean my hat? Wait..."
    bottomi "Aah! My hat! You weren't supposed to see this!"
    if mentionedhardware:
        warren "Is it safe to assume this is the \"hardware\" you mentioned earlier?"
        bottomi "Y... yeah. This is it."
    else:
        warren "Would this peculiar headgear have anything to do with the trial you were participating in?"
        bottomi "Y...yeah. It is."
    bottomi "Nobody outside of the base is supposed to know about this..."
    bottomi "But I guess it's too late for that, huh?"
    bottomi "This is what I've been helping to test here at the base."
    bottomi "It's an experimental {color=red}neural implant{/color} designed for psychically transferring information."
    bottomi "It lets me send and receive data wirelessly from my brain to a computer."
    bottomi "I don't fully know all the technical detai{nw}"
    ## White Flash
    bottomi "AAH!"
    ## Ash holding camera
    ash "This is absolutely incredible! Real life technopathy!"
    ash "The occultism forums are going to go wild when they hear about this!"
    bottomi "Good luck. The base is probably gonna make you sign an NDA before they let you leave."
    bottomi "They'll probably confiscate the photo, too."
    ash "Rats..."
    warren thought "And to think, the thing he was dead set on hiding from us was right there the whole time."
    warren "So, now that the cat is out of the bag..."
    warren "Are there any other secrets you'd like to share with us?"
    bottomi "No, I don't thi-- NNNGH!!"
    bottomi "Actually, there is, come to think of it."
    bottomi "You might have noticed that my recollection of events has been a little shaky..."
    ash "Yeah, no kidding..."
    bottomi "Well, the reason is that I've been lying to you about one important detail."
    bottomi "I didn't actually kill Orin Darsha..."
    bottomi "I made the house do it for me."
    show black with dissolve
    jump smart_house_act_4_intro
