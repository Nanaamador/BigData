def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    while True:
        n = int(input("Ingresa un número: "))
        if es_primo(n):
            print(f"{n} es primo")
        else:
            print(f"{n} no es primo")
        continuar = input("¿Quieres probar otro número? (s/n): ")
        if continuar.lower() != "s":
            print("Byeee!")
            break