﻿image bg room="pk.png"

image semi stand = "2.png"
image eye = "eye.png"
image semi walk:
    "1.png"
    0.3
    "2.png"
    0.3
    "3.png"
    0.3
    repeat
default room = "pk"

default sY=378
default mX=0
default dist=0
default standWalk=0
default test=50
default direction=0 #0 left 1 right

default sX= 0

            

screen checkMouse():
    if standWalk==0:
        key "mousedown_1" action Jump("checkDist")




# The game starts here.
label start:
    python:
        inventory = []
    jump checkroom
label checkroom:
    if room == "pk":
        jump pk
label pk:

    scene bg room

    show screen inventory_screen

    show screen checkMouse
    show screen pk

screen pk:
    if sX>561 and sX<704:
        if ikey not in inventory:

            imagebutton:
                xpos 579
                ypos 184
                idle "eye_idle.png"
                hover "eye_hover.png"
                action [Hide("displayTextScreen"),addItem(ikey),Jump("pk")]
                hovered Show("displayTextScreen", displayText = "Closet") 
                unhovered Hide("displayTextScreen")

        else:

            imagebutton:
                xpos 579
                ypos 184
                idle "eye_idle.png"
                hover "eye_hover.png"
                action Jump("pk")
                hovered Show("displayTextScreen", displayText = "Closet") 
                unhovered Hide("displayTextScreen")

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





screen inventory_screen:
    zorder 100
    #a sexy grid
    frame:
        grid 4 1:
        
            spacing 15
            xpos 0
            ypos 0

            for index, item in enumerate(inventory):
                imagebutton: 
                   idle item.image_name 
                   hover item.hover_image
                   selected_idle item.selected_image
                   action selectItem(item)

            for i in range(4 - len(inventory)):
                add "empty.png"