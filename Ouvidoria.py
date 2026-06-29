'''
Aluno: Rafael Ribeiro
Matricula: (RA: 2615130028)
Curso: Ciencias da Computação
'''
ouvidoria=[]
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
    numero=int(input("Digite qual a sua opcao: "))
    if numero==1:
        if len(ouvidoria)==0:
            print("\n--- Não possuimos reclamações no sistema ---")
        elif len(ouvidoria)>=1:
            print('--- Temos as seguintes reclamações:---')
            for item in range(len(ouvidoria)):
                print('- (',item +1,') -', ouvidoria[item])
    elif numero==2:
        novareclamacao = input('Digite sua reclamação ')
        ouvidoria.append(novareclamacao)
        print('---Sua reclamação foi adicionada com sucesso---')
    elif numero==3:
        codigo = int(input('digite numero do codigo que deseja pesquisar '))
        if codigo <= len(ouvidoria) and codigo > 0:
            print('reclamação do codigo', codigo, 'é a seguinte:', ouvidoria[codigo - 1])
        else:
            print('Codigo invalido ou não existe')
    elif numero==4:
        atualizarcod = int(input('\n---Digite o codigo da reclamação que deseja atualizar: '))
        if atualizarcod > 0 and atualizarcod <= len(ouvidoria):
            atualizacao = input('\n---Digite a atualizacao da reclamação: ')
            ouvidoria[atualizarcod-1] = atualizacao
            print('\nCodigo(',atualizarcod,')atualizado com sucesso')
        else:
            print('\n---Codigo invalido ou não existe---')
    elif numero==5:
        excluir = int(input('Digite o codigo da reclamação que deseja excluir '))
        if excluir > 0 and excluir <= len(ouvidoria):
            ouvidoria.pop(excluir -1)
            print('\n--- Reclamação excluida com sucesso ---')
        else:
            print('\n--- Codigo invalido ou nao existe---')
    elif numero==6:
        print('\n--- Existem um total de',len(ouvidoria),'reclamação(ões) ---')
    elif numero==7:
        print('\n--- Obrigado por usar o APP ---')
        break
    else:
        print('\n--- Codigo invalido ou nao existe ---')
