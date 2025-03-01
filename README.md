# Autenticação Flask com Docker

Esta é uma aplicação web desenvolvida com Flask que implementa autenticação de usuários utilizando Flask-Login, permitindo criar e ler registros de usuários. Os dados são persistidos em um container MySQL, e toda a aplicação está completamente dockerizada.

Esta aplicação faz parte de uma demonstração prática sobre containers com Docker. Para acessar a apresentação completa, visite: [Introdução aos Containers com Docker](https://carlosmoreir4.notion.site/Introdu-o-aos-Containers-com-Docker-1a6ffe98424c8062b178c1a48253c3a9?pvs=4).


## Conteúdo do Projeto

- **Aplicação Flask**
  - Implementação de autenticação com **Flask-Login**.
  - Criação e gerenciamento de usuários com senha criptografada via **bcrypt**.
  - Rotas para _login_, _registro_, _perfil_ e _logout_.

- **Banco de Dados**
  - Persistência de dados com **MySQL** em container.
  - Configuração da conexão via SQLAlchemy.

- **Dockerização**
  - **Dockerfile** para criação da imagem da aplicação.
  - **docker-compose.yml** para orquestração dos containers (aplicação e banco de dados).
  - **.dockerignore** para otimizar o processo de build, excluindo arquivos e pastas desnecessários.


## Pré-Requisitos

- **Docker** e **Docker Compose** instalados.

## Como Executar

- **Configure as Variáveis de Ambiente:**
    - Crie um arquivo `.env` na raiz do projeto com as configurações baseado no arquivo `.env.example`.

- **Build e Início dos Containers:**
  - Execute o comando abaixo para construir e iniciar os containers:
  ```bash
  docker-compose up --build
  ```

- **Acesso à Aplicação:**
   - Após o build e a inicialização dos containers, acesse a aplicação pelo navegador em: [http://localhost:5000](http://localhost:5000).

