init:
    $ current_talk = "None"
    $ current_background = "None"
    $ current_present = "None"
    $ current_move = "None"
    $ back_action = "None"
    $ menuground = "assets/menu/options_menu_options.png"
    $ menustate = "options"

screen custom_menu():
    tag menu
    modal True
    if menustate == "options":
        $ menuground = "assets/menu/options_menu_options.png"
    if menustate == "save":
        $ menuground = "assets/menu/options_menu_save.png"
    if menustate == "load":
        $ menuground = "assets/menu/options_menu_load.png"
    if menustate == "quit":
        $ menuground = "assets/menu/options_menu_quit.png"

    imagemap:
        ground menuground
        hotspot (235, 70, 370, 70) action SetVariable("menustate","options")
        hotspot (614, 70, 370, 70) action SetVariable("menustate","save")
        hotspot (985, 70, 370, 70) action SetVariable("menustate","load")
        hotspot (1344, 70, 370, 70) action SetVariable("menustate","quit")

    if menustate == "options":
        #add "gui/inventory2.png"
        use preferences
    if menustate == "save":
        use save
    if menustate == "load":
        use load
    if menustate == "quit":
        use custom_quit

    hbox align (.97,.03) spacing 20:
        textbutton "Return" action [ Hide("custom_menu"), Return(None)]

screen examine_navigation():
    vbox xalign 0.5 yalign 0.95:
        imagemap:
            ground "assets/menu/Examine_Nav_Default.png"
            hover "assets/menu/Examine_Nav_Selected.png"
            hotspot(12,12,217,88) action Show(current_move) #Move
            hotspot(838,12,275,88) keysym 'mouseup_3' action Show("inventory_screen") #Evidence
            hotspot(1690,12,217,88) action ShowMenu("custom_menu") #Options

screen button():
    vbox xalign 0.99 yalign 0.01:
        imagebutton:
            idle "assets/buttons/tracker_idle.png"
            hover "assets/buttons/tracker_hover.png"
            action ui.callsinnewcontext("nav_screen_label")

label nav_screen_label:
    window hide
    call screen examine_navigation
    return
