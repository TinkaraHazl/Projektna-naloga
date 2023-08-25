import requests
import traceback
import os

frontpage_url = 'https://www.serebii.net/pokemon/nationalpokedex.shtml'
directory = 'podatki'
frontpage_filename = 'glavna.html'
csv_filename = 'pokemoni.csv'

def download_url_to_string(url):
    """Funkcija kot argument sprejme niz in poskusi vrniti vsebino te spletne
    strani kot niz. V primeru, da med izvajanje pride do napake vrne None.
    """
    try:
        # del kode, ki morda sproži napako
        page_content = requests.get(url)
        if page_content.status_code == 200:
            return page_content.text
        else:
            raise ValueError(f"Čudna koda: {page_content.status_code}")
    except Exception:
        # koda, ki se izvede pri napaki
        # dovolj je če izpišemo opozorilo in prekinemo izvajanje funkcije
        print(f"Prišlo je do spodnje napake:\n{traceback.format_exc()}")

def save_string_to_file(text, directory, filename):
    """Funkcija zapiše vrednost parametra "text" v novo ustvarjeno datoteko
    locirano v "directory"/"filename", ali povozi obstoječo. V primeru, da je
    niz "directory" prazen datoteko ustvari v trenutni mapi.
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None


def save_frontpage(page, directory, filename):
    """Funkcija shrani vsebino spletne strani na naslovu "page" v datoteko
    "directory"/"filename"."""
    html_strani = download_url_to_string(page)
    save_string_to_file(html_strani, directory, filename)