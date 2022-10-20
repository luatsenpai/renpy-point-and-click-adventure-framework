image bg room="pk.png"

image semi stand = "2.png"
image eye = "eye.png"
image semi walk:
    "1.png"
    0.1
    "2.png"
    0.1
    "3.png"
    0.1
    repeat





default sY=378
default mX=0
default dist=0
default standWalk=0
default test=50
default direction=0 #0 left 1 right

default sX= 0







# The game starts here.
label start:
    $ inventory = Inventory()
    $ ikey = Item("Key", image="images/inv/i_key.png")
    $ equipitem = None
    $ get_ikey = False
    $ room = "pk"
    $ door_lock = True
    jump checkroom



       






transform for_overlay_posters:
    alpha 0.9

