import re
import os


def read_file_to_string(directory, filename):
    """Funkcija vrne celotno vsebino datoteke "directory"/"filename" kot niz."""
    path = os.path.join(directory, filename)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def page_to_ads(page_content):
    """Funkcija poišče posamezne oglase, ki se nahajajo v spletni strani in
    vrne seznam oglasov."""
    vzorec = r'<tr><td align = "center" class = "fooinfo" >.+?</tr >'
    return re.findall(vzorec, page_content, flags=re.DOTALL)


def get_dict_from_ad_block(block):
    """Funkcija iz niza za posamezen oglasni blok izlušči podatke o imenu, ceni
    in opisu ter vrne slovar, ki vsebuje ustrezne podatke."""
    vzorec_st = r'< td align = "center" class = "fooinfo" >  # (\d{4}) </td>'
    vzorec_pokemon = r'< td align = "center" class = "fooinfo" > <a href = "/pokemon/\w+?" >(\w+?\s?\w+?)</a ></td >'
    vzorec_ability = r'<a href = "/abilitydex/\w+?\s?\w+?.shtml" > (\w+?\s?\w+?) < /a >'
    vzorec_type = r'<a href = "/pokemon/type/(\w+?)" > <img src = "/pokedex-bw/type/\w+?.gif" border = "0" / > < /a >'
    vzorec_HP = r'<td align = "center" class = "fooinfo" > (\d{2,3}) </td>'
    vzorec_attack = r'<td align = "center" class = "fooinfo" > \d{2,3} </td> < td align = "center" class = "fooinfo" > (\d{2, 3}) < /td >'
    vzorec_defense = r'<td align = "center" class = "fooinfo" > \d{2,3} </td> <td align = "center" class = "fooinfo" > \d{2,3} </td> <td align = "center" class = "fooinfo" > (\d{2,3}) </td>'
    vzorec_sp_attack = r'<td align = "center" class = "fooinfo" > \d{2,3} </td><td align = "center" class = "fooinfo" > \d{2,3} </td><td align = "center" class = "fooinfo" > \d{2,3} </td><td align = "center" class = "fooinfo" > (\d{2,3}) </td>'
    vzorec_sp_defence = r'<td align = "center" class = "fooinfo" > \d{2,3} </td> <td align = "center" class = "fooinfo" > \d{2,3} </td> <td align = "center" class = "fooinfo" > \d{2,3} </td> <td align = "center" class = "fooinfo" > \d{2,3} </td> <td align = "center" class = "fooinfo" > (\d{2,3}) </td>'
    vzorec_speed = r'<td align = "center" class = "fooinfo" > \d{2,3} </td> <td align = "center" class = "fooinfo" > \d{2,3} </td> <td align = "center" class = "fooinfo" > \d{2,3} </td> <td align = "center" class = "fooinfo" > \d{2,3} </td> <td align = "center" class = "fooinfo" > \d{2,3} </td> <td align = "center" class = "fooinfo" > (\d{2,3}) </td>'
    try:
        stevilo = re.search(vzorec_st, block).group(1)
        pokemon = re.search(vzorec_pokemon, block).group(1)
        type = re.findall(vzorec_type, block)
        ability = re.findall(vzorec_ability, block)
        HP =  re.search(vzorec_HP, block).group(1)
        attack = re.search(vzorec_attack, block).group(1)
        defense = re.search(vzorec_defense, block).group(1)
        sp_attack = re.search(vzorec_sp_attack, block).group(1)
        sp_defence = re.search(vzorec_sp_defence, block).group(1)
        speed = re.search(vzorec_speed, block).group(1)
    except AttributeError:
        print(f"Nepopolni vzorci pri (čudnem?) oglasu\n{block}")
        raise
    return {"stevilo": stevilo, "pokemon": pokemon, "type": type, "ability": ability, 'HP': HP, 'attack': attack, 
            'defense': defense, 'special attack': sp_attack, 'special defence': sp_defence, 'speed' : speed}


def ads_from_file(filename, directory):
    """Funkcija prebere podatke v datoteki "directory"/"filename" in jih
    pretvori (razčleni) v pripadajoč seznam slovarjev za vsak oglas posebej."""
    vsebina = read_file_to_string(directory, filename)
    oglasi = page_to_ads(vsebina)
    slovarji = []
    for oglas in oglasi:
        slovarji.append(get_dict_from_ad_block(oglas))
    return slovarji

