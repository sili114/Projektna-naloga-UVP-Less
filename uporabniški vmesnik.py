import model_less
import tkinter as tk

class Vmesnik:

    def __init__(self, okno):
        self.igra = model_less.Plosca()

        self.obvestilo = tk.Label(okno, text='Pozdravljen v igri Less')
        self.obvestilo.grid(row=0, column=0)

        okno.title('Less')

        self.slednik_igralev = tk.Label(okno,text= str(model_less.plosca.igralec))
        self.slednik_igralev.grid(row=1, column=1)

        tk.Label(okno, text='Na potezi je igralec:').grid(row=1, column=0)
        tk.Label(okno, text='Preostalo število potez:').grid(row=1, column=2)

        self.stevec_potez = tk.Label(okno, text=str(model_less.plosca.poteze))
        self.stevec_potez.grid(row=1, column=3)

        reset_gumb = tk.Button(okno, text='RESETIRAJ IZBIRO FIGURE', command=self.resetiraj_figuro, state='active')
        reset_gumb.grid(row=0, column=2)

        reset = tk.Button(okno, text='NOVA IGRA', command=self.reset, state='active')
        reset.grid(row=0, column=3)

        prikaz_plosce = tk.Frame(okno)
        self.gumbi = []
        for vrstica in range(self.igra.visina):
            vrstica_gumbov = []
            for stolpec in range(self.igra.sirina):
                def pritisni_gumb(vrstica=vrstica, stolpec=stolpec):
                    self.premakni(vrstica, stolpec)
                gumb = tk.Button(prikaz_plosce, text='', height=3, width=3, command=pritisni_gumb, state='disabled')
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

        self.osvezi_polje_pred_izbiro_figure()


    def zakljuci(self):
        for vrstica in range(self.igra.visina):
            for stolpec in range(self.igra.sirina):
                self.gumbi[stolpec][vrstica].config(state='disabled')


    def osvezi(self):
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

    def osvezi_polje_pred_izbiro_figure(self):
        self.osvezi()
        self.preveri_ce_je_kdo_zmagal()
        if not self.igra.zmaga():
            self.osvezi()

    def nove_ovire(self):
        for vrstica in range(self.igra.visina):
            for stolpec in range(self.igra.sirina):
                if (vrstica, stolpec) in self.igra.ovire:
                    self.gumbi[stolpec][vrstica].config(borderwidth=5)
                else:
                    self.gumbi[stolpec][vrstica].config(borderwidth=1)


    def reset(self):
        self.igra.resetiraj_igro()
        self.osvezi()
        self.stevec_potez.config(text=str(self.igra.poteze))
        self.slednik_igralev.config(text=str(self.igra.igralec))
        self.obvestilo.config(text='Pozdravljen v igri Less')
        self.nove_ovire()



    def preveri_ce_je_kdo_zmagal(self):
        if self.igra.zmaga():
            self.obvestilo.config(text='ZMAGA IGRALCA: ' + str(self.igra.zmagovalec))
            self.zakljuci()
        elif self.igra.zmaga() == None:
            self.obvestilo.config(text='NEODLOČENO')
            self.zakljuci()

    def resetiraj_figuro(self):
        self.igra.resetiraj_izbiro_figure()
        self.osvezi_polje_pred_izbiro_figure()


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
                self.osvezi_polje_pred_izbiro_figure()
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
