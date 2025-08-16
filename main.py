from solids.integration import simpson
from solids.parsing import buildLambda
from solids.revolution import createRevolutionMesh
from solids.view import createAnimation
import matplotlib.pyplot as plt

f_str = input("f(x) = ")
a = float(input("a = "))
b = float(input("b = "))
n = int(input("Qual vai ser o número de pontos? "))

f = buildLambda(f_str)

res = simpson(f, a, b, n)

print(f"O volume do sólido é: {res} u.v.")

X, Y, Z = createRevolutionMesh(f, a, b, n)

ani = createAnimation(X, Y, Z, n)
plt.tight_layout()
plt.show()
print("Calma! Não feche ainda!")
print("Estamos gerando o vídeo da sua animação...")
ani.save('animation.mp4', writer='ffmpeg', fps=30)
print("Vídeo exportado com sucesso! Verifique a sua pasta")