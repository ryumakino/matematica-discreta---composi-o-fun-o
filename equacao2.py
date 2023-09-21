f_equacoa2 = input("\nInsira a função f(x): ")
g_equacao2 = input("Insira a função g(x): ")

f_equacoa2 = f_equacoa2.replace("^", "**")
g_equacao2 = g_equacao2.replace("^", "**")

def f2(x):
    return eval(f_equacoa2)

def g2(x):
    return eval(g_equacao2)

x = float(input("Insira o valor de x: "))

resultado2 = [g2(f2(x)), g2(g2(x)), f2(f2(x)), f2(g2(x))]
