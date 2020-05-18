#Rabattrechner von Nicolas Csaba Bohocki, 07.05.2020

print("Rabattrechner")
print("--------------------------------------")
Netto = float(input("Nettopreis? "))                                                                # Hier werden die Variablen Definiert und Deklariert
Rabatt = float(input("Rabatt in Prozent? "))                                                        
Mehrwertsteuer = float(input("Mehrwertsteuer: 9 oder 19%? "))                                       
while (Mehrwertsteuer != 9) and (Mehrwertsteuer != 19):                                             # Überprüfung ob MWS richtig
    Mehrwertsteuer = input("Mehrwertsteuer nicht korrekt. Erbitte erneute Eingabe: 9 oder 19%? ")   
    Mehrwertsteuer = int(Mehrwertsteuer)                                                            
RabattDez = float(Rabatt / 100)                                                                     # Der Rabatt wird zur weiteren Berechnung umgerechnet
Rabatt = float(1 - RabattDez)                                                                             
MehrwertsteuerDez = float(Mehrwertsteuer / 100)                                                     # Hier die Mehrwertsteuer
Mehrwertsteuer = float(MehrwertsteuerDez + 1)                                                       
NeuerPreis = float(Netto * Rabatt)                                                                  # Hier wird das Endergebnis berechnet
Endpreis = float(NeuerPreis * Mehrwertsteuer)                                                       
print("--------------------------------------")                                                     
print("Ihr zu Zahlender Bruttopreis beträgt " + str(round(Endpreis,2)) + (" €."))                   # Das Endergebnis wird Ausgegeben

