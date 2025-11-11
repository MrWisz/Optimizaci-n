import numpy as np


def gradiente_numerico(f, x, h=1e-6):
    """Calcula el gradiente numérico de f en el punto x usando diferencias centrales."""
    n = len(x)
    grad = np.zeros(n)
    for i in range(n):
        e = np.zeros(n)
        e[i] = 1
        grad[i] = (f(x + h * e) - f(x - h * e)) / (2 * h)
    return grad


def busqueda_linea_wolfe(f, grad_f, xk, dk, alpha0=1.0, rho=0.5, c1=1e-4, c2=0.9, max_iter=50):
    """
    Búsqueda lineal con condiciones de Wolfe.
    Retorna el paso α que cumple las dos condiciones.
    """
    alpha = alpha0
    fxk = f(xk)
    grad_fxk = grad_f(xk)

    for _ in range(max_iter):
        new_x = xk + alpha * dk
        f_new = f(new_x)
        grad_new = grad_f(new_x)

        # Condición de Armijo (descenso suficiente)
        if f_new > fxk + c1 * alpha * np.dot(grad_fxk, dk):
            alpha *= rho
            continue

        # Condición de curvatura
        if abs(np.dot(grad_new, dk)) > c2 * abs(np.dot(grad_fxk, dk)):
            alpha *= rho
            continue

        return alpha

    return alpha


def gradiente_descendente_wolfe(f, x0, tol=1e-6, max_iter=200):
    """
    Método de gradiente descendente con búsqueda de paso por condiciones de Wolfe.
    Calcula automáticamente el gradiente numérico.
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
        alpha = busqueda_linea_wolfe(f, grad_f, xk, dk)
        xk1 = xk + alpha * dk

        historial.append((k, xk.copy(), f(xk), alpha, norm_g))
        xk = xk1

    return xk, f(xk), historial
