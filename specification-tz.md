# Coffeemates

## Vize

Applikace na základě hodnocení ze zážitku z požití kávy doporučí nebo nedoporučí 
další kavárny nebo nápojové automaty. (Ne)doporučení bude určeno doplněním hodnocení
od ostatních uživatelů. 

Pro vylepšení získané informace může systém zvát uživatele na kávu.
Buď formou hry nebo lze dojednat spolupracovat s kavárnou. 
Může být vybrána nehodnocená kavárna nebo může být vybrán uživatel, 
u něhož je potřeba upřesnit jeho chuť. 

Z počátku bude v systému málo informací. Hodnocení od uživatelů lze doplnit 
o druh kávy a kávovaru v kavárně, alespoň do doby než bude existovat dostatek hodnocení. 

## Features

* ještě nevím

## Technologie

Hodnocení bych řadil do nějakých vektorů a na to použil třeba vzájemnou entropii. 
Jako třeba sloupec matice je uživatel a řádky jsou kavárny, hodnota je -1 (nechutnalo), 
0 (nehodnoceno), +1 (chutnalo). 
Problém je, že celý vektor by byli samé nuly, takže to chce něco jako Jaccardův index apod. 

Měly bychom navrhnout dva modely, jeden čistě uživatelský a jeden vůči kávě. 
Uživatelský by postupně převzal kontrolu, až bude dost údajů. 

## Checkpoint

Taky zatím nevím. 