# dado uma string, retorna a lambda dela
import sympy as sp

def buildLambda(f_str):
    x = sp.Symbol('x')
    
    f_sym = sp.sympify(f_str)
    
    return sp.lambdify(x, f_sym, 'numpy')
    