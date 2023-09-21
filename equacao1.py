f_equacoa1 = input("\nInsira a função f(x): ")
g_equacao1 = input("Insira a função g(x): ")

f_equacoa1 = f_equacoa1.replace("^", "**")
g_equacao1 = g_equacao1.replace("^", "**")

def f1(x):
    return eval(f_equacoa1)

def g1(x):
    return eval(g_equacao1)

x = float(input("Insira o valor de x: "))

resultado1 = [g1(f1(x)), g1(g1(x)), f1(f1(x)), f1(g1(x))]
