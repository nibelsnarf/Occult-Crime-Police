

## History #####################################################################
##
## The history screen displays dialogue that the player has already dismissed.

## The number of blocks of dialogue history Ren'Py will keep.
define config.history_length = 15

## The height of a history screen entry, or None to make the height variable at
## the cost of performance.
define history_height = None

## The position, width, and alignment of the label giving the name of the
## speaking character.
define history_name_xpos = 300
define history_name_ypos = 0
define history_name_width = 300
define history_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define history_text_xpos = 325
define history_text_ypos = 0
define history_text_width = 1200
define history_text_xalign = 0.0


screen history():

    tag menu
    ## Avoid predicting this screen, as it can be very large.
    predict False
    $ historyI = 0
    add "mm_bg_scroll"
    hbox align (0.9,0.0) spacing 20:
        imagebutton auto "assets/menu/inv_back_%s.png" action [ Hide("history")]
    style_prefix "history"

    for h in _history_list:
        window:
            ypos ((historyI * 60) + 135)
            ## This lays things out properly if history_height is None.
            has fixed:
                yfit True

            if h.who:

                label h.who:
                    style "history_name"

                    ## Take the color of the who text from the Character, if
                    ## set.
                    if "color" in h.who_args:
                        text_color h.who_args["color"]

            text h.what
        $ historyI += 1

    if not _history_list:
        label _("Nothing here!")


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize history_height
    #background "#000000"

style history_name:
    xpos history_name_xpos
    xanchor history_name_xalign
    ypos history_name_ypos
    xsize history_name_width

style history_name_text:
    min_width history_name_width
    text_align history_name_xalign
    color "#ffffff"
    outlines [(3, "000000", 0,0)]

style history_text:
    xpos history_text_xpos
    ypos history_text_ypos
    xanchor history_text_xalign
    xsize history_text_width
    min_width history_text_width
    text_align history_text_xalign
    layout ("subtitle" if history_text_xalign else "tex")
    size 24

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


