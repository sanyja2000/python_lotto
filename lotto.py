import random
lista = list(range(1,91))
huzott = []
for x in range(5):
	szam = random.choice(lista)
	lista.remove(szam)
	huzott.append(szam)
huzott.sort()
print("Huzott szamok: "+" ".join([str(i) for i in huzott]))
