init:
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

    image Miranda_Annoyed_Base_Mouth:
        pause 0.12
        pause 0.16
        pause 0.05
        pause 0.05
        pause 0.05
        pause 0.16
        pause 0.09
        "sprites/Miranda/Annoyed/Mouth_1.png"
        pause 0.09

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
                                (0,0), "Miranda_Annoyed_Base",
                                (0,0), "Miranda_Annoyed_Base_Mouth")

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

    image Miranda_Gotcha_Talk:
        "sprites/Miranda/Gotcha/Mouth_1.png"
        pause 0.1
        "sprites/Miranda/Gotcha/Mouth_2.png"
        pause 0.1
        "sprites/Miranda/Gotcha/Mouth_3.png"
        pause 0.1
        "sprites/Miranda/Gotcha/Mouth_4.png"
        pause 0.1
        "sprites/Miranda/Gotcha/Mouth_2.png"
        pause 0.1
        repeat

    image Miranda_Gotcha_Arm:
        "sprites/Miranda/Gotcha/Arm_1.png"
        pause 0.33
        "sprites/Miranda/Gotcha/Arm_2.png"
        pause 0.1
        "sprites/Miranda/Gotcha/Arm_3.png"
        pause 0.33

    image Miranda_Gotcha_Hat:
        "sprites/Miranda/Gotcha/Hat_1.png"
        pause 0.33
        "sprites/Miranda/Gotcha/Hat_2.png"
        pause 0.1
        "sprites/Miranda/Gotcha/Hat_3.png"
        pause 0.33

    image mir gotcha = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/Gotcha/Arm_3.png",
                                (0,0), "sprites/Miranda/Gotcha/Base.png",
                                (0,0), "sprites/Miranda/Gotcha/Mouth_1.png",
                                (0,0), "sprites/Miranda/Gotcha/Hat_3.png")

    image mir gotcha talk = LiveComposite((1920,1080),
                                (0,0), "Miranda_Gotcha_Arm",
                                (0,0), "sprites/Miranda/Gotcha/Base.png",
                                (0,0), "Miranda_Gotcha_Talk",
                                (0,0), "Miranda_Gotcha_Hat")

    image Miranda_HoldOn_Blink:
        "sprites/Miranda/HoldOn/Eyes_1.png"
        pause 6.0
        "sprites/Miranda/HoldOn/Eyes_2.png"
        pause 0.05
        "sprites/Miranda/HoldOn/Eyes_3.png"
        pause 0.05
        "sprites/Miranda/HoldOn/Eyes_4.png"
        pause 0.05
        "sprites/Miranda/HoldOn/Eyes_3.png"
        pause 0.05
        "sprites/Miranda/HoldOn/Eyes_2.png"
        pause 0.05
        repeat

    image Miranda_HoldOn_Talk:
        "sprites/Miranda/HoldOn/Mouth_1.png"
        pause 0.1
        "sprites/Miranda/HoldOn/Mouth_2.png"
        pause 0.1
        "sprites/Miranda/HoldOn/Mouth_3.png"
        pause 0.1
        "sprites/Miranda/HoldOn/Mouth_4.png"
        pause 0.1
        "sprites/Miranda/HoldOn/Mouth_2.png"
        pause 0.1
        repeat

    image mir holdon = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/HoldOn/Base.png",
                                (0,0), "sprites/Miranda/HoldOn/Mouth_1.png",
                                (0,0), "Miranda_HoldOn_Blink")

    image mir holdon talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/HoldOn/Base.png",
                                (0,0), "Miranda_HoldOn_Talk",
                                (0,0), "Miranda_HoldOn_Blink")

    image Miranda_Confused_Blink:
        "sprites/Miranda/Confused/Eyes_1.png"
        pause 6.0
        "sprites/Miranda/Confused/Eyes_2.png"
        pause 0.05
        "sprites/Miranda/Confused/Eyes_3.png"
        pause 0.05
        "sprites/Miranda/Confused/Eyes_4.png"
        pause 0.05
        "sprites/Miranda/Confused/Eyes_3.png"
        pause 0.05
        "sprites/Miranda/Confused/Eyes_2.png"
        pause 0.05
        repeat

    image Miranda_Confused_Talk:
        "sprites/Miranda/Confused/Mouth_1.png"
        pause 0.1
        "sprites/Miranda/Confused/Mouth_2.png"
        pause 0.1
        "sprites/Miranda/Confused/Mouth_3.png"
        pause 0.1
        "sprites/Miranda/Confused/Mouth_4.png"
        pause 0.1
        "sprites/Miranda/Confused/Mouth_2.png"
        pause 0.1
        repeat

    image mir confused = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/Confused/Base.png",
                                (0,0), "sprites/Miranda/Confused/Mouth_1.png",
                                (0,0), "Miranda_Confused_Blink")

    image mir confused talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/Confused/Base.png",
                                (0,0), "Miranda_Confused_Talk",
                                (0,0), "Miranda_Confused_Blink")

    image Miranda_ObjectionA_Talk:
        "sprites/Miranda/Objection/Mouth_A1.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_A2.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_A3.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_A4.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_A2.png"
        pause 0.1
        repeat

    image Miranda_ObjectionC_Talk:
        pause 0.28
        "sprites/Miranda/Objection/Mouth_C1.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C2.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C3.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C4.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C2.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C1.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C2.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C3.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C4.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C2.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C1.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C2.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C3.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C4.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C2.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C1.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C2.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C3.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C4.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C2.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C1.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C2.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C3.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C4.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C2.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C1.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C2.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C3.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C4.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C2.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C1.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C2.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C3.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C4.png"
        pause 0.1
        "sprites/Miranda/Objection/Mouth_C2.png"
        pause 0.1

    image Miranda_Objection_Blink:
        "sprites/Miranda/Objection/Eyes_C1.png"
        pause 6.0
        "sprites/Miranda/Objection/Eyes_C2.png"
        pause 0.05
        "sprites/Miranda/Objection/Eyes_C3.png"
        pause 0.05
        "sprites/Miranda/Objection/Eyes_C4.png"
        pause 0.05
        "sprites/Miranda/Objection/Eyes_C3.png"
        pause 0.05
        "sprites/Miranda/Objection/Eyes_C2.png"
        pause 0.05
        repeat

    image Miranda_Objection_Arms:
        "sprites/Miranda/Objection/Arm_A1.png"
        pause 0.07
        "sprites/Miranda/Objection/Arm_A2.png"
        pause 0.07
        "sprites/Miranda/Objection/Arm_B.png"
        pause 0.07
        "sprites/Miranda/Objection/Arm_C1.png"
        pause 0.07
        "sprites/Miranda/Objection/Arm_C2.png"
        pause 0.07

    image Miranda_Objection_Base:
        "sprites/Miranda/Objection/Base_A.png"
        pause 0.14
        "sprites/Miranda/Objection/Base_B.png"
        pause 0.14
        "sprites/Miranda/Objection/Base_C.png"
        pause 0.14

    image mir objectionA = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/Objection/Base_A.png",
                                (0,0), "sprites/Miranda/Objection/Mouth_A1.png",
                                (0,0), "sprites/Miranda/Objection/Arm_A1.png")

    image mir objectionA talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/Objection/Base_A.png",
                                (0,0), "Miranda_ObjectionA_Talk",
                                (0,0), "sprites/Miranda/Objection/Arm_A1.png")

    image mir objectionC = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/Objection/Base_C.png",
                                (0,0), "sprites/Miranda/Objection/Mouth_C4.png",
                                (0,0), "Miranda_Objection_Blink",
                                (0,0), "sprites/Miranda/Objection/Arm_C2.png")

    image mir objectionC talk = LiveComposite((1920,1080),
                                (0,0), "Miranda_Objection_Base",
                                (0,0), "Miranda_ObjectionC_Talk",
                                (0,0), "Miranda_Objection_Blink",
                                (0,0), "Miranda_Objection_Arms")

    image Miranda_Settle_Hat:
        "sprites/Miranda/Settle/Hat_1.png"
        pause 0.07
        "sprites/Miranda/Settle/Hat_2.png"
        pause 0.07
        "sprites/Miranda/Settle/Hat_3.png"
        pause 0.07
        "sprites/Miranda/Settle/Hat_4.png"
        pause 0.07
        "sprites/Miranda/Settle/Hat_5.png"
        pause 0.07
        "sprites/Miranda/Settle/Hat_6.png"
        pause 0.07
        "sprites/Miranda/Settle/Hat_7.png"
        pause 0.07
        "sprites/Miranda/Settle/Hat_8.png"
        pause 0.07
        "sprites/Miranda/Settle/Hat_9.png"
        pause 0.07
        "sprites/Miranda/Settle/Hat_10.png"
        pause 0.07
        "sprites/Miranda/Settle/Hat_11.png"
        pause 0.07
        "sprites/Miranda/Settle/Hat_12.png"
        pause 0.07
        "sprites/Miranda/Settle/Hat_13.png"
        pause 0.07
        "sprites/Miranda/Settle/Hat_14.png"
        pause 0.07

    image mir settle = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/Settle/Base.png",
                                (0,0), "sprites/Miranda/Default/Mouth_1.png",
                                (0,0), "Miranda_Default_Blink",
                                (0,0), "sprites/Miranda/Settle/Hat_14.png")

    image mir settle talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Miranda/Settle/Base.png",
                                (0,0), "Miranda_Default_Talk",
                                (0,0), "Miranda_Default_Blink",
                                (0,0), "Miranda_Settle_Hat")
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
            renpy.show("mir gotcha talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("mir gotcha")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def wholdonvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("mir holdon talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("mir holdon")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def wconfusedvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("mir confused talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("mir confused")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def wobjectionAvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("mir objectionA talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("mir objectionA")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def wobjectionCvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("mir objectionC talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("mir objectionC")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def wsettlevoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("mir settle talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("mir settle")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")
