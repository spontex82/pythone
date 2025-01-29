def main() :
    print("Il programma esegue il calcolo della spesa totale e, se applicabile, ne calcola lo sconto.")
    print('Inserire i prezzi seguiti da "N" se trattasi di animale o da "Y" se trattasi di oggetto.', "Digitare -1 per terminare l'inserimento dei dati ed effettuarne il calcolo")
    spesa = []
    categoria = []
    prezzo = input()
    while isPrezzoValid(prezzo) :
        spesa.append(float(prezzo[:len(prezzo)-1]))
        categoria.append(prezzo[len(prezzo)-1:])
        prezzo =input()
    if prezzo == "-1" :
        if (len(spesa)) > 0 :
            animali, oggetti = controlloCategorie(categoria)
            totale = 0
            for costo in spesa :
                print(costo)
                totale += costo
            if (animali > 0) & (oggetti > 4) :
                totale = totale - (totale / 100 * 20)
                print("La tua spesa beneficia dello sconto del 20%. Hai speso", "%.2f" %(totale) + "€")
            else :
                print("Non hai raggiunto la spesa minima per beneficiare dello sconto. Hai speso," "%.2f" %(totale) + "€")
        else :
            print("Impossibile eseguire alcun conteggio perché non sono stati inseriti valori di spesa")
    else :
        print("E' stato inserito un valore invalido, riavviare il programma")

def isPrezzoValid(stringaNumero) :
    try :
        if (len(stringaNumero) == 2) &  (stringaNumero == "-1") :
            return False
        elif (float(stringaNumero[:(len(stringaNumero)-1)]) > 0) :
            if ((stringaNumero[len(stringaNumero)-1]) == "N") | ((stringaNumero[len(stringaNumero)-1]) == "Y") :
                return True
            else :
                return False
        else :
            return False
    except ValueError :
        return False

def controlloCategorie(tipoSpesa) :
    categoria1 = 0
    categoria2 = 0
    for tipo in tipoSpesa :
        if tipo == "Y" :
            categoria1 += 1
        elif tipo == "N" :
            categoria2 += 1
    return categoria1, categoria2

main()
