def excluir(cursor, conexao):

    cursor.execute("select * from personagens order by nivel desc")

    resultado = cursor.fetchall()

    if not resultado:
        print('Nenhum personagem encontrado!')
        return

    print(f'{"NOME":^16} | {"CLASSE":^22} | {"NÍVEL":^13}')

    for lista_personagens in resultado:
        print(f'-{lista_personagens[1]:^15}- -{lista_personagens[2]:^22}- -{str(lista_personagens[3]):^12}-')

    nome = input('Qual personagem deseja excluir? ').strip().lower()

    if not nome:
        print('Erro: o nome não pode ficar vazio!')
        return

    cursor.execute("delete from personagens where lower(nome) = (%s) ", (nome,))

    if cursor.rowcount > 0:
        print('Personagem excluido com sucesso!')

    else:
        print('Personagem nao encontrado.')

    conexao.commit()

