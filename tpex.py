from mcpi.minecraft import Minecraft
mc = Minecraft.create()
swamp = -483, 62, 385
mountains = -519, 108, 264
plains = -409, 64, 239
while True:
    a = input('Where do you want to go? ')
    if a == 'swamp':
        mc.player.setPos(*swamp)
        break
    elif a == 'mountains':
        mc.player.setPos(*mountains)
        break
    elif a == 'plains':
        mc.player.setPos(*plains)
        break
    else:
        print('Enter a valid location')
