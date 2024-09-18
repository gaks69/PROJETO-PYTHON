import csv #Importar CSV local
def mostrar_menu():# Função de mostar o menu
    print("------Menu------")
    print('1.Cadastrar novo jogo')
    print('2.Listar todos os jogos')
    print("3.Buscar um jogo")
    print('4.Remover um jogo')
    print('5.Sair do programa')
def Cadastrar_novo_jogo(): #Função para cadastar um jogo dentro do arquivo csv local
    id_jogo=input('Digite o ID do Jogo: ') #Input para receber o Id do Jogo
    nome_jogo=input('Digite o nome do jogo:') #Input para receber o nome do Jogo
    autor_jogo=input('Digite o nome do autor do jogo:') #Input para receber o nome do Autor do Jogo
    nome_arquivo='jogos_video_game.csv ' # Atribui o a variavel nome_arquivo para o csv local
    with open(nome_arquivo, 'a', newline='', encoding='utf-8') as arquivo_csv: #esta linha faz com que o csv seja aberto em modo append , que adicione o que voce escrever ao final do arquivo , sem apagar os outros dados 
        escritor = csv.writer(arquivo_csv)#Atribui a variavel escritor sendo o 'escritor' do arquivo local
        escritor.writerow([id_jogo, nome_jogo, autor_jogo])# Faz com que a variavel escritor declarada acima , utilize a função writerow , que escreve uma linha no arquivo csv conforme os parametros inseridos
    
def Listar_todos_os_jogos(): #Função para istar todos os jogos dentro do arquivo csv local
    nome_arquivo='jogos_video_game.csv' # Atribui o a variavel nome_arquivo para o csv local
    with open(nome_arquivo,'r',newline='',encoding='utf-8') as arquivo_csv: #esta linha faz com que o csv seja aberto em modo reader , que apenas le os componentes dentro do arquivo
        leitor = csv.reader(arquivo_csv)# Atribui a variavel leitor sendo o 'leitor' do arquivo atribuido
        jogos = list(leitor)#Atribui a variavel jogos uma listagem de todos os componentes da variavel leitor
        if jogos:
             print("---- Lista de Jogos ----")
             for jogo in jogos:
                print(f'ID: {jogo[0]},Nome: {jogo[1]},Autor: {jogo[2]}')
        else:
             print('Nenhum jogo foi cadastrado')
def Buscar_um_jogo():
    id_jogo=input('Digite o ID do jogo que você quer achar:')
    nome_arquivo='jogos_video_game.csv'
    with open(nome_arquivo,'r',encoding='utf-8') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        encontrado=False
        for jogo in leitor:
            if jogo[0] == id_jogo:
                print(f'Jogo encontrado!:ID: {jogo[0]}, Nome: {jogo[1]}, Autor:{jogo[2]} ')
                encontrado = True
                break
        if not encontrado:
            print('Infelizmente o jogo procurado não foi econtrado :(')


def Remover_um_jogo():
    id_jogo=input('Digite o ID do jogo que você quer excluir:')
    nome_arquivo='jogos_video_game.csv'
    with open(nome_arquivo,'r',encoding='utf-8') as arquivo_csv:
        jogos=list(csv.reader(arquivo_csv))
    with open(nome_arquivo,'w',newline='',encoding='utf-8') as arquivo_csv:
        escritor=csv.writer(arquivo_csv)
        removido= False
        for jogo in jogos:
            if jogo[0] != id_jogo:
                escritor.writerow(jogo)
            else:
                removido=True
        if removido:
            print(f'O jogo com ID:{jogo[0]} foi removido com sucesso!')
        else:
            print('O jogo não foi econtrado!')


            




def menu(): #Função que da funcionalidade ao menu
    while True:
        mostrar_menu()
        escolha =input('Escolha uma opção de 1-5:')
        if escolha =='1':
            Cadastrar_novo_jogo()#chama a função do numero 1
        elif escolha == '2':
            Listar_todos_os_jogos()#chama a função do numero 2 
        elif escolha == '3':
            Buscar_um_jogo()#chama a função do numero 3
        elif escolha == '4':
            Remover_um_jogo()#chama a função do numero 4 
        elif escolha == '5':
            print("Saindo do programa...")
            break# para a função , ou seja , sai do programa
        else:
            print("Escolha inválida, por favor tente novamente.")#Mostre que se nenhuma das opções do menu forem escolhidas , uma mensagem sera mostrada e o menu aparecera novamente
        
menu()