###############################
# Inventory
#
###############################
init -1:
    # Tooltips Position Variables
    $ liveComWidth = 600
    $ liveComHeight = 75
    $titleX = 0
    $titleY = 135
    $descriptionX = 3
    $descriptionY = 240


    #Tooltips-inventory:
    image tooltip_inventory_badge=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Sheriff Badge", style="tips_top")), (descriptionX,descriptionY), Text("Proof of my profession. Lately I haven't felt truly worthy of all it represents.", style="tips_bottom"))
    image tooltip_inventory_brochure=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Smart House Brochure", style="tips_top")), (descriptionX,descriptionY), Text("A pamphlet explaining the different features of this \"Smart House\". There is an artificial intelligence called Harper, some creepy mechanical arms, and some sort of high-faluting dresser.", style="tips_bottom"))
    image tooltip_inventory_idcard=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("ID Card", style="tips_top")), (descriptionX,descriptionY), Text("Identification Card belonging to the victim. Proof of his employment at Base 24.", style="tips_bottom"))
    image tooltip_inventory_prelim=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Preliminary Autopsy Report", style="tips_top")), (descriptionX,descriptionY), Text("The victim has a stab wound in his back and bruises all over his body. Exact cause of death unknown.", style="tips_bottom"))
    image tooltip_inventory_knife=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Kitchen Knife", style="tips_top")), (descriptionX,descriptionY), Text("The knife found plunged into the victim's back. No fingerprints discovered anywhere on the hilt.", style="tips_bottom"))
    image tooltip_inventory_footprints=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Muddy Footprints", style="tips_top")), (descriptionX,descriptionY), Text("Mysterious muddy footprints found in the kitchen. Likely belong to the culprit.", style="tips_bottom"))
    image tooltip_inventory_missingshoe=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Missing Shoe", style="tips_top")), (descriptionX,descriptionY), Text("One of the victim's shoes is missing. There's no trace of it anywhere in the kitchen.", style="tips_bottom"))
    image tooltip_inventory_shoe=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Recovered Shoe", style="tips_top")), (descriptionX,descriptionY), Text("A single shoe found inside The Dressing Contraption. Almost certainly the shoe which Orin Darsha lost during his murder.", style="tips_bottom"))
    image tooltip_inventory_photo=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Chritude's Photo", style="tips_top")), (descriptionX,descriptionY), Text("A photo of the Orin Darsha's corpse, taken at 6pm. A second figure is visible standing next to the body.", style="tips_bottom"))
    image tooltip_inventory_email=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Neering's Email", style="tips_top")), (descriptionX,descriptionY), Text("An email conversation between Angela Neering and Orin Darsha a couple of days before the murder.", style="tips_bottom"))
    image tooltip_inventory_logs=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Feedback Logs", style="tips_top")), (descriptionX,descriptionY), Text("A log of feedback from the Smart House during the period of time in which Orin Darsha was killed.", style="tips_bottom"))
    image tooltip_inventory_glitter=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Fuse Box Glitter", style="tips_top")), (descriptionX,descriptionY), Text("Proof of the prank gone wrong which caused the power outage at 5:58 today.", style="tips_bottom"))
    image tooltip_inventory_prank=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Prank Video", style="tips_top")), (descriptionX,descriptionY), Text("A video of Paul Chritude's prank gone wrong which shows the power outage occurring. A large flash can be seen and a loud boom can be heard.", style="tips_bottom"))
    image tooltip_inventory_trapdoor=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Trap Door", style="tips_top")), (descriptionX,descriptionY), Text("A photo of the trap door leading to The Dressing Contraption. There seem to be fingernail scratches in the nearby carpeting.", style="tips_bottom"))
    image tooltip_inventory_autopsy=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Updated Autopsy Report", style="tips_top")), (descriptionX,descriptionY), Text("The victim has a stab wound in his back and bruises all over his body. Exact cause of death: Broken Neck.", style="tips_bottom"))
    image tooltip_inventory_cam=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Security Camera Footage", style="tips_top")), (descriptionX,descriptionY), Text("A security photo showing where Angela Neering and Orin Darsha were standing at the time of the murder.", style="tips_bottom"))


    #Tooltips-profile:
    image tooltip_profile_warren=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Miranda Warren", style="tips_top")), (descriptionX,descriptionY), Text("This is me. I am the Sheriff of Temashaw Valley. Why do I have a profile of myself in my case files?", style="tips_bottom"))
    image tooltip_profile_carlos=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Carlos Navarro Santillan Tsukada", style="tips_top")), (descriptionX,descriptionY), Text("The lone medical expert in the Temashaw Valley Sheriff's Department. A big fan of drunken Caribbean rock 'n' roll.", style="tips_bottom"))
    image tooltip_profile_ash=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Ash Jager", style="tips_top")), (descriptionX,descriptionY), Text("A young friend of mine from an old case. Obsessed with all things sacred, sinister, and strange.", style="tips_bottom"))
    image tooltip_profile_drang=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Sturmund Drang", style="tips_top")), (descriptionX,descriptionY), Text("An agent of the Federal Bureau of Investigation. Outranks me on the investigative totem pole. Additionally: A Massive Tool.", style="tips_bottom"))
    image tooltip_profile_darsha=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Orin Darsha", style="tips_top")), (descriptionX,descriptionY), Text("The victim in this case. Head of Base 24's Research and Development department. Found dead in the Smart House's kitchen.", style="tips_bottom"))
    image tooltip_profile_bottomi=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Louis Bottomi", style="tips_top")), (descriptionX,descriptionY), Text("Sort of a big scary guy. Claims to be the one who killed Orin Darsha, but there's something strange about his testimony.", style="tips_bottom"))
    image tooltip_profile_harper=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("H.A.R.P.E.R.", style="tips_top")), (descriptionX,descriptionY), Text("The Artificial Intelligence which controls all of the functions of the Smart House. Often speaks through its ARMs.", style="tips_bottom"))
    image tooltip_profile_neeringunk=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Angela Neering", style="tips_top")), (descriptionX,descriptionY), Text("The lead programmer and designer of the Smart House project.", style="tips_bottom"))
    image tooltip_profile_neering=LiveComposite((liveComWidth, liveComHeight), (titleX,titleY), ImageReference(Text("Angela Neering", style="tips_top")), (descriptionX,descriptionY), Text("The lead programmer and designer of the Smart House project. Fairly rude.", style="tips_bottom"))


    $ my_picName = ""
    transform inv_eff: # too lazy to make another version of each item, we just use ATL to make hovered items super bright
        zoom 0.52 xanchor 0.5 yanchor 0.5
        on idle:
            linear 0.2 alpha 1.0
        on hover:
            linear 0.2 alpha 2.5


    transform pro_eff: # too lazy to make another version of each item, we just use ATL to make hovered items super bright
        zoom 0.52 xanchor 0.5 yanchor 0.5
        on idle:
            linear 0.2 alpha 1.0
        on hover:
            linear 0.2 alpha 2.5

    transform arrow_eff:
        zoom 1.0
        on idle:
            linear 0.1 zoom 1.0
        on hover:
            linear 0.1 zoom 1.5
        on selected_idle:
            zoom 1.0
        on selected_hover:
            zoom 1.1

    transform flipOut:
        yanchor 0.5
        yzoom 0.01
        linear 0.1 yzoom 1.0


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

