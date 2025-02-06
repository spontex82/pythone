def main() :

    punteggio = [0, 0]
    vittoria = True
    while vittoria :
        scambio = int(input())
        if scambio == 1 :
            punteggio[0] = punteggio[0] + 1
        elif scambio == 2 :
            punteggio[1] = punteggio[1] + 1
        if ((punteggio[0] >= 3) == (punteggio[1] >= 3)) :
            vittoria = True
        elif  (punteggio[0] > 3 and punteggio[1] <= 3) or (punteggio[0] <= 3 and punteggio[1] > 3) :
            vittoria = False
    print(punteggio)

main()