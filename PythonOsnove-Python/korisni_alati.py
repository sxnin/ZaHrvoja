import random

stope_u_milje = 5280
metri_u_kilometre = 1000
betlsi = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]

def dohvati_fajl_izvana(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)

