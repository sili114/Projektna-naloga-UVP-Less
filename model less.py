class Plosca():

    def __init__(self, visina=6, sirina=6):
        self.visina = visina
        self.sirina = sirina
        self.poteze = 0
        self.plosca = [[' '] * self.visina for _ in range(self.sirina)]
        self.belefigure = [(1,1), (1,2), (2,1), (2,2)]
        self.crnefigure = [(5,5), (5,6), (6,5), (6,6)]

    def __repr__(self):
        return 'Plosca(visina={}, sirina={}, belefigure={}, crnefigure={})'.format(
            self.visina, self.sirina, self.belefigure, self.crnefigure
        )

    def __str__(self):
        polja = []
        for _ in range(self.visina):
            polja.append(self.sirina * [' '])
        for vrstica, stolpec in self.belefigure:
            polja[vrstica - 1][stolpec - 1] = 'O'
        for vrstica, stolpec in self.crnefigure:
            polja[vrstica - 1][stolpec - 1] = 'X'

        niz = ''
        rob = '+' + self.sirina * '-' + '+\n'
        for vrstica in polja:
            niz += '|' + ''.join(vrstica) + '|\n'
        return rob + niz + rob

    def je_prosto(self, x, y):
        return self.plosca[x][y] == ' '




    def prestavi_figuro(self, x, y):
        if 0 < x <= 6 and 0 < y <= 6 and je_prosto(x, y):
            if (abs(self.x - x) == 1 and y == self.y) or (abs(self.y - y) == 1 and self.x == x):
                self.x , self.y = x, y
                return True
            elif (abs(self.x - x) == 2 and y == self.y) and not je_prosto(x + 1, y):
                self.x, self.y = x, y
                return True
            elif (abs(self.y - y) == 2 and self.x == x) and not je_prosto(x, y + 1):
                self.x, self.y = x, y
                return True
            else:
                return False
        else:
            return False

plosca = Plosca()



print(plosca)
print(plosca.je_prosto(,))





BELA, CRNA = 'bela', 'crna'

class Figura:

    def __init__(self, x, y, barva):
        self.x = x
        self.y = y
        self.barva = barva

    def __str__(self):
        return '{0} figura na polju ({1}, {2})'.format(self.barva, self.x, self.y)
