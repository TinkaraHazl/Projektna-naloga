# Projektna naloga

Za svojo projektno nalogo sem izbrala analizo pokemonov, bitij iz franšize iger Pokemon. Podatke sem pridobila iz spletne strani Serebii.

## Pridobivanje podatkov
V datotekah pridobitev.py, obravnavanje.py, shranjevanje. py in skupno.py se nahaja koda za pridobivanje podatkov iz shranjevanje v csv datoteke, ki sem jih shranila v mapo csv_datoteke.
Pridobila sem naslednje podatke, ki so podrobno razloženi v datoteki analiza.py:
-  ID pokemona
-  ime pokemona
-  tip (type) pokemona
-  zmožnosti (abilities) pokemona
-  HP
-  attack
-  special attack
-  defense
-  special defense
-  speed

Tip in zmožnosti pokemona sta kategorijski lastnosti, ostale so numerične.
podatke sem shranila v tri datoteke: pokemoni.csv, kjer se nahajajo id, ime in numerične lastnosti pokemona. V types.csv sem shranila zvezo med pokemoni in njihovimi tipi, v abilities.csv pa povezavo med pokemoni in njihovimi zmožnostimi.
## Analiza podatkov
V analiza.py sem pokemone analizirala in ugotovila:
-  kateri pokemoni so najmočnejši
-  katere zmožnosti so najpogostejše
-  pogostost tipov pokemonov po različnih regijah
-  idealno ekipo pokemonov glede na regijo, v kateri se igra dogaja

