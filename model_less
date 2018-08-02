BELA, CRNA = 'bela', 'crna'

class Figura:

    def __init__(self, x, y, barva):
        self.x = x
        self.y = y
        self.barva = barva

    def __str__(self):
        return '{0} figura na polju ({1}, {2})'.format(self.barva, self.x, self.y)

ZACETNAPOLJABELI = {(1, 1), (1, 2), (2, 1), (2, 2)}
ZACETNAPOLJACRNI = {(5, 5), (5, 6), (6, 5), (6, 6)}

class Plosca:

    def __init__(self, visina=6, sirina=6):
        self.visina = visina
        self.sirina = sirina
        self.poteze = 3
        self.plosca = [[' '] * self.visina for _ in range(self.sirina)]
        self.igralec = 'O'
        for stolpec, vrstica in ZACETNAPOLJABELI:
            self.plosca[vrstica - 1][stolpec - 1] = 'O'
        for vrstica, stolpec in ZACETNAPOLJACRNI:
            self.plosca[vrstica - 1][stolpec - 1] = 'X'


    def __repr__(self):
        return 'Plosca(visina={}, sirina={}, belefigure={}, crnefigure={})'.format(
            self.visina, self.sirina, self.belefigure, self.crnefigure
        )

    def __str__(self):

        niz = ''
        rob = '+' + self.sirina * '-' + '+\n'
        for i ,vrstica in enumerate(self.plosca, 1):
            niz += '|' + ''.join(vrstica) + '|' + str(i) + '\n'
        return rob + niz + rob + ' 123456'

    def je_prosto(self, x, y):
        return self.plosca[x - 1][y - 1] == ' '


    def prestavi_figuro(self, x1, y1, x, y):
        if self.igralec == self.plosca[y1 - 1][x1 - 1]:
            if 0 < x <= 6 and 0 < y <= 6 and self.je_prosto(x, y):
                if (abs(x1 - x) == 1 and y == y1) or (abs(y1 - y) == 1 and x1 == x) or ((abs(x1 - x) == 2 and y == y1) and not self.je_prosto(min(x, x1) + 1, y)) or\
                   ((y1 - y) == 2 and x1 == x) and not self.je_prosto(x, min(y, y1) + 1):
                    self.plosca[y1 - 1][x1 - 1] = ' '
                    self.plosca[y - 1][x - 1] = self.igralec
                    self.poteze -= 1
                    if self.poteze == 0:
                        self.poteze = 3
                        if self.igralec == 'X':
                            self.igralec = 'O'
                        else:
                            self.igralec = 'X'
                else:
                    return 'NEVELJAVNA POTEZA'
            else:
                return 'NEVELJAVNA POTEZA'
        else:
            return 'Na potezi je drugi igralec!'

    def zaseda_polja(self, igralec):
        sez = set()
        for i in range(self.visina):
            for j in range(self.sirina):
                if self.plosca[i][j] == igralec:
                    sez.update((j + 1, i + 1))
        return sez

    def zmaga(self, igralec):
        if igralec == 'O' and ZACETNAPOLJACRNI == self.zaseda_polja(igralec):
            return True
        elif igralec == 'X' and ZACETNAPOLJABELI == self.zaseda_polja(igralec):
            return True
        else:
            return False
