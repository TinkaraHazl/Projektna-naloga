import os
import csv

def napisi_csv(fieldnames, rows, directory, filename):
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8', newline='') as csv_file:
        pisatelj = csv.DictWriter(csv_file, fieldnames=fieldnames)
        pisatelj.writeheader()
        for row in rows:
            pisatelj.writerow(row)
    return


def pokemoni_v_csv(slovarji, directory, filename):
    assert slovarji and (all(slovar.keys() == slovarji[0].keys() for slovar in slovarji))
    imena_stolpcev = slovarji[0]
    napisi_csv(imena_stolpcev, slovarji, directory, filename)