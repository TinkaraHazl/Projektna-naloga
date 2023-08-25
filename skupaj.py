import pridobitev
import shranjevanje
import obdelava
import os

def main(redownload=True, reparse=True):
    """Funkcija izvede celoten del pridobivanja podatkov:
    1. Oglase prenese iz bolhe
    2. Lokalno html datoteko pretvori v lepšo predstavitev podatkov
    3. Podatke shrani v csv datoteko
    """
    # 1. Najprej v lokalno datoteko shranimo glavno stran
    pot_html = os.path.join(pridobitev.directory, pridobitev.frontpage_filename)
    if redownload or not os.path.exists(pot_html):
        # če zahtevamo ponovno nalaganje ali pa html_datoteka
        # še ne obstaja, jo naložimo s spleta
        pridobitev.save_frontpage(pridobitev.frontpage_url, pridobitev.directory, pridobitev.frontpage_filename)
    else:
        print(f"Datoteka {pot_html} že obstaja")
    csv_mapa = "obdelani_podatki"
    pot_csv = os.path.join(csv_mapa, pridobitev.csv_filename)
    # 2. in 3.: obdelava html-ja in shranjevanje v csv
    if reparse or not os.path.exists(pot_csv):
        # če zahtevamo ponovno obdelavo ali pa csv_datoteka
        # še ne obstaja, jo ustvarimo (ponovno)
        vsi_slovarji = obdelava.ads_from_file(pridobitev.frontpage_filename, pridobitev.directory)
        shranjevanje.write_pokemon_to_csv(vsi_slovarji, "obdelani_podatki", pridobitev.csv_filename)
    else:
        print(f"Datoteka {pot_csv} že obstaja")
