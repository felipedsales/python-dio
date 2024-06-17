################################
# Estrutura de Repetição While #
################################

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Logar \n[2] Cadastrar \n[0] Sair \n: "))

    if opcao == 1:
        print("Logado")
    elif opcao == 2:
        print("Cadastrado")
else:
    print("Obrigado por usar nosso sistema, até logo!")