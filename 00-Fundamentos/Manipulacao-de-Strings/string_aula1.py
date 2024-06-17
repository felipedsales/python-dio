##################################
# Métodos úteis da classe string #
##################################

nome = "fEliPE"

print(nome.upper()) # Método que transforma todas os caracteres em maiúsculas
print(nome.lower()) # Método que transforma todas os caracteres em minúsculas
print(nome.title()) # Método que transforma a primeira letra em maiúsculas e o restante em minúsculas 

texto = "   Olá Mundo   "

print(texto.strip()) # Elimina espaços à esquerda e à direita da string
print(texto.rstrip()) # Elimina espaços à direita da string
print(texto.lstrip()) # Elimina espaços à esquerda da string

menu = "Python"

print("##" + menu + "##") # Exemplo do que o método abaixo faz
print(menu.center(10)) # Método serve para alinhar a string no espaço de 10 caracteres
print(menu.center(10, "#")) # Método serve para alinhar a string no espaço de 10 caracteres
                            #e adiciona um segundo parâmetro que vai ser colocado nesse espaço

print("-".join(menu)) # Adiciona a string informada entre os caracteres
