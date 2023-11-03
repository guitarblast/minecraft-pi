from mcpi import minecraft, block
from stworzaki import wyswietl_wspolrzedne, odczytaj_wpolrzedne_ludzika

mc = minecraft.Minecraft.create()


tnt = 46

def dodaj_szescian_tnt(odleglosc, rozmiar):
    mc.postToChat("UWAGA!!! Dodaje TNT!")
    x, y, z = odczytaj_wpolrzedne_ludzika() 
    mc.setBlocks(x + odleglosc, y + odleglosc, z + odleglosc, x + (rozmiar - odleglosc), y + (rozmiar - odleglosc), z + (rozmiar - odleglosc), tnt, 1)

def dodaj_kolumne_tnt(poczatkowa_wysokosc, koncowa_wysokosc, krok):
    mc.postToChat("UWAGA!!! Dodaje kolumne TNT!")
    x, y, z = odczytaj_wpolrzedne_ludzika()
    for i in range(poczatkowa_wysokosc, koncowa_wysokosc, krok):
        mc.setBlock(x + 0, y + i, z + 2, tnt, 1)

def dodaj_tunel_tnt(poczatkowa_wysokosc, koncowa_wysokosc, krok):
    mc.postToChat("UWAGA!!! Dodaje tunel TNT!")
    x, y, z = odczytaj_wpolrzedne_ludzika()
    for i in range(poczatkowa_wysokosc, koncowa_wysokosc, krok):
        mc.setBlock(x + 3, y + 0, z + i, tnt, 1)
        mc.setBlock(x + 3, y + 1, z + i, tnt, 1)

def dodaj_kolumne_materialu(poczatkowa_wysokosc, koncowa_wysokosc, krok, material, data):
    mc.postToChat("UWAGA!!! Dodaje kolumne z materialu " + str(material))
    x, y, z = odczytaj_wpolrzedne_ludzika()
    for i in range(poczatkowa_wysokosc, koncowa_wysokosc, krok):
        mc.setBlock(x + 0, y + i, z + 2, material, data)

def dodaj_szereg_z_materialu(poczatek, koniec, krok, wysokosc, material, data):
    mc.postToChat("Heeej, dodaje szereg z materialu " + str(material))
    x, y, z = odczytaj_wpolrzedne_ludzika()
    for i in range(poczatek, koniec, krok):
        # for i in range(11, -11, -1):
        # for i in [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10,]:
        mc.setBlock(x + 3, y + wysokosc, z + i, material, data)

def dodaj_kwadrat_z_materialu(poczatek, koniec, krok, wysokosc, material, data):
    mc.postToChat("Heeej, dodaje szereg z materialu " + str(material))
    x, y, z = odczytaj_wpolrzedne_ludzika()
    for i in range(poczatek, koniec, krok):
        # for i in range(11, -11, -1):
        # for i in [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10,]:
        for j in range(poczatek, koniec, krok):
            mc.setBlock(x + j, y + wysokosc, z + i, material, data)

def dodaj_kwadrat_z_materialu2(wysokosc, material, data):
    mc.postToChat("Heeej, dodaje szereg z materialu " + str(material))
    x, y, z = odczytaj_wpolrzedne_ludzika()
    bok_kostki = 3
    mc.setBlocks(x + 4, y + wysokosc, z,\
        x + 4 + bok_kostki, y + wysokosc + bok_kostki, z + bok_kostki, material, data)

def dodaj_kwadrat_z_materialu_3(dlugosc_boku, wysokosc, material, data):
    mc.postToChat("Heeej, dodaje szereg z materialu " + str(material) + ", szybko")
    x, y, z = odczytaj_wpolrzedne_ludzika()
    mc.setBlocks(\
        x - dlugosc_boku / 2, y + wysokosc, z - dlugosc_boku / 2,\
        x + dlugosc_boku / 2, y + wysokosc, z + dlugosc_boku / 2,\
        material, data\
        )

def dodaj_blok_z_materialu( material, data):
    mc.postToChat("Heeej, dodaje blok z materialu " + str(material))
    x, y, z = odczytaj_wpolrzedne_ludzika()
    mc.setBlock(x , y , z , material, data)

def ustaw_znak():
    mc.postToChat("Heeej, dodaje znak")
    x, y, z = odczytaj_wpolrzedne_ludzika()
    mc.setSign(x,y,z,68,1) ##,[line1,line2,line3,line4])

def ustaw_piramide(x, y, z, wysokosc, material, data):
    # Zbuduj warstwy piramidy
    for warstwa in range(0, wysokosc, 1):
        print("warstwa: " + str(warstwa), \
            x - warstwa / 2, y + wysokosc - warstwa, z - warstwa / 2,\
            x + warstwa / 2, y + wysokosc - warstwa, z + warstwa / 2,)
        mc.setBlocks(x - warstwa / 2, y + wysokosc - warstwa, z - warstwa / 2,\
            x + warstwa / 2, y + wysokosc - warstwa, z + warstwa / 2, \
                material, data)

