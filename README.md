# Sistema de Autenticação

Este é um sistema de autenticação simples desenvolvido em Python que permite a criação de novos usuários, exibição dos usuários registrados, e login no sistema. Ele utiliza um menu interativo para facilitar a navegação e execução das funções básicas.

## Funcionalidades

- **Criar Novo Usuário:** Permite criar novos usuários informando um nome completo e uma senha de 6 dígitos.
- **Exibir Usuários:** Exibe a lista de todos os usuários registrados no sistema.
- **Entrar no Sistema:** Permite que um usuário autenticado acesse o sistema.
- **Sair:** Fecha o sistema de autenticação.

## Estrutura do Projeto

- `print_header()`: Exibe o cabeçalho do sistema.
- `print_menu()`: Exibe o menu de opções para o usuário.
- `criar_usuario()`: Permite a criação de um novo usuário com nome completo e senha de 6 dígitos.
- `exibir_usuarios()`: Mostra todos os usuários registrados com suas respectivas senhas.
- `autenticar_usuario(usuario, senha)`: Função para validar as credenciais de um usuário.
- `entrar_sistema()`: Solicita o login de um usuário e verifica se as credenciais estão corretas.

## Como Usar

1. Clone este repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
   Execute o script principal:
   python main.py

Use o menu interativo para as operações disponíveis:
1: Criar novo usuário
2: Exibir usuários
3: Entrar no sistema
4: Sair

## Requisitos
Python 3.6 ou superior
## Observações
A senha deve conter exatamente 6 dígitos para ser aceita no sistema.
As senhas são exibidas ao listar os usuários; uma melhoria seria ocultar as senhas para garantir a privacidade.

## Melhorias Futuras
Ocultar senhas: Alterar a exibição para que as senhas não sejam mostradas ao listar usuários.
Validação de Entrada: Implementar validações mais robustas para a criação de senhas e usuários.
Persistência de Dados: Salvar os usuários em um banco de dados ou arquivo para manter os registros após o encerramento do programa.

## Contribuição
Contribuições são bem-vindas! Se encontrar problemas ou tiver sugestões, abra uma issue ou pull request.
