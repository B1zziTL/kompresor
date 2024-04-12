#vstupny udaj
oznam = "Chcem uz zmaturovat konecne"
oznamik = oznam.split()

#vytvorenie prazdnych zoznamov
kompres_oznam = []
dekompres_oznam = []
pismena = []

def kompresia(): #funkcia na kompresiu textu
    for slovo in oznamik: #cyklus na prechadzanie slov v ozname
        #nastavenie hodnoty pomocnej premennej
        pocet = 0
        
        for pismeno in slovo: #cyklus na prechadzanie pismen v slove
            #podmienka na zapisanie velkeho pismena
            if pocet == 0:
               pismena.append(pismeno.upper())
            else:
                pismena.append(pismeno)

            #zmena pomocnej premennej
            pocet += 1

        #vytvorenie noveho slova
        nove_slovo = "".join(pismena)
        kompres_oznam.append(nove_slovo)
        
        #vyprazdnenie zoznamu
        pismena.clear()

def dekompresia(): #funkcia na dekompresiu textu
    for i in kompres_oznam: #cyklus na prechadzanie hodnot v zozname
        #zapisanie velkym pismenom
        dekompres_oznam.append(i.upper())

#zavolanie funkcii
kompresia()
dekompresia()

#vypisanie pozadovanych hodnot
print("Počet slov v ozname: ",len(oznamik))
print("Kompresovaný oznam: ","".join(kompres_oznam))
print("Dekompresovaný oznam: "," ".join(dekompres_oznam))
