'''
Aluno: Rafael Ribeiro
Matricula: (RA: 2615130028)
Curso: Ciencias da Computação
'''
from operacoesbd import *

def listar_reclamacoes(conexao):
    sql = "SELECT codigo, descricao FROM ouvidoria"
    resultado = listarBancoDados(conexao, sql)

    if not resultado:
        print("\n--- Não possuimos reclamações no sistema ---")
    else:
        print('\n--- Temos as seguintes reclamações:---')
        print(f"{'CÓDIGO':<8} | {'RECLAMAÇÃO'}")
        print("-" * 40)
        for linha in resultado:
            print(f"- ({linha[0]}) - | {linha[1]}")


def registrar_reclamacao(conexao):
    novareclamacao = input('Digite sua reclamação: ')

    sql = "INSERT INTO ouvidoria (descricao) VALUES (%s)"
    dados = (novareclamacao,)

    insertNoBancoDados(conexao, sql, dados)
    print('---Sua reclamação foi adicionada com sucesso---')


def pesquisar_reclamacao(conexao):
    codigo = int(input('Digite o número do código que deseja pesquisar: '))

    sql = "SELECT codigo, descricao FROM ouvidoria WHERE codigo = %s"
    dados = [codigo]
    resultado = listarBancoDados(conexao, sql, dados)

    if resultado:
        linha = resultado[0]
        print('Reclamação do código', codigo, 'é a seguinte:', linha[1])
    else:
        print('Código inválido ou não existe')


def atualizar_reclamacao(conexao):
    atualizarcod = int(input('\n---Digite o código da reclamação que deseja atualizar: '))

    sql_busca = "SELECT codigo FROM ouvidoria WHERE codigo = %s"
    if listarBancoDados(conexao, sql_busca, [atualizarcod]):
        atualizacao = input('\n---Digite a atualização da reclamação: ')
        sql = "UPDATE ouvidoria SET descricao = %s WHERE codigo = %s"
        dados = (atualizacao, atualizarcod)

        insertNoBancoDados(conexao, sql, dados)
        print('\nCódigo (', atualizarcod, ') atualizado com sucesso')
    else:
        print('\n---Código inválido ou não existe---')


def remover_reclamacao(conexao):
    excluir = int(input('Digite o código da reclamação que deseja excluir: '))

    sql_busca = "SELECT codigo FROM ouvidoria WHERE codigo = %s"
    if listarBancoDados(conexao, sql_busca, [excluir]):
        sql = "DELETE FROM ouvidoria WHERE codigo = %s"
        insertNoBancoDados(conexao, sql, [excluir])
        print('\n--- Reclamação excluída com sucesso ---')
    else:
        print('\n--- Código inválido ou não existe---')

def mostrar_quantidade(conexao):
    sql = "SELECT COUNT(*) FROM ouvidoria"
    resultado = listarBancoDados(conexao, sql)
    total = resultado[0][0]
    print('\n--- Existem um total de', total, 'reclamação(ões) ---')

conexao = criarConexao('localhost', 'root', 'rafa2000', 'teste')

if conexao is not None:
    while True:
        print("\n" + "=" * 30)
        print("   SISTEMA DE OUVIDORIA")
        print("=" * 30)
        print("(1). Listar reclamações")
        print("(2). Registrar nova reclamação")
        print("(3). Pesquisar reclamação pelo código")
        print("(4). Atualizar reclamação")
        print("(5). Remover reclamação")
        print("(6). Mostrar quantidade total de reclamações")
        print("(7). Sair do sistema")
        print("=" * 30)

        numero = int(input("Digite qual a sua opção: "))

        if numero == 1:
            listar_reclamacoes(conexao)
        elif numero == 2:
            registrar_reclamacao(conexao)
        elif numero == 3:
            pesquisar_reclamacao(conexao)
        elif numero == 4:
            with_check = atualizar_reclamacao(conexao)
        elif numero == 5:
            remover_reclamacao(conexao)
        elif numero == 6:
            mostrar_quantidade(conexao)
        elif numero == 7:
            print('\n--- Obrigado por usar o APP ---')
            encerrarConexao(conexao)
            break
        else:
            print('\n--- Código inválido ou não existe ---')
else:
    print("Não foi possível conectar ao banco de dados MySQL.")