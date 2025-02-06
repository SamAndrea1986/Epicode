#Si scriva un programma in Python che in base alla scelta dellʼutente permetta di calcolare il perimetro di diverse figure geometriche

print("Programma di calcolo del perimetro di una figura geometrica\n")
print("Selezionare una delle seguenti figure geometriche:\n")
print('''1 - Cerchio
2 - Quadrato
3 - Rettangolo\n''')


scelta = int(input("La figura selezionata e' la numero: "))
if scelta == 1:
    r=float(input("Inserisci il valore del raggio: "))
    print ("La circonferenza del cerchio e': " , r *2 * 3.14)
elif scelta == 2:
    l=float(input("Inserisci il valore del lato: "))
    print ("Il perimetro del quadrato e': " , l *4)
elif scelta == 3:
    base=float(input("Inserisci il valore della base: "))
    alt=float(input("Inserisci il valore dell'altezza; "))
    print ("Il perimentro del rettangolo e': " , base*2+alt*2)
else:
    print ('''Non hai selezionato nessuna delle tre opzioni possibili. 
Riavvia il programma e riprova''')