screen inventory_screen_button():
    hbox align (0,0) spacing 10:
        imagebutton idle "assets/menu/evidence_default.png" hover "assets/menu/evidence_selected.png" action [ Show("inventory_screen")]
    hbox align (1.0,0) spacing 10:
        imagebutton idle "assets/menu/options_default.png" hover "assets/menu/options_selected.png" action [ Show("custom_menu")]
    hbox align (0.5,0) spacing 10:
        imagebutton auto "assets/menu/caselog_%s.png" action [ Show("history")]

screen inventory_screen():
    tag menu
    add "gui/inventory3.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown
    hbox align (.8,.0) spacing 20:
        imagebutton auto "assets/menu/inv_profile_%s.png" keysym 'mouseup_3' action [ Hide("inventory_screen"), Show("profile_screen",ImageDissolve("gui/blinds.png", 0.75)), Hide("gui_tooltip"), Hide("gui_check")]

    hbox align (0.2,0.0) spacing 20:
        imagebutton auto "assets/menu/inv_back_%s.png" action [ Hide("inventory_screen")]
    $ x = 515
    $ y = 85
    $ i = 0
    $ sorted_items = sorted(inventory.items, key=attrgetter('name'), reverse=True)
    $ next_inv_page = inv_page + 1
    if next_inv_page > int(len(inventory.items)/9):
        $ next_inv_page = 0
        $prev_inv_page = inv_page - 1
    for item in sorted_items:
        if i+1 <= (inv_page+1)*9 and i+1>inv_page*9:
            $ x += 188
            if i%3==0:
                $ y += 195
                $ x = 1386
            $ pic = item.image
            $ picName = pic.replace("gui/inv_", "").replace(".png", "")
            $ my_tooltip = "tooltip_inventory_" + picName # we use tooltips to describe what the item does.
            $ my_checker = "gui/check_" + picName + ".png"
            imagebutton idle pic hover pic xpos x ypos y action NullAction() hovered [ Play ("sound", "sound/click.wav"), Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693,), Show("gui_check", check_pic=my_checker, my_check_ypos=90 )] unhovered [ Hide("gui_tooltip"), Hide("gui_check") ] at inv_eff
            #add "gui/selected.png" xpos x ypos y anchor(.5,.5)
        $ i += 1

        if len(inventory.items)>9:
            imagebutton auto "gui/inventory_arrow_%s.png" action [SetVariable('inv_page', prev_inv_page), Show("inventory_screen")] xpos .645 ypos .40
            imagebutton auto "gui/inventory_arrow_%s.png" action [SetVariable('inv_page', next_inv_page), Show("inventory_screen")] xpos .975 ypos .40 at flip



screen present_evidence_screen():
    tag menu
    add "gui/inventory3.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown
    $ x = 515
    $ y = 85
    $ i = 0
    $ sorted_items = sorted(inventory.items, key=attrgetter('name'), reverse=True)
    $ next_inv_page = inv_page + 1
    $prev_inv_page = inv_page - 1
    if next_inv_page > int(len(inventory.items)/9):
        $ next_inv_page = 0
    if prev_inv_page < 0:
        $ prev_inv_page = int(len(inventory.items)/9)
    for item in sorted_items:
        if i+1 <= (inv_page+1)*9 and i+1>inv_page*9:
            $ x += 188
            if i%3==0:
                $ y += 195
                $ x = 1386
            $ pic = item.image
            $ picName = pic.replace("gui/inv_", "").replace(".png", "")
            $ my_tooltip = "tooltip_inventory_" + picName # we use tooltips to describe what the item does.
            $ my_checker = "gui/check_" + picName + ".png"
            imagebutton idle pic hover pic xpos x ypos y action [SetVariable("present_response", picName), Hide("present_evidence_screen"), Hide("gui_tooltip"), Hide("gui_check"), Hide("back_button"), Jump(current_present), Return(None) ] hovered [ Play ("sound", "sound/click.wav"), Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693,), Show("gui_check", check_pic=my_checker, my_check_ypos=50 )] unhovered [ Hide("gui_tooltip"), Hide("gui_check") ] at inv_eff
            #add "gui/selected.png" xpos x ypos y anchor(.5,.5)
        $ i += 1
        if len(inventory.items)>9:
            imagebutton auto "gui/inventory_arrow_%s.png" action [SetVariable('inv_page', prev_inv_page), Show("present_evidence_screen")] xpos .645 ypos .40
            imagebutton auto "gui/inventory_arrow_%s.png" action [SetVariable('inv_page', next_inv_page), Show("present_evidence_screen")] xpos .975 ypos .40 at flip

