notas = [7,5, 8.0, 9.5, 6.0, 8.5]
print("Notas: ", notas)

print("Menor nota: ", min(notas))
print("Menor nota: ", min(notas))
print("Soma: ", sum(notas))
print("Media: ", sum(notas) / len(notas))

nomes = ["Adriana", "Barbara", "Carla", "Daniel"]

print("Usando POR simples")

for nome in nomes:
    print(f"olá, (nome)")
print("Usando enumerate: ")

for indice, nome in enumerate(nomes):
    print(f"Posição (indeice): (nome)")




original = ["A", "B", "C"]
copia = list(original)

print("Original:", original)
print("copia: ", copia)
print("São iguais: ", original == copia)

copia.append("D")
print("Original: ", original)
print("copia: ", copia)
print("São iguais: ", original == copia)
