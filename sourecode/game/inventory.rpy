
init -1 python:
    import renpy.store as store
    import renpy.exports as renpy # we need this so Ren'Py properly handles rollback with classes
    from operator import attrgetter # we need this for sorting items

    inv_page = 0 # initial page of teh inventory screen
    item = None
    class Player(renpy.store.object):
        def __init__(self, name):
            self.name=name


    class Item(store.object):
        def __init__(self, name, image=""):
            self.name = name
            self.image=image # image file to use for this item


    class Inventory(store.object):
        def __init__(self):
            self.items = []
        def add(self, item): # a simple method that adds an item; we could also add conditions here (like check if there is space in the inventory)
            self.items.append(item)
        def drop(self, item):
            self.items.remove(item)



    showitems = True #turn True to debug the inventory



################ INVENTORY SCREEN   ######################

screen inventory():
    zorder 205
    tag menu
    modal True



    add "images/inv/overlay.png" at for_overlay_posters
    add "images/inv/inv_ground.png"





    $ x = 370
    $ y = 35
    $ i = 0
    $ sorted_items = inventory.items
    for item in sorted_items:
        if i+1 <= (inv_page+1)*20 and i+1>inv_page*20:
            $ x += 110
            if i%5==0:
                $ y += 110
                $ x = 370
            $ pic = item.image
            imagebutton idle pic hover pic xpos x ypos y hover_background "inv_item_bg" action [SetVariable("item", item), Show("equip_items"), With(Dissolve(0.3)), Hide('inventory')] 
        $ i += 1
    imagebutton auto "images/inv_%s.png" action [Hide('inventory'), Jump("checkroom")] xpos 1180 ypos 0 focus_mask True
image inv_item_bg:
    "images/inv/item_hover.png"
    alpha 0.7


################ INVENTORY'S ITEMS SCREEN   ######################




screen equip_items:
    add item.image xpos 1176 ypos 100



