#Define Backgrounds and Images used by this game
image act1 = "assets/backgrounds/Act1.png"

image policecarbythesideoftheroad = "assets/backgrounds/Fog_at_night.png"
image outsidebase = "assets/backgrounds/SecurityCheckpointQuickie.png"
image basewarehouse = "assets/backgrounds/basewarehousewhouse.png"
image kitchen = "assets/backgrounds/SmartHouseKitchen.png"
image victimbody = "assets/backgrounds/DarshasBody.png"
image houseflyer = Image("gui/check_brochure.png", yalign= 0.3)
image darshasid = Image("gui/check_id.png", yalign= 0.3)

# Define characters used by this game.
define typing = Character(None, callback=typingvoice, xalign=0.5, yalign=0.5, ctc="ctc_blink", ctc_position="nestled")
define nameless = Character(callback=wdefos, ctc="ctc_blink", ctc_position="nestled")
define pscanner = Character("Police Scanner", callback=wdefos, ctc="ctc_blink", ctc_position="nestled")

# Define Warren sprites
define wos = Character('Warren', callback=wdefos, ctc="ctc_blink", ctc_position="nestled")
define wthought = Character("Warren", callback=wdefos, ctc="ctc_blink", ctc_position="nestled", what_color="#66CCFF")
define wbase = Character('Warren', callback=wdefvoice, ctc="ctc_blink", ctc_position="nestled")
define wangry = Character('Warren', callback=wangryvoice, ctc="ctc_blink", ctc_position="nestled")
define wannoy = Character('Warren', callback=wannoyvoice, ctc="ctc_blink", ctc_position="nestled")
define wcasefile = Character('Warren', callback=wcasevoice, ctc="ctc_blink", ctc_position="nestled")
define wrecoil = Character('Warren', callback=wrecoilvoice, ctc="ctc_blink", ctc_position="nestled")
define whattip = Character('Warren', callback=whattipvoice, ctc="ctc_blink", ctc_position="nestled")
define wthink = Character('Warren', callback=wthinkvoice, ctc="ctc_blink", ctc_position="nestled")

# Define Carlos Sprites
define cos = Character('Carlos', callback=wdefos, ctc="ctc_blink", ctc_position="nestled")
define cdef = Character('Carlos', callback=cdefvoice, ctc="ctc_blink", ctc_position="nestled")
define cagit = Character('Carlos', callback=cagitvoice, ctc="ctc_blink", ctc_position="nestled")
define cwhis = Character('Carlos', callback=cwhisvoice, ctc="ctc_blink", ctc_position="nestled")
define clift = Character('Carlos', callback=cliftvoice, ctc="ctc_blink", ctc_position="nestled")
define chold = Character('Carlos', callback=choldvoice, ctc="ctc_blink", ctc_position="nestled")
define cser = Character('Carlos', callback=cservoice, ctc="ctc_blink", ctc_position="nestled")

# Define Guard Sprites
define gglasses = Character('Guard', callback=gglassesvoice, ctc="ctc_blink", ctc_position="nestled")
define geyes = Character('Guard', callback=geyesvoice, ctc="ctc_blink", ctc_position="nestled")
define gremglasses = Character('Guard', callback=gremglassesvoice, ctc="ctc_blink", ctc_position="nestled")
define gholdglasses = Character('Guard', callback=gholdglassesvoice, ctc="ctc_blink", ctc_position="nestled")
define greturnglasses = Character('Guard', callback=greturnglassesvoice, ctc="ctc_blink", ctc_position="nestled")

#Define Drang Sprites
define dos = Character('Drang', callback=wdefos, ctc="ctc_blink", ctc_position="nestled")
define ddef_gdown = Character('Drang', callback=ddefgdownvoice, ctc="ctc_blink", ctc_position="nestled")
define ddef_gup = Character('Drang', callback=ddefgupvoice, ctc="ctc_blink", ctc_position="nestled")
define dthink_gdown = Character('Drang', callback=dthinkgdownvoice, ctc="ctc_blink", ctc_position="nestled")
define dthink_gup = Character('Drang', callback=dthinkgupvoice, ctc="ctc_blink", ctc_position="nestled")
define dangry_gdown = Character('Drang', callback=dangrygdownvoice, ctc="ctc_blink", ctc_position="nestled")
define dangry_gup = Character('Drang', callback=dangrygupvoice, ctc="ctc_blink", ctc_position="nestled")
define ddril_gdown = Character('Drang', callback=ddrilgdownvoice, ctc="ctc_blink", ctc_position="nestled")
define ddril_gup = Character('Drang', callback=ddrilgupvoice, ctc="ctc_blink", ctc_position="nestled")
define djacket_pop = Character('Drang', callback=djpopvoice, ctc="ctc_blink", ctc_position="nestled")
define djacket_popped = Character('Drang', callback=djpoppedvoice, ctc="ctc_blink", ctc_position="nestled")

#Define Ash Sprites
define aos = Character('Ash', callback=wdefos, ctc="ctc_blink", ctc_position="nestled")
define aunk = Character('???', callback=astandardvoice, ctc="ctc_blink", ctc_position="nestled")
define adef = Character('Ash', callback=astandardvoice, ctc="ctc_blink", ctc_position="nestled")
define acam = Character('Ash', callback=acameravoice, ctc="ctc_blink", ctc_position="nestled")

#Define Bottomi Sprites
define bunk = Character('???', callback=bstandardvoice, ctc="ctc_blink", ctc_position="nestled")
define bdef = Character('Bottomi', callback=bstandardvoice, ctc="ctc_blink", ctc_position="nestled")

# The game starts here.
label start:
    python:
        player = Player("Derp")
        chocolate = Item("Chocolate",image="gui/inv_chocolate.png")
        banana = Item("Banana", image="gui/inv_banana.png")
        gun = Item("Gun", image="gui/inv_gun.png")
        laser = Item("Laser Gun", image="gui/inv_laser.png")
        autopsy = Item("Autopsy Report", image="gui/inv_autopsy.png")

        badge = Item("Sherriff's Badge", image="gui/inv_badge.png")
        brochure = Item("Smart House Brochure", image="gui/inv_brochure.png")
        footprints = Item("Muddy Footprints", image="gui/inv_footprints.png")
        missingshoe = Item("Missing Shoe", image="gui/inv_missingshoe.png")
        idcard = Item("Victim's ID Card", image="gui/inv_id.png")
        prelim = Item("Preliminary Autopsy", image="gui/inv_autopsy.png")
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

    call case_1 from _call_case_1


label case_1:
    #jump meeting_drang_outro
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

label endgame:
    "End game"
    $ renpy.full_restart()
    return
