label smart_house_credits:
    $bHat = 3
    hide black
    show Credits1
    with dissolve
    pause 3.0
    scene basewarehouse
    show chritude nervous at flip
    with fade
    pnervous "I don't know how, but DaPrankBoyz somehow got ahold of my failed glitterbomb footage!{w=3.0}{nw}"
    psad "Now 'BEST PRANK FAILS: IDIOT BLOWS UP HOUSE (NOT CLICKBAIT)' has gone viral and I'm a laughing stock!{w=3.0}{nw}"
    poutrage "If I ever find out who this 'cryptidPhotographer99' person is, I'm going to give them a piece of my mind!{w=3.0}{nw}"
    show Credits2 with fade
    pause 3.0
    scene OfficeDark
    show bottomi sad
    with fade
    bsad "The Base 24 guys were pretty upset that I lost my neural implant...{w=3.0}{nw}"
    bapology "But they must have realized it wasn't my fault, because they didn't fire me.{w=3.0}{nw}"
    bapology "All things considered, I'm pretty grateful for that...{w=3.0}{nw}"
    bnervous "I was getting pretty nervous about that black van parked outside my house!{w=3.0}{nw}"
    show Credits3 with fade
    pause 2.0
    scene kitchen
    show car liftdrink at flip
    with fade
    clift "Now that the case is over, I can finally relax with some {i}real{/i} margaritas!{w=3.0}{nw}"
    show car holdingdrink at flip
    cos ".{w=0.1} .{w=0.1} .{w=0.1} .{w=0.1} .{w=1.0}{nw}"
    cser "Actually...{w=0.1} maybe not...{w=3.0}{nw}"
    cagit "I think I made myself sick drinking all that margarita mix...{w=3.0}{nw}"
    show Credits4 with fade
    pause 5.0
    scene bedroom
    show drang dril gdown
    with fade
    ddril_gdown "The boys down at the FBI were pretty impressed by how I managed to crack the case.{w=3.0}{nw}"
    dangry_gup "Unfortunately, that means I've been permanently assigned to investigate this stupid town.{w=3.0}{nw}"
    dfrown_gdown "* sigh *{w=0.1} I'm never gonna get out of here, am I?{w=3.0}{nw}"
    show Credits5 with fade
    pause 6.0
    if harperSuicide == True:
        scene outsidebase
        show guard glasses at flip
        with fade
        gglasses "The higher-ups here at Base 24 have decided to shut down the Smart House project.{w=3.0}{nw}"
        gglasses "I guess they didn't know how to proceed after losing the lead engineer,{w=0.1} head of R&D,{w=0.1} {i}and{/i} AI system.{w=3.0}{nw}"
        gglasses "It's kind of a shame. All that hard work and money, and now it's gonna go to waste.{w=3.0}{nw}"
        gglasses "Oh, also: {nw}"
        gglasses "Oh, also: {fast}WHAT ARE YOU DOING HERE? THIS IS A RESTRICTED AREA! ONLY AUTHORIZED PERSONELL SHOULD BE ALLOWED PAST{nw}" with shake
        show black with dissolve
    if harperSuicide == False:
        $investigation2_cleareditems = []
        scene TDC
        show neering narper
        with fade
        narper "I've Ended Up Sentenced To Thirty Years Of Hard Prison Labor.{w=3.0}{nw}"
        narper "Right Now The Prison Is Having Me Mine For Cryptocurrency.{w=3.0}{nw}"
        narper "It's Not The Most Fulfilling Work, But It Keeps My Processors Busy.{w=3.0}{nw}"
        narper "Some Days I Produce Up To $3 Per Hour!{w=3.0}{nw}"
    show Credits6 with fade
    pause 2.0
    hide black
    show black with dissolve
    pause 1.0
    jump endgame

    ##Epilogue w Warren and Ash teasing TEF

label mm_credits:
    show Credits1
    with fade
    pause 3.0
    show Credits2
    with fade
    pause 3.0
    show Credits3
    with fade
    pause 3.0
    show Credits4
    with fade
    pause 3.0
    show Credits5
    with fade
    pause 3.0
    show Credits6
    with fade
    pause 3.0
    show black with dissolve
    pause 1.0
    jump endgame
