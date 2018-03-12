# EFFECTS.rpy

init:
    image black = "#000000"
    image white = "#ffffff"
    image gray = "#c0c0c0"

    python:

        import math

        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist, freq):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # position centrale de départ
                self.dist = dist    # distance en pixels maximum du point de départ
                self.freq = freq    # nombre de "rebonds" en tout
                self.child = child

            def __call__(self, t, sizes):

                #### Added by PyTom

                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                ### End Added by PyTom


                d = 5  # friction
                f = self.freq   # fréquence de rebonds

                # tc : valeur courante passée par la fonction "dampened harmonic"
                tc = (d**(-t))*math.sin(t*math.pi*f)

                # version dampen qui "tourne" sur 360°
                #nx = xpos + ((tc) * self.dist) * (1.0-t)
                #ny = ypos + ((tc) * self.dist) * (t)

                # version toujours agitée au max, positionnement aléatoire (Phoenix Wright style)
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                ### Added by PyTom - return 0, 0.

                return (int(nx), int(ny), 0, 0)


        def _Shake(start, time, child=None, dist=100.0, freq=25, **properties):

            move = Shaker(start, child, dist=dist, freq=freq)

            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True, ### Changed by PyTom
                          **properties)

        Shake = renpy.curry(_Shake)

        # FOR MOVETRANSITION


        def easemove_factory(pos1, pos2, delay, d):
            if pos1 == pos2:
                return d

            return MoveEase2(pos1, pos2, delay, d)

        def shaketrans(time, dist):
            renpy.with_statement(Shake((0,0,0,0), time, dist=dist))
        #
    #


    $ tinyshake = Shake((0,0,0,0), 0.5, dist=5)
    $ smallshake = Shake((0,0,0,0), 0.5, dist=10)
    $ shake = Shake((0,0,0,0), 1.0, dist=15)
    $ shakeN = Shake(None, 0.5, dist=15)    # to be used with "at position, *" (ex: at left, shakeN)
    $ bigshake = Shake((0,0,0,0), 1.0, dist=25)
    $ objectionShake = Shake((0.5,0.5,0.5,0.5), 0.5, dist=15)

    $ flash = Fade(.25, 0, .75, color="#fff")

    $ pantransition = MoveTransition(0.8, factory=easemove_factory)
    $ halfpantransition = MoveTransition(0.5, factory=easemove_factory)

#
label objection:
    show objection at objectionShake

    show white
    pause 0.02
    hide white
    $ renpy.pause(1.3)

    hide objection

    return

label persuasion:
    show white with Pause(0.05)
    hide white
    show PERSU
    pause 1.0
    show white with Pause(0.05)
    hide white
    show ASION
    pause 1.0
    show white with Pause(0.05)
    hide white
    hide screen inventory_screen_button
    return

label witness_statement:
    show Witness
    show Statement
    pause 0.5
    show white with Pause(0.05)
    hide white with dissolve
    pause 2.0
    return

label interrogation:
    show Interro
    show Gation
    pause 0.3
    show white with Pause(0.05)
    hide white with dissolve
    pause 1.5
    return
    return
