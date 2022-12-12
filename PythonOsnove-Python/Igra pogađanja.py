
tajnarijec = "žirafa"
pogodi = ""
pogodi_pokušaja = 0
pogodi_ograničenje = 3
prekoračili_broj_pokušaja = False


while pogodi != tajnarijec and not(prekoračili_broj_pokušaja):
    if pogodi_pokušaja < pogodi_ograničenje:
        pogodi = input("Unesite riječ: ")
        pogodi_pokušaja += 1
    else:
        prekoračili_broj_pokušaja = True


if prekoračili_broj_pokušaja:
    print("Prekoračili ste broj pokušaja, IZGUBILI STE! ")
else:
    print("Bravo, pogodili ste riječ!")



