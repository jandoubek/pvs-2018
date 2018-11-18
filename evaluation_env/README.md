# Evaluation env

Pro vyvoj, spousteni a udrzbu evaluation env je dobre mit specialni virtualni python prostredi.

Minimalisticky pristup k takovemu prostredi je nasledujici.

Jmeno prostredi je na vas. Doporucuji stejne jako jmeno python projektu - tzn. evaluation_env.

NOTE: Virtual env vam do adresarove struktury vytvori parallelni instalaci zavislych knihoven. Prosim necommitujte toto do gitu.

## Virtual environment

### create virtual env

 `virtualenv <name-of-env>`

### start virtual env

 `source <name-of-env>/bin/activate`

### install expected packages

 `pip install -r <requirements.txt file>`

### deactivate virtual env

 `deactivate`