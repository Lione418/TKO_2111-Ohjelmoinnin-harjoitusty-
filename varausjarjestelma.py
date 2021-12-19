#Tuodaan aikaominaisuudet, jotta ohjelma tietää mikä päivä on
import datetime
tanaan = datetime.date.today()
vkPv = ("maananta","tiistai","keskiviikko","torstai","perjantai","lauantai","sunnuntai")
viikonpv = tanaan.weekday()

#Luetaan tarjolla olevat elokuvat
elokuvat = {}
with open("elokuvat.csv") as tiedosto:
   for rivi in tiedosto:
        tiedot = rivi.strip().split(",")
        elokuvat[tiedot[0]] = [tiedot[1],tiedot[2]]

def lisaaElokuva():
    avain = input("Anna elokuvan nimi: ")
    arvo1 = input("Anna elokuvan ikäraja: ")
    arvo2 = input("Anna elokuvan kesto (esim. '1h 33min'): ")
    f = open("elokuvat.csv", "a")
    f.write(f"{avain},{arvo1},{arvo2}")
    f.close()
    print(f"Lisäsit elokuvan: {avain}, {arvo1}, {arvo2}")
    elokuvat[avain] = [arvo1,arvo2]

def elokuvavalikko():
    print("Ohjelmistossa nyt: ")
    for nimi in elokuvat:
        tiedot = ""
        for i in elokuvat[nimi]:
            tiedot += ", "
            tiedot += i
        print(f"{nimi}{tiedot}")

def tanaanOhjelmistossa():
    print(f"Tänään on {vkPv[viikonpv]}")

def huomennaOhjelmistossa():
    print(f"Huomenna on {vkPv[viikonpv + 1]}")

def ohjelmisto():
    pass


print("Tervetuloa!")
jatkuu = True
while jatkuu:
    #Aloitusvalikko
    print("Valitse seuraavista:")
    print("(E) Elokuvat")
    print("(T) Tänään")
    print("(H) Huomenna")
    print("(S) Selaa ohjelmistoa")
    print("(X) Poistu")
    x = input()

    #Elokuvavalikko
    if x == "E":
        elokuvavalikko()

    #Tänään ohjelmistossa
    elif x == "T":
        tanaanOhjelmistossa()

    #Huomenna ohjelmistossa
    elif x == "H":
        huomennaOhjelmistossa()

    #Selaa ohjelmistoa
    elif x == "S":
        ohjelmisto()

    elif x == "X":
        jatkuu = False

    #Ylläpitäjän käyttöliittymä
    elif x == "9876":
        admin = True
        print("Hei ylläpitäjä!")
        while admin == True:
            print("(1) Lisää elokuva")
            y = input()

            if y == "1":
                lisaaElokuva
    
