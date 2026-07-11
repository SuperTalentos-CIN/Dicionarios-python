#Dicionários

#Quando usar: Quando você tem informações que precisam de "etiquetas" (chaves) para fazer sentido, ou quando precisa relacionar um identificador único a um bloco de informações.

#Exemplo do mundo real: A ficha completa de um usuário (onde as chaves são "nome", "idade", "email"), o catálogo de um estoque (chave: código do produto, valor: quantidade), ou para processar dados que vêm da internet no formato JSON.

#     chave(key) valor(value)
pessoa = {"nome": "Ana", 
          "idade": 28, 
          "cidade": "Recife"}

# Usando a função dict()
carro = dict(marca="Ford", modelo="Ka", ano=2020)

print(carro["marca"])

# Dicionário vazio
vazio1 = {}
vazio2 = dict()

#======================================================

#2. Acesso dos dados

pessoa = {"nome": "Ana", 
          "idade": 28}

#Acesso direto 

print(f"O nome da pessoa é {pessoa['nome']} e sua idade é {pessoa['idade']} anos")

#Usando .get() 
email = pessoa.get("email") 
print(email) # None

email = pessoa.get("email", "Sem email cadastrado") # Se tiver email, ele me retorna o email e se não tiver ele me retorna a frase ao lado

print(email)

 #        keys    values
pessoa = {"nome": "Ana", 
          "idade": 28,
          "Dinheiro": 1000}

# Pegando todas as chaves, valores ou pares 
chaves = pessoa.keys() 

print(f"As chaves são {chaves}")

valores = pessoa.values() 
print()
print(f"Os valores são {valores}")

pares = pessoa.items()  
print() 
print(f"Os itens são {pares}")

#======================================================

#3. Adicionar e atualizar

pessoa = {"nome": "Ana"}

# Adição de uma chave-valor
pessoa["idade"] = 29
pessoa["nome"] = "Kahor"

# pessoa["idade"] += 1

# print(pessoa.items())

# Atualizando várias chaves de uma vez com .update()
pessoa.update({"cidade": "Recife", 
               "profissao": "Dev"})

print(pessoa.items())

# ======================================================
# 4. Remoção de itens

algo = {"nome": "Vinicius",
            "idade": 16,
            "cidade": "Los angeles"}

kahor = {"nome": "Kahor",
         "idade": 16,
         "cidade": "Recife"}

print(algo["cidade"])
print(kahor["cidade"])

dicionario = {"a": 1,
              "b": 2,
              "c": 3,
              "d": 4}
# Remoção de uma chave específica (Gera erro se não existir)
del dicionario['c']

# Remove uma chave específica e armazena o valor dela
valor = dicionario.pop("b") 
print(valor)
print()
print(dicionario)

# Remove e retorna o último par chave-valor inserido
ultimo_par = dicionario.popitem()
print(ultimo_par)
print()
print(dicionario)

#Limpa o dicionário inteiro
dicionario.clear()

#======================================================
#5. Verificação de existência

pessoa = {"nome": "Ana",
          "idade": 28,
          "email": "ana@gmail.com"}

# Checa se a CHAVE existe (não olha os valores)
# if "email" in pessoa:
#     print("A chave email existe!")
# else:
#     print("A chave não existe")

# Verifica o tamanho (quantos pares chave-valor existem)

quantidade = len(pessoa) # length = comprimento]
print(quantidade)


#======================================================

#6. Iteração de loops

pessoa = {"nome": "Ana", 
          "idade": 28, 
          "cidade": "Recife"}

#Loop pelas chaves (padrão)
for chave in pessoa:
    print(chave)

#Loop pelos valores
for valor in pessoa.values():
    print(valor)

# Loop pelas chaves E valores ao mesmo tempo (O mais útil)
for chave, valor in pessoa.items():
    print(f"O {chave} é {valor}")

#======================================================

#7. União de dicionários

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Método 1: Operador Pipe | (Disponível a partir do Python 3.9)
novo_dict = dict1 | dict2 

#======================================================
#8 Dicionários com listas:

# Dicionário onde a chave é o nome do aluno e o valor é uma lista de notas
boletim = {
    "Ana": [8.5, 9.0, 10.0],
    "João": [5.0, 6.5, 7.0]
}

# Pegando a lista inteira da Ana
# notas_ana = boletim["Ana"]
# print(notas_ana) 

# # Pegando APENAS a primeira nota da Ana (Índice 0)
# primeira_nota = boletim['Ana'][0]
# print(primeira_nota)

# # O João fez uma prova de recuperação e tirou 9
boletim["João"].append(9.0)
# print(boletim["João"])

for aluno, notas in boletim.items():
    # 'aluno' é a string, 'notas' é a lista
    media = sum(notas) / len(notas)
    print(f"O aluno {aluno} tem média {media:.3f}")

	# # Se quiser ver nota por nota:
    # for nota in notas:
    #     print(f"- {nota}")





