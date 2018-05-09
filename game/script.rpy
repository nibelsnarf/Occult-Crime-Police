#Define Backgrounds and Images used by this game
image act1 = "assets/backgrounds/Act1.png"
image act2 = "assets/backgrounds/Act2.png"
image act3 = "assets/backgrounds/Act3.png"
image act4 = "assets/backgrounds/Act4.png"
image act5 = "assets/backgrounds/Act5.png"
image act6 = "assets/backgrounds/Act6.png"

image policecarbythesideoftheroad = "assets/backgrounds/IntroCar.png"
image outsidebase = "assets/backgrounds/Checkpoint.png"
image outsidebaseboth = "assets/backgrounds/CheckpointBoth.png"
image outsidebasecarlos = "assets/backgrounds/CheckpointCarlos.png"
image outsidebaseguard = "assets/backgrounds/CheckpointGuard.png"
image basewarehouse = "assets/backgrounds/Warehouse.png"
image kitchen = "assets/backgrounds/SmartHouseKitchin.png"
image victimbody = "assets/backgrounds/DarshasBody.png"
image houseflyer = Image("gui/check_brochure.png", yalign= 0.3)
image chritudesPhoto = Image("gui/check_photo.png", yalign= 0.3)
image darshasid = Image("gui/check_idcard.png", yalign= 0.3)
image PERSU = Image("gui/PERSU.png", yalign= 0.45)
image ASION = Image("gui/ASION.png", yalign= 0.45)
image BottomiHead = "assets/backgrounds/BottomiHead.png"
image OfficeDark = "assets/backgrounds/OfficeDark.png"
image OfficeLight = "assets/backgrounds/OfficeBright.png"
image bedroom = "assets/backgrounds/Bedroome.png"
image TrapDoor = "gui/check_trapdoor.png"
image neeringEmail = "gui/check_email.png"
image thePaper = "gui/check_logs.png"
image FuseBoxOpen = "assets/backgrounds/FuseBoxOpen.png"
image FuseBoxClosed = "assets/backgrounds/FuseBoxClosed.png"
image FuseBoxGlitter = "assets/backgrounds/FuseBoxGlitter.png"
image SecurityCam = "assets/backgrounds/SecurityCam.png"
image kitchenDarkA = "assets/backgrounds/SmartHouseKitchinDarkA.png"
image kitchenDark = "assets/backgrounds/SmartHouseKitchinDark.png"
image bedroomD1 = "assets/backgrounds/BedroomeDark1.png"
image bedroomD2 = "assets/backgrounds/BedroomeDark2.png"
image Flashback1 = "assets/backgrounds/Flashback1.png"
image Flashback2 = "assets/backgrounds/Flashback2.png"
image Flashback3 = "assets/backgrounds/Flashback3.png"

#Prank Video Images
image PVid1 = "gui/Prank1.png"
image PVid2 = "gui/Prank2.png"
image PVid3 = "gui/Prank3.png"
image PVid4 = "gui/Prank4.png"
image PVid5 = "gui/Prank5.png"
image PVid6 = "gui/Prank6.png"

# Define characters used by this game.
define typing = Character(None, callback=typingvoice, xalign=0.5, yalign=0.5, ctc="ctc_blink", ctc_position="fixed")
define nameless = Character(callback=wdefos, ctc="ctc_blink", ctc_position="fixed")
define pscanner = Character("Police Scanner", callback=wdefos, ctc="ctc_blink", ctc_position="fixed",color="#ffffff")
define marsha = Character("Orin Darsha", callback=wdefos, ctc="ctc_blink", ctc_position="fixed")

