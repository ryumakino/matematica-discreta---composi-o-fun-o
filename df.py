
for i in range(3):
    f_formula = input("\nInsira a função f(x): ")
    g_formula = input("Insira a função g(x): ")

    f_formula = f_formula.replace("^", "**")
    g_formula = g_formula.replace("^", "**")

    def f(x):
        return eval(f_formula)


    def g(x):
        return eval(g_formula)


    x = float(input("Insira o valor de x: "))

    resultado = [g(f(x)), g(g(x)), f(f(x)), f(g(x))]

    print("\n(g ∘ f)(", x, ") =", resultado[0])
    print("(g ∘ g)(", x, ") =", resultado[1])
    print("(f ∘ f)(", x, ") =", resultado[2])
    print("(f ∘ g)(", x, ") =", resultado[3])
