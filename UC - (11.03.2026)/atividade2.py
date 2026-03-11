notas = ()

notas["nome"] = input("Qual o seu nome:")
notas["nota1"] = int(input("nota 1 prova: "))
notas["nota2"] = float(input("nota 2 prova:"))

media = (notas["nota1"] + notas["nota2"])/ 2

notas["media"] = media

if notas["media"] >= 7:
    print
