import
def mostrar_menu():
    print("------Menu------")
    print('1.Cadastrar novo jogo')
    print('2.Listar todos os jogos')
    print("3.Buscar um jogo")
    print('4.Remover um jogo')
    print('5.Sair do programa')
def Cadastrar_novo_jogo():
    id_jogo=input('DIgite o ID do Jogo: ')
    nome_jogo=input('Digite o nome do jogo:')
    autor_jogo=input('Digite o nome do autor do jogo:')
    nome_arquivo='jogos_video_game'
    with open(nome_arquivo, 'a', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow([id_jogo, nome_jogo, autor_jogo])
    
def Listar_todos_os_jogos():
    print(' Ainda não esta pronto')
def Buscar_um_jogo():
    print('Ainda não esta completo')
def Remover_um_jogo():
    print('Ainda não esta completo')

def menu():
    while True:
        mostrar_menu()
        escolha =input('Escolha uma opção de 1-5:')
        if escolha =='1':
            Cadastrar_novo_jogo()
        elif escolha == '2':
            Listar_todos_os_jogos()
        elif escolha == '3':
            Buscar_um_jogo()
        elif escolha == '4':
            Remover_um_jogo()
        elif escolha == '5':
            print("Saindo do programa...")
            break
        else:
            print("Escolha inválida, por favor tente novamente.")
        
menu()