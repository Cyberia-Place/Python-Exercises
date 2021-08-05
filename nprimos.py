def primos(n):
    # Corrobora que n sea mayor a 0 sin ser decimal
    if n < 1 or n - int(n) != 0:
        return print("Introduzca un número natural mayor a 0.")

    # Inicializa la lista de primos vacía.
    primos_lista = list()

    # Es el número evaluado a ser primo. Se inicializa en 2 porque es el
    # primer primo posible.
    num = 2

    # Es la variable que se usa para contar la cantidad de divisores del num.
    divisores = 0
    while len(primos_lista) < n:
        # Evalúa todos los naturales menores a num y superiores a 1.
        for nat in range(2, num):
            if num % nat == 0:
                divisores += 1

        # Si no encuentra divisores significa que sólo tiene dos,
        # uno y sí mismo, y por tanto es primo.
        if divisores == 0:
            primos_lista.append(num)
        else:
            divisores = 0

        # Le suma uno a num para evaluar el número siguiente al reingresar
        # al while loop.
        num += 1

    print(primos_lista)


primos(1.5)
primos(-5)
primos(0)
primos(50)
