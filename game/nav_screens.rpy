###############################
# Inventory
#
###############################
init:
    $ present_response = 0

init -1 python:
    from operator import attrgetter # we need this for sorting items

    inv_page = 0 # initial page of teh inventory screen
    item = None
    class Player(renpy.store.object):
        def __init__(self, name):
            self.name=name
    player = Player("Derp")

    class Item(store.object):
        def __init__(self, name, image=""):
            self.name = name
            self.image=image # image file to use for this item

    class Inventory(store.object):
        def __init__(self):
            self.items = []
        def add(self, item): # a simple method that adds an item; we could also add conditions here (like check if there is space in the inventory)
            if item not in self.items:
                self.items.append(item)
        def drop(self, item):
            self.items.remove(item)

    def item_use():
        item.use()

    #Tooltips:
    style.tips_top = Style(style.default)
    #style.title.font="gui/arial.ttf"
    style.tips_top.size=14
    style.tips_top.color="fff"
    style.tips_top.outlines=[(3, "6b7eef", 0,0)]
    style.tips_top.kerning = 5

    style.tips_bottom = Style(style.tips_top)
    style.tips_top.size=48
    style.tips_bottom.outlines=[(0, "6b7eef", 1, 1), (0, "6b7eef", 2, 2)]
    style.tips_bottom.kerning = 2

    style.button.background=Frame("gui/frame.png",25,25)
    style.button.yminimum=52
    style.button.xminimum=52
    style.button_text.color="000"


    showitems = False #turn True to debug the inventory
    def display_items_overlay():
        if showitems:
            inventory_show = "Inventory: "
            for i in range(0, len(inventory.items)):
                item_name = inventory.items[i].name
                if i > 0:
                    inventory_show += ", "
                inventory_show += item_name

            ui.frame()
            ui.text(inventory_show, color="#000")
    config.overlay_functions.append(display_items_overlay)

screen inventory_screen_button:
    hbox align (0.01,0.01) spacing 10:
        #textbutton "Show Case Files" action [ Show("inventory_screen")]
        imagebutton idle "assets/menu/court_record_default.png" hover "assets/menu/court_record_selected.png" action [ Show("inventory_screen")]

screen inventory_screen:
    tag menu
    add "gui/inventory2.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown
    hbox align (.97,.04) spacing 20:
        textbutton "Profiles" keysym 'mouseup_3' action [ Hide("inventory_screen"), Show("profile_screen"), Hide("gui_tooltip"), Hide("gui_check")]

    hbox align (0.03,0.04) spacing 20:
        textbutton "Back" action [ Hide("inventory_screen")]
    $ x = 515
    $ y = -20
    $ i = 0
    $ sorted_items = sorted(inventory.items, key=attrgetter('name'), reverse=True)
    $ next_inv_page = inv_page + 1
    if next_inv_page > int(len(inventory.items)/9):
        $ next_inv_page = 0
    for item in sorted_items:
        if i+1 <= (inv_page+1)*9 and i+1>inv_page*9:
            $ x += 235
            if i%3==0:
                $ y += 215
                $ x = 1050
            $ pic = item.image
            $ picName = pic.replace("gui/inv_", "").replace(".png", "")
            $ my_tooltip = "tooltip_inventory_" + picName # we use tooltips to describe what the item does.
            $ my_checker = "gui/check_" + picName + ".png"
            imagebutton idle pic hover pic xpos x ypos y action NullAction() hovered [ Play ("sound", "sound/click.wav"), Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693,), Show("gui_check", check_pic=my_checker, my_check_ypos=90 )] unhovered [ Hide("gui_tooltip"), Hide("gui_check") ] at inv_eff
            #add "gui/selected.png" xpos x ypos y anchor(.5,.5)
        $ i += 1
        if len(inventory.items)>9:
            textbutton _("Next Page") action [SetVariable('inv_page', next_inv_page), Show("inventory_screen")] xpos .75 ypos .685 xpadding 40 ypadding 20

