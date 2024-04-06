def print_header():
    print("=" * 50)
    print("{:^50}".format("SISTEMA DE AUTENTICAÇÃO"))
    print("=" * 50)
    print()

def print_menu():
    print("1. Criar novo usuário")
    print("2. Exibir usuários")
    print("3. Entrar no sistema")
    print("4. Sair")

def criar_usuario():
    novo_usuario = input("Digite o nome completo do usuário: ")
    senha = input("Digite a senha: ")
    if len(senha) != 6:
        print("A senha deve conter apenas 6 dígitos.")
        senha = input("Digite a senha novamente: ")
    usuarios[novo_usuario] = senha

def exibir_usuarios():
    print("Usuários registrados:")
    for usuario, senha in usuarios.items():
        print(f"Usuário: {usuario}, Senha: {senha}")

def autenticar_usuario(usuario, senha):
    if usuario in usuarios and usuarios[usuario] == senha:
        return True
    else:
        return False

def entrar_sistema():
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    if autenticar_usuario(usuario, senha):
        print("=" * 50)
        print("{:^50}".format("ENTROU NO SISTEMA"))
        print("=" * 50)
        print()
    else:
        print("VOCÊ NÃO TEM AUTORIZAÇÃO PARA ENTRAR NO SISTEMA")

usuarios = {}

print_header()
print("Bem-vindo ao sistema de autenticação!")

while True:
    print_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_usuario()
    elif opcao == "2":
        exibir_usuarios()
    elif opcao == "3":
        entrar_sistema()
    elif opcao == "4":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
