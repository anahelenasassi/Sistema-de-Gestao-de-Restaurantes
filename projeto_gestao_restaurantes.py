""" PARTICIPANTES (Grupo C)
    Ana Helena Sassi Meinschmiedt
    Alessandra Conceição Santiago Guimarães
    Brenda Flávia de Azeredo
    Enzo de Arruda Santos Scalassara
    Michael Santana
"""
#Iniciando com três restaurantes fictícios para facilitar os testes
restaurante1 = ["Sabor Mexicano", "Rua das Margaritas, 123", "(555) 555-1234", "30-45", []]
r1_prato1 = ["Tacos de Carne Assada", 18.99]
r1_prato2 = ["Quesadillas de Frango", 14.99]
r1_prato3 = ["Burrito Vegetariano", 12.99]
cardapio_r1 = [r1_prato1, r1_prato2, r1_prato3]
restaurante1[4] = cardapio_r1

restaurante2 = ["Delícias Italianas", "Avenida das Pizzas, 456", "(555) 987-6543", "40-55", []]
r2_prato1 = ["Pizza Margherita", 21.99]
r2_prato2 = ["Lasanha à Bolonhesa", 17.99]
r2_prato3 = ["Spaghetti Carbonara", 15.99]
cardapio_r2 = [r2_prato1, r2_prato2, r2_prato3]
restaurante2[4] = cardapio_r2

restaurante3 = ["Sabor Oriental", "Praça do Sushi, 789", "(555) 321-7890", "25-40", []]
r3_prato1 = ["Sushi Variado (12 peças)", 24.99]
r3_prato2 = ["Tempurá de Legumes", 16.99]
r3_prato3 = ["Frango Xadrez com Arroz", 18.99]
cardapio_r3 = [r3_prato1, r3_prato2, r3_prato3]
restaurante3[4] = cardapio_r3

lista_de_restaurantes = [restaurante1, restaurante2, restaurante3]


def menu(lista_de_restaurantes):
    """Função principal que inicia todas as outras a partir de seu menu de texto, recebe como parâmetro uma
    lista de restaurantes formatada no padrão [Nome, Endereço, Telefone, Tempo de Entrega Médio, Cardápio], sendo
    o parâmetro Cardápio uma lista no formato [Nome_do_prato, Preço]"""

    while True:
        print("\n\033[1;94mSISTEMA DE GERENCIAMENTO DE RESTAURANTES\033[0m")
        resposta = input(f'''\033[4mEscolha uma das opções\033[0m:
    1 - Lista de Restaurantes
    2 - Adicionar Restaurante
    3 - Editar Restaurante
    4 - Remover Restaurantes
    5 - Gestão dos Cardápios
    6 - Sair \n''')

        if resposta == "1":
            listar_restaurante(lista_de_restaurantes)
        elif resposta == "2":
            adicionar_restaurante(lista_de_restaurantes)
        elif resposta == "3":
            editar_restaurante(lista_de_restaurantes)
        elif resposta == "4":
            remover_restaurante(lista_de_restaurantes)
        elif resposta == "5":
            editar_cardapio(lista_de_restaurantes)
        elif resposta == "6":
            print("Até mais! Saindo do programa...")
            break
        else:
            print('\n\033[91mOPÇÃO INVÁLIDA. Digite 1, 2, 3, 4 ou 5.\033[0m')


def listar_restaurante(lista_de_restaurantes):
    """Função para printar nome, endereço, telefone, tempo de entrega e cardápio de todos os restaurantes contidos na
     lista que a função recebe como parâmetro"""
    print("\033[1;4;94mLISTA DE RESTAURANTES\033[0m")

    # Loop para acessar a lista de dados de cada restaurante, contidos na lista de restaurantes
    for restaurante in lista_de_restaurantes:
        print(f"\n\033[1mNome\033[0m: {restaurante[0]} \n\033[1mEndereço\033[0m: {restaurante[1]}")
        print(f"\033[1mTelefone\033[0m: {restaurante[2]} \n\033[1mTempo de Entrega\033[0m: {restaurante[3]} minutos")
        print("\033[1mCardápio\033[0m:")
        # Loop para acessar os dados da lista do cardápio
        for i in range(len(restaurante[4])):
            print(f"\033[1m{i+1}\033[0m- {restaurante[4][i][0]} - R$ {restaurante[4][i][1]:.2f}")


