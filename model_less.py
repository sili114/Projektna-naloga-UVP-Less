BELI, CRNI = '0', 'X'

ZACETNAPOLJABELI = {(0, 0), (1, 0), (0, 1), (1, 1)}
ZACETNAPOLJACRNI = {(5, 5), (5, 4), (4, 5), (4, 4)}

import random

class Plosca:

    def __init__(self, visina=6, sirina=6):
        self.visina = visina
        self.sirina = sirina
        self.poteze = 3
        self.plosca = [[' '] * self.visina for _ in range(self.sirina)]
        self.igralec = BELI
        self.izbrana_figura = None
        self.skok = 1
        self.belefigure = []
        self.crnefigure = []
        self.ovire = []
        self.zmagovalec = None
        self.testni = False
        for vrstica, stolpec in ZACETNAPOLJABELI:
            self.plosca[stolpec][vrstica] = BELI
            self.belefigure.append((vrstica, stolpec))
        for vrstica, stolpec in ZACETNAPOLJACRNI:
            self.plosca[stolpec][vrstica] = CRNI
            self.crnefigure.append((vrstica, stolpec))
        while len(self.ovire) < 6:
            c = random.randint(0, 5)
            d = random.randint(0, 5)
            if (c, d) not in self.ovire:
                self.ovire.append((c, d))



    def __repr__(self):
        return 'Plosca(visina={}, sirina={}, belefigure={}, crnefigure={}, ovire={})'.format(
            self.visina, self.sirina, self.belefigure, self.crnefigure, self.ovire
        )

    def __str__(self):

        niz = ''
        rob = '+' + self.sirina * '-' + '+\n'
        for i ,vrstica in enumerate(self.plosca, 1):
            niz += '|' + ''.join(vrstica) + '|' + str(i) + '\n'
        return rob + niz + rob + ' 123456'

    def je_prosto(self, x, y):
        return self.plosca[y][x] == ' '

    def izberi_figuro(self, x, y):
        if self.izbrana_figura is None and self.igralec == self.plosca[y][x]:
            self.izbrana_figura = (x, y)

    def menjava_igralca(self):
        if self.poteze <= 0:
            self.poteze = 3
            if self.igralec == CRNI:
                self.igralec = BELI
            else:
                self.igralec = CRNI

    def figura_se_lahko_prestavi(self, x1, y1, x, y):
        if abs(x1 - x) == 1 and y == y1 or abs(y1 - y) == 1 and x == x1:
            if (x, y) in self.ovire:
                if self.poteze - 2 >= 0:
                    self.skok = 2
                    return True
                return False
            return True
        elif abs(x1 - x) == 2 and y == y1 and not self.je_prosto(min(x, x1) + 1, y):
            return not ((x, y) in self.ovire or (min(x, x1) + 1, y) in self.ovire)
        elif abs(y1 - y) == 2 and x1 == x and not self.je_prosto(x, min(y, y1) + 1):
            return not((x, y) in self.ovire or (x, min(y, y1) + 1) in self.ovire)
        else:
            return False


    def polja_na_voljo(self):
        polja = []
        if self.izbrana_figura:
            x, y = self.izbrana_figura
            opcija = [(x, y + 1), (x, y + 2), (x, y - 1), (x, y - 2), (x + 1, y), (x + 2, y), (x - 1, y), (x - 2, y)]
            for x1, y1 in opcija:
                if self.je_v_polju(x1, y1):
                    if self.figura_se_lahko_prestavi(x, y, x1, y1) and self.je_prosto(x1, y1):
                        polja.append((x1, y1))
        self.skok = 1
        return polja




    def je_v_polju(self, x, y):
        return 0 <= x < self.sirina and 0 <= y < self.visina


    def prestavi_figuro(self, x, y):
        if self.izbrana_figura and self.je_v_polju(x, y) and self.je_prosto(x, y):
            x1, y1 = self.izbrana_figura
            if self.figura_se_lahko_prestavi(x1, y1, x, y):
                self.plosca[y1][x1] = ' '
                self.plosca[y][x] = self.igralec
                self.poteze -= self.skok
                self.izbrana_figura = None
                if self.igralec == BELI:
                    self.belefigure.remove((x1, y1))
                    self.belefigure.append((x, y))
                else:
                    self.crnefigure.remove((x1, y1))
                    self.crnefigure.append((x, y))
                self.skok = 1
                self.menjava_igralca()


    def resetiraj_izbiro_figure(self):
        self.izbrana_figura = None


    def resetiraj_igro(self):
        self.__init__()


    def zmaga(self):
        if ZACETNAPOLJACRNI == set(self.belefigure) and ZACETNAPOLJABELI == set(self.crnefigure) and self.poteze == 3:
            return None
        elif ZACETNAPOLJABELI == set(self.crnefigure):
            self.zmagovalec = CRNI
            return True
        elif ZACETNAPOLJACRNI == set(self.belefigure):
            if self.testni and self.poteze == 3 and self.igralec ==BELI:
                self.zmagovalec = BELI
                return True
            elif not self.testni:
                self.testni = True
                self.igralec = CRNI
                if not self.poteze == 3:
                    self.poteze = 3 - self.poteze
                return False
            else:
                return False
        else:
            return False

plosca = Plosca()
