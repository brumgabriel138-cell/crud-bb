personagens = []


def cadastrar():
    print('=-=' * 10)

    persona = {}
    persona['nome'] = str(input('Digite o nome: ').strip())

    if not persona['nome']:
        print('Erro: o nome não pode ficar vazio!')
        return

    persona['classe'] = str(input('Digite a classe: ').strip())

    if not persona['classe']:
        print('Erro: a classe não pode ficar vazia!')
        return

    try:
        persona['nivel'] = int(input('Digite o nível: ').strip())

        if persona['nivel'] < 0:
            print('Erro: o nível não pode ser negativo!')
            return

    except ValueError:
        print('Erro: o nível precisa ser um número inteiro!')
        return

    personagens.append(persona)
    print('Personagem cadastrado com sucesso!')


def atualizar():
    print('=-=' * 10)

    for personas in personagens:
        print(f'{personas["nome"]:^15}')

    att = str(input('Qual personagem deseja alterar? ').strip().lower())

    encontrado = False

    for personas in personagens:
        if personas['nome'].lower() == att:
            encontrado = True

            v = str(input('O que você deseja mudar no personagem? ').strip().lower())

            if v in ['nivel', 'level', 'xp']:
                try:
                    nivel = int(input('Digite o novo nível: ').strip())

                    if nivel < 0:
                        print('Erro: o nível não pode ser negativo!')
                    else:
                        personas['nivel'] = nivel
                        print('Nível alterado com sucesso!')

                except ValueError:
                    print('Erro: o nível precisa ser um número inteiro!')

            elif v == 'classe':
                classe = str(input('Digite a nova classe: ').strip())

                if not classe:
                    print('Erro: a classe não pode ficar vazia!')
                else:
                    personas['classe'] = classe
                    print('Classe alterada com sucesso!')

            elif v == 'nome':
                nome = str(input('Digite o novo nome: ').strip())

                if not nome:
                    print('Erro: o nome não pode ficar vazio!')
                else:
                    personas['nome'] = nome
                    print('Nome alterado com sucesso!')

            else:
                print('Erro: campo inválido! Escolha nome, classe ou nivel.')

            break

    if not encontrado:
        print('Erro: personagem não encontrado!')


def excluir():
    print('=-=' * 10)

    if len(personagens) == 0:
        print('Nenhum personagem encontrado!')
    else:
        encontrado = False

        for personas in personagens:
            print(f'{personas["nome"]:^15}')

        x = str(input('Qual personagem deseja excluir? ').strip().lower())

        if not x:
            print('Erro: o nome não pode ficar vazio!')
            return

        for personas in personagens:
            if personas['nome'].lower() == x:
                encontrado = True
                personagens.remove(personas)
                break

        if encontrado:
            print('Excluído com sucesso!')
        else:
            print('Personagem não encontrado!')


def menu():
    print('=== PERSONAGENS ===')
    print('1 - Cadastrar')
    print('2 - Listar personagens')
    print('3 - Atualizar personagem')
    print('4 - Excluir personagem')
    print('5 - Encerrar')

    return str(input('Escolha a opção: ').strip())


while True:
    opcao = menu()

    if opcao == '1':
        cadastrar()

    elif opcao == '2':
        if len(personagens) == 0:
            print('Nenhum personagem encontrado!')
        else:
            print(f'{"NOME":^15} {"CLASSE":^15} {"NÍVEL":^15}')

            for persona in personagens:
                print(
                    f'{persona["nome"]:^15} '
                    f'{persona["classe"]:^15} '
                    f'{persona["nivel"]:^15}'
                )

    elif opcao == '3':
        if len(personagens) == 0:
            print('Nenhum personagem encontrado!')
        else:
            atualizar()

    elif opcao == '4':
        if len(personagens) == 0:
            print('Nenhum personagem encontrado!')
        else:
            excluir()

    elif opcao == '5':
        print('Bye bye!')
        break

    else:
        print('Opção inválida!')
        continue

    while True:
        voltar = str(input('Deseja voltar ao menu? [S/N]: ').strip().upper())

        if voltar in ['S', 'SIM']:
            break

        elif voltar in ['N', 'NAO', 'NÃO']:
            print('Bye bye!')
            break

        else:
            print('Resposta inválida! Digite S ou N.')

    if voltar in ['N', 'NAO', 'NÃO']:
        break