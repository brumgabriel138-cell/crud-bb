def atualizar(cursor, conexao):

    cursor.execute("select * from personagens order by nivel desc")
        
    resultado = cursor.fetchall()    
    
    if not resultado:
            print('nenhum personagem encontrado')
            return

    print(f'{'=-=-=-= PERSONAGENS =-=-=-=':.^60}')

    print(f'{"NOME":^16} | {"CLASSE":^22} | {"NÍVEL":^13}')

    for lista_personagens in resultado:
        print(f'-{lista_personagens[1]:^15}- -{lista_personagens[2]:^22}- -{str(lista_personagens[3]):^12}-')

    att = input('Qual personagem deseja alterar? ').strip().lower()

    for persona in resultado:
        if persona[1].lower() == att:
            campo = input('O que você deseja mudar? ').strip().lower()

            if campo in ['nivel', 'level', 'xp']:
                try:
                    nivel = int(input('Digite o novo nível: ').strip())

                    if nivel < 0:
                        print('Erro: o nível não pode ser negativo!')
                    else:
                        cursor.execute("update personagens set nivel = (%s) where lower(nome) = (%s)", (nivel, att))
                        
                        if cursor.rowcount > 0:
                            print('Nível alterado com sucesso!')

                        else:
                            print('nenhum personagem encontrado.')

                        conexao.commit()

                except ValueError:
                    print('Erro: o nível precisa ser um número inteiro!')

            elif campo == 'classe':
                classe = input('Digite a nova classe: ').strip()

                if not classe:
                    print('Erro: a classe não pode ficar vazia!')
                else:
                    cursor.execute("update personagens set class = (%s) where lower(nome) = (%s)", (classe, att))

                    if cursor.rowcount > 0:
                        print('Classe alterada com sucesso!')

                    else:
                        print('nenhum personagem encontrado.')

                    conexao.commit()

            elif campo == 'nome':
                nome = input('Digite o novo nome: ').strip()

                if not nome:
                    print('Erro: o nome não pode ficar vazio!')
                else:
                    cursor.execute("update personagens set nome = (%s) where lower(nome) = (%s)", (nome, att))

                    if cursor.rowcount > 0:
                        print('Nome alterado com sucesso!')

                    else:
                        print('nenhum personagem encontrado.')

                    conexao.commit()

            else:
                print('Erro: campo inválido!')

            return

    print('Erro: personagem não encontrado!')