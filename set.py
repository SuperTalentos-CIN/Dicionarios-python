#Quando usar: Quando você precisa garantir que não haja itens repetidos, fazer operações de conjuntos matemáticos (interseção, união, diferença) ou quando você só quer saber "isso existe aqui dentro?" de forma super rápida.

acessos = ["usuario1", "usuario2", "usuario1", "usuario3", "usuario2"]

acessos_unicos = list(set(acessos))
print(acessos_unicos)
print(len(acessos_unicos))
#Exemplo do mundo real: Uma lista de CPFs que já votaram em uma eleição (ninguém pode votar duas vezes), descobrir os "amigos em comum" entre você e outra pessoa no Facebook (interseção), ou sortear números de loteria.