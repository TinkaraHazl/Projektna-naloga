import requests
import traceback
import os

url = 'https://www.serebii.net/pokemon/nationalpokedex.shtml'
directory = 'podatki'
frontpage_filename = 'glavna.html'
csv_files = ['pokemoni.csv', 'types.csv', 'abilities.csv']

def url_v_niz(url):
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
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None


def shrani_frontpage(url, directory, filename):
    html_strani = url_v_niz(url)
    niz_v_datoteko(html_strani, directory, filename)

