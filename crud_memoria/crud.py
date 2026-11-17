from utils import (cadastrar, excluir, atualizar, menu)

personagens = []

while True:
    opcao = menu()

    if opcao == '1':
        cadastrar(personagens)

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
            atualizar(personagens)

    elif opcao == '4':
        if len(personagens) == 0:
            print('Nenhum personagem encontrado!')
        else:
            excluir(personagens)

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