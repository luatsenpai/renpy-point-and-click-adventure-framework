screen checkMouse():
    if standWalk==0:
        key "mousedown_1" action Jump("checkDist")
label room:

    if direction==0:
        if standWalk==0:


            show semi stand:
                xpos sX
                ypos sY
                xzoom 1.0

            $ renpy.pause(hard=True)
            
            jump checkroom
        else:
            $ standWalk=1

            show semi walk:
                xpos sX
                ypos sY
                xzoom 1.0
                linear dist/100.0 xpos mX

            $ renpy.pause(delay=dist/100.0, hard=True)
            $ sX=mX
            $ standWalk=0
            jump checkroom
    else:
        if standWalk==0:


            show semi stand:
                xpos sX
                ypos sY
                xzoom -1.0

            $ renpy.pause(hard=True)
            jump checkroom
        else:


            show semi walk:
                xpos sX
                ypos sY
                xzoom -1.0
                linear dist/100.0 xpos mX

            $ renpy.pause(delay=dist/100.0, hard=True)
            $ sX=mX
            $ standWalk=0
            jump checkroom

label checkDist:
    $ mX=renpy.get_mouse_pos()[0]
    if mX>1154:
        $mX=1154
    if mX>sX:

        $ dist = mX-sX
        $ standWalk = 1
        $ direction = 0
        jump room

    else:

        $ dist = sX-mX
        $ standWalk = 1
        $ direction = 1
        jump room