import numpy as np

def createRevolutionMesh(f, a, b, n):
    theta = np.linspace(0, 2*np.pi, n)
    x = np.linspace(a,b,n)
    
    X, Theta = np.meshgrid(x, theta)
    Y = f(X) * np.cos(Theta)
    Z = f(X) * np.sin(Theta)

    return X,Y,Z