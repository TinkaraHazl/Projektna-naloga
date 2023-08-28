import os
import csv

def napisi_csv(fieldnames, rows, directory, filename):
    """
    Funkcija v csv datoteko podano s parametroma "directory"/"filename" zapiše
    vrednosti v parametru "rows" pripadajoče ključem podanim v "fieldnames"
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    # ko odpremo datoteko, podamo neobevzni argument newline in ga nastavimo na prazen niz,
    # sicer bomo na windowsih imeli grd csv, kjer bo vsaki dejanski vrstici sledila prazna
    with open(path, 'w', encoding='utf-8', newline='') as csv_file:
        pisatelj = csv.DictWriter(csv_file, fieldnames=fieldnames)
        pisatelj.writeheader()
        for row in rows:
            pisatelj.writerow(row)
    return


def pokemoni_v_csv(ads, directory, filename):
    """Funkcija vse podatke iz parametra "ads" zapiše v csv datoteko podano s
    parametroma "directory"/"filename". Funkcija predpostavi, da so ključi vseh
    slovarjev parametra ads enaki in je seznam ads neprazen."""
    # Stavek assert preveri da zahteva velja
    # Če drži se program normalno izvaja, drugače pa sproži napako
    # Prednost je v tem, da ga lahko pod določenimi pogoji izklopimo v
    # produkcijskem okolju
    assert ads and (all(slovar.keys() == ads[0].keys() for slovar in ads))
    imena_stolpcev = sorted(ads[0])
    napisi_csv(imena_stolpcev, ads, directory, filename)


#def shrani_osebe(pokemoni):
#       ze_videni = set()
#       for pokemon in pokemoni:
#           if pokemon["ability"] is not None:
#               for ability in pokemon["ability"]:
#                   if igralec["id"] not in ze_videni:
#                       pisatelj.writerow([igralec["id"], igralec["ime"]])
#                       ze_videni.add(igralec["id"])
#           for igralec in film["reziserji"]:
#               if igralec["id"] not in ze_videni:
#                   pisatelj.writerow([igralec["id"], igralec["ime"]])
#                   ze_videni.add(igralec["id"])
