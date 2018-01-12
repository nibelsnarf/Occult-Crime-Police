#Define Backgrounds and Images used by this game
image act1 = "assets/backgrounds/Act1.png"

image policecarbythesideoftheroad = "assets/backgrounds/Fog_at_night.png"
image outsidebase = "assets/backgrounds/SecurityCheckpointQuickie.png"
image basewarehouse = "assets/backgrounds/basewarehousewhouse.png"
image kitchen = "assets/backgrounds/SmartHouseKitchen.png"
image victimbody = "assets/backgrounds/DarshasBody.png"
image houseflyer = Image("gui/check_brochure.png", yalign= 0.3)
image darshasid = Image("gui/check_idcard.png", yalign= 0.3)

# Define characters used by this game.
define typing = Character(None, callback=typingvoice, xalign=0.5, yalign=0.5, ctc="ctc_blink", ctc_position="fixed")
define nameless = Character(callback=wdefos, ctc="ctc_blink", ctc_position="fixed")
define pscanner = Character("Police Scanner", callback=wdefos, ctc="ctc_blink", ctc_position="fixed")

# Define Warren sprites
define wos = Character('Warren', callback=wdefos, ctc="ctc_blink", ctc_position="fixed")
define wthought = Character("Warren", callback=wdefos, ctc="ctc_blink", ctc_position="fixed", what_color="#66CCFF")
define wbase = Character('Warren', callback=wdefvoice, ctc="ctc_blink", ctc_position="fixed")
define wangry = Character('Warren', callback=wangryvoice, ctc="ctc_blink", ctc_position="fixed")
define wannoy = Character('Warren', callback=wannoyvoice, ctc="ctc_blink", ctc_position="fixed")
define wcasefile = Character('Warren', callback=wcasevoice, ctc="ctc_blink", ctc_position="fixed")
define wrecoil = Character('Warren', callback=wrecoilvoice, ctc="ctc_blink", ctc_position="fixed")
define whattip = Character('Warren', callback=whattipvoice, ctc="ctc_blink", ctc_position="fixed")
define wthink = Character('Warren', callback=wthinkvoice, ctc="ctc_blink", ctc_position="fixed")
define wgotcha = Character('Warren', callback=wgotchavoice, ctc="ctc_blink", ctc_position="fixed")

# Define Carlos Sprites
define cos = Character('Carlos', callback=wdefos, ctc="ctc_blink", ctc_position="fixed")
define cdef = Character('Carlos', callback=cdefvoice, ctc="ctc_blink", ctc_position="fixed")
define cagit = Character('Carlos', callback=cagitvoice, ctc="ctc_blink", ctc_position="fixed")
define cwhis = Character('Carlos', callback=cwhisvoice, ctc="ctc_blink", ctc_position="fixed")
define clift = Character('Carlos', callback=cliftvoice, ctc="ctc_blink", ctc_position="fixed")
define chold = Character('Carlos', callback=choldvoice, ctc="ctc_blink", ctc_position="fixed")
define cser = Character('Carlos', callback=cservoice, ctc="ctc_blink", ctc_position="fixed")
define cconfuse = Character('Carlos', callback=cconfusevoice, ctc="ctc_blink", ctc_position="fixed")
define cgloves = Character('Carlos', callback=cglovesvoice, ctc="ctc_blink", ctc_position="fixed")

# Define Guard Sprites
define gglasses = Character('Guard', callback=gglassesvoice, ctc="ctc_blink", ctc_position="fixed")
define geyes = Character('Guard', callback=geyesvoice, ctc="ctc_blink", ctc_position="fixed")
define gremglasses = Character('Guard', callback=gremglassesvoice, ctc="ctc_blink", ctc_position="fixed")
define gholdglasses = Character('Guard', callback=gholdglassesvoice, ctc="ctc_blink", ctc_position="fixed")
define greturnglasses = Character('Guard', callback=greturnglassesvoice, ctc="ctc_blink", ctc_position="fixed")

