import os

restaurantes = [{'nome': 'Pizza', 'categoria': 'Italiana', 'ativo': False,},
                {'nome': 'Mr.Myiazaki', 'categoria': 'Japones', 'ativo':True},
                {'nome': 'Big Kahuna', 'categoria': 'Hamburger', 'ativo':True}]

def exibir_nome_do_programa():

    print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚█████╗░███████║██████╦╝██║░░██║██████╔╝
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")
    
def exibir_opcoes():
    '''Essa funcao é responsavel de exibir as opcaoes do menu'''
    print('1. Cadastrar restaurante')
    print('2. Listrar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair')

def cadastro_restaurante():
    ''' Essa funcão é responsavel por cadastrar um novo restaurante
    
    Inputs: - Nome do restaurante
            - Categoria
            
    Output: - Adiciona um novo restaurante a lista

    '''
    exibir_subtitulo('Cadastro de restaurante')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    voltar_menu_inicial()

def lista_restaurantes():
    '''Essa funcao é responsavel de mostra a lista de restaurantes cadastrados'''
    exibir_subtitulo('Lista de restaurantes cadastrados')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status ')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_menu_inicial()

def alternar_estado_restaurante():
    '''Essa funcao é responsavel para ativar e desativar o restaurante do app'''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alteranl o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_menu_inicial()

def finalizar_app():
    '''Essa funcao é responsavel para finalizar o app'''
    exibir_subtitulo('Finalizando app')

def exibir_subtitulo(texto):
    '''Exibir os nomes da funcoes'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_menu_inicial():
    '''Funcao retorna ao menu'''
    input('\nAperte "ENTER" para voltar ao menu principal ')
    main()

def opcao_invalida():
    ''' Funcao de invalides de resposta e retorno ao menu'''
    print('Opcao invalida!\n')
    voltar_menu_inicial()

def escolher_opcao():
    '''Execuçao de funcoes'''
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))
        if opcao_escolhida == 1:
            cadastro_restaurante()
        elif opcao_escolhida == 2:
            lista_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Funcao pricipal'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
