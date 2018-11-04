# Coffeemates

nebo Coffeesearch, Coffea, Coffeesense

## Vize

Spojovat milovníky kávy a pomoci jim najít v daném místě a čase tu nejchutnější pro ně.

## Features

* Na novém místě najdi kde mají kafe podle mého gusta.
* Doporuč kde objevit nové kavové zážitky (predikce potenciální oblíbené kavárny 
nebo také doplnění modelu).
* Ukládání uživatelových dat ohledně pití kávy. 
* Možnost "následovat" uživatele se stejným kávovým profilem.
* Možnost sdílení mého kávového profilu na sociální sítě.

## Technologie

* Na prototyp backendu bych použil Python/Flask. Finalní řesení bych udělal v cloudu Azure nebo AWS podle zkušenosti.
* Pro frontend může být využita cross-platform webová technologie Cordova, Ionic alebo NativeScript, která umožní tvorbu aplikace pro všechny platformy současně - web, Android, iOS. 
* Backend a frontend budou spolu komunikovat prostřednictvím REST API.
* Implementované budou dva matematické modely: jeden čistě uživatelský a jeden vůči kávě. Ze začátku by byl použit kávový model. Uživatelský model by postupně převzal kontrolu, až bude sesbírano dost uživatelských recenzií.
* Hodnocení kávy bude mít tři možné výstupy: chutnalo, nechutnalo, nehodnoceno. Algoritmus pro doporučování kávy bude využívat entropii dat a grafové aloritmy.
* Možná integrace s hlavními sociálními sítěmi.

## Checkpoint

1. Sezbírání kaváren
1. Sezbíraní testovacích dat
2. Prototyp pro validaci matematického modelu a testovacích dat
3. Samotný vývoj aplikace - separace backendu a frontendu
4. Validace nastaveni features
5. Release do app storů a do cloudu
