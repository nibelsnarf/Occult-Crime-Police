init:
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

    image Bottomi_Standard_Implant:
        "sprites/Bottomi/Standard/Implant_1.png"
        pause 3.0
        "sprites/Bottomi/Standard/Implant_2.png"
        pause 0.05
        "sprites/Bottomi/Standard/Implant_1.png"
        pause 0.05
        "sprites/Bottomi/Standard/Implant_2.png"
        pause 0.05

    image bottomi standard = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Standard/Base.png",
                                (0,0), "sprites/Bottomi/Standard/Mouth_1.png",
                                (0,0), "Bottomi_Standard_Blink",
                                (0,0), "sprites/Bottomi/Standard/Hat.png")

    image bottomi standard talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Standard/Base.png",
                                (0,0), "Bottomi_Standard_Talk",
                                (0,0), "Bottomi_Standard_Blink",
                                (0,0), "sprites/Bottomi/Standard/Hat.png")

    image bottomi standard hatless = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Standard/Base.png",
                                (0,0), "sprites/Bottomi/Standard/Mouth_1.png",
                                (0,0), "Bottomi_Standard_Blink",
                                (0,0), "Bottomi_Standard_Implant")

    image bottomi standard hatless talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Standard/Base.png",
                                (0,0), "Bottomi_Standard_Talk",
                                (0,0), "Bottomi_Standard_Blink",
                                (0,0), "Bottomi_Standard_Implant")

    image Bottomi_Apology_Blink:
        "sprites/Bottomi/Apology/Eyes_1.png"
        pause 5.0
        "sprites/Bottomi/Apology/Eyes_2.png"
        pause 0.05
        "sprites/Bottomi/Apology/Eyes_3.png"
        pause 0.05
        "sprites/Bottomi/Apology/Eyes_4.png"
        pause 0.05
        "sprites/Bottomi/Apology/Eyes_5.png"
        pause 0.05
        "sprites/Bottomi/Apology/Eyes_4.png"
        pause 0.05
        "sprites/Bottomi/Apology/Eyes_3.png"
        pause 0.05
        "sprites/Bottomi/Apology/Eyes_2.png"
        pause 0.05
        repeat

    image Bottomi_Apology_Talk:
        "sprites/Bottomi/Apology/Mouth_1.png"
        pause 0.1
        "sprites/Bottomi/Apology/Mouth_2.png"
        pause 0.1
        "sprites/Bottomi/Apology/Mouth_3.png"
        pause 0.1
        "sprites/Bottomi/Apology/Mouth_4.png"
        pause 0.1
        "sprites/Bottomi/Apology/Mouth_2.png"
        pause 0.1
        repeat

    image Bottomi_Apology_Implant:
        "sprites/Bottomi/Apology/Implant_1.png"
        pause 3.0
        "sprites/Bottomi/Apology/Implant_2.png"
        pause 0.05
        "sprites/Bottomi/Apology/Implant_1.png"
        pause 0.05
        "sprites/Bottomi/Apology/Implant_2.png"
        pause 0.05

    image Bottomi_Apology_Arm:
        "sprites/Bottomi/Apology/Arm_1.png"
        pause 0.2
        "sprites/Bottomi/Apology/Arm_2.png"
        pause 0.2
        "sprites/Bottomi/Apology/Arm_3.png"
        pause 0.2
        "sprites/Bottomi/Apology/Arm_2.png"
        pause 0.2

    image bottomi apologetic = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Apology/Base.png",
                                (0,0), "sprites/Bottomi/Apology/Mouth_1.png",
                                (0,0), "Bottomi_Apology_Blink",
                                (0,0), "Bottomi_Apology_Arm",
                                (0,0), "sprites/Bottomi/Apology/Hat.png")

    image bottomi apologetic talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Apology/Base.png",
                                (0,0), "Bottomi_Apology_Talk",
                                (0,0), "Bottomi_Apology_Blink",
                                (0,0), "Bottomi_Apology_Arm",
                                (0,0), "sprites/Bottomi/Apology/Hat.png")

    image bottomi apologetic hatless = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Apology/Base.png",
                                (0,0), "sprites/Bottomi/Apology/Mouth_1.png",
                                (0,0), "Bottomi_Apology_Blink",
                                (0,0), "Bottomi_Apology_Arm",
                                (0,0), "Bottomi_Apology_Implant")

    image bottomi apologetic hatless talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Apology/Base.png",
                                (0,0), "Bottomi_Apology_Talk",
                                (0,0), "Bottomi_Apology_Blink",
                                (0,0), "Bottomi_Apology_Arm",
                                (0,0), "Bottomi_Apology_Implant")

    image Bottomi_Despair_Blink:
        "sprites/Bottomi/Despair/Eyes_1.png"
        pause 5.0
        "sprites/Bottomi/Despair/Eyes_2.png"
        pause 0.05
        "sprites/Bottomi/Despair/Eyes_3.png"
        pause 0.05
        "sprites/Bottomi/Despair/Eyes_4.png"
        pause 0.05
        "sprites/Bottomi/Despair/Eyes_5.png"
        pause 0.05
        "sprites/Bottomi/Despair/Eyes_4.png"
        pause 0.05
        "sprites/Bottomi/Despair/Eyes_3.png"
        pause 0.05
        "sprites/Bottomi/Despair/Eyes_2.png"
        pause 0.05
        repeat

    image Bottomi_Despair_Talk:
        "sprites/Bottomi/Despair/Mouth_1.png"
        pause 0.1
        "sprites/Bottomi/Despair/Mouth_2.png"
        pause 0.1
        "sprites/Bottomi/Despair/Mouth_3.png"
        pause 0.1
        "sprites/Bottomi/Despair/Mouth_4.png"
        pause 0.1
        "sprites/Bottomi/Despair/Mouth_2.png"
        pause 0.1
        repeat

    image Bottomi_Despair_Implant:
        "sprites/Bottomi/Despair/Implant_1.png"
        pause 3.0
        "sprites/Bottomi/Despair/Implant_2.png"
        pause 0.05
        "sprites/Bottomi/Despair/Implant_1.png"
        pause 0.05
        "sprites/Bottomi/Despair/Implant_2.png"
        pause 0.05

    image bottomi despair = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Despair/Base.png",
                                (0,0), "sprites/Bottomi/Despair/Mouth_1.png",
                                (0,0), "Bottomi_Despair_Blink",
                                (0,0), "sprites/Bottomi/Despair/Hat.png")

    image bottomi despair talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Despair/Base.png",
                                (0,0), "Bottomi_Despair_Talk",
                                (0,0), "Bottomi_Despair_Blink",
                                (0,0), "sprites/Bottomi/Despair/Hat.png")

    image bottomi despair hatless = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Despair/Base.png",
                                (0,0), "sprites/Bottomi/Despair/Mouth_1.png",
                                (0,0), "Bottomi_Despair_Blink",
                                (0,0), "Bottomi_Despair_Implant")

    image bottomi despair hatless talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Despair/Base.png",
                                (0,0), "Bottomi_Despair_Talk",
                                (0,0), "Bottomi_Despair_Blink",
                                (0,0), "Bottomi_Despair_Implant")

    image Bottomi_FreakOut_Base:
        "sprites/Bottomi/FreakOut/Base_1.png"
        pause 0.05
        "sprites/Bottomi/FreakOut/Base_2.png"
        pause 0.05
        "sprites/Bottomi/FreakOut/Base_3.png"
        pause 0.05
        "sprites/Bottomi/FreakOut/Base_2.png"
        pause 0.05
        "sprites/Bottomi/FreakOut/Base_1.png"
        pause 0.1
        "sprites/Bottomi/FreakOut/Base_1.png"
        pause 0.1
        "sprites/Bottomi/FreakOut/Base_2.png"
        pause 0.1
        "sprites/Bottomi/FreakOut/Base_3.png"
        pause 0.1
        "sprites/Bottomi/FreakOut/Base_2.png"
        pause 0.1
        "sprites/Bottomi/FreakOut/Base_1.png"
        pause 0.5
        "sprites/Bottomi/FreakOut/Base_1.png"
        pause 0.5
        "sprites/Bottomi/FreakOut/Base_2.png"
        pause 0.5
        "sprites/Bottomi/FreakOut/Base_3.png"
        pause 0.5
        "sprites/Bottomi/FreakOut/Base_2.png"
        pause 0.5
        "sprites/Bottomi/FreakOut/Base_1.png"
        pause 1.0
        "sprites/Bottomi/FreakOut/Base_1.png"
        pause 1.0
        "sprites/Bottomi/FreakOut/Base_2.png"
        pause 1.0
        "sprites/Bottomi/FreakOut/Base_3.png"
        pause 1.0
        "sprites/Bottomi/FreakOut/Base_2.png"
        pause 1.0
        "sprites/Bottomi/FreakOut/Base_1.png"
        pause 0.1

    image Bottomi_FreakOut_Hat:
          "sprites/Bottomi/FreakOut/Hat_1.png"
          pause 0.05
          "sprites/Bottomi/FreakOut/Hat_2.png"
          pause 0.05
          "sprites/Bottomi/FreakOut/Hat_3.png"
          pause 0.05
          "sprites/Bottomi/FreakOut/Hat_2.png"
          pause 0.05
          "sprites/Bottomi/FreakOut/Hat_1.png"
          pause 0.1
          "sprites/Bottomi/FreakOut/Hat_1.png"
          pause 0.1
          "sprites/Bottomi/FreakOut/Hat_2.png"
          pause 0.1
          "sprites/Bottomi/FreakOut/Hat_3.png"
          pause 0.1
          "sprites/Bottomi/FreakOut/Hat_2.png"
          pause 0.1
          "sprites/Bottomi/FreakOut/Hat_1.png"
          pause 0.5
          "sprites/Bottomi/FreakOut/Hat_1.png"
          pause 0.5
          "sprites/Bottomi/FreakOut/Hat_2.png"
          pause 0.5
          "sprites/Bottomi/FreakOut/Hat_3.png"
          pause 0.5
          "sprites/Bottomi/FreakOut/Hat_2.png"
          pause 0.5
          "sprites/Bottomi/FreakOut/Hat_1.png"
          pause 1.0
          "sprites/Bottomi/FreakOut/Hat_1.png"
          pause 1.0
          "sprites/Bottomi/FreakOut/Hat_2.png"
          pause 1.0
          "sprites/Bottomi/FreakOut/Hat_3.png"
          pause 1.0
          "sprites/Bottomi/FreakOut/Hat_2.png"
          pause 1.0
          "sprites/Bottomi/FreakOut/Hat_1.png"
          pause 0.1

    image bottomi freak = LiveComposite((1920,1080),
                                (0,0), "Bottomi_FreakOut_Base",
                                (0,0), "Bottomi_FreakOut_Hat")

    image bottomi freak hatless = LiveComposite((1920,1080),
                                (0,0), "Bottomi_FreakOut_Base")

    image Bottomi_Fuzzy_Talk:
        "sprites/Bottomi/Fuzzy/Mouth_1.png"
        pause 0.1
        "sprites/Bottomi/Fuzzy/Mouth_2.png"
        pause 0.1
        "sprites/Bottomi/Fuzzy/Mouth_3.png"
        pause 0.1
        "sprites/Bottomi/Fuzzy/Mouth_4.png"
        pause 0.1
        "sprites/Bottomi/Fuzzy/Mouth_2.png"
        pause 0.1
        repeat

    image Bottomi_Fuzzy_Bonk:
        "sprites/Bottomi/Fuzzy/Bonk_1.png"
        pause 0.07
        "sprites/Bottomi/Fuzzy/Bonk_2.png"
        pause 0.07
        "sprites/Bottomi/Fuzzy/Bonk_3.png"
        pause 0.07
        "sprites/Bottomi/Fuzzy/Bonk_4.png"
        pause 0.07
        "sprites/Bottomi/Fuzzy/Bonk_5.png"
        pause 0.07
        "sprites/Bottomi/Fuzzy/Bonk_6.png"
        pause 0.07
        "sprites/Bottomi/Fuzzy/Bonk_7.png"
        pause 0.07
        "sprites/Bottomi/Fuzzy/Bonk_8.png"
        pause 0.07
        "sprites/Bottomi/Fuzzy/Bonk_9.png"
        pause 0.07
        "sprites/Bottomi/Fuzzy/Bonk_10.png"
        pause 0.07
        "sprites/Bottomi/Fuzzy/Bonk_11.png"
        pause 0.07
        "sprites/Bottomi/Fuzzy/Bonk_12.png"
        pause 0.07
        "sprites/Bottomi/Fuzzy/Bonk_13.png"
        pause 0.07
        "sprites/Bottomi/Fuzzy/Bonk_14.png"
        pause 0.07
        "sprites/Bottomi/Fuzzy/Bonk_15.png"
        pause 0.07

    image bottomi fuzzy = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Fuzzy/Base.png",
                                (0,0), "Bottomi_Fuzzy_Bonk")

    image bottomi fuzzy talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Fuzzy/Base.png",
                                (0,0), "Bottomi_Fuzzy_Talk")

    image bottomi fuzzy hatless = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Fuzzy/Base.png",
                                (0,0), "Bottomi_Fuzzy_Bonk")

    image bottomi fuzzy hatless talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Fuzzy/Base.png",
                                (0,0), "Bottomi_Fuzzy_Talk")

    image Bottomi_Kaboom_Base:
        "sprites/Bottomi/Explode/Base_1.png"
        pause 0.6
        "sprites/Bottomi/Explode/Base_2.png"
        pause 0.6
        "sprites/Bottomi/Explode/Base_3.png"
        pause 0.6
        "sprites/Bottomi/Explode/Base_4.png"
        pause 0.6
        "sprites/Bottomi/Explode/Base_5.png"
        pause 0.6
        "sprites/Bottomi/Explode/Explode_1.png"
        pause 0.6

    image Bottomi_Kaboom_Hat:
        "sprites/Bottomi/Explode/Hat_1.png"
        pause 0.6
        "sprites/Bottomi/Explode/Hat_2.png"
        pause 0.6
        "sprites/Bottomi/Explode/Hat_3.png"
        pause 0.6
        "sprites/Bottomi/Explode/Hat_4.png"
        pause 0.6
        "sprites/Bottomi/Explode/Hat_5.png"
        pause 0.6
        "sprites/Bottomi/Explode/Explode_1.png"
        pause 0.6

    image Bottomi_Kaboom_Explode:
        "sprites/Bottomi/Explode/Explode_1.png"
        pause 0.6
        "sprites/Bottomi/Explode/Explode_2.png"
        pause 0.6
        "sprites/Bottomi/Explode/Explode_3.png"
        pause 0.6
        "sprites/Bottomi/Explode/Explode_4.png"
        pause 0.6
        "sprites/Bottomi/Explode/Explode_5.png"
        pause 0.6
        "sprites/Bottomi/Explode/Explode_1.png"
        pause 0.6

    image bottomi kaboom = LiveComposite((1920,1080),
                                (0,0), "Bottomi_Kaboom_Base",
                                (0,0), "Bottomi_Kaboom_Hat")

    image bottomi kaboom hatless = LiveComposite((1920,1080),
                                (0,0), "Bottomi_Kaboom_Base",
                                (0,0), "Bottomi_Kaboom_Explode")

    image Bottomi_Mad_Blink:
        "sprites/Bottomi/Mad/Eyes_1.png"
        pause 5.0
        "sprites/Bottomi/Mad/Eyes_2.png"
        pause 0.05
        "sprites/Bottomi/Mad/Eyes_3.png"
        pause 0.05
        "sprites/Bottomi/Mad/Eyes_4.png"
        pause 0.05
        "sprites/Bottomi/Mad/Eyes_5.png"
        pause 0.05
        "sprites/Bottomi/Mad/Eyes_4.png"
        pause 0.05
        "sprites/Bottomi/Mad/Eyes_3.png"
        pause 0.05
        "sprites/Bottomi/Mad/Eyes_2.png"
        pause 0.05
        repeat

    image Bottomi_Mad_Talk:
        "sprites/Bottomi/Mad/Mouth_1.png"
        pause 0.1
        "sprites/Bottomi/Mad/Mouth_2.png"
        pause 0.1
        "sprites/Bottomi/Mad/Mouth_3.png"
        pause 0.1
        "sprites/Bottomi/Mad/Mouth_4.png"
        pause 0.1
        "sprites/Bottomi/Mad/Mouth_2.png"
        pause 0.1
        repeat

    image Bottomi_Mad_Implant:
        "sprites/Bottomi/Mad/Implant_1.png"
        pause 3.0
        "sprites/Bottomi/Mad/Implant_2.png"
        pause 0.05
        "sprites/Bottomi/Mad/Implant_1.png"
        pause 0.05
        "sprites/Bottomi/Mad/Implant_2.png"
        pause 0.05

    image Bottomi_Mad_Arms:
        "sprites/Bottomi/Mad/Arms_1.png"
        pause 0.1
        "sprites/Bottomi/Mad/Arms_2.png"
        pause 0.1
        repeat

    image bottomi mad = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Mad/Base.png",
                                (0,0), "sprites/Bottomi/Mad/Mouth_1.png",
                                (0,0), "Bottomi_Mad_Blink",
                                (0,0), "Bottomi_Mad_Arms",
                                (0,0), "sprites/Bottomi/Mad/Hat.png")

    image bottomi mad talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Mad/Base.png",
                                (0,0), "Bottomi_Mad_Talk",
                                (0,0), "Bottomi_Mad_Blink",
                                (0,0), "Bottomi_Mad_Arms",
                                (0,0), "sprites/Bottomi/Mad/Hat.png")

    image bottomi mad hatless = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Mad/Base.png",
                                (0,0), "sprites/Bottomi/Mad/Mouth_1.png",
                                (0,0), "Bottomi_Mad_Blink",
                                (0,0), "Bottomi_Mad_Arms",
                                (0,0), "Bottomi_Mad_Implant")

    image bottomi mad hatless talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Mad/Base.png",
                                (0,0), "Bottomi_Mad_Talk",
                                (0,0), "Bottomi_Mad_Blink",
                                (0,0), "Bottomi_Mad_Arms",
                                (0,0), "Bottomi_Mad_Implant")


    image Bottomi_Nervous_Blink:
        "sprites/Bottomi/Nervous/Eyes_1.png"
        pause 5.0
        "sprites/Bottomi/Nervous/Eyes_2.png"
        pause 0.05
        "sprites/Bottomi/Nervous/Eyes_3.png"
        pause 0.05
        "sprites/Bottomi/Nervous/Eyes_4.png"
        pause 0.05
        "sprites/Bottomi/Nervous/Eyes_5.png"
        pause 0.05
        "sprites/Bottomi/Nervous/Eyes_4.png"
        pause 0.05
        "sprites/Bottomi/Nervous/Eyes_3.png"
        pause 0.05
        "sprites/Bottomi/Nervous/Eyes_2.png"
        pause 0.05
        repeat

    image Bottomi_Nervous_Talk:
        "sprites/Bottomi/Nervous/Mouth_1.png"
        pause 0.1
        "sprites/Bottomi/Nervous/Mouth_2.png"
        pause 0.1
        "sprites/Bottomi/Nervous/Mouth_3.png"
        pause 0.1
        "sprites/Bottomi/Nervous/Mouth_4.png"
        pause 0.1
        "sprites/Bottomi/Nervous/Mouth_2.png"
        pause 0.1
        repeat

    image Bottomi_Nervous_Implant:
        "sprites/Bottomi/Nervous/Implant_1.png"
        pause 3.0
        "sprites/Bottomi/Nervous/Implant_2.png"
        pause 0.05
        "sprites/Bottomi/Nervous/Implant_1.png"
        pause 0.05
        "sprites/Bottomi/Nervous/Implant_2.png"
        pause 0.05

    image Bottomi_Nervous_Arms:
        "sprites/Bottomi/Nervous/Arms_1.png"
        pause 0.07
        "sprites/Bottomi/Nervous/Arms_2.png"
        pause 0.07
        "sprites/Bottomi/Nervous/Arms_3.png"
        pause 0.07
        "sprites/Bottomi/Nervous/Arms_4.png"
        pause 0.07
        "sprites/Bottomi/Nervous/Arms_5.png"
        pause 0.07
        repeat

    image bottomi nervous = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Nervous/Base.png",
                                (0,0), "sprites/Bottomi/Nervous/Mouth_1.png",
                                (0,0), "Bottomi_Nervous_Blink",
                                (0,0), "Bottomi_Nervous_Arms",
                                (0,0), "sprites/Bottomi/Nervous/Hat.png")

    image bottomi nervous talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Nervous/Base.png",
                                (0,0), "Bottomi_Nervous_Talk",
                                (0,0), "Bottomi_Nervous_Blink",
                                (0,0), "Bottomi_Nervous_Arms",
                                (0,0), "sprites/Bottomi/Nervous/Hat.png")

    image bottomi nervous hatless = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Nervous/Base.png",
                                (0,0), "sprites/Bottomi/Nervous/Mouth_1.png",
                                (0,0), "Bottomi_Nervous_Blink",
                                (0,0), "Bottomi_Nervous_Arms",
                                (0,0), "Bottomi_Nervous_Implant")

    image bottomi nervous hatless talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Nervous/Base.png",
                                (0,0), "Bottomi_Nervous_Talk",
                                (0,0), "Bottomi_Nervous_Blink",
                                (0,0), "Bottomi_Nervous_Arms",
                                (0,0), "Bottomi_Nervous_Implant")

    image Bottomi_Remember_Blink:
        "sprites/Bottomi/Remember/Eyes_1.png"
        pause 5.0
        "sprites/Bottomi/Remember/Eyes_2.png"
        pause 0.05
        "sprites/Bottomi/Remember/Eyes_3.png"
        pause 0.05
        "sprites/Bottomi/Remember/Eyes_4.png"
        pause 0.05
        "sprites/Bottomi/Remember/Eyes_3.png"
        pause 0.05
        "sprites/Bottomi/Remember/Eyes_2.png"
        pause 0.05
        repeat

    image Bottomi_Remember_Talk:
        "sprites/Bottomi/Remember/Mouth_1.png"
        pause 0.1
        "sprites/Bottomi/Remember/Mouth_2.png"
        pause 0.1
        "sprites/Bottomi/Remember/Mouth_3.png"
        pause 0.1
        "sprites/Bottomi/Remember/Mouth_1.png"
        pause 0.1
        "sprites/Bottomi/Remember/Mouth_4.png"
        pause 0.1
        "sprites/Bottomi/Remember/Mouth_2.png"
        pause 0.1
        repeat

    image Bottomi_Remember_Implant:
        "sprites/Bottomi/Remember/Implant_1.png"
        pause 3.0
        "sprites/Bottomi/Remember/Implant_2.png"
        pause 0.05
        "sprites/Bottomi/Remember/Implant_1.png"
        pause 0.05
        "sprites/Bottomi/Remember/Implant_2.png"
        pause 0.05

    image bottomi remembering = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Remember/Base.png",
                                (0,0), "sprites/Bottomi/Remember/Mouth_1.png",
                                (0,0), "Bottomi_Remember_Blink",
                                (0,0), "sprites/Bottomi/Remember/Hat.png")

    image bottomi remembering talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Remember/Base.png",
                                (0,0), "Bottomi_Remember_Talk",
                                (0,0), "Bottomi_Remember_Blink",
                                (0,0), "sprites/Bottomi/Remember/Hat.png")

    image bottomi remembering hatless = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Remember/Base.png",
                                (0,0), "sprites/Bottomi/Remember/Mouth_1.png",
                                (0,0), "Bottomi_Remember_Blink",
                                (0,0), "Bottomi_Remember_Implant")

    image bottomi remembering hatless talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Remember/Base.png",
                                (0,0), "Bottomi_Remember_Talk",
                                (0,0), "Bottomi_Remember_Blink",
                                (0,0), "Bottomi_Remember_Implant")

    image Bottomi_Sad_Blink:
        "sprites/Bottomi/Sad/Eyes_1.png"
        pause 5.0
        "sprites/Bottomi/Sad/Eyes_2.png"
        pause 0.05
        "sprites/Bottomi/Sad/Eyes_3.png"
        pause 0.05
        "sprites/Bottomi/Sad/Eyes_4.png"
        pause 0.05
        "sprites/Bottomi/Sad/Eyes_3.png"
        pause 0.05
        "sprites/Bottomi/Sad/Eyes_2.png"
        pause 0.05
        repeat

    image Bottomi_Sad_Talk:
        "sprites/Bottomi/Sad/Mouth_1.png"
        pause 0.1
        "sprites/Bottomi/Sad/Mouth_2.png"
        pause 0.1
        "sprites/Bottomi/Sad/Mouth_3.png"
        pause 0.1
        "sprites/Bottomi/Sad/Mouth_1.png"
        pause 0.1
        "sprites/Bottomi/Sad/Mouth_4.png"
        pause 0.1
        "sprites/Bottomi/Sad/Mouth_2.png"
        pause 0.1
        repeat

    image Bottomi_Sad_Implant:
        "sprites/Bottomi/Sad/Implant_1.png"
        pause 3.0
        "sprites/Bottomi/Sad/Implant_2.png"
        pause 0.05
        "sprites/Bottomi/Sad/Implant_1.png"
        pause 0.05
        "sprites/Bottomi/Sad/Implant_2.png"
        pause 0.05

    image bottomi sad = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Sad/Base.png",
                                (0,0), "sprites/Bottomi/Sad/Mouth_1.png",
                                (0,0), "Bottomi_Sad_Blink",
                                (0,0), "sprites/Bottomi/Sad/Hat.png")

    image bottomi sad talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Sad/Base.png",
                                (0,0), "Bottomi_Sad_Talk",
                                (0,0), "Bottomi_Sad_Blink",
                                (0,0), "sprites/Bottomi/Sad/Hat.png")

    image bottomi sad hatless = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Sad/Base.png",
                                (0,0), "sprites/Bottomi/Sad/Mouth_1.png",
                                (0,0), "Bottomi_Sad_Blink",
                                (0,0), "Bottomi_Sad_Implant")

    image bottomi sad hatless talk = LiveComposite((1920,1080),
                                (0,0), "sprites/Bottomi/Sad/Base.png",
                                (0,0), "Bottomi_Sad_Talk",
                                (0,0), "Bottomi_Sad_Blink",
                                (0,0), "Bottomi_Sad_Implant")

