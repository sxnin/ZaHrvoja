# kako uhvatiti/pronaći određenu grešku kad se pojavi

try:
    vrijednost = 10 / 1
    broj = int(input("Unesite broj: "))
    print(broj)
except ZeroDivisionError:
    print("Dijeljenje sa NUlom nije dozvoljeno!")
except ValueError:
    print("Pogrešan unos!")


