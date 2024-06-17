###########################
# Interpolação de Strings #
###########################

nome = "Felipe"
idade = 25
profissao = "Progamador"
linguagem = "Python"
saldo = 12.000

# Old Style %
print("Nome: %s Idade: %d Profissão: %s Linguagem %s Salário %f" % (nome, idade, profissao, linguagem, saldo))
# Nesse método é necessário informar o tipo de variável com %d para int, %s para string e %f para float
# Também precisa informar as variáveis que seram chamadas, na ordem respectiva

# Método Format
print("Nome:{} Idade:{} Profissão:{} Linguagem:{} Salário:{}".format(nome, idade,profissao,linguagem,saldo))
# Nesse método é necessário informar onde a variável deve aparecer, utilizando {} 
# As variáveis seram exibidas, na ordem respectiva
# É possível informar a posição da variável dentro das {}, por exemplo "Nome:{1}" seria informado a variável idade

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
# 2° Modo que é possível usar esse método

dados = {"nome": "Felipe", "idade": 25} 
# Definição de dicionário para atribuir valores as variáveis
print("Nome: {nome} Idade: {idade}".format(**dados))
# 3° Modo para utilizar o método

#f strings
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.3f}") # .3f significa que seram adicionadas 3 casas depois da vírgula em uma variável float
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}") # Adiciona mais 10 casas antes da vírgula
# Nesse método precisamos colocar o f antes da string e informar o nome das variáveis entre chaves{} 