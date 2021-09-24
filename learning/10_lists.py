names = ["Amine", "Joachim le boss", "Sacha", 27, ["France", "Maroc", "Espagne"], True]

print(str(names[4]))
names[4].append("Italie")
names[1] = names[1].replace("le boss", "le big boss")
print(str(names[:3]))
print(str(names[4]))
print(str(names[4][3]))
names.insert(1, "Manuel")
names[5].sort()
listttt = names.copy()
names[0] = "e"
print(listttt)
print(names)


