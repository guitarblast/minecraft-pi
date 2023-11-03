from mcpi import minecraft, block
from stworzaki import wyswietl_wspolrzedne, odczytaj_wpolrzedne_ludzika

mc = minecraft.Minecraft.create()

def wyswietl_wszystkie_bloki():
    id_bloku = 0
    x, y, z = mc.player.getPos()
    for i in range(0, 300):
        # print(i)
        id_bloku = i
        for data_id in range(0, 11):
            mc.setBlock(x + i, y , z + data_id, id_bloku, data_id)
            # print(j)
            # id_bloku += 1
            # # print("i = " + str(i) + ", j = " + str(j))
            # mc.setBlock(x + i, y , z + j, id_bloku, 1)