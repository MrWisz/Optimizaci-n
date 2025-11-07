import numpy as np

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


def gradiente_descendente_armijo(f, grad_f, x0, tol=1e-6, max_iter=200):
    """
    Método de gradiente descendente con búsqueda de paso Armijo.
    """
    xk = np.array(x0, dtype=float)
    historial = []

    for k in range(max_iter):
        gk = grad_f(xk)
        norm_g = np.linalg.norm(gk)
        if norm_g < tol:
            break

        dk = -gk
        alpha = armijo(f, grad_f, xk, dk)
        xk1 = xk + alpha * dk
        historial.append((k, xk.copy(), f(xk), alpha, norm_g))
        xk = xk1

    return xk, f(xk), historial