# Define Warren sprites yellow
define wos = Character('Warren', callback=wdefos, ctc="ctc_blink", ctc_position="fixed", color="#d5d590")
define wthought = Character("Warren", callback=wdefos, ctc="ctc_blink", ctc_position="fixed", what_color="#66CCFF", color="#d5d590")
define wbase = Character('Warren', callback=wdefvoice, ctc="ctc_blink", ctc_position="fixed", color="#d5d590")
define wangry = Character('Warren', callback=wangryvoice, ctc="ctc_blink", ctc_position="fixed", color="#d5d590")
define wannoy = Character('Warren', callback=wannoyvoice, ctc="ctc_blink", ctc_position="fixed", color="#d5d590")
define wcasefile = Character('Warren', callback=wcasevoice, ctc="ctc_blink", ctc_position="fixed", color="#d5d590")
define wrecoil = Character('Warren', callback=wrecoilvoice, ctc="ctc_blink", ctc_position="fixed", color="#d5d590")
define whattip = Character('Warren', callback=whattipvoice, ctc="ctc_blink", ctc_position="fixed", color="#d5d590")
define wthink = Character('Warren', callback=wthinkvoice, ctc="ctc_blink", ctc_position="fixed", color="#d5d590")
define wgotcha = Character('Warren', callback=wgotchavoice, ctc="ctc_blink", ctc_position="fixed", color="#d5d590")
define wholdon = Character('Warren', callback=wholdonvoice, ctc="ctc_blink", ctc_position="fixed", color="#d5d590")
define wconfused = Character('Warren', callback=wconfusedvoice, ctc="ctc_blink", ctc_position="fixed", color="#d5d590")
define wobjectionA = Character('Warren', callback=wobjectionAvoice, ctc="ctc_blink", ctc_position="fixed", color="#d5d590")
define wobjectionC = Character('Warren', callback=wobjectionCvoice, ctc="ctc_blink", ctc_position="fixed", color="#d5d590")
define wsettle = Character('Warren', callback=wsettlevoice, ctc="ctc_blink", ctc_position="fixed", color="#d5d590")

# Define Carlos Sprites orange/red
define cos = Character('Carlos', callback=wdefos, ctc="ctc_blink", ctc_position="fixed", color="#ecb379")
define cdef = Character('Carlos', callback=cdefvoice, ctc="ctc_blink", ctc_position="fixed", color="#ecb379")
define cagit = Character('Carlos', callback=cagitvoice, ctc="ctc_blink", ctc_position="fixed", color="#ecb379")
define clift = Character('Carlos', callback=cliftvoice, ctc="ctc_blink", ctc_position="fixed", color="#ecb379")
define chold = Character('Carlos', callback=choldvoice, ctc="ctc_blink", ctc_position="fixed", color="#ecb379")
define cser = Character('Carlos', callback=cservoice, ctc="ctc_blink", ctc_position="fixed", color="#ecb379")
define cthink = Character('Carlos', callback=cthinkvoice, ctc="ctc_blink", ctc_position="fixed", color="#ecb379")

# Define Guard Sprites dark grey
define gos = Character('Guard', callback=wdefos, ctc="ctc_blink", ctc_position="fixed", color="#a6a6a6")
define gglasses = Character('Guard', callback=gglassesvoice, ctc="ctc_blink", ctc_position="fixed", color="#a6a6a6")
define geyes = Character('Guard', callback=geyesvoice, ctc="ctc_blink", ctc_position="fixed", color="#a6a6a6")
define gremglasses = Character('Guard', callback=gremglassesvoice, ctc="ctc_blink", ctc_position="fixed", color="#a6a6a6")
define gholdglasses = Character('Guard', callback=gholdglassesvoice, ctc="ctc_blink", ctc_position="fixed", color="#a6a6a6")
define greturnglasses = Character('Guard', callback=greturnglassesvoice, ctc="ctc_blink", ctc_position="fixed", color="#a6a6a6")

#Define Drang Sprites dark blue
define dos = Character('Drang', callback=wdefos, ctc="ctc_blink", ctc_position="fixed", color="#607cd2")
define ddef_gdown = Character('Drang', callback=ddefgdownvoice, ctc="ctc_blink", ctc_position="fixed", color="#607cd2")
define ddef_gup = Character('Drang', callback=ddefgupvoice, ctc="ctc_blink", ctc_position="fixed", color="#607cd2")
define dfrown_gdown = Character('Drang', callback=dfrowngdownvoice, ctc="ctc_blink", ctc_position="fixed", color="#607cd2")
define dfrown_gup = Character('Drang', callback=dfrowngupvoice, ctc="ctc_blink", ctc_position="fixed", color="#607cd2")
define dthink_gdown = Character('Drang', callback=dthinkgdownvoice, ctc="ctc_blink", ctc_position="fixed", color="#607cd2")
define dthink_gup = Character('Drang', callback=dthinkgupvoice, ctc="ctc_blink", ctc_position="fixed", color="#607cd2")
define dangry_gdown = Character('Drang', callback=dangrygdownvoice, ctc="ctc_blink", ctc_position="fixed", color="#607cd2")
define dangry_gup = Character('Drang', callback=dangrygupvoice, ctc="ctc_blink", ctc_position="fixed", color="#607cd2")
define ddril_gdown = Character('Drang', callback=ddrilgdownvoice, ctc="ctc_blink", ctc_position="fixed", color="#607cd2")
define ddril_gup = Character('Drang', callback=ddrilgupvoice, ctc="ctc_blink", ctc_position="fixed", color="#607cd2")
define djacket_pop = Character('Drang', callback=djpopvoice, ctc="ctc_blink", ctc_position="fixed", color="#607cd2")
define djacket_popped = Character('Drang', callback=djpoppedvoice, ctc="ctc_blink", ctc_position="fixed", color="#607cd2")
define dfrazzled = Character('Drang', callback=dfrazzledvoice, ctc="ctc_blink", ctc_position="fixed", color="#607cd2")

