import pridobitev
import shranjevanje
import obdelava
import os

def main(redownload=True, reparse=True):
    pot_html = os.path.join(pridobitev.directory, pridobitev.frontpage_filename)
    if redownload or not os.path.exists(pot_html):
        pridobitev.shrani_frontpage(pridobitev.url, pridobitev.directory, pridobitev.frontpage_filename)
    else:
        print(f"Datoteka {pot_html} že obstaja")
    
    csv_mapa = "obdelani_podatki"
    seznami_slovarjev = [obdelava.slovarji_glavno(pridobitev.frontpage_filename, pridobitev.directory),
                obdelava.slovarji_type(pridobitev.frontpage_filename, pridobitev.directory), 
                obdelava.slovarji_ability(pridobitev.frontpage_filename, pridobitev.directory)]
    for i, csv_file in enumerate(pridobitev.csv_files):
        pot = os.path.join(csv_mapa, csv_file)
        if reparse or not os.path.exists(pot):
            shranjevanje.pokemoni_v_csv(seznami_slovarjev[i], "obdelani_podatki", csv_file)
        else:
            print(f"Datoteka {pot} že obstaja")
            
main()