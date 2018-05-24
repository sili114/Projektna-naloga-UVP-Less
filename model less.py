BELA, CRNA = 'bela', 'crna'

class Figura:

    def __init__(self, x, y, barva):
        self.x = x
        self.y = y
        self.stevec = 0
        self.barva = barva

    def __str__(self):
        return '{0} figura na polju ({1}, {2})'.format(self.barva, self.x, self.y)

    def prestavi_figuro(self, x, y):
        if je_veljavna_poteza(self, x, y):
            self.x = x
            self.y = y
            self.stevec += 1
            if self.stevec == 3:
                self.stevec = 0



    def je_veljavna_poteza(self, x, y):
        if 0 <= x < 7 and 0 <= y < 7:
            if polje[x, y] == 0:
                polje[self.x, self.y] = 0
                polje[x, y] = 1
                return True
            else:
                return False

    def je_na_potezi(self):
        return self.barva == BARVA

    
