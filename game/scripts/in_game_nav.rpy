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

    add "mm_bg_scroll" alpha 0.75

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
        hotspot (235, 140, 370, 70) action SetVariable("menustate","options")
        hotspot (614, 140, 370, 70) action SetVariable("menustate","save")
        hotspot (985, 140, 370, 70) action SetVariable("menustate","load")
        hotspot (1344, 140, 370, 70) action SetVariable("menustate","quit")

    if menustate == "options":
        use preferences
    if menustate == "save":
        use save
    if menustate == "load":
        use load
    if menustate == "quit":
        use custom_quit

    hbox align (0.97,-0.01) spacing 20:
        imagebutton auto "assets/menu/inv_back_%s.png" action [ Hide("custom_menu")]

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
