magas = []
ala = []

print("Magasságok: ")
userInput = None
while userInput != 0:
    userInput = int(input( ))
    if userInput >= 180:
        magas.append(userInput)
    elif userInput != 0:
        ala.append(userInput)

print("Alacsonyak:", *ala)
print("Magasak: ", *magas)

atl = 0
for i in magas:
    atl += i

for i in ala:
    atl += i
print(f"A tanulók átlag magassága: {round(atl / (len(magas)+len(ala)), 2)} cm")

if len(ala) > 0:
    maxh = 0
    for i in ala:
        if i > maxh:
            maxh = i

    print(f"A legmagasabb alacsony tanuló magassága: {maxh} cm")