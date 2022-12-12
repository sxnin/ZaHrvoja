from Pitanja import Pitanja


pitanje_prompt = [
    "Koje su boje jabuke?\n(a) Crvene/Zelene\n(b) Ljubicaste\n(c) Narancaste\n\n",
    "Koje su boje banane?\n(a) plavoZelene\n(b) RozoKricave\n(c) Zute\n\n",
    "Koje su boje jagode?\n(a) Zute\n(b) Crvene\n(c) Plave\n\n"
]

upiti = [
    Pitanja(pitanje_prompt[0], "a"),
    Pitanja(pitanje_prompt[1], "c"),
    Pitanja(pitanje_prompt[2], "b"),
]

def pokreni_test(Unos_Upita):
    score = 0
    for pitanje in upiti:
        odgovor = input(pitanje.pitanje)
        if odgovor == pitanje.odgovor:
            score += 1
    print("Imate " + str(score) + "/" + str(len(upiti)) + " točnih odgovora!")

pokreni_test(upiti)



