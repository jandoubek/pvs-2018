[//]: <> FORMAT: 1A
[//]: <> HOST: http://coffea.cz/

# Coffea

## Aplikační rozhraní Python serveru [/api]

### Doporučení vhodné kávy [GET]

Vrátí doporučený typ kávy a kavárnu, které by se mohli líbit uživateli na základě jeho preferencí.

+ Response 200 (application/json)
```json
    {
        "cafe":
        {
            "id": 1,
            "name": "Kavárna na rohu",
            "rating": 2.5,
            "position":
            {
                "latitude": 10.123,
                "longitude": 30.848
            }
            
        },
        "coffee": 
        {
            "id":" 5,
            "name": "Bomba Cappuccino",
            "rating": 4.8
        }
    }
```
    
### Doporučerní vhodné kavárny [GET]

Vrátí vhodnou kavárnu, která by se mohla líbit uživateli na základě jeho preferencí.

+ Response 200 (application/json)
```json
    {
        "cafe":
        {
            "id": 1,
            "name": "Kavárna na rohu",
            "rating": 2.5,
            "position":
            {
                "latitude": 10.123,
                "longitude": 30.848
            }
            
        }
    }
```
    
### Objevení nové kávy [GET]

Vrátí nový typ kávy a kavárnu, které by mohli být pro uživatele zajímavé a současne je ješte nezkusil.

+ Response 200 (application/json)
```json
    {
        "cafe":
        {
            "id": 1,
            "name": "Kavárna na rohu",
            "rating": 2.5,
            "position":
            {
                "latitude": 10.123,
                "longitude": 30.848
            }
            
        },
        "coffee": 
        {
            "id":" 5,
            "name": "Bomba Cappuccino",
            "rating": 4.8
        }
    }
```
    
### Objevení nové kavárny [GET]

Vrátí novou kavárnu, která by se mohla líbit uživateli a ve které ješte nebyl na základě jeho preferencí.

+ Response 200 (application/json)
```json
    {
        "cafe":
        {
            "id": 1,
            "name": "Kavárna na rohu",
            "rating": 2.5,
            "position":
            {
                "latitude": 10.123,
                "longitude": 30.848
            }
            
        }
    }
```
    
### Získání hodnocení vybrané kávy [GET]

Zjistí aktuální hodnocení kávy z matematického modelu.

+ Request (application/json)
```json
    {
        "id": 5
    }
```
    
+ Response 200 (application/json)
```json
    {
        "nazev": "Vánoční Cappuccino",
        "rating": 4.4
    }
```

### Přidání nového hodnocení kávy [POST]

Záznam nového hodnocení kávy od uživatele, které je vloženo do matematického modelu.

+ Request (application/json)
```json
    {
        "rating": [
            {
                "criteria": "serving",
                "value": 4
            },
            {
                "criteria": "environment", 
                "value": 5
            },
            {
                "criteria": "color",
                "value": 3
            },
            {   
                "criteria": "appearance",
                "value": 4
            },
            {  
                "criteria": "aroma",
                "value": 5 
            },
            {
                "criteria": "taste",
                "value": 2
            },
        ]
    }
```