screen present_evidence_screen:
    tag menu
    add "gui/inventory2.png" # the background

    modal True #prevent clicking on other stuff when inventory is shown
    $ x = 515
    $ y = -20
    $ i = 0
    $ sorted_items = sorted(inventory.items, key=attrgetter('name'), reverse=True)
    $ next_inv_page = inv_page + 1
    if next_inv_page > int(len(inventory.items)/9):
        $ next_inv_page = 0
    for item in sorted_items:
        if i+1 <= (inv_page+1)*9 and i+1>inv_page*9:
            $ x += 235
            if i%3==0:
                $ y += 215
                $ x = 1050
            $ pic = item.image
            $ picName = pic.replace("gui/inv_", "").replace(".png", "")
            $ my_tooltip = "tooltip_inventory_" + picName # we use tooltips to describe what the item does.
            $ my_checker = "gui/check_" + picName + ".png"
            imagebutton idle pic hover pic xpos x ypos y action [SetVariable("present_response", picName), Hide("present_evidence_screen"), Hide("gui_tooltip"), Hide("gui_check"), Hide("back_button"), Jump(current_present), Return(None) ] hovered [ Play ("sound", "sound/click.wav"), Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693,), Show("gui_check", check_pic=my_checker, my_check_ypos=50 )] unhovered [ Hide("gui_tooltip"), Hide("gui_check") ] at inv_eff
            #add "gui/selected.png" xpos x ypos y anchor(.5,.5)
        $ i += 1
        if len(inventory.items)>9:
            textbutton _("Next Page") action [SetVariable('inv_page', next_inv_page), Show("present_evidence_screen")] xpos .75 ypos .685 xpadding 40 ypadding 20

screen gui_tooltip (my_picture="", my_tt_xpos=58, my_tt_ypos=687):
    add my_picture xpos my_tt_xpos ypos my_tt_ypos

screen gui_check (check_pic="", my_check_xpos=150, my_check_ypos=100):
    add check_pic xpos my_check_xpos ypos my_check_ypos


init -1:
    $ my_picName = ""
    transform inv_eff: # too lazy to make another version of each item, we just use ATL to make hovered items super bright
        zoom 0.5 xanchor 0.5 yanchor 0.5
        on idle:
            linear 0.2 alpha 1.0
        on hover:
            linear 0.2 alpha 2.5

    image inventory_information = Text("INFORMATION", style="tips_top")
    #Tooltips-inventory:
    image tooltip_inventory_badge=LiveComposite((1800, 73), (3,135), ImageReference(Text("Sheriff Badge", style="tips_top")), (3,200), Text("Proof of my profession. Lately I haven't felt truly worthy of all it represents.", style="tips_bottom"))
    image tooltip_inventory_brochure=LiveComposite((1800, 73), (3,135), ImageReference(Text("Smart House Brochure", style="tips_top")), (3,200), Text("A pamphlet explaining the different features of this \"Smart House\". There is an artificial intelligence called Harper, some creepy mechanical arms, and some sort of high-faluting dresser.", style="tips_bottom"))
    image tooltip_inventory_id=LiveComposite((1800, 73), (3,135), ImageReference(Text("ID Card", style="tips_top")), (3,200), Text("Identification Card belonging to the victim. Proof of his employment at Base 24.", style="tips_bottom"))
    image tooltip_inventory_autopsy=LiveComposite((1800, 73), (3,135), ImageReference(Text("Autopsy Report", style="tips_top")), (3,200), Text("The victim has a stab wound in his back and bruises all over his body. Exact cause of death unknown.", style="tips_bottom"))
    image tooltip_inventory_knife=LiveComposite((1800, 73), (3,135), ImageReference(Text("Kitchen Knife", style="tips_top")), (3,200), Text("The knife found plunged into the victim's back. No fingerprints discovered anywhere on the hilt.", style="tips_bottom"))
    image tooltip_inventory_footprints=LiveComposite((1800, 73), (3,135), ImageReference(Text("Muddy Footprints", style="tips_top")), (3,200), Text("Mysterious muddy footprints found in the kitchen. Likely belong to the culprit.", style="tips_bottom"))
    image tooltip_inventory_missingshoe=LiveComposite((1800, 73), (3,135), ImageReference(Text("Missing Shoe", style="tips_top")), (3,200), Text("One of the victim's shoes is missing. There's no trace of it anywhere in the kitchen.", style="tips_bottom"))

