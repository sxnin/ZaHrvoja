class Student:

    def __init__(self, ime, razred, prosjek, probni_rad):
        self.ime = ime
        self.razred = razred
        self.prosjek = prosjek
        self.probni_rad = probni_rad

    def on_honor_roll(self):
        if self.prosjek >= 3.5:
            return True
        else:
            return False




