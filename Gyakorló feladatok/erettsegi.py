a = int(input("Kérem a maximális pontszámot: "))
b = int(input("Kérem az elért pontszámot: "))

if b / a > 0.9:
    print("Gratulálok, szép teljesítmény!")
elif b / a >= 0.25:
    print("A vizsga sikeres")
else: 
    print("A vizsga sikertelen")