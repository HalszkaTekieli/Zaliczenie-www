zakres = int(input("Podaj górny zakres liczb, wśród których chcesz znaleźć liczby Armstronga: "))

for n in range(10, zakres):
    dlugosc = len(str(n))
    cyfry = list(map(int, str(n)))
    suma = 0
    for c in cyfry:
        suma += c ** dlugosc
        if suma > n:
            break
    if suma == n:
        print(n)