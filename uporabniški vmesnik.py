import model_less
import tkinter as tk

VELIKOST_POLJA = 12
ODMIK = 5
ZACETNAPOLJABELI = {(1, 1), (1, 2), (2, 1), (2, 2)}
ZACETNAPOLJACRNI = {(5, 5), (5, 6), (6, 5), (6, 6)}

class Vmesnik:

    def __init__(self, okno):
        self.igra = model_less.Plosca()

        self.obvestilo = tk.Label(okno, text='Pozdravljen v igri Less!')
        self.obvestilo.grid(row=0, column=0)

        self.slednik_igralev = tk.Label(okno, text='Na potezi je igralec: ' + str(model_less.plosca.igralec) +'!')
        self.slednik_igralev.grid(row=1, column=0)

        self.stevec_potez = tk.Label(okno, text='Preostalo število potez:' + str(model_less.plosca.poteze))
        self.stevec_potez.grid(row=1, column=1)

        prikaz_plosce = tk.Frame(okno)
        self.gumbi = []
        for vrstica in range(self.igra.visina):
            vrstica_gumbov = []
            for stolpec in range(self.igra.sirina):
                def pritisni_gumb(vrstica=vrstica, stolpec=stolpec):
                    self.premakni(vrstica, stolpec)
                gumb = tk.Button(prikaz_plosce, text='', height=1, width=1, command=pritisni_gumb, state='disabled')
                gumb.grid(row=vrstica, column=stolpec)
                vrstica_gumbov.append(gumb)
            self.gumbi.append(vrstica_gumbov)
        prikaz_plosce.grid(row=2, column=0, columnspan=2)
        for vrstica, stolpec in self.igra.belefigure:
            self.gumbi[stolpec][vrstica].config(text='0', state='active')
        for vrstica, stolpec in self.igra.crnefigure:
            self.gumbi[stolpec][vrstica].config(text='X', state='active')
        self.osvezi_polje_po_potezi()

    def osvezi_polje_po_potezi(self):
        for vrstica in range(self.igra.visina):
            for stolpec in range(self.igra.sirina):
                if self.igra.igralec == 'O':
                    if (vrstica, stolpec) in self.igra.belefigure:
                        self.gumbi[stolpec][vrstica].config(text='0', state='active')
                    else:
                        self.gumbi[stolpec][vrstica].config(state='disabled')
                else:
                    if (vrstica, stolpec) in self.igra.crnefigure:
                        self.gumbi[stolpec][vrstica].config(text='X', state='active')
                    else:
                        self.gumbi[stolpec][vrstica].config(state='disabled')

    def osvezi_polje_po_izbiri_figure(self):
        for vrstica in range(self.igra.visina):
            for stolpec in range(self.igra.sirina):
                if (vrstica, stolpec) not in self.igra.belefigure and (vrstica, stolpec) not in self.igra.crnefigure:
                    self.gumbi[stolpec][vrstica].config(state='active')
                else:
                    self.gumbi[stolpec][vrstica].config(state='disabled')




    def premakni(self, vrstica, stolpec):
        if self.igra.izbrana_figura:
            x, y = self.igra.izbrana_figura
            self.igra.prestavi_figuro(vrstica, stolpec)
            self.gumbi[y][x].config(text=' ')
            self.gumbi[vrstica][stolpec].config(text=str(self.igra.igralec))
            self.stevec_potez.config(text=str(self.igra.poteze))
            self.osvezi_polje()
        else:
            self.igra.izberi_figuro(vrstica, stolpec)
            self.osvezi_polje_po_izbiri_figure()

okno = tk.Tk()
pravi = Vmesnik(okno)
okno.mainloop()