screen gui_tooltip (my_picture="", my_tt_xpos=620, my_tt_ypos=800):
    add my_picture xpos my_tt_xpos ypos 75

screen gui_check (check_pic="", my_check_xpos=42, my_check_ypos=100):
    add check_pic xpos 40 ypos 200 size (550,550)



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
    style.tips_top.color="193f23"
    style.tips_top.outlines=[(3, "76bf89", 0,0)]
    style.tips_top.kerning = 5

    style.tips_bottom = Style(style.tips_top)
    style.tips_top.size=48
    style.tips_bottom.outlines=[(0, "76bf89", 1, 1), (0, "76bf89", 2, 2)]
    style.tips_bottom.kerning = 2

    style.button.background=Frame("gui/frame.png",25,25)
    style.button.yminimum=52
    style.button.xminimum=52
    style.button_text.color="000"


screen profile_screen():
    tag menu
    add "gui/inventory3.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown
    hbox align (.8,.0) spacing 20:
        imagebutton auto "assets/menu/inv_inventory_%s.png" keysym 'mouseup_3' action [ Hide("profile_screen"), Show("inventory_screen",ImageDissolve("gui/blinds.png", 0.75)), Hide("gui_tooltip"), Hide("gui_check")]

    hbox align (0.2,0.0) spacing 20:
        imagebutton auto "assets/menu/inv_back_%s.png" action [ Hide("profile_screen")]

    $ x = 515 # coordinates of the top left item position
    $ y = 85
    $ i = 0
    $ sorted_items = sorted(profile.items, key=attrgetter('name'), reverse=True)
    $ next_pro_page = pro_page + 1
    $ prev_pro_page = pro_page - 1
    if next_pro_page > int(len(profile.items)/9):
        $ next_pro_page = 0
    if prev_pro_page < 0:
        $ prev_pro_page = int(len(profile.items)/9)
    for item in sorted_items:
        if i+1 <= (pro_page+1)*9 and i+1>pro_page*9:
            $ x += 188
            if i%3==0:
                $ y += 195
                $ x = 1386
            $ pic = item.image
            $ picName = pic.replace("gui/inv_", "").replace(".png", "")
            $ my_tooltip = "tooltip_profile_" + picName # we use tooltips to describe what the item does.
            $ my_checker = "gui/check_" + picName + ".png"
            #add "gui/inv_hover.png" xpos x ypos y anchor(.5,.5)
            imagebutton idle pic hover pic xpos x ypos y action NullAction() hovered [ Play("sound", "sound/click.wav"), Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693), Show("gui_check", check_pic=my_checker, my_check_ypos=100,) ] unhovered [Hide("gui_tooltip"), Hide("gui_check")] at inv_eff

        $ i += 1
        if len(profile.items)>9:
            imagebutton auto "gui/inventory_arrow_%s.png" action [SetVariable('pro_page', prev_pro_page), Show("profile_screen")] xpos .645 ypos .40
            imagebutton auto "gui/inventory_arrow_%s.png" action [SetVariable('pro_page', next_pro_page), Show("profile_screen")] xpos .975 ypos .40 at flip


screen back_button():
    hbox align (0.2,0.0) spacing 20:
        imagebutton auto "assets/menu/inv_back_%s.png" action [ SetVariable("present_response", "Back"), Hide("back_button"), Hide("present_profile_screen"), Hide("present_evidence_screen"), Jump(current_present)]

