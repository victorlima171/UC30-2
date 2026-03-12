#sem função
print("Olá mundo!")
print("Olá mundo!")
print("Olá mundo!")

#com função
def exibMensagem():
    print("Olá mundo!")

exibMensagem()
exibMensagem()
exibMensagem()

# função com parametro
def saudar(nome):
    print(f"Olá {nome}!")

saudar("gaby")

#parametros obrigatorios
def exitbirBoasVindas(pessoa, mensagem):
    print(f"{mensagem}, {pessoa}")

exitbirBoasVindas("Ana", "Bom dia")

def exitbirBoasVindas(mensagem = "Olá", pessoa = "João"):
    print(f"{mensagem}, {pessoa}")


# Função que retorna um valor
def calcularMedia(nota1,nota2):
    media = (nota1 + nota2) 
    return media

resultado = calcularMedia(8.0, 9.0)
print(f"Media: {resultado}")


# função que retorna multiplos valores
def obterMaiorMenor(a,b,c):
    maior = max(a, b, c)
    menor = min(a, b, c)
    return maior, menor

maxValor, minValor = obterMaiorMenor(10, 5, 8)
print(f"Maioe: {maxValor} = menor: {minValor}")