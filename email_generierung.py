#Programm zur E-Mail-Generierung
#von Nicolas Csaba Bohocki
#18.05.2020
Vorname = ["Andreas","Bernd","Christoph"]                               #Deklarieren und Definieren der Listen
Nachname = ["Müller","Meyer","Schmidt"]
Zeichen = [".","-","_"]
Provider = ["hotmail","web","googlemail","gmail","freenet"]
Domain = ["de","com","org","en","fr"]

for VName in Vorname:                                                   #Hier werden die Bedingungen für das Generieren der E-Mail definiert
    for NName in Nachname:
        for Symbol in Zeichen:
            for eMail in Provider:
                for Endung in Domain:
                    print(VName+Symbol+NName+"@"+eMail+"."+Endung)      #Hier wird die eMail-Adresse generiert
