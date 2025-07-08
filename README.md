CRUD com Python, Flask e SQLite

Este é um projeto simples de CRUD (Create, Read, Update, Delete) feito com Python, Flask e SQLite, com interface web usando HTML e CSS.  
Foi criado como parte do meu aprendizado na área de desenvolvimento backend e está disponível no meu portfólio.

Funcionalidades

-  Cadastrar usuários (nome e e-mail)
-  Listar usuários
-  Editar dados de um usuário
-  Deletar usuário

Tecnologias usadas

- Python 3
- Flask
- SQLite
- HTML5 e CSS3

Estrutura do projeto

crud-python-flask/
├── app.py
├── init_db.py
├── database.db
├── static/
│ └── style.css
└── templates/
  ├── index.html
  ├── add.html
  └── edit.html

Como rodar o projeto localmente

1. Clone o repositório:

   git clone https://github.com/rcustodio1/crud-python-flask.git
   cd crud-python-flask

2. Instale as dependências:

pip install flask

3. Crie o banco de dados:

python init_db.py

4. Inicie o servidor:

python app.py

5. Acesse no navegador:

http://127.0.0.1:5000

Licença

Este projeto está licenciado sob a Licença MIT.

🔗 Desenvolvido por Rafael Custódio – Estudante de Análise e Desenvolvimento de Sistemas
