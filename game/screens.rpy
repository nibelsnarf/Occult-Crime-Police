# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

init python:
     _game_menu_screen = "custom_menu"

init:
     $ save_name = "Prologue"
     $ picked_case = 0

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=True):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"
            window:
                id "window"

                has vbox:
                    box_wrap True
                    style "say_vbox"


                text what id "what"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"



    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

style say_two_window_vbox:
    yalign 0.93

style say_who_window:
    ypos -50
    top_padding 3
    background Frame("assets/menu/BorderedWindow.png", 170,170)
    xpadding 45
    xmargin 200

style say_window:
    ypos 210
    background "assets/menu/OCP_TextboxTest.png"
    top_padding 50
    xpadding 100
    xmargin 110

    #ysize 225
    #box_wrap True

style say_vbox:
    box_wrap True
##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.975

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:
                    if not chosen:
                        button:
                            action action
                            style "menu_choice_button"

                            text caption style "menu_choice"
                    elif chosen == True:
                        button:
                            action action
                            style "menu_choice_chosen_button"

                            text caption style "menu_choice_chosen"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default:
        background None

style menu_choice_button is button:
      xminimum int(config.screen_width * 0.90)
      xmaximum int(config.screen_width * 0.90)
      yminimum int(config.screen_height * 0.05)
      top_margin 7
      padding(30,10)
      idle_background "#3A8256"
      hover_background "#479e69"

style menu_choice:
      size 28
      color "FFFFFF"
      #outlines [(1, "#000", 0, 0)]
      xalign 0.0
      hover_xalign 0.01
      text_align 0.0

#style menu_choice_chosen:
    #color "cccccc"
    #strikethrough True



##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    #use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    #use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .5
        yalign .75
        background "#FFFFFF00"
        has vbox


        textbutton _("Start Game") action Start() text_style "mm_text"
        textbutton _("Load Game") action ShowMenu("load")  text_style "mm_text"
        textbutton _("Options") action ShowMenu("mm_prefs")  text_style "mm_text"
        textbutton _("Quit") action Quit(confirm=False)  text_style "mm_text"

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"
        xsize 500
        ysize 75
        ymargin 10
        background "#299363"
        hover_background "#2bb269"

    style mm_text:
        size 36
        xalign 0.5
        yalign 0.5



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():
    frame:
        style "file_picker_frame"

        xalign 0.5
        yalign 0.5
        xmargin 300

        has vbox

        null height 5

        #The buttons at the top allow the user to pick a
        #page of files.
        hbox:
            xalign 0.5
            style_group "file_picker_nav"

            textbutton _("Prev"):
                action FilePagePrevious()

            for i in range(1, 7):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 1
        $ rows = 3

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action [Stop(channel="movie"), FileAction(i)]
                    xfill True
                    style "large_button"

                    has hbox
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)

        hbox:
            xalign 0.5
            style_group "file_picker_nav"

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Regular"):
                action FilePage(1)

            textbutton _("Quick"):
                action FilePage("quick")

            textbutton _("Return"):
                action Return()

        null height 5

screen save():
    tag menu
    use file_picker

screen load():
    tag menu
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Custom Quit Screen
#
# For use in Game Menu. Asks if player really wants to quit.

screen custom_quit():
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 100
        text "Do you really want to quit?\nUnsaved progress may be lost." size 40 color "#000000"
        textbutton _("Yes") action Quit(confirm=None)


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    #tag menu

    vbox ypos 0.5:
        frame:
            style_group "pref"
            has vbox

            label _("Display")
            textbutton _("Window") action Preference("display", "window")
            textbutton _("Fullscreen") action Preference("display", "fullscreen")

        frame:
            style_group "pref"
            has vbox

            label _("Transitions")
            textbutton _("All") action Preference("transitions", "all")
            textbutton _("None") action Preference("transitions", "none")

        frame:
            style_group "pref"
            has vbox

            textbutton _("Joystick...") action Preference("joystick")

        frame:
            style_group "pref"
            has vbox

            label _("Music Volume")
            bar value Preference("music volume")

        frame:
            style_group "pref"
            has vbox

            label _("Sound Volume")
            bar value Preference("sound volume")

            if config.sample_sound:
                textbutton _("Test"):
                    action Play("sound", config.sample_sound)
                    style "soundtest_button"

        if config.has_voice:
            frame:
                style_group "pref"
                has vbox

                label _("Voice Volume")
                bar value Preference("voice volume")

                textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                if config.sample_voice:
                    textbutton _("Test"):
                        action Play("voice", config.sample_voice)
                        style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 0.4
        top_margin 5

    style Display:
        color "653F1A"

    style pref_vbox:
        xfill True

    style say_label:
        size 60
        bold False
        kerning -3
        font "NeoBulletin Semi Bold.ttf"
        color "000000"

    style say_dialogue:
        size 35
        kerning 0
        font "NeoBulletin Semi Bold.ttf"
        color "abd8b7"
        outlines [(2, "000000", 0,0)]

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Main Menu Preferences
#
# I need a separate screen for the preferences menu on the main menu

screen mm_prefs():
    modal True
    add "assets/backgrounds/preferences.png" xalign 0.5 yalign 0.9
    use preferences
    textbutton "Return" action [ Hide("mm_prefs"), Return(None)] xalign 0.5 yalign 0.9


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"
