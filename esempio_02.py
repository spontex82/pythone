def main() :
     
    letteraDaRipetere = input("Dammi la lettera da ripetere ")
    altezzaAlbero = int(input("Quanto lo vuoi alto? "))
    for i in range(0, altezzaAlbero) :
        print(" " * (altezzaAlbero - i -1) + letteraDaRipetere * (2 * i + 1))

main()