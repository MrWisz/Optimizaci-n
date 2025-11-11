import numpy as np


def gradiente_numerico(f, x, h=1e-6):
    """
    Calcula el gradiente numérico de f en el punto x usando diferencias centrales.
    f: función f(x), donde x es un vector numpy.
    x: punto de evaluación (np.array).
    h: paso para la aproximación.
    """
    n = len(x)
    grad = np.zeros(n)
    for i in range(n):
        e = np.zeros(n)
        e[i] = 1
        grad[i] = (f(x + h * e) - f(x - h * e)) / (2 * h)
    return grad


def armijo(f, grad_f, xk, dk, alpha0=1.0, rho=0.5, c1=1e-4, max_iter=50):
    """
    Regla de Armijo (búsqueda de paso con descenso suficiente).
    """
    alpha = alpha0
    fxk = f(xk)
    grad_fxk = grad_f(xk)

    for _ in range(max_iter):
        new_x = xk + alpha * dk
        if f(new_x) <= fxk + c1 * alpha * np.dot(grad_fxk, dk):
            return alpha
        alpha *= rho
    return alpha


def gradiente_descendente_armijo(f, x0, tol=1e-6, max_iter=200):
    """
    Método de gradiente descendente con búsqueda de paso Armijo.
    Calcula automáticamente el gradiente mediante diferencias centrales.
    """
    xk = np.array(x0, dtype=float)
    historial = []

    for k in range(max_iter):
        gk = gradiente_numerico(f, xk)
        norm_g = np.linalg.norm(gk)
        if norm_g < tol:
            break

        dk = -gk
        grad_f = lambda x: gradiente_numerico(f, x)
        alpha = armijo(f, grad_f, xk, dk)
        xk1 = xk + alpha * dk

        historial.append((k, xk.copy(), f(xk), alpha, norm_g))
        xk = xk1

    return xk, f(xk), historial