#Define Ash Sprites tree green
define aos = Character('Ash', callback=wdefos, ctc="ctc_blink", ctc_position="fixed", color="#b3cd98")
define aunk = Character('???', callback=astandardvoice, ctc="ctc_blink", ctc_position="fixed", color="#b3cd98")
define adef = Character('Ash', callback=astandardvoice, ctc="ctc_blink", ctc_position="fixed", color="#b3cd98")
define acam = Character('Ash', callback=acameravoice, ctc="ctc_blink", ctc_position="fixed", color="#b3cd98")
define aannoy = Character('Ash', callback=aannoyedvoice, ctc="ctc_blink", ctc_position="fixed", color="#b3cd98")
define aconfident = Character('Ash', callback=aconfidentvoice, ctc="ctc_blink", ctc_position="fixed", color="#b3cd98")
define aflippant = Character('Ash', callback=aflippantvoice, ctc="ctc_blink", ctc_position="fixed", color="#b3cd98")
define aposit = Character('Ash', callback=apositingvoice, ctc="ctc_blink", ctc_position="fixed", color="#b3cd98")
define apsyched = Character('Ash', callback=apsychedvoice, ctc="ctc_blink", ctc_position="fixed", color="#b3cd98")
define asad = Character('Ash', callback=asadvoice, ctc="ctc_blink", ctc_position="fixed", color="#b3cd98")
define asurprise = Character('Ash', callback=asurprisedvoice, ctc="ctc_blink", ctc_position="fixed", color="#b3cd98")
define athink = Character('Ash', callback=athinkingvoice, ctc="ctc_blink", ctc_position="fixed", color="#b3cd98")
define aunsure = Character('Ash', callback=aunsurevoice, ctc="ctc_blink", ctc_position="fixed", color="#b3cd98")

#Define Bottomi Sprites teal
define bos = Character('Bottomi', callback=wdefos, ctc="ctc_blink", ctc_position="fixed", color="#9cbfe3")
define bunk = Character('???', callback=bstandardvoice, ctc="ctc_blink", ctc_position="fixed", color="#9cbfe3")
define bunkos = Character('???', callback=wdefos, ctc="ctc_blink", ctc_position="fixed", color="#9cbfe3")
define bdef = Character('Bottomi', callback=bstandardvoice, ctc="ctc_blink", ctc_position="fixed", color="#9cbfe3")
define bapology = Character('Bottomi', callback=bapologeticvoice, ctc="ctc_blink", ctc_position="fixed", color="#9cbfe3")
define bdespair = Character('Bottomi', callback=bdespairvoice, ctc="ctc_blink", ctc_position="fixed", color="#9cbfe3")
define bfuzzy = Character('Bottomi', callback=bfuzzyvoice, ctc="ctc_blink", ctc_position="fixed", color="#9cbfe3")
define bmad = Character('Bottomi', callback=bmadvoice, ctc="ctc_blink", ctc_position="fixed", color="#9cbfe3")
define bnervous = Character('Bottomi', callback=bnervousvoice, ctc="ctc_blink", ctc_position="fixed", color="#9cbfe3")
define bremember = Character('Bottomi', callback=bremembervoice, ctc="ctc_blink", ctc_position="fixed", color="#9cbfe3")
define bsad = Character('Bottomi', callback=bsadvoice, ctc="ctc_blink", ctc_position="fixed", color="#9cbfe3")

