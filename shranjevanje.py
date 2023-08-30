import csv

def pokemoni_v_csv(slovarji, filename):
    with open(filename, 'w') as f:
        pisatelj = csv.writer(f)
        pisatelj.writerow(['id', 'pokemon', 'type', 'ability', 'HP',
                           'attack', 'defense', 'special attack', 'special defence', 'speed'])
        for slovar in slovarji:
            pisatelj.writerow([slovar['id'], slovar['pokemon'], slovar['HP'],
                               slovar['attack'], slovar['defense'], slovar['special attack'],
                               slovar['special defence'], slovar['speed']])

def abilities_v_csv(slovarji, filename):
    with open(filename, 'w') as f:
        pisatelj = csv.writer(f)
        pisatelj.writerow(["pokemon", "ability"])
        for slovar in slovarji:
            for ability in slovar["ability"]:
                pisatelj.writerow([slovar["pokemon"], ability])

def types_v_csv(slovarji, filename):
    with open(filename, 'w') as f:
        pisatelj = csv.writer(f)
        pisatelj.writerow(["pokemon", "type"])
        for slovar in slovarji:
            for ability in slovar["type"]:
                pisatelj.writerow([slovar["pokemon"], ability])
