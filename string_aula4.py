##############################
# String de múltiplas linhas #
##############################

# Esse técnica serve para exibir uma string em várias linhas e manter o recuo

nome = "Felipe"

mensagem = f"""
   Olá meu nome é {nome},
 Eu estou aprendendo Python.
     Essa mensagem tem diferentes recuos.
"""

print(mensagem)

# Pode ser útil para fazer menus de exibição

print(
    """
    ============= MENU =============

    1 - Depositar
    2 - Sacar
    0 - Sair

    ================================

            Obrigado por usar nosso sistema!!!!
"""
)