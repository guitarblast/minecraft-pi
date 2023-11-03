from mcpi import minecraft

mc = minecraft.Minecraft.create()


def wyswietl_wspolrzedne(x, y, z):
    print("Pozycja ludzika:")
    print(x, y, z)

def odczytaj_wpolrzedne_ludzika():
    x, y, z = mc.player.getPos()
    wyswietl_wspolrzedne(x, y, z)
    return x, y, z

def wyswietl_obecna_pozycje():
    x, y, z = mc.player.getPos()
    wyswietl_wspolrzedne(x, y, z)

def wyswietl_stworzaki():
    x, y, z = mc.player.getPos()
    wyswietl_wspolrzedne(x, y, z)
    metody = dir(mc) ## .sort()
    print(metody)
    print(len(metody))
    for metoda in metody:
        print("  ." + metoda)
    print(mc.getPlayerEntityIds())
    # print(mc.getPlayerEntityId())
    metody = dir(mc.entity) ## .sort()
    print(metody)
    print(len(metody))
    for metoda in metody:
        print("  ." + metoda)
    # stworzaki = mc.entity.getName()
    stworzaki = mc.entity.getEntities(0)
    print(stworzaki)

def zrob_schody(material):
    x, y, z = mc.player.getPos()
    wyswietl_wspolrzedne(x, y, z)
    for i in range(0,30):
        mc.setBlocks( x+i, y+i, z+5, x+i, y+i, z+1, material)
        
        
        