def adicionar_restaurante(lista_de_restaurantes):
    """Função para adicionar um restaurante à lista
    de restaurantes(não permite adicionar o cardápio)"""

    nome = input('Digite o Nome do Restaurante: ').title()
    endereco = input('Digite o Endereço [Rua, nº]: ').title()
    telefone = input('Digite o Telefone [(DD) 00000-0000]: ')
    tempo_entrega = input('Digite o Tempo Médio de Entrega [minutos]: ')
    restaurante = [nome, endereco, telefone, tempo_entrega, []]

    lista_de_restaurantes.append(restaurante)
    print(f"\n\033[92mRestaurante '{nome}' adicionado com sucesso.\033[0m")


def editar_restaurante(lista_de_restaurantes):
    """Função para editar um restaurante da lista de
    restaurantes(não permite edição do cardápio)"""
    counter = 0

    for restaurante in lista_de_restaurantes:
        print(f"\033[1mNome:\033[0m {restaurante[0]}")
        counter += 1

    nome_restaurante = input("\033[4mDigite o nome do restaurante que deseja editar\033[0m: ").title()

    # Varre a lista de restaurantes, comparando o nome de cada restaurante com o nome fornecido pelo input
    for restaurante in lista_de_restaurantes:

        if restaurante[0] == nome_restaurante:
            restaurante[0] = input("Digite o novo nome: ").title()
            restaurante[1] = input("Digite o novo endereço: ").title()
            restaurante[2] = input("Digite o novo telefone: ")
            restaurante[3] = input("Digite o novo tempo de entrega: ")
            print(f"\n\033[92mRestaurante '{nome_restaurante}' editado com sucesso.\033[0m")
            return

    print(f"\n\033[91mRestaurante '{nome_restaurante}' não encontrado na lista.\033[0m")


def remover_restaurante(lista_de_restaurantes):
    """Função para remover um restaurante da lista de restaurantes"""
    counter = 0

    for restaurante in lista_de_restaurantes:
        print(f"\033[1mNome:\033[0m {restaurante[0]}")
        counter += 1

    nome_restaurante = input("\033[4mDigite o nome do restaurante que deseja remover\033[0m: ").title()

    # Varre a lista de restaurantes, comparando o nome de cada restaurante com o nome fornecido pelo input
    for restaurante in lista_de_restaurantes:
        if restaurante[0] == nome_restaurante:
            lista_de_restaurantes.remove(restaurante)
            print(f"\n\033[92mRestaurante '{nome_restaurante}' removido com sucesso.\033[0m")
            return

    print(f"\n\033[91mRestaurante '{nome_restaurante}' não encontrado na lista.\033[0m")


def editar_cardapio(lista_de_restaurantes):
    """Função principal referente a alterações no cardápio, utilizando um menu próprio"""
    counter = 1

    # Lista todos os restaurantes disponíveis e atribui-lhes uma chave(índice) para acesso
    for restaurante in lista_de_restaurantes:
        print(f"\033[1m{counter}\033[0m - {restaurante[0]}")
        counter += 1

    while True:
        resposta = input(f"Selecione o restaurante em que você deseja fazer alterações no cardápio [1, 2, 3,...]:\n").title()
        # Validação do input
        if resposta.isdigit():
            if 1 <= int(resposta) <= len(lista_de_restaurantes):
                resposta = int(resposta)
                resposta -= 1
                break
        else:
            print("\n\033[91mOPÇÃO INVÁLIDA. Tente novamente!\033[0m")

    # Após escolher o restaurante em que o usuário deseja realizar alterações no cardápio, ele deve escolher
    # o tipo de alteração que deseja realizar
    while True:
        resposta_crud = input(f'''\n\033[4mRestaurante selecionado\033[0m: \033[1m{lista_de_restaurantes[resposta][0]}\033[0m
    \033[4mEscolha uma das opções\033[0m:
        1 - Adicionar Prato
        2 - Editar Prato
        3 - Remover Prato
        4 - Voltar ao Menu Principal
        ''')

        if resposta_crud == "1":
            adicionar_prato(lista_de_restaurantes[resposta])
        elif resposta_crud == "2":
            if len(lista_de_restaurantes[resposta][4]) > 0:
                editar_prato(lista_de_restaurantes[resposta])
            else:
                print('\n\033[91mNão há pratos neste restaurante.\033[0m')
                return
        elif resposta_crud == "3":
            if len(lista_de_restaurantes[resposta][4]) > 0:
                remover_prato(lista_de_restaurantes[resposta])
            else:
                print('\n\033[91mNão há pratos neste restaurante.\033[0m')
                return

        # Retorna para o loop inicial da função menu()
        elif resposta_crud == "4":
            return

        else:
            print('\n\033[91mOPÇÃO INVÁLIDA. Digite 1, 2, 3 ou 4.\033[0m')


