#SISTEMA DE GESTÂO DE BIBLIOTECA

#Dicionario p/ armanezar os livros
catalago = {}

#Dicionario p/ armanezar os emprestimos ativos
emprestimoAtivos = {}

#lista p/ armazenar o historico de transição
historico = {}

#Função: Adicionar livro

def adicionarLivro(codigo, titulo, autor, quantidade):
    if codigo in catalogo:
        print(f"Erro: livro com codigo {codigo} já existe")
        return False
    
catalago[codigo] = {
    "titulo": titulo,
    "autor": autor,
    "quantidade": quantidade 
}

print(f"Livro '{titulo}' adicionado com sucesso")
return True

adicionarLivro("1001", "Codigo Limpo", "Robert Martin", 2)z