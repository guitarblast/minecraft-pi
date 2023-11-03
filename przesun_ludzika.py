def przesun_ludzika(dx, dy, dz):
    x, y, z = mc.player.getPos()
    mc.player.setPos(x + dx, y + dy, z + dz)

    x, y, z = mc.player.getPos()
    print("Moja pozycja to (x, y, z):" + str(x), str(y), str(z))