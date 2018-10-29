# Coffea (Kávovník)

## Vízia

Tvorba personalizovaného profilu preferncie káv a kávovín. Na základe užívateľského profilu budú odporúčané optimálne kaviarne v blízkosti užívateľa alebo kaviarne s atratktívnymi kávami, ktoré by mu mohli chutiť.

## Features

- hodnotenie práve vypitej kávy a kaviarne
- vyhľadanie kaviarní v mojom okolí
- odporúčanie atraktívnych druhov káv, resp. kavairní
- zobranie môjho "kávového profilu" a zdieľanie medzi užívateľmi, resp. porovnávanie

## Technológia

Využitie webovej technológie PhoneGap, Ionic alebo NativeScript na tvorbu aplikácie pre všetky platformy súčasne - web, Android, iOS. Aplikácia bude komunikovať s back-end serverom pomocou REST API a bude sa automaticky synchronizovať na pozadí. Aplikácia tiež bude podporovať offline mód vhodý pre kaviarne, kde nie je dostupný internet. Dáta budu uložené v MySQL databáze a pomocou grafových algoritmov budú generované odporúčania pre užívateľov.

## Checkpoint

1. Extrahovanie zoznamu kaviarní, nimi ponúkaných káv a ich recenzí z webov do privátnej DB
2. Využitie mapových podkladov na zobrazenie kaviarní a pridružených informácií
3. Rozhranie na hodnotenie káv a kaviarní a ich evidenciu
4. Užívateľské účty - prihlasovanie, osobné údaje, kávový profil užívateľa
5. Rozhranie pre vyhľadávanie/odporúčanie kaviarní
