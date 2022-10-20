label getkey:
    hide screen checkMouse
    hide screen pk
    if get_ikey == False:
        "You got a {color=ff6c00}Key{/color}"
        $ inventory.add(ikey)
        $ get_ikey = True
        jump checkroom
    else:
        "Empty"
        jump checkroom