###############################
# Profiles
#
###############################

init -1 python:
    from operator import attrgetter # we need this for sorting items

    pro_page = 0 # initial page of teh inventory screen
    item = None

    class Person(store.object):
        def __init__(self, name, image=""):
            self.name = name
            self.image=image # image file to use for this item

    class Profiles(store.object):
        def __init__(self):
            self.items = []
        def add(self, item): # a simple method that adds an item; we could also add conditions here (like check if there is space in the inventory)
            self.items.append(item)
        def drop(self, item):
            self.items.remove(item)

    def item_use():
        item.use()

    #Tooltips:
    style.tips_top = Style(style.default)
    #style.title.font="gui/arial.ttf"
    style.tips_top.size=14
    style.tips_top.color="fff"
    style.tips_top.outlines=[(3, "6b7eef", 0,0)]
    style.tips_top.kerning = 5

    style.tips_bottom = Style(style.tips_top)
    style.tips_top.size=48
    style.tips_bottom.outlines=[(0, "6b7eef", 1, 1), (0, "6b7eef", 2, 2)]
    style.tips_bottom.kerning = 2

    style.button.background=Frame("gui/frame.png",25,25)
    style.button.yminimum=52
    style.button.xminimum=52
    style.button_text.color="000"


screen profile_screen:
    tag menu
    add "gui/inventory2.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown
    hbox align (.97,.04) spacing 20:
        textbutton "Inventory" keysym 'mouseup_3' action [ Hide("profile_screen"), Show("inventory_screen"), Hide("gui_tooltip"), Hide("gui_check")]

    hbox align (0.03,0.04) spacing 20:
        textbutton "Back" action [ Hide("profile_screen")]

    $ x = 515 # coordinates of the top left item position
    $ y = -20
    $ i = 0
    $ sorted_items = sorted(profile.items, key=attrgetter('name'), reverse=True)
    $ next_pro_page = pro_page + 1
    if next_pro_page > int(len(profile.items)/9):
        $ next_pro_page = 0
    for item in sorted_items:
        if i+1 <= (pro_page+1)*9 and i+1>pro_page*9:
            $ x += 235
            if i%3==0:
                $ y += 215
                $ x = 1050
            $ pic = item.image
            $ picName = pic.replace("gui/inv_", "").replace(".png", "")
            $ my_tooltip = "tooltip_profile_" + picName # we use tooltips to describe what the item does.
            $ my_checker = "gui/check_" + picName + ".png"
            imagebutton idle pic hover pic xpos x ypos y action NullAction() hovered [ Play("sound", "sound/click.wav"), Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693), Show("gui_check", check_pic=my_checker, my_check_ypos=100,) ] unhovered [Hide("gui_tooltip"), Hide("gui_check")] at pro_eff
            #add "gui/selected.png" xpos x ypos y anchor(.5,.5)
        $ i += 1
        if len(profile.items)>9:
            textbutton _("Next Page") action [SetVariable('pro_page', next_pro_page), Show("profile_screen")] xpos .475 ypos .83

screen back_button:
    hbox align (0.03,0.04) spacing 20:
        textbutton "Back" action [ SetVariable("present_response", "Back"), Hide("back_button"), Hide("present_profile_screen"), Hide("present_evidence_screen"), Jump(back_action)]

screen present_profile_screen:
    tag menu
    add "gui/inventory2.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown


    $ x = 515 # coordinates of the top left item position
    $ y = -20
    $ i = 0
    $ sorted_items = sorted(profile.items, key=attrgetter('name'), reverse=True)
    $ next_pro_page = pro_page + 1
    if next_pro_page > int(len(profile.items)/9):
        $ next_pro_page = 0
    for item in sorted_items:
        if i+1 <= (pro_page+1)*9 and i+1>pro_page*9:
            $ x += 235
            if i%3==0:
                $ y += 215
                $ x = 1050
            $ pic = item.image
            $ picName = pic.replace("gui/inv_", "").replace(".png", "")
            $ my_tooltip = "tooltip_profile_" + picName # we use tooltips to describe what the item does.
            $ my_checker = "gui/check_" + picName + ".png"
            imagebutton idle pic hover pic xpos x ypos y action [SetVariable("present_response", picName), Hide("present_profile_screen"), Hide("gui_tooltip"), Hide("gui_check"), Hide("back_button"), Jump(current_present), Return(None)] hovered [ Play("sound", "sound/click.wav"), Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693), Show("gui_check", check_pic=my_checker, my_check_ypos=100,) ] unhovered [Hide("gui_tooltip"), Hide("gui_check")] at pro_eff
            #add "gui/selected.png" xpos x ypos y anchor(.5,.5)
        $ i += 1
        if len(profile.items)>9:
            textbutton _("Next Page") action [SetVariable('pro_page', next_pro_page), Show("present_profile_screen")] xpos .475 ypos .83

