import model_less
import tkinter as tk

ZACETNAPOLJABELI = {(1, 1), (1, 2), (2, 1), (2, 2)}
ZACETNAPOLJACRNI = {(5, 5), (5, 6), (6, 5), (6, 6)}

class Vmesnik:

    def __init__(self, okno):
        self.igra = model_less.Plosca()

        self.obvestilo = tk.Label(okno, text='Pozdravljen v igri Less')
        self.obvestilo.grid(row=0, column=0)


        self.slednik_igralev = tk.Label(okno,text= str(model_less.plosca.igralec))
        self.slednik_igralev.grid(row=1, column=1)

        tk.Label(okno, text='Na potezi je igralec:').grid(row=1, column=0)
        tk.Label(okno, text='Preostalo število potez:').grid(row=1, column=2)

        self.stevec_potez = tk.Label(okno, text=str(model_less.plosca.poteze))
        self.stevec_potez.grid(row=1, column=3)

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
        for vrstica, stolpec in self.igra.ovire:
            self.gumbi[stolpec][vrstica].config(borderwidth= 5)
        self.osvezi_polje_po_potezi()

    def zakljuci(self):
        for vrstica in range(self.igra.visina):
            for stolpec in range(self.igra.sirina):
                self.gumbi[stolpec][vrstica].config(state='disabled')


    def osvezi_polje_po_potezi(self):
        for vrstica in range(self.igra.visina):
            for stolpec in range(self.igra.sirina):
                if self.igra.igralec == '0':
                    if (vrstica, stolpec) in self.igra.belefigure:
                        self.gumbi[stolpec][vrstica].config(text='0', state='active')
                    elif (vrstica, stolpec) in self.igra.crnefigure:
                        self.gumbi[stolpec][vrstica].config(text='X',state='disabled')
                    else:
                        self.gumbi[stolpec][vrstica].config(text=' ',state='disabled')
                else:
                    if (vrstica, stolpec) in self.igra.crnefigure:
                        self.gumbi[stolpec][vrstica].config(text='X', state='active')
                    elif (vrstica, stolpec) in self.igra.belefigure:
                        self.gumbi[stolpec][vrstica].config(text='0',state='disabled')
                    else:
                        self.gumbi[stolpec][vrstica].config(text=' ',state='disabled')
        if self.igra.zmaga():
            self.obvestilo.config(text='ZMAGA IGRALCA: ' + str(self.igra.igralec))
            self.zakljuci()
        elif self.igra.testni:
            self.osvezi_polje_po_potezi()




    def osvezi_polje_po_izbiri_figure(self):
        for vrstica in range(self.igra.visina):
            for stolpec in range(self.igra.sirina):
                if (vrstica, stolpec) not in self.igra.belefigure and (vrstica, stolpec) not in self.igra.crnefigure:
                    self.gumbi[stolpec][vrstica].config(state='active')
                else:
                    self.gumbi[stolpec][vrstica].config(state='disabled')




    def premakni(self, vrstica, stolpec):
        if self.igra.izbrana_figura:
            self.igra.prestavi_figuro(stolpec, vrstica)
            if not self.igra.izbrana_figura:
                self.stevec_potez.config(text=str(self.igra.poteze))
                self.slednik_igralev.config(text=str(self.igra.igralec))
                self.osvezi_polje_po_potezi()
        else:
            self.igra.izberi_figuro(stolpec, vrstica)
            if self.igra.izbrana_figura:
                self.osvezi_polje_po_izbiri_figure()
                self.stevec_potez.config(text=str(self.igra.poteze))

def glavna_zanka():
    okno = tk.Tk()
    pravi = Vmesnik(okno)
    okno.mainloop()

glavna_zanka()
