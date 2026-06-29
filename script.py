lista=[]
while True:
    print('(1)lista \n----------\n(2)adicionar \n---------- \n(3)quantidade \n---------- \n(4)remover \n----------\n(5)substituir \n----------\n(6)sair')
    numero=int(input('Digite um numero: '))
    if numero==1:
       if len(lista)>0:
           for item in lista:
               print('-',item)
       else:
           print('Sem filmes no momento')
    elif numero==2:
        novo=input('Digite o nome do filme: ')
        lista.append(novo)
        print('-',novo,'foi adicionado com sucesso')
    elif numero==3:
        print('Temos',len(lista),'filmes no momento')
    elif numero==4:
        lixo = input('Digite a posicao do filme: ')
        if lixo >=1 and lixo<=len(lista):
            lista.pop(lixo -1)
            print('-',lixo,'foi removido com sucesso')
        else:
            print('Sem filmes no momento')

