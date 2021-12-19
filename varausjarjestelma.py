#Ajettava aluksi tiedosto salit.py, joka alustaa salitiedot tämän ohjelman käyttöön

import json
import datetime
import numpy as np
#Luodaan aikaominaisuudet, jotta ohjelma tietää mikä päivä on ja osaa nimetä ne
tanaan = datetime.date.today()
#Lopussa ylimääräinen maanantai, jotta "huomenna"-toiminnot toimivat sunnuntainakin
vkPv = ("maanantai","tiistai","keskiviikko","torstai","perjantai","lauantai","sunnuntai","maanantai")
viikonpv = tanaan.weekday()
pv = []
for i in vkPv:
    pv.append(i[:2])
paiva = ""
aika = ""
msali = ""
sali = {}


#Luetaan tarjolla olevat elokuvat
elokuvat = {}
with open("elokuvat.csv") as tiedosto:
   for rivi in tiedosto:
        tiedot = rivi.strip().split(",")
        elokuvat[tiedot[0]] = [tiedot[1],tiedot[2]]

#Tuodaan salitiedot
with open("pieni_sali.json", 'r') as f:
    pieni_sali = json.load(f)
with open("heureka_sali.json", 'r') as f:
    heureka_sali = json.load(f)
with open("iso_sali.json", 'r') as f:
    iso_sali = json.load(f)

def lisaaElokuva():
    avain = input("Anna elokuvan nimi (tai poistu painamalla P): ")
    if avain == "P":
        return
    arvo1 = input("Anna elokuvan ikäraja: ")
    arvo2 = input("Anna elokuvan kesto (esim. '1h 33min'): ")
    f = open("elokuvat.csv", "a")
    f.write(f"{avain},{arvo1},{arvo2}\n")
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


def haeOhjelmisto(paiva: str):
    print("Pieni sali: ")
    print("klo 12 --- " + pieni_sali[f"{paiva}1e"])
    print("klo 15 --- "+ pieni_sali[f"{paiva}2e"])
    print("klo 18 --- "+ pieni_sali[f"{paiva}3e"])

   
    print("Heureka-sali: ")
    print("klo 12 --- " + heureka_sali[f"{paiva}1e"])
    print("klo 15 --- "+ heureka_sali[f"{paiva}2e"])
    print("klo 18 --- "+ heureka_sali[f"{paiva}3e"])

    
    print("Iso sali: ")
    print("klo 12 --- " + iso_sali[f"{paiva}1e"])
    print("klo 15 --- "+ iso_sali[f"{paiva}2e"])
    print("klo 18 --- "+ iso_sali[f"{paiva}3e"])

    g = input("Varaa näistä? (V)")
    if g == "V":
        varaaPaikka(paiva)


def valitsePaiva():
    paiva = input("Valitse päivä (ma/ti/ke/to/pe/la/su) tai palaa (P) ")
    if paiva == "P":
        return
    else:
        return paiva

def kysySali():
    msali = input("Mikä sali? (P/H/I) ")
    return msali

def valitseSali(msali):      
    if msali == "P":
        sali = pieni_sali
    elif msali == "H":
        sali = heureka_sali
    elif msali == "I":
        sali = iso_sali
    else:
        return
    return sali

def valitseAika():
    aika = input("Valitse aika (12/15/18): ")
    if aika == "12":
        aika = "1"
    elif aika == "15":
        aika = "2"
    elif aika == "18":
        aika = "3"
    else:
        return
    return aika
def tulostaSali(paiva, sali, aika):
    
    print(sali[f"{paiva}{aika}e"])
    for line in np.array(sali[f"{paiva}{aika}"]):
            print ('  '.join(map(str, line)))

def ohjelmisto():
    paiva = valitsePaiva()
    try:
        haeOhjelmisto(paiva)
    except:
        print("Jotain meni pieleen")

def salitietojenPaivitys(msali, sali):
    if msali == "P":
        with open("pieni_sali.json", 'w') as f:
            json.dump(sali, f, indent=2)
    elif msali == "H":
        with open("heureka_sali.json", 'w') as f:
            json.dump(sali, f, indent=2)
    elif msali == "I":
        with open("iso_sali.json", 'w') as f:
            json.dump(sali, f, indent=2)
    else:
        print("Jokin meni vikaan.")

def varaaPaikka(paiva:str):
    msali = kysySali()
    sali = valitseSali(msali)
    aika = valitseAika()
    tulostaSali(paiva, sali, aika)

    rivi = int(input("Valitse rivi: "))
    paikka = int(input("Valitse paikka: "))
    if (sali[f"{paiva}{aika}"])[rivi][paikka] == "0":
        (sali[f"{paiva}{aika}"])[rivi][paikka] = "X"
        tulostaSali(paiva, sali, aika)
        print("Paikka varattu")
    
    salitietojenPaivitys(msali, sali)



def selaaVarauksia():
    paiva = valitsePaiva()
    msali = kysySali()
    sali = valitseSali(msali)
    aika = valitseAika()
    tulostaSali(paiva, sali, aika)

def lisaaNaytos(nimi: str):
    paiva = valitsePaiva()
    msali = kysySali()
    sali = valitseSali(msali)
    aika = valitseAika()
    sali[f"{paiva}{aika}e"] = nimi
    salitietojenPaivitys(msali, sali)

        


#Game on
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
        print(f"Tänään on {vkPv[viikonpv]}. Päivän näytökset: ")
        paiva = pv[viikonpv]    
        haeOhjelmisto(pv[viikonpv])

    #Huomenna ohjelmistossa
    elif x == "H":
        print(f"Huomenna on {vkPv[viikonpv + 1]}. Huomisen näytökset: ")
        paiva = pv[viikonpv+1]
        haeOhjelmisto(pv[viikonpv +1])

    #Selaa ohjelmistoa
    elif x == "S":
        ohjelmisto()

    elif x == "X":
        jatkuu = False

    #Ylläpitäjän käyttöliittymä
    elif x == "9876":
        print("Hei ylläpitäjä!")
        admin = True
        while admin:
            print("(1) Lisää elokuva")
            print("(2) Selaa varauksia")
            print("(3) Lisää näytös")
            print("(X) Palaa päävalikkoon")
            y = input()

            if y == "1":
                lisaaElokuva()

            if y == "2":
                selaaVarauksia()
            
            if y == "3":
                elokuvavalikko()
                nimi = input("Valitse elokuva (kirjoita nimi): ")
                lisaaNaytos(nimi)

            elif y == "X":
                admin = False
    
