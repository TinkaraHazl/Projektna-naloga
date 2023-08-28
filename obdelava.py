import re
import os
import pridobitev

def datoteka_v_niz(directory, filename):
    """Funkcija vrne celotno vsebino datoteke "directory"/"filename" kot niz."""
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def stran_v_bloke(vsebina):
   """Funkcija poišče posamezne oglase, ki se nahajajo v spletni strani in
   vrne seznam oglasov."""
   #bloki = []
   vzorec = re.compile(r'<tr>\n\s*<td align="center" class="fooinfo">\n' r'.+?' r'\n\s*</tr>', 
       flags=re.DOTALL,
       )
   #for najdba in vzorec.finditer(vsebina):
   #    print(najdba)
   #    bloki.append(vsebina[najdba.start() : najdba.end()])
   #return bloki
   return re.findall(vzorec, vsebina)

vsebina = datoteka_v_niz(pridobitev.directory, pridobitev.frontpage_filename)
bloki = stran_v_bloke(vsebina)

def slovar_iz_bloka(blok):
    """Funkcija iz niza za posamezen oglasni blok izlušči podatke o imenu, ceni
    in opisu ter vrne slovar, ki vsebuje ustrezne podatke."""
    vzorec_st = r'<td align="center" class="fooinfo">\n\s*#(\d{4})\n\s*</td>'
    vzorec_pokemon = r'<a href="/pokemon/\w+?.*?">(.+?)</a>\n\s*</td>'
    vzorec_ability = r'<a href="/abilitydex/.+?.shtml">(.+?)\s?</a>'
    vzorec_type = r'<a href="/pokemon/type/(\w+?)"><img src="/pokedex-bw/type/.+?.gif" border="0" /></a>'
    vzorec_HP = r'<td align="center" class="fooinfo">(\d{1,3})</td>'
    vzorec_attack = r'<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">(\d{1,3})</td>'
    vzorec_defense = r'<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">(\d{1,3})</td>'
    vzorec_sp_attack = r'<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">(\d{1,3})</td>'
    vzorec_sp_defence = r'<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">\d{1,3}</td>\n\s*<td align="center" class="fooinfo">(\d{1,3})</td>'
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
        sp_defence = re.search(vzorec_sp_defence, blok).group(1)
        speed = re.search(vzorec_speed, blok).group(1)
    except AttributeError:
        print(f"Nepopolni vzorci pri (čudnem?) vzorcu\n{blok}")
        raise
    return {"id": int(stevilo), "pokemon": pokemon, "type": type, "ability": ability, 'HP': int(HP), 'attack': int(attack), 
            'defense': int(defense), 'special attack': int(sp_attack), 'special defence': int(sp_defence), 'speed' : int(speed)}

def izloci_type(niz):
    vzorec_type = r'<a href="/pokemon/type/(\w+?)"><img src="/pokedex-bw/type/\w+?.gif" border="0" /></a>'
    types = []
    for type in vzorec_type.finditer(niz):
            types.append(
                {
                    "id": int(type.groupdict()["id"]),
                    "type": type.groupdict()["type"],
                }
            )
    return types

def izloci_ability(niz):
    vzorec_ability = re.compile(r'<a href="/abilitydex/.+?.shtml">(.+?)\s?</a>')
    abilities = list(set(re.findall(vzorec_ability, niz)))
    slovarji_abilities = []
    for i, a in enumerate(abilities):
        slovar = {'id' : i, 'ability' : a}
        slovarji_abilities.append(slovar)
    return slovarji_abilities


def seznam_slovarjev(filename, directory):
    """Funkcija prebere podatke v datoteki "directory"/"filename" in jih
    pretvori (razčleni) v pripadajoč seznam slovarjev za vsak oglas posebej."""
    vsebina = datoteka_v_niz(directory, filename)
    bloki = stran_v_bloke(vsebina)
    slovarji = []
    for blok in bloki:
        slovarji.append(slovar_iz_bloka(blok))
    return slovarji

#print(seznam_slovarjev(pridobitev.frontpage_filename, pridobitev.directory))
#print(izloci_ability(vsebina))