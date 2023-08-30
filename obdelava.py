import re
import os

def datoteka_v_niz(directory, filename):
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
    
def stran_v_bloke(vsebina):
   vzorec = re.compile(r'<tr>\n\s*<td align="center" class="fooinfo">\n' r'.+?' r'\n\s*</tr>', 
       flags=re.DOTALL,)
   return re.findall(vzorec, vsebina)

def slovar_iz_bloka(blok):
    vzorec_st = r'<td align="center" class="fooinfo">\n\s*#(\d{4})\n\s*</td>'
    vzorec_pokemon = r'<a href="/pokemon/\w+?.*?">(.+?)</a>\n\s*</td>'
    vzorec_ability = r'<a href="/abilitydex/.+?.shtml">(.+?)\s?</a>'
    vzorec_type = r'<a href="/pokemon/type/(\w+?)"><img src="/pokedex-bw/type/.+?.gif" border="0" /></a>'
    vzorec_HP = r'<td align="center" class="fooinfo">(\d{1,3})</td>'
    vzorec_attack = r'<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">(\d{1,3})</td>'
    vzorec_defense = r'<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">(\d{1,3})</td>'
    vzorec_sp_attack = r'<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">(\d{1,3})</td>'
    vzorec_sp_defense = r'<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">(\d{1,3})</td>'
    vzorec_speed = r'<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">(\d{1,3})</td>'
    try:
        stevilo = re.search(vzorec_st, blok).group(1)
        pokemon = re.search(vzorec_pokemon, blok).group(1)
        type = re.findall(vzorec_type, blok)
        ability = re.findall(vzorec_ability, blok)
        HP =  re.search(vzorec_HP, blok).group(1)
        attack = re.search(vzorec_attack, blok).group(1)
        defense = re.search(vzorec_defense, blok).group(1)
        sp_attack = re.search(vzorec_sp_attack, blok).group(1)
        sp_defense = re.search(vzorec_sp_defense, blok).group(1)
        speed = re.search(vzorec_speed, blok).group(1)
    except AttributeError:
        print(f"Nepopolni vzorci pri (čudnem?) vzorcu\n{blok}")
        raise
    return {"id": int(stevilo), "pokemon": pokemon, 'type': type, 'ability': ability, 'HP': int(HP), 'attack': int(attack), 
            'defense': int(defense), 'special attack': int(sp_attack), 'special defense': int(sp_defense), 'speed' : int(speed)}

def slovarji_glavno(filename, directory):
    vsebina = datoteka_v_niz(directory, filename)
    bloki = stran_v_bloke(vsebina)
    slovarji = []
    for blok in bloki:
        slovarji.append(slovar_iz_bloka(blok))
    return slovarji
