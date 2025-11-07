import math

def crear_funcion(expr: str):
    def f(x):
        return eval(expr, {"x": x, "math": math,
                           "sin": math.sin, "cos": math.cos, "tan": math.tan,
                           "tanh": math.tanh, "exp": math.exp, "log": math.log,
                           "sqrt": math.sqrt, "pi": math.pi, "e": math.e})
    return f