#Define Drang Sprites
define dos = Character('Drang', callback=wdefos, ctc="ctc_blink", ctc_position="fixed")
define ddef_gdown = Character('Drang', callback=ddefgdownvoice, ctc="ctc_blink", ctc_position="fixed")
define ddef_gup = Character('Drang', callback=ddefgupvoice, ctc="ctc_blink", ctc_position="fixed")
define dthink_gdown = Character('Drang', callback=dthinkgdownvoice, ctc="ctc_blink", ctc_position="fixed")
define dthink_gup = Character('Drang', callback=dthinkgupvoice, ctc="ctc_blink", ctc_position="fixed")
define dangry_gdown = Character('Drang', callback=dangrygdownvoice, ctc="ctc_blink", ctc_position="fixed")
define dangry_gup = Character('Drang', callback=dangrygupvoice, ctc="ctc_blink", ctc_position="fixed")
define ddril_gdown = Character('Drang', callback=ddrilgdownvoice, ctc="ctc_blink", ctc_position="fixed")
define ddril_gup = Character('Drang', callback=ddrilgupvoice, ctc="ctc_blink", ctc_position="fixed")
define djacket_pop = Character('Drang', callback=djpopvoice, ctc="ctc_blink", ctc_position="fixed")
define djacket_popped = Character('Drang', callback=djpoppedvoice, ctc="ctc_blink", ctc_position="fixed")

#Define Ash Sprites
define aos = Character('Ash', callback=wdefos, ctc="ctc_blink", ctc_position="fixed")
define aunk = Character('???', callback=astandardvoice, ctc="ctc_blink", ctc_position="fixed")
define adef = Character('Ash', callback=astandardvoice, ctc="ctc_blink", ctc_position="fixed")
define acam = Character('Ash', callback=acameravoice, ctc="ctc_blink", ctc_position="fixed")
define aannoy = Character('Ash', callback=aannoyedvoice, ctc="ctc_blink", ctc_position="fixed")
define aconfident = Character('Ash', callback=aconfidentvoice, ctc="ctc_blink", ctc_position="fixed")
define aflippant = Character('Ash', callback=aflippantvoice, ctc="ctc_blink", ctc_position="fixed")
define aposit = Character('Ash', callback=apositingvoice, ctc="ctc_blink", ctc_position="fixed")
define apsyched = Character('Ash', callback=apsychedvoice, ctc="ctc_blink", ctc_position="fixed")
define asad = Character('Ash', callback=asadvoice, ctc="ctc_blink", ctc_position="fixed")
define asurprise = Character('Ash', callback=asurprisedvoice, ctc="ctc_blink", ctc_position="fixed")
define athink = Character('Ash', callback=athinkingvoice, ctc="ctc_blink", ctc_position="fixed")
define aunsure = Character('Ash', callback=aunsurevoice, ctc="ctc_blink", ctc_position="fixed")

#Define Bottomi Sprites
define bunk = Character('???', callback=bstandardvoice, ctc="ctc_blink", ctc_position="fixed")
define bdef = Character('Bottomi', callback=bstandardvoice, ctc="ctc_blink", ctc_position="fixed")
define bapology = Character('Bottomi', callback=bapologeticvoice, ctc="ctc_blink", ctc_position="fixed")
define bdespair = Character('Bottomi', callback=bdespairvoice, ctc="ctc_blink", ctc_position="fixed")
define bfreak = Character('Bottomi', callback=bfreakvoice, ctc="ctc_blink", ctc_position="fixed")
define bfuzzy = Character('Bottomi', callback=bfuzzyvoice, ctc="ctc_blink", ctc_position="fixed")
define bkaboom = Character('Bottomi', callback=bkaboomvoice, ctc="ctc_blink", ctc_position="fixed")
define bmad = Character('Bottomi', callback=bmadvoice, ctc="ctc_blink", ctc_position="fixed")
define bnervous = Character('Bottomi', callback=bnervousvoice, ctc="ctc_blink", ctc_position="fixed")
define bremember = Character('Bottomi', callback=bremembervoice, ctc="ctc_blink", ctc_position="fixed")

