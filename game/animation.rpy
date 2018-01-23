init:
    $ imagewidth = config.screen_width
    $ imageheight = config.screen_height

    image ctc_blink:
        xalign 0.94
        yalign 0.92
        "assets/menu/CTC1.png"
        linear 0.25 zoom 1.1
        linear 0.25 zoom 1.0
        repeat

    image mm_bg_scroll:
        "assets/backgrounds/MM_BG_Lines.png"
        ypan 0
        linear 100 ypan 360
        repeat

    image willitblend:
        yalign 0.0
        xalign 0.475
        zoom 0.5
        "assets/menu/OCP_Logo2.png"
        additive 0.25

    image pressStart:
        alpha 0.0
        yalign 0.9
        xalign 0.5
        "assets/backgrounds/pressStart.png"
        ease 2.0 alpha 1.0
        ease 2.0 alpha 0.0
        repeat

    image mm_glitch:
        zoom 2.87
        "assets/backgrounds/glitch1.png"
        pause 0.05
        "assets/backgrounds/glitch2.png"
        pause 0.05
        "assets/backgrounds/glitch3.png"
        pause 0.05
        "assets/backgrounds/glitch4.png"
        pause 0.05
        "assets/backgrounds/glitch5.png"
        pause 0.05
        repeat

    image splashscreen_bg = LiveComposite((1920,1080),
                                (0,0), "mm_bg_scroll",
                                (0,0), "assets/backgrounds/MM_BG_Vignette.png",
                                (0,0), "assets/backgrounds/TemashawValleyLogo.png"
                                )

    image main_menu_bg = LiveComposite((1920,1080),
                                (0,0), "mm_bg_scroll",
                                (0,0), "assets/backgrounds/MM_BG_Vignette.png",
                                #(0,0), "willitblend"
                                )

    transform flip:
        xzoom -1

    transform menuFade:
        zoom 0.0
        linear 0.3 zoom 1.1
        linear 0.1 zoom 1.0

    image outsidebaseboth = LiveComposite((1920,1080),
                                (0,0), "outsidebase",
                                (0,0), "assets/backgrounds/CheckpointCarlos.png",
                                (0,0), "assets/backgrounds/CheckpointGuard.png")

    image outsidebaseaaa = LiveComposite((1920,1080),
                                (0,0), "outsidebase",
                                (0,0), "assets/backgrounds/CheckpointCarlosSelected.png",
                                (0,0), "assets/backgrounds/CheckpointGuardSelected.png")

    image outsidebasecarlos = LiveComposite((1920,1080),
                                (0,0), "outsidebase",
                                (0,0), "assets/backgrounds/CheckpointCarlos.png")

    image outsidebaseguard = LiveComposite((1920,1080),
                                (0,0), "outsidebase",
                                (0,0), "assets/backgrounds/CheckpointGuard.png")

    image kitchendrang = LiveComposite((1920,1080),
                                (0,0), "kitchen",
                                (0,0), "assets/backgrounds/KitchenDrang.png")

    image basewarehousepaul = LiveComposite((1920,1080),
                                (0,0), "basewarehouse",
                                (0,0), "assets/backgrounds/basewarehousechritude.png")

    image Miranda_Default_Talk:
        "sprites/Miranda/Default/Mouth_1.png"
        pause 0.1
        "sprites/Miranda/Default/Mouth_2.png"
        pause 0.1
        "sprites/Miranda/Default/Mouth_3.png"
        pause 0.1
        "sprites/Miranda/Default/Mouth_4.png"
        pause 0.1
        "sprites/Miranda/Default/Mouth_5.png"
        pause 0.1
        "sprites/Miranda/Default/Mouth_3.png"
        pause 0.1
        repeat

    image Miranda_Default_Blink:
        "sprites/Miranda/Default/Eyes_1.png"
        pause 2.5
        "sprites/Miranda/Default/Eyes_2.png"
        pause 0.05
        "sprites/Miranda/Default/Eyes_3.png"
        pause 0.05
        "sprites/Miranda/Default/Eyes_4.png"
        pause 0.05
        "sprites/Miranda/Default/Eyes_5.png"
        pause 0.05
        "sprites/Miranda/Default/Eyes_4.png"
        pause 0.05
        "sprites/Miranda/Default/Eyes_3.png"
        pause 0.05
        "sprites/Miranda/Default/Eyes_2.png"
        pause 0.05
        repeat

    image mir default = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/Default/Base.png",
                                (0,0), "sprites/Miranda/Default/Mouth_1.png",
                                (0,0), "Miranda_Default_Blink" )

    image mir default talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/Default/Base.png",
                                (0,0), "Miranda_Default_Talk",
                                (0,0), "Miranda_Default_Blink" )

    image Miranda_CaseFile_Talk:
        "sprites/Miranda/CaseFile/Mouth_1.png"
        pause 0.1
        "sprites/Miranda/CaseFile/Mouth_2.png"
        pause 0.1
        "sprites/Miranda/CaseFile/Mouth_3.png"
        pause 0.1
        "sprites/Miranda/CaseFile/Mouth_4.png"
        pause 0.1
        "sprites/Miranda/CaseFile/Mouth_3.png"
        pause 0.1
        repeat



    image Miranda_CaseFile_Blink:
        "sprites/Miranda/CaseFile/Eyes_1.png"
        pause 3.0
        "sprites/Miranda/CaseFile/Eyes_2.png"
        pause 0.05
        "sprites/Miranda/CaseFile/Eyes_3.png"
        pause 0.05
        "sprites/Miranda/CaseFile/Eyes_4.png"
        pause 0.05
        "sprites/Miranda/CaseFile/Eyes_5.png"
        pause 0.05
        "sprites/Miranda/CaseFile/Eyes_4.png"
        pause 0.05
        "sprites/Miranda/CaseFile/Eyes_3.png"
        pause 0.05
        "sprites/Miranda/CaseFile/Eyes_2.png"
        pause 0.05
        repeat

    image Miranda_CaseFile_Arm:
        "sprites/Miranda/CaseFile/Arm_01.png"
        pause 2.0
        "sprites/Miranda/CaseFile/Arm_02.png"
        pause 0.07
        "sprites/Miranda/CaseFile/Arm_03.png"
        pause 0.07
        "sprites/Miranda/CaseFile/Arm_04.png"
        pause 0.07
        "sprites/Miranda/CaseFile/Arm_05.png"
        pause 0.07
        "sprites/Miranda/CaseFile/Arm_06.png"
        pause 0.07
        "sprites/Miranda/CaseFile/Arm_07.png"
        pause 0.07
        "sprites/Miranda/CaseFile/Arm_08.png"
        pause 0.07
        "sprites/Miranda/CaseFile/Arm_09.png"
        pause 0.07
        "sprites/Miranda/CaseFile/Arm_10.png"
        pause 0.07
        "sprites/Miranda/CaseFile/Arm_11.png"
        pause 0.07
        "sprites/Miranda/CaseFile/Arm_12.png"
        pause 0.07
        "sprites/Miranda/CaseFile/Arm_01.png"
        pause 3.0
        repeat

    image mir casefile = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/CaseFile/Base.png",
                                (0,0), "sprites/Miranda/CaseFile/Mouth_1.png",
                                (0,0), "Miranda_CaseFile_Blink",
                                (0,0), "Miranda_CaseFile_Arm")

    image mir casefile talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/CaseFile/Base.png",
                                (0,0), "Miranda_CaseFile_Talk",
                                (0,0), "Miranda_CaseFile_Blink",
                                (0,0), "Miranda_CaseFile_Arm")

    image Miranda_Angry_Talk:
        "sprites/Miranda/Angry/Mouth_1.png"
        pause 0.1
        "sprites/Miranda/Angry/Mouth_2.png"
        pause 0.1
        "sprites/Miranda/Angry/Mouth_3.png"
        pause 0.1
        "sprites/Miranda/Angry/Mouth_4.png"
        pause 0.1
        "sprites/Miranda/Angry/Mouth_2.png"
        pause 0.1
        repeat

    image Miranda_Angry_Blink:
        "sprites/Miranda/Angry/Eyes_1.png"
        pause 2.3
        "sprites/Miranda/Angry/Eyes_2.png"
        pause 0.05
        "sprites/Miranda/Angry/Eyes_3.png"
        pause 0.05
        "sprites/Miranda/Angry/Eyes_4.png"
        pause 0.05
        "sprites/Miranda/Angry/Eyes_5.png"
        pause 0.05
        "sprites/Miranda/Angry/Eyes_4.png"
        pause 0.05
        "sprites/Miranda/Angry/Eyes_3.png"
        pause 0.05
        "sprites/Miranda/Angry/Eyes_2.png"
        pause 0.05
        repeat

    image mir angry = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/Angry/Base.png",
                                (0,0), "sprites/Miranda/Angry/Mouth_1.png",
                                (0,0), "Miranda_Angry_Blink")

    image mir angry talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/Angry/Base.png",
                                (0,0), "Miranda_Angry_Talk",
                                (0,0), "Miranda_Angry_Blink")

    image Miranda_Annoyed_Base:
        "sprites/Miranda/Annoyed/Base_01.png"
        pause 0.12
        "sprites/Miranda/Annoyed/Base_04.png"
        pause 0.16
        "sprites/Miranda/Annoyed/Base_08.png"
        pause 0.05
        "sprites/Miranda/Annoyed/Base_09.png"
        pause 0.05
        "sprites/Miranda/Annoyed/Base_10.png"
        pause 0.05
        "sprites/Miranda/Annoyed/Base_11.png"
        pause 0.16
        "sprites/Miranda/Annoyed/Base_15.png"
        pause 0.09
        "sprites/Miranda/Annoyed/Base_17.png"
        pause 0.09
        "sprites/Miranda/Annoyed/Base_19.png"
        pause 0.09
        "sprites/Miranda/Annoyed/Base_21.png"
        pause 0.05

    image Miranda_Annoyed_Talk:
        "sprites/Miranda/Annoyed/Mouth_1.png"
        pause 0.1
        "sprites/Miranda/Annoyed/Mouth_2.png"
        pause 0.1
        "sprites/Miranda/Annoyed/Mouth_3.png"
        pause 0.1
        "sprites/Miranda/Annoyed/Mouth_4.png"
        pause 0.1
        "sprites/Miranda/Annoyed/Mouth_3.png"
        pause 0.1
        repeat

    image Miranda_Annoyed_Blink:
        "sprites/Miranda/Annoyed/Eyes_1.png"
        pause 3.0
        "sprites/Miranda/Annoyed/Eyes_2.png"
        pause 0.05
        "sprites/Miranda/Annoyed/Eyes_3.png"
        pause 0.05
        "sprites/Miranda/Annoyed/Eyes_4.png"
        pause 0.05
        "sprites/Miranda/Annoyed/Eyes_3.png"
        pause 0.05
        "sprites/Miranda/Annoyed/Eyes_2.png"
        pause 0.05
        repeat

    image mir annoy anim = LiveComposite((1920,1080),
                                (0,0), "Miranda_Annoyed_Base")

    image mir annoy talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/Annoyed/Base_21.png",
                                (0,0), "Miranda_Annoyed_Talk",
                                (0,0), "Miranda_Annoyed_Blink")

    image mir annoy base = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/Annoyed/Base_21.png",
                                (0,0), "sprites/Miranda/Annoyed/Mouth_1.png",
                                (0,0), "Miranda_Annoyed_Blink")

    image Miranda_HatTip_Arm:
        "sprites/Miranda/HatTip/Arm_1.png"
        pause 0.2
        "sprites/Miranda/HatTip/Arm_2.png"
        pause 0.3
        "sprites/Miranda/HatTip/Arm_3.png"
        pause 0.06
        "sprites/Miranda/HatTip/Arm_4.png"
        pause 0.06
        "sprites/Miranda/HatTip/Arm_5.png"
        pause 0.06
        "sprites/Miranda/HatTip/Arm_6.png"
        pause 0.06
        "sprites/Miranda/HatTip/Arm_7.png"
        pause 0.06

    image Miranda_HatTip_Talk:
        "sprites/Miranda/HatTip/Mouth_1.png"
        pause 0.1
        "sprites/Miranda/HatTip/Mouth_2.png"
        pause 0.1
        "sprites/Miranda/HatTip/Mouth_3.png"
        pause 0.1
        "sprites/Miranda/HatTip/Mouth_4.png"
        pause 0.1
        "sprites/Miranda/HatTip/Mouth_5.png"
        pause 0.1
        "sprites/Miranda/HatTip/Mouth_3.png"
        pause 0.1
        repeat

    image Miranda_HatTip_Blink:
        "sprites/Miranda/HatTip/Eyes_1.png"
        pause 2.3
        "sprites/Miranda/HatTip/Eyes_2.png"
        pause 0.05
        "sprites/Miranda/HatTip/Eyes_3.png"
        pause 0.05
        "sprites/Miranda/HatTip/Eyes_4.png"
        pause 0.05
        "sprites/Miranda/HatTip/Eyes_5.png"
        pause 0.05
        "sprites/Miranda/HatTip/Eyes_4.png"
        pause 0.05
        "sprites/Miranda/HatTip/Eyes_3.png"
        pause 0.05
        "sprites/Miranda/HatTip/Eyes_2.png"
        pause 0.05
        repeat

    image mir hattip = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/HatTip/Base.png",
                                (0,0), "sprites/Miranda/HatTip/Mouth_1.png",
                                (0,0), "Miranda_HatTip_Blink",
                                (0,0), "sprites/Miranda/HatTip/Arm_7.png")

    image mir hattip talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/HatTip/Base.png",
                                (0,0), "Miranda_HatTip_Talk",
                                (0,0), "Miranda_HatTip_Blink",
                                (0,0), "Miranda_HatTip_Arm")

    image Miranda_Recoil_Base:
        "sprites/Miranda/Recoil/Base_1.png"
        pause 0.2
        "sprites/Miranda/Recoil/Base_2.png"
        pause 0.05
        "sprites/Miranda/Recoil/Base_3.png"
        pause 0.05
        "sprites/Miranda/Recoil/Base_4.png"
        pause 0.05
        "sprites/Miranda/Recoil/Base_5.png"
        pause 0.2
        "sprites/Miranda/Recoil/Base_6.png"
        pause 0.05
        "sprites/Miranda/Recoil/Base_7.png"
        pause 0.05
        "sprites/Miranda/Recoil/Base_8.png"
        pause 0.1
        "sprites/Miranda/Recoil/Base_9.png"
        pause 0.1

    image Miranda_Recoil_Hat:
        pause 2.0
        "sprites/Miranda/Recoil/Hat_01.png"
        pause 0.1
        "sprites/Miranda/Recoil/Hat_02.png"
        pause 0.1
        "sprites/Miranda/Recoil/Hat_03.png"
        pause 0.1
        "sprites/Miranda/Recoil/Hat_04.png"
        pause 0.1
        "sprites/Miranda/Recoil/Hat_05.png"
        pause 0.1
        "sprites/Miranda/Recoil/Hat_06.png"
        pause 0.1
        "sprites/Miranda/Recoil/Hat_07.png"
        pause 0.1
        "sprites/Miranda/Recoil/Hat_08.png"
        pause 0.1
        "sprites/Miranda/Recoil/Hat_09.png"
        pause 0.1
        "sprites/Miranda/Recoil/Hat_10.png"
        pause 0.1
        "sprites/Miranda/Recoil/Hat_11.png"
        pause 0.1
        "sprites/Miranda/Recoil/Hat_12.png"
        pause 0.1
        "sprites/Miranda/Recoil/Hat_13.png"
        pause 0.1
        "sprites/Miranda/Recoil/Hat_14.png"
        pause 0.1
        "sprites/Miranda/Recoil/Hat_15.png"
        pause 0.1
        "sprites/Miranda/Recoil/Hat_16.png"
        pause 0.1
        "sprites/Miranda/Recoil/Hat_17.png"
        pause 0.1
        "sprites/Miranda/Recoil/Hat_18.png"
        pause 0.1
        "sprites/Miranda/Recoil/Hat_19.png"
        pause 0.1
        "sprites/Miranda/Recoil/Hat_20.png"
        pause 0.1
        "sprites/Miranda/Recoil/Hat_21.png"
        pause 0.1
        "sprites/Miranda/Recoil/Hat_22.png"
        pause 0.1

    image Miranda_Recoil_Talk:
        "sprites/Miranda/Recoil/Talk_1.png"
        pause 0.1
        "sprites/Miranda/Recoil/Talk_2.png"
        pause 0.1
        "sprites/Miranda/Recoil/Talk_3.png"
        pause 0.1
        "sprites/Miranda/Recoil/Talk_4.png"
        pause 0.1
        "sprites/Miranda/Recoil/Talk_3.png"
        pause 0.1
        "sprites/Miranda/Recoil/Talk_2.png"
        pause 0.1
        repeat


    image mir recoil anim = LiveComposite((1920,1080),
                                (0,0), "Miranda_Recoil_Base",
                                (0,0), "Miranda_Recoil_Hat")

    image mir recoil base = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/Recoil/Talk_1.png")

    image mir recoil talk = LiveComposite((1920,1080),
                                (0,0), "Miranda_Recoil_Talk")

    image Miranda_Thinking_Arm:
        "sprites/Miranda/Thinking/Arm_1.png"
        pause 0.4
        "sprites/Miranda/Thinking/Arm_2.png"
        pause 0.4
        "sprites/Miranda/Thinking/Arm_3.png"
        pause 0.4
        "sprites/Miranda/Thinking/Arm_4.png"
        pause 0.4
        repeat

    image Miranda_Thinking_Talk:
        "sprites/Miranda/Thinking/Mouth_1.png"
        pause 0.1
        "sprites/Miranda/Thinking/Mouth_2.png"
        pause 0.1
        "sprites/Miranda/Thinking/Mouth_3.png"
        pause 0.1
        "sprites/Miranda/Thinking/Mouth_4.png"
        pause 0.1
        "sprites/Miranda/Thinking/Mouth_2.png"
        pause 0.1
        repeat

    image Miranda_Thinking_Blink:
        "sprites/Miranda/Thinking/Eyes_1.png"
        pause 6.0
        "sprites/Miranda/Thinking/Eyes_2.png"
        pause 0.05
        "sprites/Miranda/Thinking/Eyes_3.png"
        pause 0.05
        "sprites/Miranda/Thinking/Eyes_4.png"
        pause 0.05
        "sprites/Miranda/Thinking/Eyes_3.png"
        pause 0.05
        "sprites/Miranda/Thinking/Eyes_2.png"
        pause 0.05
        repeat

    image mir thinking = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/Thinking/Base.png",
                                (0,0), "Miranda_Thinking_Arm",
                                (0,0), "sprites/Miranda/Thinking/Mouth_1.png",
                                (0,0), "Miranda_Thinking_Blink")

    image mir thinking talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/Thinking/Base.png",
                                (0,0), "Miranda_Thinking_Arm",
                                (0,0), "Miranda_Thinking_Talk",
                                (0,0), "Miranda_Thinking_Blink")

    image mir gotcha = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/Gotcha.png")

    image mir holdon = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/HoldOn.png")



    image Carlos_Default_Blink:
        "sprites/Carlos/Standard/Eye_1.png"
        pause 6.0
        "sprites/Carlos/Standard/Eye_2.png"
        pause 0.05
        "sprites/Carlos/Standard/Eye_3.png"
        pause 0.05
        "sprites/Carlos/Standard/Eye_4.png"
        pause 0.05
        "sprites/Carlos/Standard/Eye_3.png"
        pause 0.05
        "sprites/Carlos/Standard/Eye_2.png"
        pause 0.05
        repeat


    image Carlos_Default_Talk:
        "sprites/Carlos/Standard/Mouth_1.png"
        pause 0.1
        "sprites/Carlos/Standard/Mouth_2.png"
        pause 0.1
        "sprites/Carlos/Standard/Mouth_3.png"
        pause 0.1
        "sprites/Carlos/Standard/Mouth_4.png"
        pause 0.1
        repeat

    image car default = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/Standard/Base.png",
                                (0,0), "sprites/Carlos/Standard/Mouth_1.png",
                                (0,0), "Carlos_Default_Blink" )

    image car default talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/Standard/Base.png",
                                (0,0), "Carlos_Default_Talk",
                                (0,0), "Carlos_Default_Blink")

    image Carlos_Agitated_Blink:
        "sprites/Carlos/Agitated/Eyes_1.png"
        pause 3.0
        "sprites/Carlos/Agitated/Eyes_2.png"
        pause 0.05
        "sprites/Carlos/Agitated/Eyes_3.png"
        pause 0.05
        "sprites/Carlos/Agitated/Eyes_4.png"
        pause 0.05
        "sprites/Carlos/Agitated/Eyes_5.png"
        pause 0.05
        "sprites/Carlos/Agitated/Eyes_4.png"
        pause 0.05
        "sprites/Carlos/Agitated/Eyes_3.png"
        pause 0.05
        "sprites/Carlos/Agitated/Eyes_2.png"
        pause 0.05
        repeat

    image Carlos_Agitated_Talk:
        "sprites/Carlos/Agitated/Mouth_1.png"
        pause 0.1
        "sprites/Carlos/Agitated/Mouth_2.png"
        pause 0.1
        "sprites/Carlos/Agitated/Mouth_3.png"
        pause 0.1
        "sprites/Carlos/Agitated/Mouth_4.png"
        pause 0.1
        "sprites/Carlos/Agitated/Mouth_2.png"
        pause 0.1
        repeat

    image Carlos_Agitated_Arms:
        "sprites/Carlos/Agitated/Arms_1.png"
        pause 0.1
        "sprites/Carlos/Agitated/Arms_2.png"
        pause 0.1
        "sprites/Carlos/Agitated/Arms_3.png"
        pause 0.05
        "sprites/Carlos/Agitated/Arms_4.png"
        pause 0.1
        "sprites/Carlos/Agitated/Arms_5.png"
        pause 5.0
        repeat

    image car agitated = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/Agitated/Base.png",
                                (0,0), "sprites/Carlos/Agitated/Mouth_1.png",
                                (0,0), "Carlos_Agitated_Blink",
                                (0,0), "Carlos_Agitated_Arms" )

    image car agitated talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/Agitated/Base.png",
                                (0,0), "Carlos_Agitated_Talk",
                                (0,0), "Carlos_Agitated_Blink",
                                (0,0), "Carlos_Agitated_Arms")

    image Carlos_Whisper_Blink:
        "sprites/Carlos/Whisper/Eyes_1.png"
        pause 5.0
        "sprites/Carlos/Whisper/Eyes_2.png"
        pause 0.05
        "sprites/Carlos/Whisper/Eyes_3.png"
        pause 0.05
        "sprites/Carlos/Whisper/Eyes_4.png"
        pause 0.05
        "sprites/Carlos/Whisper/Eyes_3.png"
        pause 0.05
        "sprites/Carlos/Whisper/Eyes_2.png"
        pause 0.05
        repeat

    image Carlos_Whisper_Talk:
        "sprites/Carlos/Whisper/Mouth_1.png"
        pause 0.1
        "sprites/Carlos/Whisper/Mouth_2.png"
        pause 0.1
        "sprites/Carlos/Whisper/Mouth_3.png"
        pause 0.1
        "sprites/Carlos/Whisper/Mouth_4.png"
        pause 0.1
        "sprites/Carlos/Whisper/Mouth_2.png"
        pause 0.1
        repeat

    image car whisper = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/Whisper.png")

    image car whisper talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/Whisper/Base.png",
                                (0,0), "Carlos_Whisper_Talk",
                                (0,0), "Carlos_Whisper_Blink",
                                (0,0), "sprites/Carlos/Whisper/Arm.png")

    image Carlos_HoldingDrink_Blink:
        "sprites/Carlos/HoldingDrink/Eyes_1.png"
        pause 5.5
        "sprites/Carlos/HoldingDrink/Eyes_2.png"
        pause 0.05
        "sprites/Carlos/HoldingDrink/Eyes_3.png"
        pause 0.05
        "sprites/Carlos/HoldingDrink/Eyes_4.png"
        pause 0.05
        "sprites/Carlos/HoldingDrink/Eyes_5.png"
        pause 0.05
        "sprites/Carlos/HoldingDrink/Eyes_4.png"
        pause 0.05
        "sprites/Carlos/HoldingDrink/Eyes_3.png"
        pause 0.05
        "sprites/Carlos/HoldingDrink/Eyes_2.png"
        pause 0.05
        repeat

    image Carlos_HoldingDrink_Talk:
        "sprites/Carlos/HoldingDrink/Mouth_1.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Mouth_2.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Mouth_3.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Mouth_4.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Mouth_2.png"
        pause 0.1
        repeat

    image Carlos_HoldingDrink_Arm:
        "sprites/Carlos/HoldingDrink/Arm_01.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_02.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_03.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_04.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_05.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_06.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_07.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_08.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_09.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_10.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_11.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_12.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_13.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_14.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_15.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_16.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_17.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_18.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_19.png"
        pause 0.1
        "sprites/Carlos/HoldingDrink/Arm_20.png"
        pause 0.1


    image car liftdrink = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/HoldingDrink/Base.png",
                                (0,0), "sprites/Carlos/HoldingDrink/Mouth_1.png",
                                (0,0), "Carlos_HoldingDrink_Blink",
                                (0,0), "sprites/Carlos/HoldingDrink/Arm_20.png" )

    image car liftdrink talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/HoldingDrink/Base.png",
                                (0,0), "Carlos_HoldingDrink_Talk",
                                (0,0), "Carlos_HoldingDrink_Blink",
                                (0,0), "Carlos_HoldingDrink_Arm")

    image car holdingdrink = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/HoldingDrink/Base.png",
                                (0,0), "sprites/Carlos/HoldingDrink/Mouth_1.png",
                                (0,0), "Carlos_HoldingDrink_Blink",
                                (0,0), "sprites/Carlos/HoldingDrink/Arm_20.png")

    image car holdingdrink talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/HoldingDrink/Base.png",
                                (0,0), "Carlos_HoldingDrink_Talk",
                                (0,0), "Carlos_HoldingDrink_Blink",
                                (0,0), "sprites/Carlos/HoldingDrink/Arm_20.png")


    image Carlos_Serious_Blink:
        "sprites/Carlos/Serious/Eyes_1.png"
        pause 4.5
        "sprites/Carlos/Serious/Eyes_2.png"
        pause 0.05
        "sprites/Carlos/Serious/Eyes_3.png"
        pause 0.05
        "sprites/Carlos/Serious/Eyes_4.png"
        pause 0.05
        "sprites/Carlos/Serious/Eyes_3.png"
        pause 0.05
        "sprites/Carlos/Serious/Eyes_2.png"
        pause 0.05
        repeat


    image Carlos_Serious_Talk:
        "sprites/Carlos/Serious/Mouth_1.png"
        pause 0.1
        "sprites/Carlos/Serious/Mouth_2.png"
        pause 0.1
        "sprites/Carlos/Serious/Mouth_3.png"
        pause 0.1
        "sprites/Carlos/Serious/Mouth_4.png"
        pause 0.1
        "sprites/Carlos/Serious/Mouth_2.png"
        pause 0.1
        repeat

    image car serious = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/Serious/Base.png",
                                (0,0), "sprites/Carlos/Serious/Mouth_1.png",
                                (0,0), "Carlos_Serious_Blink" )

    image car serious talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/Serious/Base.png",
                                (0,0), "Carlos_Serious_Talk",
                                (0,0), "Carlos_Serious_Blink")

    image car confused = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/Confused.png")

    image car gloves = LiveComposite((1920,1080),
                                (0,0), "sprites/Carlos/Gloves.png")

    image Guard_Talk:
        "sprites/Guard/Standard/Mouth_1.png"
        pause 0.1
        "sprites/Guard/Standard/Mouth_2.png"
        pause 0.1
        "sprites/Guard/Standard/Mouth_3.png"
        pause 0.1
        "sprites/Guard/Standard/Mouth_4.png"
        pause 0.1
        repeat

    image Guard_Blink:
        "sprites/Guard/Standard/Eyes_1.png"
        pause 5.0
        "sprites/Guard/Standard/Eyes_2.png"
        pause 0.04
        "sprites/Guard/Standard/Eyes_3.png"
        pause 0.04
        "sprites/Guard/Standard/Eyes_4.png"
        pause 0.04
        "sprites/Guard/Standard/Eyes_3.png"
        pause 0.04
        "sprites/Guard/Standard/Eyes_2.png"
        pause 0.04
        "sprites/Guard/Standard/Eyes_2.png"
        pause 0.04
        "sprites/Guard/Standard/Eyes_3.png"
        pause 0.04
        "sprites/Guard/Standard/Eyes_4.png"
        pause 0.04
        "sprites/Guard/Standard/Eyes_3.png"
        pause 0.04
        "sprites/Guard/Standard/Eyes_2.png"
        pause 0.04
        repeat

    image Guard_Remove_Glasses:
        "sprites/Guard/RemoveGlasses/Glasses_1.png"
        pause 0.5
        "sprites/Guard/RemoveGlasses/Glasses_2.png"
        pause 0.05
        #show white
        #pause 0.05
        #hide white
        "sprites/Guard/RemoveGlasses/Glasses_3.png"
        pause 0.05
        "sprites/Guard/RemoveGlasses/Glasses_4.png"
        pause 0.1
        "sprites/Guard/RemoveGlasses/Glasses_5.png"
        pause 0.1

    image guard glasses talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Guard/Standard/Base.png",
                                (0,0), "Guard_Talk",
                                (0,0), "sprites/Guard/Standard/Glasses.png")

    image guard glasses = LiveComposite((1920,1080),
                                (0,0), "sprites/Guard/Standard/Base.png",
                                (0,0), "sprites/Guard/Standard/Mouth_1.png",
                                (0,0), "sprites/Guard/Standard/Glasses.png")

    image guard eyes talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Guard/Standard/Base.png",
                                (0,0), "Guard_Talk",
                                (0,0), "Guard_Blink")

    image guard eyes = LiveComposite((1920,1080),
                                (0,0), "sprites/Guard/Standard/Base.png",
                                (0,0), "sprites/Guard/Standard/Mouth_1.png",
                                (0,0), "Guard_Blink")

    image guard removeglasses talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Guard/RemoveGlasses/Base.png",
                                (0,0), "Guard_Talk",
                                (0,0), "Guard_Blink",
                                (0,0), "sprites/Guard/RemoveGlasses/Glasses_1.png")

    image guard removeglasses = LiveComposite((1920,1080),
                                (0,0), "sprites/Guard/RemoveGlasses/Base.png",
                                (0,0), "sprites/Guard/Standard/Mouth_1.png",
                                (0,0), "Guard_Blink",
                                (0,0), "Guard_Remove_Glasses")

    image guard holdglasses talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Guard/RemoveGlasses/Base.png",
                                (0,0), "Guard_Talk",
                                (0,0), "Guard_Blink",
                                (0,0), "sprites/Guard/RemoveGlasses/Glasses_5.png")

    image guard holdglasses = LiveComposite((1920,1080),
                                (0,0), "sprites/Guard/RemoveGlasses/Base.png",
                                (0,0), "sprites/Guard/Standard/Mouth_1.png",
                                (0,0), "Guard_Blink",
                                (0,0), "sprites/Guard/RemoveGlasses/Glasses_5.png")

    image guard returnglasses = LiveComposite((1920,1080),
                                (0,0), "sprites/Guard/RemoveGlasses/Base.png",
                                (0,0), "sprites/Guard/Standard/Mouth_1.png",
                                (0,0), "Guard_Blink",
                                (0,0), "sprites/Guard/RemoveGlasses/Glasses_1.png")


    image Drang_Standard_Talk:
        "sprites/Drang/Standard/Mouth_1.png"
        pause 0.1
        "sprites/Drang/Standard/Mouth_2.png"
        pause 0.1
        "sprites/Drang/Standard/Mouth_3.png"
        pause 0.1
        "sprites/Drang/Standard/Mouth_4.png"
        pause 0.1
        "sprites/Drang/Standard/Mouth_2.png"
        pause 0.1
        repeat

    image Drang_Standard_Blink:
        "sprites/Drang/Standard/Eyes_1.png"
        pause 5.0
        "sprites/Drang/Standard/Eyes_2.png"
        pause 0.05
        "sprites/Drang/Standard/Eyes_3.png"
        pause 0.05
        "sprites/Drang/Standard/Eyes_4.png"
        pause 0.05
        "sprites/Drang/Standard/Eyes_3.png"
        pause 0.05
        "sprites/Drang/Standard/Eyes_2.png"
        pause 0.05
        repeat

    image drang default gdown = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Standard/Base.png",
                                (0,0), "sprites/Drang/Standard/Mouth_1.png",
                                (0,0), "Drang_Standard_Blink",
                                (0,0), "sprites/Drang/Standard/Glasses_1.png" )

    image drang default gdown talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Standard/Base.png",
                                (0,0), "Drang_Standard_Talk",
                                (0,0), "Drang_Standard_Blink",
                                (0,0), "sprites/Drang/Standard/Glasses_1.png" )

    image drang default gup = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Standard/Base.png",
                                (0,0), "sprites/Drang/Standard/Mouth_1.png",
                                (0,0), "Drang_Standard_Blink",
                                (0,0), "sprites/Drang/Standard/Glasses_2.png" )

    image drang default gup talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Standard/Base.png",
                                (0,0), "Drang_Standard_Talk",
                                (0,0), "Drang_Standard_Blink",
                                (0,0), "sprites/Drang/Standard/Glasses_2.png" )


    image Drang_Thinking_Talk:
        "sprites/Drang/Thinking/Mouth_1.png"
        pause 0.1
        "sprites/Drang/Thinking/Mouth_2.png"
        pause 0.1
        "sprites/Drang/Thinking/Mouth_3.png"
        pause 0.1
        "sprites/Drang/Thinking/Mouth_4.png"
        pause 0.1
        "sprites/Drang/Thinking/Mouth_2.png"
        pause 0.1
        repeat

    image Drang_Thinking_Blink:
        "sprites/Drang/Thinking/Eyes_1.png"
        pause 5.0
        "sprites/Drang/Thinking/Eyes_2.png"
        pause 0.05
        "sprites/Drang/Thinking/Eyes_3.png"
        pause 0.05
        "sprites/Drang/Thinking/Eyes_4.png"
        pause 0.05
        "sprites/Drang/Thinking/Eyes_3.png"
        pause 0.05
        "sprites/Drang/Thinking/Eyes_2.png"
        pause 0.05
        repeat

    image Drang_Thinking_Hand:
        "sprites/Drang/Thinking/Hand_1.png"
        pause 1.0
        "sprites/Drang/Thinking/Hand_2.png"
        pause 0.2
        "sprites/Drang/Thinking/Hand_3.png"
        pause 1.0
        "sprites/Drang/Thinking/Hand_2.png"
        pause 0.2
        repeat

    image drang think gdown = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Thinking/Base.png",
                                (0,0), "sprites/Drang/Thinking/Mouth_1.png",
                                (0,0), "Drang_Thinking_Blink",
                                (0,0), "sprites/Drang/Thinking/Glasses_1.png",
                                (0,0), "Drang_Thinking_Hand" )

    image drang think gdown talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Thinking/Base.png",
                                (0,0), "Drang_Thinking_Talk",
                                (0,0), "Drang_Thinking_Blink",
                                (0,0), "sprites/Drang/Thinking/Glasses_1.png",
                                (0,0), "Drang_Thinking_Hand"  )

    image drang think gup = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Thinking/Base.png",
                                (0,0), "sprites/Drang/Thinking/Mouth_1.png",
                                (0,0), "Drang_Thinking_Blink",
                                (0,0), "sprites/Drang/Thinking/Glasses_2.png",
                                (0,0), "Drang_Thinking_Hand"  )

    image drang think gup talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Thinking/Base.png",
                                (0,0), "Drang_Thinking_Talk",
                                (0,0), "Drang_Thinking_Blink",
                                (0,0), "sprites/Drang/Thinking/Glasses_2.png",
                                (0,0), "Drang_Thinking_Hand" )

    image Drang_Angry_Talk:
        "sprites/Drang/Angry/Mouth_1.png"
        pause 0.1
        "sprites/Drang/Angry/Mouth_2.png"
        pause 0.1
        "sprites/Drang/Angry/Mouth_3.png"
        pause 0.1
        "sprites/Drang/Angry/Mouth_4.png"
        pause 0.1
        "sprites/Drang/Angry/Mouth_2.png"
        pause 0.1
        repeat

    image Drang_Angry_Blink:
        "sprites/Drang/Angry/Eyes_1.png"
        pause 5.0
        "sprites/Drang/Angry/Eyes_2.png"
        pause 0.05
        "sprites/Drang/Angry/Eyes_3.png"
        pause 0.05
        "sprites/Drang/Angry/Eyes_4.png"
        pause 0.05
        "sprites/Drang/Angry/Eyes_3.png"
        pause 0.05
        "sprites/Drang/Angry/Eyes_2.png"
        pause 0.05
        repeat

    image drang angry gdown = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Angry/Base.png",
                                (0,0), "sprites/Drang/Angry/Mouth_1.png",
                                (0,0), "Drang_Angry_Blink",
                                (0,0), "sprites/Drang/Angry/Glasses_1.png" )

    image drang angry gdown talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Angry/Base.png",
                                (0,0), "Drang_Angry_Talk",
                                (0,0), "Drang_Angry_Blink",
                                (0,0), "sprites/Drang/Angry/Glasses_1.png" )

    image drang angry gup = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Angry/Base.png",
                                (0,0), "sprites/Drang/Angry/Mouth_1.png",
                                (0,0), "Drang_Angry_Blink",
                                (0,0), "sprites/Drang/Angry/Glasses_2.png" )

    image drang angry gup talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Angry/Base.png",
                                (0,0), "Drang_Angry_Talk",
                                (0,0), "Drang_Angry_Blink",
                                (0,0), "sprites/Drang/Angry/Glasses_2.png" )


    image Drang_Dril_Talk:
        "sprites/Drang/Dril/Mouth_1.png"
        pause 0.15
        "sprites/Drang/Dril/Mouth_2.png"
        pause 0.15
        "sprites/Drang/Dril/Mouth_3.png"
        pause 0.15
        "sprites/Drang/Dril/Mouth_4.png"
        pause 0.15
        "sprites/Drang/Dril/Mouth_2.png"
        pause 0.15
        repeat

    image Drang_Dril_Blink:
        "sprites/Drang/Dril/Eyes_1.png"
        pause 5.0
        "sprites/Drang/Dril/Eyes_2.png"
        pause 0.05
        "sprites/Drang/Dril/Eyes_3.png"
        pause 0.05
        "sprites/Drang/Dril/Eyes_4.png"
        pause 0.05
        "sprites/Drang/Dril/Eyes_3.png"
        pause 0.05
        "sprites/Drang/Dril/Eyes_2.png"
        pause 0.05
        repeat

    image drang dril gdown = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Dril/Base.png",
                                (0,0), "sprites/Drang/Dril/Mouth_1.png",
                                (0,0), "Drang_Dril_Blink",
                                (0,0), "sprites/Drang/Dril/Glasses_1.png" )

    image drang dril gdown talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Dril/Base.png",
                                (0,0), "Drang_Dril_Talk",
                                (0,0), "Drang_Dril_Blink",
                                (0,0), "sprites/Drang/Dril/Glasses_1.png" )

    image drang dril gup = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Dril/Base.png",
                                (0,0), "sprites/Drang/Dril/Mouth_1.png",
                                (0,0), "Drang_Dril_Blink",
                                (0,0), "sprites/Drang/Dril/Glasses_2.png" )

    image drang dril gup talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Dril/Base.png",
                                (0,0), "Drang_Dril_Talk",
                                (0,0), "Drang_Dril_Blink",
                                (0,0), "sprites/Drang/Dril/Glasses_2.png" )

    image Drang_Jacket_Talk:
        "sprites/Drang/Jacket/Mouth_1.png"
        pause 0.1
        "sprites/Drang/Jacket/Mouth_2.png"
        pause 0.1
        "sprites/Drang/Jacket/Mouth_3.png"
        pause 0.1
        "sprites/Drang/Jacket/Mouth_4.png"
        pause 0.1
        "sprites/Drang/Jacket/Mouth_2.png"
        pause 0.1
        repeat

    image Drang_Jacket_Arms:
        "sprites/Drang/Jacket/Arms_01.png"
        pause 0.15
        "sprites/Drang/Jacket/Arms_03.png"
        pause 0.15
        "sprites/Drang/Jacket/Arms_05.png"
        pause 0.4
        "sprites/Drang/Jacket/Arms_10.png"
        pause 0.075
        "sprites/Drang/Jacket/Arms_11.png"
        pause 0.05
        "sprites/Drang/Jacket/Arms_12.png"
        pause 0.05
        "sprites/Drang/Jacket/Arms_13.png"
        pause 0.05
        "sprites/Drang/Jacket/Arms_14.png"
        pause 0.05
        "sprites/Drang/Jacket/Arms_15.png"
        pause 0.05
        "sprites/Drang/Jacket/Arms_16.png"
        pause 0.05
        "sprites/Drang/Jacket/Arms_17.png"
        pause 0.05
        "sprites/Drang/Jacket/Arms_18.png"
        pause 0.05


    image drang jacket pop = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Jacket/Base.png",
                                (0,0), "sprites/Drang/Jacket/Mouth_1.png",
                                (0,0), "Drang_Jacket_Arms",
                                (0,0), "sprites/Drang/Jacket/Glasses.png" )

    image drang jacket pop talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Jacket/Base.png",
                                (0,0), "Drang_Jacket_Talk",
                                (0,0), "sprites/Drang/Jacket/Arms_01.png",
                                (0,0), "sprites/Drang/Jacket/Glasses.png" )

    image drang jacket popped = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Jacket/Base.png",
                                (0,0), "sprites/Drang/Jacket/Mouth_1.png",
                                (0,0), "sprites/Drang/Jacket/Arms_18.png",
                                (0,0), "sprites/Drang/Jacket/Glasses.png" )

    image drang jacket popped talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Drang/Jacket/Base.png",
                                (0,0), "Drang_Jacket_Talk",
                                (0,0), "sprites/Drang/Jacket/Arms_18.png",
                                (0,0), "sprites/Drang/Jacket/Glasses.png" )

    image Ash_Standard_Blink:
        "sprites/Ash/Standard/Eyes_1.png"
        pause 5.0
        "sprites/Ash/Standard/Eyes_2.png"
        pause 0.05
        "sprites/Ash/Standard/Eyes_3.png"
        pause 0.05
        "sprites/Ash/Standard/Eyes_4.png"
        pause 0.05
        "sprites/Ash/Standard/Eyes_3.png"
        pause 0.05
        "sprites/Ash/Standard/Eyes_2.png"
        pause 0.05
        repeat

    image Ash_Standard_Talk:
        "sprites/Ash/Standard/Mouth_1.png"
        pause 0.1
        "sprites/Ash/Standard/Mouth_2.png"
        pause 0.1
        "sprites/Ash/Standard/Mouth_3.png"
        pause 0.1
        "sprites/Ash/Standard/Mouth_4.png"
        pause 0.1
        "sprites/Ash/Standard/Mouth_2.png"
        pause 0.1
        repeat

    image ash standard = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Standard/Base.png",
                                (0,0), "sprites/Ash/Standard/Mouth_1.png",
                                (0,0), "Ash_Standard_Blink")

    image ash standard talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Standard/Base.png",
                                (0,0), "Ash_Standard_Talk",
                                (0,0), "Ash_Standard_Blink")

    image Ash_Camera_Polaroid:
        "sprites/Ash/Camera/Polaroid_1.png"
        pause 0.1
        "sprites/Ash/Camera/Polaroid_2.png"
        pause 0.1
        "sprites/Ash/Camera/Polaroid_3.png"
        pause 0.1
        "sprites/Ash/Camera/Polaroid_4.png"
        pause 0.1
        "sprites/Ash/Camera/Polaroid_5.png"
        pause 0.1
        "sprites/Ash/Camera/Polaroid_6.png"
        pause 0.1
        "sprites/Ash/Camera/Polaroid_7.png"
        pause 0.1
        "sprites/Ash/Camera/Polaroid_8.png"
        pause 0.1
        "sprites/Ash/Camera/Polaroid_9.png"
        pause 0.1
        "sprites/Ash/Camera/Polaroid_10.png"
        pause 0.1

    image Ash_Camera_Talk:
        "sprites/Ash/Camera/Mouth_1.png"
        pause 0.1
        "sprites/Ash/Camera/Mouth_2.png"
        pause 0.1
        "sprites/Ash/Camera/Mouth_3.png"
        pause 0.1
        "sprites/Ash/Camera/Mouth_4.png"
        pause 0.1
        "sprites/Ash/Camera/Mouth_2.png"
        pause 0.1
        repeat

    image ash camera = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Camera/Base.png",
                                (0,0), "sprites/Ash/Camera/Mouth_1.png",
                                (0,0), "sprites/Ash/Camera/Arms.png")

    image ash camera talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Camera/Base.png",
                                (0,0), "Ash_Camera_Talk",
                                (0,0), "sprites/Ash/Camera/Arms.png")

    image ash annoyed = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Annoyed.png")

    image ash confident = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Confident.png")

    image ash flippant = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Flippant.png")

    image ash positing = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Positing.png")

    image ash psyched = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Psyched.png")

    image ash sad = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Sad.png")

    image ash surprised = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Surprised.png")

    image ash thinking = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Thinking.png")

    image ash unsure = LiveComposite((1920,1080),
                                (0,0), "sprites/Ash/Unsure.png")


    image Bottomi_Standard_Blink:
        "sprites/Bottomi/Standard/Eyes_1.png"
        pause 5.0
        "sprites/Bottomi/Standard/Eyes_2.png"
        pause 0.05
        "sprites/Bottomi/Standard/Eyes_3.png"
        pause 0.05
        "sprites/Bottomi/Standard/Eyes_4.png"
        pause 0.05
        "sprites/Bottomi/Standard/Eyes_3.png"
        pause 0.05
        "sprites/Bottomi/Standard/Eyes_2.png"
        pause 0.05
        repeat

    image Bottomi_Standard_Talk:
        "sprites/Bottomi/Standard/Mouth_1.png"
        pause 0.1
        "sprites/Bottomi/Standard/Mouth_2.png"
        pause 0.1
        "sprites/Bottomi/Standard/Mouth_3.png"
        pause 0.1
        "sprites/Bottomi/Standard/Mouth_1.png"
        pause 0.1
        "sprites/Bottomi/Standard/Mouth_4.png"
        pause 0.1
        "sprites/Bottomi/Standard/Mouth_2.png"
        pause 0.1
        repeat

    image bottomi standard = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Standard/Base.png",
                                (0,0), "sprites/Bottomi/Standard/Mouth_1.png",
                                (0,0), "Bottomi_Standard_Blink")

    image bottomi standard talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Standard/Base.png",
                                (0,0), "Bottomi_Standard_Talk",
                                (0,0), "Bottomi_Standard_Blink")

    image bottomi apologetic = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Apologetic.png")

    image bottomi despair = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Despair.png")

    image bottomi freak = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/FreakOut.png")

    image bottomi fuzzy = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Fuzzy.png")

    image bottomi kaboom = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Kaboom.png")

    image bottomi mad = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Mad.png")

    image bottomi nervous = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Nervous.png")

    image bottomi remembering = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Remembering.png")

    image bottomi sad = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Sad.png")



    image chritude conceited = LiveComposite((1920,1080),
                                (0,0), "sprites/Chritude/Conceited.png")

    image chritude glitter = LiveComposite((1920,1080),
                                (0,0), "sprites/Chritude/Glitter.png")

    image chritude laugh = LiveComposite((1920,1080),
                                (0,0), "sprites/Chritude/Laugh.png")

    image chritude outrage = LiveComposite((1920,1080),
                                (0,0), "sprites/Chritude/Outrage.png")

    image chritude sad = LiveComposite((1920,1080),
                                (0,0), "sprites/Chritude/Sad.png")

    image chritude standard = LiveComposite((1920,1080),
                                (0,0), "sprites/Chritude/Standard.png")

