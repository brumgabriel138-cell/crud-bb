
def cadastrar(personagens):
    print('=-=' * 10)

    nome = input('Digite o nome: ').strip()

    if not nome:
        print('Erro: o nome não pode ficar vazio!')
        return

    classe = input('Digite a classe: ').strip()

    if not classe:
        print('Erro: a classe não pode ficar vazia!')
        return

    try:
        nivel = int(input('Digite o nível: ').strip())

        if nivel < 0:
            print('Erro: o nível não pode ser negativo!')
            return

    except ValueError:
        print('Erro: o nível precisa ser um número inteiro!')
        return

    persona = {
        'nome': nome,
        'classe': classe,
        'nivel': nivel
    }

    personagens.append(persona)
    print('Personagem cadastrado com sucesso!')


def atualizar(personagens):
    print('=-=' * 10)

    for persona in personagens:
        print(f'{persona["nome"]:^15}')

    att = input('Qual personagem deseja alterar? ').strip().lower()

    for persona in personagens:
        if persona['nome'].lower() == att:
            campo = input('O que você deseja mudar? ').strip().lower()

            if campo in ['nivel', 'level', 'xp']:
                try:
                    nivel = int(input('Digite o novo nível: ').strip())

                    if nivel < 0:
                        print('Erro: o nível não pode ser negativo!')
                    else:
                        persona['nivel'] = nivel
                        print('Nível alterado com sucesso!')

                except ValueError:
                    print('Erro: o nível precisa ser um número inteiro!')

            elif campo == 'classe':
                classe = input('Digite a nova classe: ').strip()

                if not classe:
                    print('Erro: a classe não pode ficar vazia!')
                else:
                    persona['classe'] = classe
                    print('Classe alterada com sucesso!')

            elif campo == 'nome':
                nome = input('Digite o novo nome: ').strip()

                if not nome:
                    print('Erro: o nome não pode ficar vazio!')
                else:
                    persona['nome'] = nome
                    print('Nome alterado com sucesso!')

            else:
                print('Erro: campo inválido!')

            return

    print('Erro: personagem não encontrado!')


def excluir(personagens):
    print('=-=' * 10)

    if not personagens:
        print('Nenhum personagem encontrado!')
        return

    for persona in personagens:
        print(f'{persona["nome"]:^15}')

    nome = input('Qual personagem deseja excluir? ').strip().lower()

    if not nome:
        print('Erro: o nome não pode ficar vazio!')
        return

    for persona in personagens:
        if persona['nome'].lower() == nome:
            personagens.remove(persona)
            print('Excluído com sucesso!')
            return

    print('Personagem não encontrado!')


def menu():
    print('=== PERSONAGENS ===')
    print('1 - Cadastrar')
    print('2 - Listar personagens')
    print('3 - Atualizar personagem')
    print('4 - Excluir personagem')
    print('5 - Encerrar')

    return input('Escolha a opção: ').strip()
