# Programm zur Wortveränderung und dem Zählen von a's, c's und e's
# von Nicolas Csaba Bohocki
# 07.05.2020

print("Programm zur Wortveränderung und dem Zählen von a's, c's und e's")
print("----------------------------")
Wort = str(input("Geben sie ihr Wort ein: "))                   # Eingabe des gewünschten Wortes
aCounter = 0                                                    # Definieren und Deklarieren der Zähler für die einzelnen Zeichen
cCounter = 0
eCounter = 0
WLänge = len(Wort)                                              # Länge des Wortes wird berechnet
WGross = Wort.upper()                                           # Das Wort wird Gross geschrieben
WKürzung = str(Wort[1:len(Wort)-1])                             # Das Wort wird um das erste und das letzte Char gekürzt
WortLänge = int(len(Wort))
for i in Wort:
    if i == "a":
        aCounter = aCounter + 1
    elif i == "c":
        cCounter = cCounter + 1
    elif i == "e":
       eCounter = eCounter + 1
    else:
        pass
print("Anzahl der Zeichen ihres Wortes: "+str(WLänge))          # Ausgabe der Veränderungen
print("Ihr Wort in Grossbuchstaben: "+str(WGross))
print("Ihr Wort gekürzt: "+str(WKürzung))
print("Anzahl der A's: "+str(aCounter))                         # Ausgabe der gezählten Zeichen
print("Anzahl der C's: "+str(cCounter))
print("Anzahl der E's: "+str(eCounter))
