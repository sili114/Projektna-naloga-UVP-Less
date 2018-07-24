class Plosca:

    def __init__(self, visina=6, sirina=6):
        self.visina = visina
        self.sirina = sirina
        self.poteze = 0
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
            polja[vrstica][stolpec] = 'O'
        for vrstica, stolpec in self.crnefigure:
            polja[vrstica][stolpec] = 'X'

        niz = ''
        rob = '+' + self.sirina * '-' + '+\n'
        for vrstica in polja:
            niz += '|' + ''.join(vrstica) + '|\n'
        return rob + niz + rob

    def prestavi_figuro(self, x, y):
        if (x, y) & self.zasedena_polja


    def zasedena_polja(self):
        zasedena = set()
        for figura in self.belefigure:
            zasedena.update(figura.zasedena_polja())
        for figura in self.crnefigure:
            zasedena.update(figura.zasedena_polja())
        return zasedena





BELA, CRNA = 'bela', 'crna'

class Figura:

    def __init__(self, x, y, barva):
        self.x = x
        self.y = y
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