#Define Chritude Sprites
define punk = Character('???', callback=bstandardvoice, ctc="ctc_blink", ctc_position="fixed")
define pdef = Character('Chritude', callback=pstandardvoice, ctc="ctc_blink", ctc_position="fixed")
define pconceited = Character('Chritude', callback=pconceitedvoice, ctc="ctc_blink", ctc_position="fixed")
define pglitter = Character('Chritude', callback=pglittervoice, ctc="ctc_blink", ctc_position="fixed")
define plaugh = Character('Chritude', callback=plaughvoice, ctc="ctc_blink", ctc_position="fixed")
define poutrage = Character('Chritude', callback=poutragevoice, ctc="ctc_blink", ctc_position="fixed")
define psad = Character('Chritude', callback=psadvoice, ctc="ctc_blink", ctc_position="fixed")

label splashscreen:
    play music "music/HoveringGhost.ogg"
    show main_menu_bg
    pause 0.5
    show willitblend
    pause 0.05
    hide willitblend
    pause 0.025
    show willitblend
    pause 0.025
    hide willitblend
    pause 0.05
    show willitblend
    pause 0.5
    show pressStart
    pause
    hide pressStart
    hide splashscreen_bg
    play sound "sound/clickStart.wav"
    show mm_glitch
    pause 0.3
    hide mm_glitch
    return

# The game starts here.
label start:
    python:
        player = Player("Derp")
        autopsy = Item("Autopsy Report", image="gui/inv_autopsy.png")

        badge = Item("Sherriff's Badge", image="gui/inv_badge.png")
        brochure = Item("Smart House Brochure", image="gui/inv_brochure.png")
        footprints = Item("Muddy Footprints", image="gui/inv_footprints.png")
        missingshoe = Item("Missing Shoe", image="gui/inv_missingshoe.png")
        idcard = Item("Victim's ID Card", image="gui/inv_idcard.png")
        prelim = Item("Preliminary Autopsy", image="gui/inv_prelim.png")
        knife = Item("Kitchen Knife", image="gui/inv_knife.png")

        gun = Person("Gun", image="gui/pro_gun.png")
        laser = Person("Laser Gun", image="gui/pro_laser.png")
        warren = Person("Miranda Warren", image="gui/inv_warren.png")
        carlos = Person("Carlos Navarro Santillan Tsukada", image="gui/inv_carlos.png")
        ash = Person("Ash Jager", image="gui/inv_ash.png")
        drang = Person("Sturmund Drang", image="gui/inv_drang.png")
        darsha = Person("Orin Darsha", image="gui/inv_darsha.png")

        inventory = Inventory()
        profile = Profiles()

    stop music fadeout 0.5
    call case_1 from _call_case_1


label case_1:
    #jump case_2
    jump smart_house_act_1

label talkTest:
    show mir default
    show drang default
    ddef_gdown "Standard Talking With Glasses Down"
    ddef_gup "Now With Glasses Up"
    dangry_gdown "Getting Angry with the GDown"
    dangry_gup "But Now, The G is Up"
    dthink_gdown "Ah, Contemplative"
    dthink_gup "Now The Thinks Increase"
    ddril_gdown "if i am banned from the zoo for flipping off the monkeys i will face god and walk backwards into hell"
    ddril_gup "everyone keeps asking me if they can fuck the flag. buddy, they wont even let me fuck it"
    djacket_pop "are you ready to see my collar POP"
    djacket_popped "that was fun wasnt it"

    wthink "Thinking Talking Animation"
    wbase "Standard Talking Animaion"
    wangry "Angry Talking Animation"
    show mir annoy anim
    pause 0.94
    wannoy "Annoyed Talking Animation"
    wcasefile "Holding Case File Talking Animation"
    show mir recoil anim
    wos "GGGGUAAAAAAAAAAAAAAGHHH! {w=4.0}"
    wrecoil "Having Recoiled Talking Animation"
    whattip "Tipping Hat Talking Animation"

    call endgame from _call_endgame
    return

label jumpToMenu:
    menu:
        "Outside Base":
            jump outside_base_intro
        "Meeting Ash":
            jump meeting_ash_intro
        "Meeting Drang":
            jump meeting_drang_intro
        "Investigation 1":
            jump meeting_drang_outro
        "Act 2 Intro":
            jump smart_house_act_2
        "Testimony 1":
            jump testimony1_intro
        "Testimony 2":
            jump testimony2_intro
        "Testimony 3":
            jump testimony3_intro
        "Act 3 Intro":
            jump smart_house_act_3_intro

label endgame:
    "End game"
    $ renpy.full_restart()
    return
