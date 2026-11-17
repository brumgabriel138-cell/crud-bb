from crud_funçoes.atualizar import atualizar
from crud_funçoes.cadastrar import cadastrar
from crud_funçoes.excluir import excluir
from interface.interfaces import menu
from banco_de_dados.conexao import conectar

conexao = conectar()
cursor = conexao.cursor()
personagens = []

def main():
    while True:
        opcao = menu()

        if opcao == '1':
            cadastrar(cursor, conexao)

        elif opcao == '2':
            print(f'{'=-=-=-= PERSONAGENS =-=-=-=':.^60}')
            
            cursor.execute("select * from personagens order by nivel desc")
            
            resultado = cursor.fetchall()

            print(f'{"NOME":^16} | {"CLASSE":^22} | {"NÍVEL":^13}')
            
            for lista_personagens in resultado:
                print(f'-{lista_personagens[1]:^15}- -{lista_personagens[2]:^22}- -{str(lista_personagens[3]):^12}-')

        elif opcao == '3':
            atualizar(cursor, conexao)

        elif opcao == '4':
            excluir(cursor, conexao)

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

if __name__ == "__main__":
    main()