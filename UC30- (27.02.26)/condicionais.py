estatura = float(input("Digite sua altura: "))
estatura = estatura * 100

#Em python, f-strings (f"...") São usadas inserir textos traduzidos dinamicamente dentro de uma frase.

print(f"Sua altura é de {estatura}")
print("Sua altura é de:", estatura)

nome = input("Digite seu nome: ")
idade = 23

texto = "Meu nome é {} e tenho {} anos.".format(nome, idade)
texto = "Meu nome é {n} e tenho {i} anos.".format(n=nome, i=idade)
texto = "Meu nome é %s e tenho %d anos.".format(nome, idade)
print(texto)

