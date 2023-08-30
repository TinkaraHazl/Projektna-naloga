import pridobitev
import shranjevanje
import obdelava
import os

pridobitev.shrani_frontpage(pridobitev.url, pridobitev.directory, pridobitev.frontpage_filename)

pokemoni = obdelava.slovarji_glavno(pridobitev.frontpage_filename, pridobitev.directory)

if not os.path.exists('csv_datoteke'):
    os.makedirs('csv_datoteke')

shranjevanje.pokemoni_v_csv(pokemoni, os.path.join('csv_datoteke', 'pokemoni.csv'))
shranjevanje.abilities_v_csv(pokemoni, os.path.join('csv_datoteke', 'abilities.csv'))
shranjevanje.types_v_csv(pokemoni, os.path.join('csv_datoteke', 'types.csv'))