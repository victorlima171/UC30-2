# Calculadora simplificada

def calculadora():
    """Versão simplificada: menu compacto e opção 0 para sair."""
    while True:
        print("\nCALCULADORA")
        print("1 - Soma   2 - Subtração   3 - Multiplicação   4 - Divisão   0 - Sair")
        opcao = input("Opção: ").strip()

        if opcao == "0":
            print("Saindo...")
            break

        if opcao not in ("1", "2", "3", "4"):
            print("Opção inválida.")
            continue

        try:
            a = float(input("Primeiro valor: "))
            b = float(input("Segundo valor: "))
        except ValueError:
            print("Digite números válidos.")
            continue

        if opcao == "1":
            r, s = a + b, "+"
        elif opcao == "2":
            r, s = a - b, "-"
        elif opcao == "3":
            r, s = a * b, "*"
        else:
            if b == 0:
                print("Erro: divisão por zero.")
                continue
            r, s = a / b, "/"

        print(f"{a} {s} {b} = {r}")


if __name__ == "__main__":
    calculadora()