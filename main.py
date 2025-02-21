import os

chamados = []
contador_id = 1

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def topbar(text):
    print(f"-+-+- {text} -+-+-")

def cadastrar_chamado(descricao, prioridade):
    global contador_id
    chamado = {
        'id': contador_id,
        'descricao': descricao,
        'prioridade': prioridade,
        'status': 'Aberto',
    }
    chamados.append(chamado)
    contador_id += 1
    print(f'Chamado {chamado['id']} inserido!')


def buscar_chamado(termo):
    resultado = []
    for i in chamados:
        if termo == str(i['id']) or termo.lower() in i['descricao'].lower():
            resultado.append(i)
    if resultado:
        for c in resultado:
            print(
                f'ID: {c['id']}, Descrição: {c['descricao']}, Prioridade: {c['prioridade']}, Status: {c['status']}')
    else:
        print('Nenhum chamado encontrado...')


def remover_chamado(id_chamado):
    for i in chamados:
        if i['id'] == id_chamado:
            print(f'Chamado encontrado: \n{i}\n\nConfirma a remoção?\nDigite "S" para confirmar: ')
            chamados.remove(i)
            print(f'Chamado {id_chamado} removido!')
            return
    print(f'chamado {id_chamado} não encontrado')


def listar_chamados():
    if not chamados:
        print('Nenhum chamado cadastrado.')
    else:
        for c in sorted(chamados, key=lambda x: x['prioridade']):
            print(
                f'ID: {c['id']}, Descrição: {c['descricao']}, Prioridade: {['Alta','Média','Baixa'][c['prioridade']-1]}, Status: {c['status']}')


def exibir_estatisticas():
    abertos = 0
    for i in chamados:
        if i['status'] == 'Aberto':
            abertos += 1
    finalizados = len(chamados) - abertos
    print(
        f'Total: {len(chamados)}, Chamados abertos: {abertos}, Chamados finalizados: {finalizados}')


def reverter_lista():
    chamados.reverse()
    print('Lista revertida!')


def limpar_lista():
    chamados.clear()
    print("Lista limpa!")


def finalizar_chamado(id_finalizar):
    for i in chamados:
        if i['id'] == id_finalizar:
            i['status'] = 'finalizado'
            cls()
            topbar('Finalizar Chamados')
            print(f'Chamado {id_finalizar} finalizado!')
            input('Pressione qualquer tecla para continuar...')
            return
    cls()
    topbar('Finalizar Chamados')
    print(f'Chamado {id_finalizar} não encontrado')
    input('Pressione qualquer tecla para continuar...')

while True:
    cls()
    print("-+-+- Sistema de Chamados -+-+-")
    print("1. Cadastrar Chamado")
    print("2. Buscar Chamado")
    print("3. Remover Chamado")
    print("4. Listar Chamados")
    print("5. Exibir Estatísticas")
    print("6. Inverter Lista de Chamados")
    print("7. Limpar Chamados")
    print("8. Finalizar Chamado")
    print("0. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cls()
        topbar('Cadastro de Chamado')
        descricao = input('Descrição: ')
        prioridade = int(input('Prioridade 1-3 (1 é maior e 3 menor): '))
        if prioridade not in [1,2,3]:
            print("Por favor, siga os padrões de resposta.")
            input('Pressione qualquer tecla para continuar...')
            continue
        cls()
        topbar('Cadastro de Chamado')
        print(f'Confirma estes dados?\nDescrição: {descricao}\nPrioridade: {['Alta','Média','Baixa'][prioridade-1]} ({prioridade})')
        _b = input('Pressione qualquer tecla para confirmar, ou 0 para cancelar...')
        if _b == '0':
            continue
        cadastrar_chamado(descricao, prioridade)
        cls()
        topbar('Cadastro de Chamado')
        print('Chamado cadastrado com sucesso!')
        input('Pressione qualquer tecla para continuar...')
    elif opcao == '2':
        cls()
        topbar('Buscar Chamado')
        termo = input('Digite ID ou descrição: ')
        cls()
        topbar('Buscar Chamado')
        buscar_chamado(termo)
        input('Pressione qualquer tecla para continuar...')
        
    elif opcao == '3':
        cls()
        topbar('Buscar Chamado')
        id_chamado = int(input('Digite o ID do chamado para remover: '))
        remover_chamado(id_chamado)
        cls()
        topbar('Remover Chamado')
        input('Pressione qualquer tecla para continuar...')
    elif opcao == '4':
        cls()
        topbar('Lista de Chamados')
        listar_chamados()
        input('Pressione qualquer tecla para continuar...')
    elif opcao == '5':
        cls()
        topbar('Estatísticas')
        exibir_estatisticas()
        input('Pressione qualquer tecla para continuar...')
    elif opcao == '6':
        cls()
        topbar('Inverter Lista de Chamados')
        reverter_lista()
        input('Pressione qualquer tecla para continuar...')
    elif opcao == '7':
        cls()
        topbar('Limpar Chamados')
        desicao = input("Gostaria de limpar a lista de chamados? (S/N): ")
        if desicao.lower() == 's':
            limpar_lista()
            cls()
            topbar('Limpar Chamados')
            print('Lista de chamados limpa!')
            input('Pressione qualquer tecla para continuar...')
        elif desicao.lower() == 'n':
            cls()
            topbar('Limpar Chamados')
            print('Ação cancelada!')
            input('Pressione qualquer tecla para continuar...')
            continue
    elif opcao == '8':
        cls()
        topbar('Finalizar Chamados')
        id_finalizar = int(input("Digite o ID do chamado para finalizar: "))
        finalizar_chamado(id_finalizar)
    elif opcao == '0':
        print('Saindo...')
        break
    else:
        cls()
        topbar('Opção inválida')
        print('Por favor digite uma das opções válidas no menu.\n')
        input('Pressione qualquer tecla para continuar...')