init python:
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
            renpy.show("bottomi apologetic talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi apologetic")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def bdespairvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi despair talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi despair")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def bfuzzyvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi fuzzy talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi fuzzy")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def bmadvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi mad talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi mad")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def bnervousvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi nervous talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi nervous")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def bremembervoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi remembering talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi remembering")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def bsadvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi sad talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi sad")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

######################
### Hatless Voices ###
######################

    def bstandardhatlessvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi standard hatless talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi standard hatless")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def bapologetichatlessvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi apologetic hatless talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi hatless apologetic")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def bdespairhatlessvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi despair hatless talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi despair hatless")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def bfuzzyhatlessvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi fuzzy hatless talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi hatless fuzzy")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def bmadhatlessvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi mad hatless talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi mad hatless")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def bnervoushatlessvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi nervous hatless talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi nervous hatless")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def brememberhatlessvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi remembering hatless talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi remembering hatless")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")

    def bsadhatlessvoice(event, interact=True, **kwargs):
        if event == "show":
            renpy.show("bottomi sad hatless talk")
            renpy.sound.play("sound/TextNoiseFIX.ogg", loop=True)
        elif event == "slow_done":
            renpy.show("bottomi sad hatless")
            renpy.sound.stop()
            renpy.restart_interaction()
        elif event == "end":
            renpy.play("sound/sfx-pichoop.wav")