init python:
    def wdefvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("mir default talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("mir default")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def wdefos(event, interact=True, **kwargs):
        if event == "show":
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def wcasevoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("mir casefile talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("mir casefile")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def wannoyvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("mir annoy talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("mir annoy base")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")


    def wangryvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("mir angry talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("mir angry")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def whattipvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("mir hattip talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("mir hattip")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def wrecoilvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("mir recoil talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("mir recoil base")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def wthinkvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("mir thinking talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("mir thinking")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def wgotchavoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("mir gotcha")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("mir gotcha")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def wholdonvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("mir holdon")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("mir holdon")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def astandardvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("ash standard talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("ash standard")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def acameravoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("ash camera talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("ash camera")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def aannoyedvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("ash annoyed")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("ash annoyed")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def aconfidentvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("ash confident")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("ash confident")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def aflippantvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("ash flippant")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("ash flippant")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def apositingvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("ash positing")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("ash positing")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def apsychedvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("ash psyched")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("ash psyched")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def asadvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("ash sad")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("ash sad")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def asurprisedvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("ash surprised")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("ash surprised")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def athinkingvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("ash thinking")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("ash thinking")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def aunsurevoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("ash unsure")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("ash unsure")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def cdefvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("car default talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("car default")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def cagitvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("car agitated talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("car agitated")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def cwhisvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("car whisper")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("car whisper")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def cliftvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("car liftdrink talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("car liftdrink")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def choldvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("car holdingdrink talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("car holdingdrink")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def cservoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("car serious talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("car serious")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def cconfusevoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("car confused")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("car confused")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def cglovesvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("car gloves")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("car gloves")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def gglassesvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("guard glasses talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("guard glasses")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def geyesvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("guard eyes talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("guard eyes")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def gremglassesvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("guard removeglasses talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("guard removeglasses")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def gholdglassesvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("guard holdglasses talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("guard holdglasses")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def greturnglassesvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("guard removeglasses talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("guard returnglasses")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def ddefgdownvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang default talk gdown")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang default gdown")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def ddefgupvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang default talk gup")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang default gup")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def dthinkgdownvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang think gdown talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang think gdown")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def dthinkgupvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang think gup talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang think gup")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def dangrygdownvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang angry gdown talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang angry gdown")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def dangrygupvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang angry gup talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang angry gup")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def ddrilgdownvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang dril gdown talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang dril gdown")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def ddrilgupvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang dril gup talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang dril gup")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def djpopvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang jacket pop talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang jacket pop")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def djpoppedvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("drang jacket popped talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("drang jacket popped")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def bstandardvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi standard talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi standard")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def bapologeticvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi apologetic")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi apologetic")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def bdespairvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi despair")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi despair")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def bfreakvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi freak")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi freak")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def bfuzzyvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi fuzzy")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi fuzzy")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def bkaboomvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi kaboom")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi kaboom")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def bmadvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi mad")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi mad")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def bnervousvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi nervous")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi nervous")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def bremembervoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi remembering")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi remembering")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def bsadvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi sad")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi sad")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def pconceitedvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("chritude conceited")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("chritude conceited")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def pglittervoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("chritude glitter")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("chritude glitter")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def plaughvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("chritude laugh")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("chritude laugh")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def poutragevoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("chritude outrage")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("chritude outrage")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def psadvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("chritude sad")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("chritude sad")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def pstandardvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("chritude standard")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("chritude standard")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def typingvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.sound.play("sound/typewriter.ogg", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")


init python:
    for file in renpy.list_files():
        if file.endswith('.png'): ##this is your file type
            name = file.replace('sprites/', '').replace('.png','')#Here we add ‘flip’ to our image
            renpy.image(name, Image(file))
