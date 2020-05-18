# Programm zur Berechnung von Fakultäten
# von Nicolas Csaba Bohocki
# 07.05.2020

print("Programm zur Berechnung von Fakultäten")
print("--------------------------------------")
Counter = 1                                                                 # Definieren und Deklarieren von Variablen
Hilfszahl = 1
Fakultät = 1
Zahl = int(input("Geben sie ihre Zahl ein: "))                              # Definieren und Deklarieren der gewünschten Fakultät als Integer
while Counter < Zahl:                                                       # Berechnen der Fakultät
    Fakultät = Fakultät * (Counter + 1)
    Counter = Counter + 1
print("Die Fakultät ihrer Zahl "+str(Zahl)+" ist "+str(Fakultät)+".")       # Ausgabe der Endgültigen Fakultät