#########################
# Fatiamento de Strings #
#########################

# Funciona com três parâmetros start:stop:step
nome = "Felipe Santos de Sales"

print(nome[0]) 
# Retorna o índice que no caso é a primeira letra

print(nome[-1]) 
# Retorna a última letra

print(nome[5]) 
# Retorna o sexto caractere pois conta a partir de 0

print(nome[:6]) 
# Retorna os 6 primeiros caracteres
# Nesse caso não foi informado o start só o stop

print(nome[7:])
# Retorna a partir do 7° caractere
# Nesse caso não foi informado o stop só o start

print(nome[14:22])
# Retorna os caracteres no intervalo entre o 10° e 22° caractere
# Nesse caso foram informados o start e o stop

print(nome[10:16:2])
# Retorna os caracteres no intervalo entre o 10° e 22° caractere no iontervalo de 2 caracteres
# Nesse caso foram informados o start, stop e step

print(nome[:])
# Retorna todos os caracteres

print(nome[::-1])
# Retorna todos os caracteres de trás para frente por estar usando um número negativo