def main() :

    punteggio = [0, 0]
    vittoria = False
    while not(vittoria) :
        scambio = int(input())
        if scambio == 1 :
            punteggio[0] = punteggio[0] + 1
        elif scambio == 2 :
            punteggio[1] = punteggio[1] + 1
        if (punteggio[0] > 3 and (punteggio[0] - punteggio[1]) >= 2) :
            vittoria = True
        elif (punteggio[1] > 3 and (punteggio[1] - punteggio[0]) >= 2) :
            vittoria = True
    print(stampa_punteggio(punteggio))

def stampa_punteggio(punteggioDaCalcolare) :
    punteggioCalcolato = [0, 0]
    for numero in range(0, 2) :
        if punteggioDaCalcolare[numero] == 1 :
            punteggioCalcolato[numero] = 15
        elif punteggioDaCalcolare[numero] == 2 :
            punteggioCalcolato[numero] = 30
        elif punteggioDaCalcolare[numero] >= 3 :
            punteggioCalcolato[numero] = 40
    if (punteggioCalcolato[0] == 40 and punteggioCalcolato[1] == 40) and (punteggioDaCalcolare[0] > punteggioDaCalcolare[1]) :
        return("Ha vinto il primo giocatore per vantaggio")
    elif (punteggioCalcolato[0] == 40 and punteggioCalcolato[1] == 40) and (punteggioDaCalcolare[1] > punteggioDaCalcolare[0]) :
        return("Ha vinto il secondo giocatore per vantaggio")
    if punteggioDaCalcolare[0] > punteggioDaCalcolare[1] :
        return("Ha vinto il primo giocatore per %s" %punteggioCalcolato)
    else :
        return("Ha vinto il secondo giocatore per %s" %punteggioCalcolato)

main()