def ustaw_piramide_z_komnata(wysokosc, material, data):
    # Wypisanie wiadomosci na ekranie
    mc.postToChat("Heeej, buduje piramide z komnata, z materialu: " + str(material))

    # Przypisanie zmiennym x, y, z pozycje glowy Steva Pia
    x, y, z = odczytaj_wpolrzedne_ludzika()

    # zbuduj piramide
    ustaw_piramide(x, y, z, wysokosc, material, data)

    # Zrob pusta komnate (z powietrza)
    mc.setBlocks(x - 1, y - 1, z - 1, x + 1, y + 1, z + 1, block.AIR.id, 1)

def ustaw_piramide_z_fosa(wysokosc, material, data, wysokosc2, material2, data2):
    # Wypisanie wiadomosci na ekranie
    mc.postToChat("Heeej, buduje piramide z fosa, z materialu: " + str(material))

    # Przypisanie zmiennym x, y, z pozycje glowy Steva Pia
    x, y, z = odczytaj_wpolrzedne_ludzika()

    # zbuduj piramide
    ustaw_piramide(x, y, z, wysokosc, material, data)
    ustaw_piramide(x, y, z, wysokosc2, material2, data2)

    # Zrob pusta komnate (z powietrza)
    zbuduj_pusta_komnate( x, y, z)

    zrob_cztery_sciany( wysokosc/2+1, -10, 0, block.AIR.id, 1)


def ustaw_jedzonko(material, data):
    mc.postToChat("Heeej, dodaje szereg z materialu: " + str(material))

    x, y, z = odczytaj_wpolrzedne_ludzika()
    # Zrob jedzonko
    mc.setBlock(x + 1, y, z, material, data)

def ustaw_material(material, data):
    mc.postToChat("Heeej, dodaje szereg z materialu " + str(material))
    x, y, z = odczytaj_wpolrzedne_ludzika()
    # Zrob material
    mc.setBlocks(x + 1, y, z, x + 1, y + 4, z, material, data)

imiona = "Hikaru i Haru"
imiona = "Momoko i Lukasz"

print(imiona)

def zbuduj_pusta_komnate( x, y, z):
    mc.setBlocks(x - 1, y - 1, z - 1, x + 1, y + 1, z + 1, block.AIR.id, 1)

def zrob_pionowy_plasterek(x1, y1, z1, x2, y2, z2, material, data):
    x, y, z = odczytaj_wpolrzedne_ludzika()
    mc.setBlocks(x + x1, y + y1, z + z1, x + x2, y + y2, z + z2, material, data)

def zrob_cztery_sciany(szerokosc, dol, gora, material, data):
    r = szerokosc / 2
    x, y, z = odczytaj_wpolrzedne_ludzika()
    mc.setBlocks( x-r, y+dol, z+r, x+r, y+gora, z+r, material, data)
    mc.setBlocks( x-r, y+gora, z-r, x+r, y+dol, z-r, material, data)
    mc.setBlocks( x-r, y+dol, z+r, x-r, y+gora, z-r, material, data)
    mc.setBlocks( x+r, y+gora, z+r, x+r, y+dol, z-r, material, data)

def zrob_piramide_z_pietrami( dal, wys, odl, material, data):
    x, y, z = odczytaj_wpolrzedne_ludzika()
    mc.setBlocks()

def ustaw_piramide_bez_fosy(wysokosc, material, data, wysokosc2, material2, data2, x1, y1, z1, x2, y2, z2, material3, data3):
    # Wypisanie wiadomosci na ekranie
    mc.postToChat("Heeej, buduje piramide z fosa, z materialu: " + str(material))

    # Przypisanie zmiennym x, y, z pozycje glowy Steva Pia
    x, y, z = odczytaj_wpolrzedne_ludzika()

    # zbuduj piramide
    ustaw_piramide(x, y, z, wysokosc, material, data)
    ustaw_piramide(x, y, z, wysokosc2, material2, data2)
    # mc.setBlocks( x+x1, y+y1, z+z1, x-x1, y+y1, z-z1, material3, data3)
    # mc.setBlocks( x+x2, y+y2, z+z2, x-x2, y+y2, z-z2, material3, data3)

def zrob_budynek():

     x, y, z = odczytaj_wpolrzedne_ludzika()

     zrob_cztery_sciany( szerokosc=20, dol=30, gora=64, material=block.BEDROCK.id, data=1)

     dodaj_kwadrat_z_materialu_3( dlugosc_boku=20, wysokosc=30, material=block.LAPIS_LAZULI_BLOCK.id, data=1)
     dodaj_kwadrat_z_materialu_3( dlugosc_boku=20, wysokosc=35, material=block.LAPIS_LAZULI_BLOCK.id, data=1)
     dodaj_kwadrat_z_materialu_3( dlugosc_boku=20, wysokosc=40, material=block.LAPIS_LAZULI_BLOCK.id, data=1)
     dodaj_kwadrat_z_materialu_3( dlugosc_boku=20, wysokosc=45, material=block.LAPIS_LAZULI_BLOCK.id, data=1)
     dodaj_kwadrat_z_materialu_3( dlugosc_boku=20, wysokosc=50, material=block.LAPIS_LAZULI_BLOCK.id, data=1)
     dodaj_kwadrat_z_materialu_3( dlugosc_boku=20, wysokosc=0, material=block.COBWEB.id, data=1)

