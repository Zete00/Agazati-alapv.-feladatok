with open("autok.txt", "r", encoding="utf-8") as in_file:
    beolvas = in_file.readlines()
    adatok = []
    for i in beolvas:
        resz = i.strip().split(";")
        atmenet = [resz[0],int(resz[1]),resz[2]]
        adatok.append(atmenet)

    print(f"A nyolcadik autó rendszáma: {adatok[7][0]}")
    print(*adatok[9])
    print(f"A tizenötödik autó márkája: {adatok[14][2]}")
    print(f"A hetedik autó évjárata: {adatok[6][1]}")

    for i in range(len(adatok)):
        print(f"{adatok[i][2]}, {2025-adatok[i][1]} éves, a rendszáma: {adatok[i][0]}")