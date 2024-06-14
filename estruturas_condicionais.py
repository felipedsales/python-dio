###########################
# Estruturas Condicionais #
###########################
# If #Elif # Else

idade = int(input("Digite sua idade: "))
if idade < 18:
    print("Você é de menor")
elif idade >= 18 and idade <65:
    print("Você é adulto")
else:
    print("Você é idoso")