MESI = ("Gennaio  " +
        "Febbraio " +
        "Marzo    " +
        "Aprile   " +
        "Maggio   " +
        "Giugno   " +
        "Luglio   " +
        "Agosto   " +
        "Settembre" +
        "Ottobre  " +
        "Novembre " +
        "Dicembre " )
numero_mese = int(input("Inserisci il numero del mese "))
print(MESI[((numero_mese - 1)*9):(((numero_mese - 1)*9) + 9)])