screen present_profile_screen():
    tag menu
    add "gui/inventory3.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown


    $ x = 515 # coordinates of the top left item position
    $ y = 85
    $ i = 0
    $ sorted_items = sorted(profile.items, key=attrgetter('name'), reverse=True)
    $ next_pro_page = pro_page + 1
    if next_pro_page > int(len(profile.items)/9):
        $ next_pro_page = 0
    for item in sorted_items:
        if i+1 <= (pro_page+1)*9 and i+1>pro_page*9:
            $ x += 188
            if i%3==0:
                $ y += 195
                $ x = 1386
            $ pic = item.image
            $ picName = pic.replace("gui/inv_", "").replace(".png", "")
            $ my_tooltip = "tooltip_profile_" + picName # we use tooltips to describe what the item does.
            $ my_checker = "gui/check_" + picName + ".png"
            imagebutton idle pic hover pic xpos x ypos y action [SetVariable("present_response", picName), Hide("present_profile_screen"), Hide("gui_tooltip"), Hide("gui_check"), Hide("back_button"), Jump(current_present), Return(None)] hovered [ Play("sound", "sound/click.wav"), Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693), Show("gui_check", check_pic=my_checker, my_check_ypos=100,) ] unhovered [Hide("gui_tooltip"), Hide("gui_check")] at pro_eff
            #add "gui/selected.png" xpos x ypos y anchor(.5,.5)
        $ i += 1
        if len(profile.items)>9:
            imagebutton auto "gui/inventory_arrow_%s.png" action [SetVariable('pro_page', prev_pro_page), Show("present_profile_screen")] xpos .645 ypos .40
            imagebutton auto "gui/inventory_arrow_%s.png" action [SetVariable('pro_page', next_pro_page), Show("present_profile_screen")] xpos .975 ypos .40 at flip





###########################
# Testimony Screen

###########################
init:
    $ mc_maxhealth = 5
    $ mc_health = mc_maxhealth
    $ mc_health_display = mc_health
    python:
        def settesti(current, left, right, press, advice, cs):
            store.testipart = current
            store.testileft = left
            store.testiright = right
            store.testipress = press
            store.testiobject = object
            store.showtestimony = True
            store.testadvice = advice
            store.currentStatement = cs

screen testi():
    $ CurrentTestimony = store.testipart
    if store.testileft <> None:
        imagebutton auto "assets/menu/testi_arrow_%s.png" keysym 'K_LEFT' action Jump(store.testileft) xpos 0.05 ypos 0.58 at flip
    if store.testiright <> None:
        imagebutton auto "assets/menu/testi_arrow_%s.png" keysym 'K_RIGHT' action Jump(store.testiright) xpos 0.18 ypos 0.58
    hbox align (1.0,0) spacing 10:
        imagebutton idle "assets/menu/options_default.png" hover "assets/menu/options_selected.png" action [ShowMenu("custom_menu")]
    vbox align (-0.1,0.075) spacing 30:
        textbutton "Press" style "testiButton" text_style "testiText" action [Jump(store.testipress)]
        textbutton "Present" style "testiButton" text_style "testiText" action [SetVariable("CurrentTestimony", store.testipart), Show("present_evidence_screen"), Show("back_button"), SetVariable("back_action", store.testipart)]
        textbutton "Advice" style "testiButton" text_style "testiText" action [ SetVariable("CurrentTestimony", store.testipart), Jump(store.testadvice)]
    bar left_bar "assets/menu/health_left.png" right_bar "assets/menu/health_right.png" range mc_maxhealth value mc_health xmaximum 530 ysize 100 xpos 0.37 ypos 0.01 thumb None

    $ m = 0
    hbox align (0.33,0.785) spacing 10:
        for m in range(0,testiLength):
            if m == (store.currentStatement - 1):
                image "assets/menu/TestiDotHighlight.png"
            else:
                image "assets/menu/TestiDot.png"
            $m == m+1

screen healthBar():
    bar left_bar "assets/menu/health_left.png" right_bar "assets/menu/health_right.png" range mc_maxhealth value mc_health_display xmaximum 530 ysize 100 xalign 0.5 yalign 0.05 thumb None

init -2:

    style testiButton:
        size_group "mm"
        xsize 750
        ysize 150
        ymargin 10
        background Frame("assets/menu/OCP_TextboxTest2.png",75)
        hover_xpos 40

    style testiText:
        size 48
        text_align 1.0
        font "Young.ttf"
        hover_color "c5e6ca"
        xalign 0.65
        yalign 0.5
        hover_xalign 0.7


###########################
# Debug JumpTo Button

###########################

screen jumpTo():
    hbox align (1.2,1.2) spacing 0:
        textbutton "jump2" keysym 'j' action Jump("jumpToMenu")