def adicionar_prato(restaurante):
    """Função para adicionar um prato ao cardápio do restaurante"""
    prato = input("Digite o nome do prato:\n").title()

    while True:
        preco = input("Digite o preço do prato:\n")
        # Validação do input como uma string que pode ser convertida para float
        if preco.replace('.', '', 1).isdigit() or preco.replace(',', '', 1).isdigit():
            if ',' in preco:
                preco = preco.replace(',', '.', 1)
            preco = float(preco)
            break

    restaurante[4].append([prato, preco])

    print(f"\n\033[92mO prato \"{prato}\" com o preço R${preco:.2f} foi adicionado ao cardápio com sucesso!\033[0m")


def editar_prato(restaurante):
    """Função para editar um prato do cardápio do restaurante"""
    print(f"\n\n\033[4mCardápio atual do restaurante {restaurante[0]}\033[0m:\n")
    counter = 1

    # Lista todos os pratos disponíveis no cardápio e atribui-lhes uma chave(índice) para acesso
    for elem in restaurante[4]:
        print(f"{counter} - {elem[0]}  - R${elem[1]:.2f}")
        counter += 1

    while True:
        resposta = input("Selecione o prato que você deseja editar:\n")
        if resposta.isdigit():
            # Validação do input como um int no range dos índices da lista
            if 1 <= int(resposta) <= len(restaurante[4]):
                resposta = int(resposta)
                resposta -= 1
                break

    print(f"Nome atual do prato: \"{restaurante[4][resposta][0]}\"")
    print(f"Preço atual do prato: \"{restaurante[4][resposta][1]:.2f}\"")

    nome = input("Novo nome para o prato:\n").title()

    while True:
        preco = input("Novo preço para o prato:\n")

        # Validação do input como uma string que pode ser convertida para float
        if preco.replace('.', '', 1).isdigit() or preco.replace(',', '', 1).isdigit():
            if ',' in preco:
                preco = preco.replace(',', '.', 1)
            preco = float(preco)
            break


    print(f"\n\n\033[92mO prato \"{restaurante[4][resposta][0]}\" - R${restaurante[4][resposta][1]} foi alterado para:\n\033[0m"
          f"{nome} -  R${preco:.2f}")

    restaurante[4][resposta][0] = nome
    restaurante[4][resposta][1] = preco


def remover_prato(restaurante):
    """Função para remover um prato do cardápio do restaurante"""
    print(f"\n\n\033[4mCardápio atual do restaurante {restaurante[0]}\033[0m:")
    counter = 1

    # Lista todos os pratos disponíveis no cardápio e atribui-lhes uma chave(índice) para acesso
    for elem in restaurante[4]:
        print(f"{counter} - {elem[0]} -  R${elem[1]:.2f}")
        counter += 1

    while True:
        resposta = input("Selecione o prato que você deseja remover:\n")
        if resposta.isdigit():
            # Validação do input como um int no range dos índices da lista
            if 1 <= int(resposta) <= len(restaurante[4]):
                resposta = int(resposta)
                resposta -= 1
                break

    print(f"\033[92mO prato {restaurante[4][resposta][0]} foi removido do cardápio com sucesso!\033[0m")
    restaurante[4].pop(resposta)


menu(lista_de_restaurantes)
