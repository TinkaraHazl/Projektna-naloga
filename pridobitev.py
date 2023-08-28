import requests
import traceback
import os

url = 'https://www.serebii.net/pokemon/nationalpokedex.shtml'
directory = 'podatki'
frontpage_filename = 'glavna.html'
csv_filename = 'pokemoni.csv'

def url_v_niz(url):
    """Funkcija kot argument sprejme niz in poskusi vrniti vsebino te spletne
    strani kot niz. V primeru, da med izvajanje pride do napake vrne None.
    """
    try:
        # del kode, ki morda sproži napako
        vsebina = requests.get(url)
        if vsebina.status_code == 200:
            return vsebina.text
        else:
            raise ValueError(f"Čudna koda: {vsebina.status_code}")
    except Exception:
        # koda, ki se izvede pri napaki
        # dovolj je če izpišemo opozorilo in prekinemo izvajanje funkcije
        print(f"Prišlo je do spodnje napake:\n{traceback.format_exc()}")

def niz_v_datoteko(text, directory, filename):
    """Funkcija zapiše vrednost parametra "text" v novo ustvarjeno datoteko
    locirano v "directory"/"filename", ali povozi obstoječo. V primeru, da je
    niz "directory" prazen datoteko ustvari v trenutni mapi.
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None


def shrani_frontpage(url, directory, filename):
    """Funkcija shrani vsebino spletne strani na naslovu "page" v datoteko
    "directory"/"filename"."""
    html_strani = url_v_niz(url)
    niz_v_datoteko(html_strani, directory, filename)

