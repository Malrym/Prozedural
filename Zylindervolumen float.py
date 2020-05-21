#Programm zur Berechnung des Volumens eines Zylinder mit Fließkommazahlen
#von Nicolas Csaba Bohocki
#21.05.2020
print("Berechnung eines Zylindervolumens")
print("---------------------------------")
import math
Länge = 0                                                               #Deklarieren von Variablen
Radius = 0
Durchmesser = 0
Volumen = 0
Länge = float(input("Länge in cm: "))                                    #Deklarieren der Variable "Länge" per Eingabeaufforderung in Zentimeter
print("Radius oder Durchmesser? ")                                      #Überprüfung der Einheit des zu berechnenden Zylinders
Einheit = input("(rad/dur): ")
if Einheit == "rad":                                                    #Berechnen des Flächeninhalts mithilfe des Radius
    Radius = float(input("Radius in cm: "))
    Volumen = Länge*(2*float(math.pi)*Radius)
elif Einheit == "dur":                                                  #Berechnen des Flächeninhalts mithilfe des Durchmessers
    Durchmesser = float(input("Durchmesser in cm: "))
    Volumen = Länge*(((Durchmesser**2)/4)*float(math.pi))
else:
    Ende = input("Eingabe Falsch. Eingabe, um Programm zu beenden: ")
    if Ende == Ende:
        exit()
print("Volumen des Zylinders beträgt " + str(round(Volumen,2)) + " cm^3")   #Ausgabe des Volumens in Kubikzentimeter
