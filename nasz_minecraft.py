from mcpi import minecraft, block
import mcpi
from dodaj_materialy import dodaj_szescian_tnt, dodaj_kolumne_tnt, dodaj_tunel_tnt, dodaj_kolumne_materialu, dodaj_szereg_z_materialu, dodaj_blok_z_materialu, dodaj_kwadrat_z_materialu, dodaj_kwadrat_z_materialu2, dodaj_kwadrat_z_materialu_3, ustaw_piramide_z_fosa, ustaw_znak, ustaw_piramide, ustaw_jedzonko, ustaw_material, ustaw_piramide_z_komnata, zrob_pionowy_plasterek, zrob_cztery_sciany, ustaw_piramide_bez_fosy, zrob_budynek
from wyswietl_wszystkie_bloki import wyswietl_wszystkie_bloki
from stworzaki import wyswietl_stworzaki, zrob_schody
import os

print(f"Sciezka do mcpi:  {os.path.dirname(mcpi.__file__)}")


#zrob_pionowy_plasterek(-10, 0, -10, 10, 20, -10, block.GLOWSTONE_BLOCK.id, 1)
# Zrob pusta komnate (z powietrza)
# ustaw_piramide_z_komnata(9, block.GLOWSTONE_BLOCK.id, 1)
# ustaw_piramide_z_fosa(12, 1, 10, block.GLASS.id, 1)
# ustaw_jedzonko(block.RAIL.id, 1)
# ustaw_material(block.LADDER  .id, 1)
# ustaw_znak()
# dodaj_szereg_z_materialu(-10, 5, 1, 0, block.RAIL.id, 1)
# dodaj_kwadrat_z_materialu(dlugosc_boku, wysokosc, material, data)
# dodaj_kwadrat_z_materialu( 19, 60, 64, 64, block.DIAMOND_BLOCK.id, 2)
# dodaj_kwadrat_z_materialu_3(dlugosc_boku=20, wysokosc=10, material=block.DIAMOND_BLOCK.id, data=1)
# dodaj_kwadrat_z_materialu2(1, block.COAL_ORE.id, 1)
# ustaw_piramide_bez_fos
# y( 60, block.GLASS.id, 1, 58, block.AIR.id, 1, 20, 20, 20, 10, 40, 10, block.GLOWING_OBSIDIAN.id, 1)
# zrob_cztery_sciany(szerokosc=3, dol=-1, gora=34, material=block.LAPIS_LAZULI_BLOCK, data=1)
# mc.player.setPos(x, y + 100, z)
# set_interval(przesun_ludzika, .1)
# for i in range(0,100):
#     mc.setBlock(x + 2 + i * 1, y + 3, z, i)
# wyswietl_stworzaki()
# wyswietl_wszystkie_bloki()

# dodaj_kolumne_tnt(10 , 0, 1)
# 
# zrob_schody(block.STAIRS_WOOD.id)
#
# zrob_budynek()
# 
# 
# 
dodaj_tunel_tnt(1000, -1000, -1)
# dodaj_kolumne_materialu(200, 0, -1, block.DIAMOND_BLOCK.id, 1)
#dodaj_kolumne_materialu(200, 0, -1, block.DIAMOND_BLOCK.id, 1)
#dodaj_blok_z_materialu.Block.(id, 1)
# dodaj_blok_z_materialu(.WATER foll
#                                                                                                                                                                                                                                                                                               