init -1:
    transform pro_eff: # too lazy to make another version of each item, we just use ATL to make hovered items super bright
        zoom 0.5 xanchor 0.5 yanchor 0.5
        on idle:
            linear 0.2 alpha 1.0
        on hover:
            linear 0.2 alpha 2.5

    image profile_information = Text("ass", style="tips_top")
    #Tooltips-profile:
    image tooltip_profile_warren=LiveComposite((1800, 73), (3,135), ImageReference(Text("Miranda Warren", style="tips_top")), (3,200), Text("This is me. I am the Sheriff of Temashaw Valley. Why do I have a profile of myself in my case files?", style="tips_bottom"))
    image tooltip_profile_carlos=LiveComposite((1800, 73), (3,135), ImageReference(Text("Carlos Navarro Santillan Tsukada", style="tips_top")), (3,200), Text("The lone medical expert in the Temashaw Valley Sheriff's Department. A big fan of drunken Caribbean rock 'n' roll.", style="tips_bottom"))
    image tooltip_profile_ash=LiveComposite((1800, 73), (3,135), ImageReference(Text("Ash Jager", style="tips_top")), (3,200), Text("A young friend of mine from an old case. Obsessed with all things sacred, sinister, and strange.", style="tips_bottom"))
    image tooltip_profile_drang=LiveComposite((1800, 73), (3,135), ImageReference(Text("Sturmund Drang", style="tips_top")), (3,200), Text("An agent of the Federal Bureau of Investigation. Outranks me on the investigative totem pole. Additionally: A Massive Tool.", style="tips_bottom"))
    image tooltip_profile_darsha=LiveComposite((1800, 73), (3,135), ImageReference(Text("Orin Darsha", style="tips_top")), (3,200), Text("The victim in this case. Head of Base 24's Research and Development department. Found dead in the Smart House's kitchen.", style="tips_bottom"))


###########################
# Modal screen

###########################
screen modalScreen:
    modal True

###########################
# Testimony Screen

###########################
init:
    $ mc_maxhealth = 5
    $ mc_health = mc_maxhealth
    python:
        def settesti(current, left, right, press, advice):
            store.testipart = current
            store.testileft = left
            store.testiright = right
            store.testipress = press
            store.testiobject = object
            store.showtestimony = True
            store.testadvice = advice

transform flipped:
    xzoom -1

screen testi:
    if store.testileft <> None:
        imagebutton idle "assets/menu/testi_arrow_default.png" hover "assets/menu/testi_arrow_selected.png" action Jump(store.testileft) xpos 0.015 ypos 0.795 at flipped
    if store.testiright <> None:
        imagebutton idle "assets/menu/testi_arrow_default.png" hover "assets/menu/testi_arrow_selected.png" action Jump(store.testiright) xpos 0.883 ypos 0.795

    imagemap:
        ground "assets/menu/ce_menu_default.png"
        hover "assets/menu/ce_menu_selected.png"
        hotspot(60,50,530,133) action [Jump(store.testipress)] #Press
        hotspot(60,227,530,133) action [Show("present_evidence_screen"), Show("back_button"), SetVariable("back_action", store.testipart)] #Advice
        hotspot(60,404,530,133) action [Jump(store.testadvice)] #Present
        hotspot(1690,10,220,90) action [ShowMenu("custom_menu")] #Menu
    bar range mc_maxhealth value mc_health xmaximum 530 xpos 60 ypos 0.55
