import datetime
tanaan = datetime.date.today()
vkPv = ("maananta","tiistai","keskiviikko","torstai","perjantai","lauantai","sunnuntai")
viikonpv = tanaan.weekday()

def elokuvavalikko():
    pass

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
    x = input()
    print("Valitsit: " + x)

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

    #Ylläpitäjän käyttöliittymä
    elif x == "9876":
        print("Hei ylläpitäjä!")
        jatkuu = False
