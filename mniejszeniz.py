wielkosc = int(input())
tablica = [0] * wielkosc

for i in range(0, wielkosc):
    tablica[i] = int(input())

print()
wielkosc2 = int(input())
tablica2 = [0] * wielkosc2
wielkosci = [0] * wielkosc2

for i in range(0, wielkosc2):
    tablica2[i] = int(input())

print()

for i in range(0, wielkosc2):
    for j in range(0, wielkosc):
        if tablica2[i] > tablica[j]:
            wielkosci[i] += 1

    print(wielkosci[i])