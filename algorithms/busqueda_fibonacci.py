def fibonacci(n):
    F = [0, 1]
    for i in range(2, n+1):
        F.append(F[-1] + F[-2])
    return F


def busqueda_fibonacci(funcion, a, b, L):
    def fib(n):
        F = [0, 1]
        for i in range(2, n+1):
            F.append(F[-1] + F[-2])
        return F

    n = 1
    while fib(n)[-1] <= (b - a) / L:
        n += 1
    F = fib(n)
    k = 1
    lam = a + (F[n-2] / F[n]) * (b - a)
    mu = a + (F[n-1] / F[n]) * (b - a)
    f_lam = funcion(lam)
    f_mu = funcion(mu)
    historial = []

    while k < n - 1:
        if f_lam > f_mu:
            historial.append((k, a, b, lam, f_lam, mu, f_mu, "Derecha"))
            a = lam
            lam = mu
            f_lam = f_mu
            mu = a + (F[n-k-1] / F[n-k]) * (b - a)
            f_mu = funcion(mu)
        else:
            historial.append((k, a, b, lam, f_lam, mu, f_mu, "Izquierda"))
            b = mu
            mu = lam
            f_mu = f_lam
            lam = a + (F[n-k-2] / F[n-k]) * (b - a)
            f_lam = funcion(lam)
        k += 1

    return (a + b) / 2, funcion((a + b) / 2), historial
