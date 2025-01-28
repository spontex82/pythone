def main() :
    votazione = []
    print("Con la seguente funzione si può dare un giudizio (da 0 a 10) per valutare l'indice di gradimento del film")
    voto = input()
    while isNumberValid(voto) : 
        votazione.append(int(voto))
        voto = input()
    lunghezzaVettore = len(votazione)
    if lunghezzaVettore > 2 :
        votazione.remove(min(votazione))
        votazione.remove(max(votazione))
        print("%.2f" %(sum(votazione) / len(votazione)))
    elif lunghezzaVettore > 0 & lunghezzaVettore < 2 :
        print("Non ho abbastanza valori per poter stimare una media corretta")
    else :
        print("I dati inseriti non sono validi")

def isNumberValid(stringaNumero) :
    if len(stringaNumero) > 0 :
        if stringaNumero.isdigit() :
            if int(stringaNumero) < 11 :
                return True
        else :
            return False

main()
