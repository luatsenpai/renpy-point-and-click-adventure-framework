label pk:

    scene bg room
    show semi stand:
        xpos 378
        ypos 0
        xzoom -1.0


    show screen checkMouse
    show screen pk
label pk_walk:
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
screen pk:

    if sX>561 and sX<704:
        imagebutton:
            xpos 579
            ypos 184
            idle "eye_idle.png"
            hover "eye_hover.png"
            action [Hide("displayTextScreen"), Jump("getkey")]
            hovered Show("displayTextScreen", displayText = "Closet") 
            unhovered Hide("displayTextScreen")
    elif sX>984 and sX<1145:
        imagebutton:
            xpos 1012
            ypos 184
            idle "eye_idle.png"
            hover "eye_hover.png"
            action [Hide("displayTextScreen"), Jump("door")]
            hovered Show("displayTextScreen", displayText = "Door") 
            unhovered Hide("displayTextScreen")
    imagebutton auto "images/inv_%s.png" action Show('inventory') xpos 1180 ypos 0 focus_mask True
label door:
    hide screen checkMouse
    hide screen pk
    if door_lock == True:
        if item == ikey:
            $ inventory.drop(ikey)
            $ door_lock = False
            $ equipitem == None
            $ room == "bedroom"
            jump checkroom
        else:
            "Door Lock"
            jump checkroom 
    else:
        $ room == "bedroom"
        jump checkroom