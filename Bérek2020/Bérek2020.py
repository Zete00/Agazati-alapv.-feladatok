print("3. feladat")

with open("berek2020.txt", "r", encoding="utf-8") as in_file:
    beolvas = in_file.readlines()
    atmenet = []
    adatok = []
    for i in beolvas:
        resz = i.strip().split(";")
        atmenet = [resz[0], resz[1], resz[2], int(resz[3]), int(resz[4])]
        adatok.append(atmenet)

    berossz = 0
    for i in adatok:
        berossz += i[4]

    atl = berossz / len(adatok)
    kerekitve = round(atl / 1000, 1)

    print(f"Dolgozók száma: {len(adatok)}")
    print(f"Bérek átlaga: {kerekitve} Ft")

    reszleg = input("Kérem egy részleg nevét: ")
    if reszleg in ["beszerzés", "pénzügy", "asztalosműhely", "értékesítés", "lakatosműhely", "karbantartás", "szerelőműhely"]:
        maxim = 0
        indexmax = 0

        for i in range(len(adatok)):
            if adatok[i][2] == reszleg:
                if adatok[i][-1] > maxim:
                    maxim = adatok[i][-1]
                    indexmax = i

        print("A legtöbbet kereső dolgozó a megadott részlegen:")
        print(f"Név: {adatok[indexmax][0]}")
        print(f"Neme: {adatok[indexmax][1]}")
        print(f"Belépés: {adatok[indexmax][3]}")
        print(f"Bér: {adatok[indexmax][4]}")
    else:
        print("A megadott részleg nem létegik a cégnél!")

    besz = 0
    penz = 0
    aszt = 0
    ert = 0
    lak = 0
    kar = 0
    szer = 0
    szem = 0

    for i in adatok:
        if i[2] == "beszerzés":
            besz += 1
        elif i[2] == "pénzügy":
            penz += 1
        elif i[2] == "asztalosműhely":
            aszt += 1
        elif i[2] == "értékesítés":
            ert += 1
        elif i[2] == "lakatosműhely":
            lak += 1
        elif i[2] == "karbantartás":
            kar += 1
        elif i[2] == "szerelőműhely":
            szer += 1
        elif i[2] == "személyzeti":
            szem += 1

    print("statisztika")
    print(f"beszerzés - {besz} fő")
    print(f"pénzügy - {penz} fő")
    print(f"asztalosműhely - {aszt} fő")
    print(f"értékesítés - {ert} fő")
    print(f"lakatosműhely - {lak} fő")
    print(f"karbantartás - {kar} fő")
    print(f"szerelőműhely - {szer} fő")
    print(f"személyzeti - {szem} fő")
