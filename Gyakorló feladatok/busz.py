def atlagfogyasztas(tavolsag, fogyasztas):
    return (fogyasztas / tavolsag) * 100

with open("fogyasztas.txt", "r", encoding="utf-8") as in_file:
    beolvas = in_file.readlines()
    atmenet = []
    adatok = []
    for i in beolvas:
        resz = i.strip().split(";")
        atmenet = [resz[0], int(resz[1]), float(resz[2])]
        adatok.append(atmenet)

    print(f"A beolvasott buszok száma: {len(adatok)}")
    
    maxkm = 0
    index = 0
    indexmax = 0
    for i in adatok:
        if i[1] > maxkm:
            maxkm = i[1]
            indexmax = index
        index += 1

    print(f"A legnagyobb távolságot megtett busz rendszáma: {adatok[indexmax][0]}")

    print("A 9 liternél többet fogyasztó buszok listája:")

    for i in adatok:
        fogyaszt = atlagfogyasztas(i[1], i[2])
        fogyaszt = round(fogyaszt, 2)
        if fogyaszt > 9:
            print(i[0], fogyaszt)