import random

def busqueda_local(funcion, rango=(-1.3, 1.3), max_iter=1000, step=0.01, minimizar=True):
    x_actual = random.uniform(*rango)
    valor_actual = funcion(x_actual)
    historial = []

    for k in range(max_iter):
        vecinos = [x_actual + step, x_actual - step]
        vecinos = [v for v in vecinos if rango[0] < v < rango[1]]
        if not vecinos:
            break

        valores = [funcion(v) for v in vecinos]

        if minimizar:
            mejor_idx = min(range(len(valores)), key=lambda i: valores[i])
            mejora = valores[mejor_idx] < valor_actual
        else:
            mejor_idx = max(range(len(valores)), key=lambda i: valores[i])
            mejora = valores[mejor_idx] > valor_actual

        historial.append((k+1, x_actual, valor_actual, vecinos[mejor_idx], valores[mejor_idx], "Sí" if mejora else "No"))

        if mejora:
            x_actual, valor_actual = vecinos[mejor_idx], valores[mejor_idx]
        else:
            break

    return x_actual, valor_actual, historial
