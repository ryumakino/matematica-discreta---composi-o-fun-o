f_equacoa3 = input("\nInsira a função f(x): ")
g_equacao3 = input("Insira a função g(x): ")

f_equacoa3 = f_equacoa3.replace("^", "**")
g_equacao3 = g_equacao3.replace("^", "**")

def f3(x):
    return eval(f_equacoa3)

def g3(x):
    return eval(g_equacao3)

x = float(input("Insira o valor de x: "))

resultado3 = [g3(f3(x)), g3(g3(x)), f3(f3(x)), f3(g3(x))]
