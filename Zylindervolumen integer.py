#Programm zur Berechnung des Volumens eines Zylinder mit Ganzzahlen
#von Nicolas Csaba Bohocki
#19.05.2020
print("Berechnung eines Zylindervolumens")
print("---------------------------------")
import math
Länge = 0                                                               #Deklarieren von Variablen
Radius = 0
Durchmesser = 0
Volumen = 0
Länge = int(input("Länge in cm: "))                                     #Deklarieren der Variable "Länge" per Eingabeaufforderung in Zentimeter
print("Radius oder Durchmesser? ")                                      #Überprüfung der Einheit des zu berechnenden Zylinders
Einheit = input("(rad/dur): ")
if Einheit == "rad":                                                    #Berechnen des Flächeninhalts mithilfe des Radius
    Radius = int(input("Radius in cm: "))
    Volumen = Länge*(Radius*int(math.pi))
elif Einheit == "dur":                                                  #Berechnen des Flächeninhalts mithilfe des Durchmessers
    Durchmesser = int(input("Durchmesser in cm: "))
    Volumen = Länge*(((Durchmesser**2)/4)*int(math.pi))
else:
    Ende = input("Eingabe Falsch. Eingabe, um Programm zu beenden: ")
    if Ende == Ende:
        exit()
print("Volumen des Zylinders beträgt " + str(int(Volumen)) + " cm^3")   #Ausgabe des Volumens in Kubikzentimeter
