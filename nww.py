def NWD(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c

    return a

def NWW(a, b):
    return a * b // NWD(a, b)

def NWW_all(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = NWW(result, num)
    return result

ilosc_setow = int(input())

wyniki = []
for i in range(ilosc_setow):
    ilosc = int(input())
    tabs  = [0]*ilosc

    print()
    for j in range(0, ilosc):
        tabs[j] = int(input())
        
    wyniki.append(NWW_all(tabs))

print()
for i, wynik in enumerate(wyniki):
    print(wynik)