#Define Chritude Sprites pink
define pos = Character('Chritude', callback=wdefos, ctc="ctc_blink", ctc_position="fixed", color="#dda1dd")
define punk = Character('???', callback=pstandardvoice, ctc="ctc_blink", ctc_position="fixed", color="#dda1dd")
define pdef = Character('Chritude', callback=pstandardvoice, ctc="ctc_blink", ctc_position="fixed", color="#dda1dd")
define pconceited = Character('Chritude', callback=pconceitedvoice, ctc="ctc_blink", ctc_position="fixed", color="#dda1dd")
define pglitterin = Character('Chritude', callback=pglitterinvoice, ctc="ctc_blink", ctc_position="fixed", color="#dda1dd")
define pglitter = Character('Chritude', callback=pglittervoice, ctc="ctc_blink", ctc_position="fixed", color="#dda1dd")
define plaugh = Character('Chritude', callback=plaughvoice, ctc="ctc_blink", ctc_position="fixed", color="#dda1dd")
define poutrage = Character('Chritude', callback=poutragevoice, ctc="ctc_blink", ctc_position="fixed", color="#dda1dd")
define psad = Character('Chritude', callback=psadvoice, ctc="ctc_blink", ctc_position="fixed", color="#dda1dd")
define pnervous = Character('Chritude', callback=pnervousvoice, ctc="ctc_blink", ctc_position="fixed", color="#dda1dd")
#define psurprise = Character('Chritude', callback=psurpvoice, ctc="ctc_blink", ctc_position="fixed")

#Define Harper Sprites light gray
define hos = Character('H.A.R.P.E.R.', callback=wdefos, ctc="ctc_blink", ctc_position="fixed", color="#bfbfbf")
define hunk = Character('???', callback=hbasevoice, ctc="ctc_blink", ctc_position="fixed", color="#bfbfbf")
define hbase = Character('H.A.R.P.E.R.', callback=hbasevoice, ctc="ctc_blink", ctc_position="fixed", color="#bfbfbf")
define hno = Character('H.A.R.P.E.R.', callback=hnovoice, ctc="ctc_blink", ctc_position="fixed", color="#bfbfbf")
define hyes = Character('H.A.R.P.E.R.', callback=hyesvoice, ctc="ctc_blink", ctc_position="fixed", color="#bfbfbf")
define hwave = Character('H.A.R.P.E.R.', callback=hwavevoice, ctc="ctc_blink", ctc_position="fixed", color="#bfbfbf")
define hturn = Character('H.A.R.P.E.R.', callback=hturnvoice, ctc="ctc_blink", ctc_position="fixed", color="#bfbfbf")

#Define Neering Sprites yellow green
define nos = Character('Neering', callback=wdefos, ctc="ctc_blink", ctc_position="fixed", color="#26d926")
define nunk = Character('???', callback=ndefvoice, ctc="ctc_blink", ctc_position="fixed", color="#26d926")
define noff = Character('???', callback=noffvoice, ctc="ctc_blink", ctc_position="fixed", color="#26d926")
#define nfiddle = Character('Neering', callback=wdefos, ctc="ctc_blink", ctc_position="fixed")
define ndef = Character('Neering', callback=ndefvoice, ctc="ctc_blink", ctc_position="fixed", color="#26d926")
define ndismissive = Character('Neering', callback=ndismissivevoice, ctc="ctc_blink", ctc_position="fixed", color="#26d926")
define ngrumble = Character('Neering', callback=ngrumblevoice, ctc="ctc_blink", ctc_position="fixed", color="#26d926")
#define nheady = Character('Neering', callback=wdefos, ctc="ctc_blink", ctc_position="fixed")
define nangry = Character('Neering', callback=nangryvoice, ctc="ctc_blink", ctc_position="fixed", color="#26d926")
define nlaugh = Character('Neering', callback=nlaughvoice, ctc="ctc_blink", ctc_position="fixed", color="#26d926")
define nsmug = Character('Neering', callback=nsmugvoice, ctc="ctc_blink", ctc_position="fixed", color="#26d926")
define nuneasy = Character('Neering', callback=nuneasyvoice, ctc="ctc_blink", ctc_position="fixed", color="#26d926")
define nglitch = Character('Neering', callback=nglitchvoice, ctc="ctc_blink", ctc_position="fixed", color="#f76e90")
define narper = Character('H.A.R.P.E.R.', callback=narpervoice, ctc="ctc_blink", ctc_position="fixed", color="#f76e90")
define narperglitch = Character('H.A.R.P.E.R.', callback=narperglitchvoice, ctc="ctc_blink", ctc_position="fixed", color="#f76e90")


