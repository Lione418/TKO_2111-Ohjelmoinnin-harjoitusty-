import json

#Salit

#Salien alustus
#Saleja on kolme eri kokoista. Jokaisessa on jokaisena päivänä 3 näytöstä, jotka indeksoitu ma1, ma2, jne.
#Jokaisella näytösajalla on e-loppuinen lisätunniste (esim. ke3e), johon tallennetaan kys. ajankotana esitettävän elokuvan nimi.
#Salit on tallennettu matriiseina sanakirjan sisään, joka on viety json-tiedostoon.

#pieni = 6 x 8 = 30
pieni = []
for i in range(6):
    arvo = []
    for j in range(9):
        if i == 0:
            if j == 0:
                arvo.append(" ")
            else:
                arvo.append(str(j))
        elif j == 0:
            arvo.append(str(i))
        else:
            arvo.append("0")
    pieni.append(arvo)


#heureka = 8 x 13
heureka = []
for i in range(9):
    arvo = []
    for j in range(14):
        if i == 0:
            if j == 0:
                arvo.append(" ")
            else:
                arvo.append(str(j))
        elif j == 0:
            arvo.append(str(i))
        else:
            arvo.append("0")
    heureka.append(arvo)

#iso = 10 x 20
iso = []
for i in range(11):
    arvo = []
    for j in range(21):
        if i == 0:
            if j == 0:
                arvo.append(" ")
            else:
                arvo.append(str(j))
        elif j == 0:
            arvo.append(str(i))
        else:
            arvo.append("0")
    iso.append(arvo)

pieni_sali={}
heureka_sali={}
iso_sali={}

paivat=["ma","ti","ke","to","pe","la","su"]
salit=[pieni, heureka, iso]

for s in salit:
    for i in paivat:
        for j in range(3):
            if s == pieni:
                pieni_sali[f"{i}{j+1}"]=s
                pieni_sali[f"{i}{j+1}e"]="Ei näytöstä"
            elif s == heureka:
                heureka_sali[f"{i}{j+1}"]=s
                heureka_sali[f"{i}{j+1}e"]="Ei näytöstä"
            elif s == iso:
                iso_sali[f"{i}{j+1}"]=s
                iso_sali[f"{i}{j+1}e"]="Ei näytöstä"

#"Tyhjät" salit omiin tiedostoihinsa
with open("pieni_sali.json", 'w') as f:
    json.dump(pieni_sali, f, indent=2)
with open("heureka_sali.json", 'w') as f:
    json.dump(heureka_sali, f, indent=2)
with open("iso_sali.json", 'w') as f:
    json.dump(iso_sali, f, indent=2)
