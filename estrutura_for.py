#################
# Estrutura For #
#################

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# Exibe as vogais contidas no valor digitado
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
        
else: 
    print() #Pula uma linha
    print("Final da repetição")
# Else não é comum mas existe a possibilidade de usá-lo