label splashscreen:
    play sound "sound/BootNoise2.ogg"
    play music "sound/MenuNoise2.ogg" fadein 3.5
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
    play sound "sound/Degauss.ogg"
    show mm_glitch
    pause 0.5
    hide mm_glitch
    return

# The game starts here.
label start:
    python:
        player = Player("Derp")

        badge = Item("Sherriff's Badge", image="gui/inv_badge.png")
        brochure = Item("Smart House Brochure", image="gui/inv_brochure.png")
        footprints = Item("Muddy Footprints", image="gui/inv_footprints.png")
        missingshoe = Item("Missing Shoe", image="gui/inv_missingshoe.png")
        shoe = Item("Darsha's Shoe", image="gui/inv_shoe.png")
        idcard = Item("Victim's ID Card", image="gui/inv_idcard.png")
        prelim = Item("Preliminary Autopsy", image="gui/inv_prelim.png")
        autopsy = Item("Updated Autopsy", image="gui/inv_autopsy.png")
        knife = Item("Kitchen Knife", image="gui/inv_knife.png")
        photo = Item("Chritude's Photo", image="gui/inv_photo.png")
        email = Item("Neering's Email", image="gui/inv_email.png")
        logs = Item("Feedback Logs", image="gui/inv_logs.png")
        glitter = Item("Fuse Box Glitter", image="gui/inv_glitter.png")
        trapdoor = Item("Trap Door", image="gui/inv_trapdoor.png")
        prank = Item("Prank Footage", image="gui/inv_prank.png")
        cam = Item("Security Camera Footage", image="gui/inv_cam.png")


        gun = Person("Gun", image="gui/pro_gun.png")
        laser = Person("Laser Gun", image="gui/pro_laser.png")
        warren = Person("Miranda Warren", image="gui/inv_warren.png")
        carlos = Person("Carlos Navarro Santillan Tsukada", image="gui/inv_carlos.png")
        ash = Person("Ash Jager", image="gui/inv_ash.png")
        drang = Person("Sturmund Drang", image="gui/inv_drang.png")
        darsha = Person("Orin Darsha", image="gui/inv_darsha.png")
        bottomi = Person("Louis Bottomi", image="gui/inv_bottomi.png")
        harper = Person("H.A.R.P.E.R.", image="gui/inv_harper.png")
        neeringunk = Person("Angela Neering", image="gui/inv_neeringunk.png")
        neering = Person("Angela Neering", image="gui/inv_neering.png")

        inventory = Inventory()
        profile = Profiles()

    stop music fadeout 0.5
    $renpy.start_predict("sprites/Carlos*.*")
    $renpy.start_predict("sprites/Miranda*.*")
    $renpy.start_predict("sprites/Guard*.*")
    call case_1 from _call_case_1


label case_1:
    #jump case_2
    jump smart_house_act_1

label jumpToMenu:
    menu:
        "Act 3 Intro":
            jump smart_house_act_3_intro
        "Act 4 Intro":
            $inventory.add(shoe)
            $inventory.add(glitter)
            $inventory.add(logs)
            $inventory.add(footprints)
            $inventory.add(photo)
            $inventory.add(prelim)
            $inventory.add(cam)
            $inventory.add(brochure)
            $inventory.add(prank)
            $inventory.add(email)
            $inventory.add(trapdoor)
            jump smart_house_act_4_intro
        "Act 5 Intro":
            jump smart_house_act_5_intro
        "Testimony 8":
            $inventory.add(email)
            $inventory.add(trapdoor)
            jump testimony8_intro
        "Testimony 9":
            $inventory.add(logs)
            $inventory.add(email)
            jump testimony9_intro
        "Act 6 Intro":
            $inventory.add(cam)
            $inventory.add(brochure)
            $inventory.add(prank)
            $profile.add(harper)
            $profile.add(neering)
            jump smart_house_act_6_intro

label endgame:
    #"End game"
    $ renpy.full_restart()
    return
