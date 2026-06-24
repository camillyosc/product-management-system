def mostrarmenu():
    print ('''
        1 - Adicionar produto  
        2 - Listar produtos  
        3 - Buscar produto pelo nome  
        4 - Editar quantidade ou preço de um produto  
        5 - Sair
''')


produtos = []
escolha = 0

while escolha != 5:
    
    mostrarmenu()

    try:
        escolha= int(input('Escolha uma das opções do menu:'))
    except ValueError:
        print('Erro! Digite apenas números:')
        escolha = 0


    if escolha == 1:
        nome_produto = input('Digite o nome do produto:').lower()

        while True:
            try:
                quantidade_produto = int(input('Digite a quantidade:'))
                preço_produto = float(input('Digite o preço do produto:'))
                produtos_internos = [nome_produto, quantidade_produto, preço_produto]
                produtos.append(produtos_internos)
                break

            except ValueError:
                print('Erro! Digite apenas números! Digite novamente:')

    if escolha == 2:
        if not produtos:
            print('Não possui produtos cadastrados!')
        else:
            for p in produtos:
                nome_produto = p[0]
                quantidade_produto = p[1]
                preço_produto = p[2]
                
                print(f'Nome {nome_produto} | Quantidade: {quantidade_produto} | Preço: R${preço_produto:.2f}')

    
    if escolha == 3:
        nome_produto = input('Digite o nome do produto que você quer buscar suas informações:').lower()
        encontrado = False
        for p in produtos:
            nome_produto_lista = p[0]

            if nome_produto == nome_produto_lista:
                quantidade_produto = p[1]
                preço_produto = p[2]

                print(f'A quantidade disponível é de {quantidade_produto}')
                print(f'E o preço dele é R${preço_produto:.2f}') 
                encontrado = True
                break
                
        if not encontrado: 
                print('Produto não encontrado.')

    
    if escolha == 4:
        nome_produto=input('Digite o nome do produto que você quer editar:').lower()
        encontrado = False
        for p in produtos:
            nome_produto_lista = p[0]

            if nome_produto == nome_produto_lista:
                alterar_quantidade = input('Deseja alterar a quantidade? S/N').lower()
                if alterar_quantidade == 's':
                    while True:
                        try:
                            nova_quantidade = int(input('Digite a nova quantidade:'))
                            p[1] = nova_quantidade
                            print(f'A nova quantidade é {nova_quantidade}')
                            break
                        except ValueError:
                            print('Erro! Digite apenas números.')
       
                

                alterarpreço = input('Deseja alterar o preço? S/N').lower()
                if alterarpreço == 's':
                    while True:
                        try:
                            novo_preço = float(input('Digite o novo preço:'))
                            p[2] = novo_preço
                            print(f'O novo preço é {novo_preço:.2f}')
                            break
                        except ValueError:
                            print('Erro! Digite apenas números.')

                encontrado = True
                break

        if not encontrado:
            print('Produto não cadastrado!')

    if escolha == 5:
        print('Saindo do programa...')

print('O programa está sendo encerrado.')
                



    



