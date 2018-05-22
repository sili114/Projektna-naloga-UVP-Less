BELA, CRNA = 'bela', 'crna'

class Figura:

    def __init__(self, x, y, barva):
        self.x = x
        self.y = y
        self.stevec = 0
        self.barva = barva

    def prestavi_figuro(self, x, y):
        if je_veljavna_poteza(self, x, y):
            self.x = x
            self.y = y
            self.stevec += 1
            if self.stevec % 3 == 0:



    def je_veljavna_poteza(self, x, y):
        if 0 <= x < 7 and 0 <= y < 7:
            
