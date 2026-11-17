def cadastrar(cursor, conexao):
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

    cursor.execute("insert into personagens (nome, class, nivel) values (%s, %s, %s)", (nome, classe, nivel))

    conexao.commit()

    print('Personagem cadastrado com sucesso!')