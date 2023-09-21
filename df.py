from equacao1 import f1, g1, resultado1
from equacao2 import f2,g2, resultado2
from equacao3 import f3,g3, resultado3

# Somar os resultados
soma_resultados = sum(resultado1) + sum(resultado2) + sum(resultado3)

print("\n(g1 ∘ f1)(", x, ") =", resultado1[0])
print("(g1 ∘ g1)(", x, ") =", resultado1[1])
print("(f1 ∘ f1)(", x, ") =", resultado1[2])
print("(f1 ∘ g1)(", x, ") =", resultado1[3])

print("\n(g2 ∘ f2)(", x, ") =", resultado2[0])
print("(g2 ∘ g2)(", x, ") =", resultado2[1])
print("(f2 ∘ f2)(", x, ") =", resultado2[2])
print("(f2 ∘ g2)(", x, ") =", resultado2[3])

print("\n(g3 ∘ f3)(", x, ") =", resultado3[0])
print("(g3 ∘ g3)(", x, ") =", resultado3[1])
print("(f3 ∘ f3)(", x, ") =", resultado3[2])
print("(f3 ∘ g3)(", x, ") =", resultado3[3])

print("\nSoma dos resultados =", soma_resultados)
