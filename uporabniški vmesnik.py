import model_less
import tkinter as tk

VELIKOST_POLJA = 12
ODMIK = 5

class Vmesnik:

    def __init__(self, okno):
        self.igra = model_less.Plosca()
        self.okno = okno

        prikaz_plosce = tk.Frame(okno)
        self.gumbi = []
        for vrstica in range(self.plosca.visina):
            vrstica_gumbov = []
            for stolpec in range(self.plosca.sirina):
                def pritisni_gumb(vrstica=vrstica, stolpec=stolpec):
                    self.premakni(vrstica, stolpec)
                gumb = tk.Button(prikaz_plosce, text='', height=1, width=1, command=pritisni_gumb)
                gumb.grid(row=vrstica, column=stolpec)
                vrstica_gumbov.append(gumb)
            self.gumbi.append(vrstica_gumbov)
        prikaz_plosce.grid(row=1, column=0, columnspan=2)

        for gumb in self.gumbi:



    def premakni(self, vrstica, stolpec):
        if self.igra.izbrana_figura:
            x, y = self.igra.izbrana_figura
            self.igra.prestavi_figuro(vrstica, stolpec)
            self.gumbi[y][x].config(text=' ')
            self.gumbi[vrstica][stolpec].config(text=str(self.igra.igralec))
        else:
            self.igra.izberi_figuro(vrstica, stolpec)
            
