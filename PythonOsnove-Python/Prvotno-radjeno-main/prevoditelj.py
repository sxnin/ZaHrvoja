# Ova funkcija svaki samoglasnik mijenja u slovo G
def prevoditelj(pojam):
    prevod = ""
    for slovo in pojam:
        if slovo.lower() in "aeiou":
            if slovo.isupper():
                prevod = prevod + "G"
            else:
                prevod = prevod + "g"
        else:
            prevod = prevod + slovo
    return prevod

print(prevoditelj(input("Unesite riječ: ")))


