# Review-Master

## Plataforma de Reviews de Filmes

### Descrição

Review-Master é uma plataforma web para que os usuários possam visualizar, adicionar, editar e excluir críticas de filmes. A aplicação é construída utilizando o framework Django e segue o modelo MVT (Model-View-Template).

### Funcionalidades

- **Autenticação de Usuários:**
  - Registro de novos usuários
  - Login de usuários existentes
  - Logout

- **Críticas de Filmes:**
  - Visualização de filmes
  - Detalhes de uma filme específica
  - Criação de novas críticas
  - Edição de críticas existentes
  - Exclusão de críticas

### Tecnologias Utilizadas

- Python
- Django
- SQLite (padrão, pode ser alterado para outro banco de dados)
- HTML/CSS para templates

### Requisitos

- Python 3.x
- Git

### Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/Ramos-GS/Review-Master.git
    cd Review-Master
    ```

2. Crie um ambiente virtual e ative-o:

    ```bash
    python -m venv .env
    ```

    Ative o ambiente virtual:

    - No Windows:
    
      ```bash
      .env\Scripts\activate
      ```

    - No macOS/Linux:
    
      ```bash
      source .env/bin/activate
      ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure o banco de dados e execute as migrações:

    ```bash
    python manage.py migrate
    ```

5. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

### Endpoints

#### Autenticação

- `GET /register/` - Página de registro de novos usuários
- `GET /login/` - Página de login de usuários
- `GET /logout/` - Logout de usuários

#### Críticas de Filmes

- `GET /` - Página inicial
- `GET /movies/` - Lista de todas os filmes
- `GET /movies/<int:movie_id>/` - Detalhes de um filme específica
- `POST /movies/<int:movie_id>/review/` - Criação de uma nova crítica
- `GET /review/<int:review_id>/edit/` - Página de edição de uma crítica existente
- `POST /review/<int:review_id>/edit/` - Atualização de uma crítica existente
- `POST /review/<int:review_id>/delete/` - Exclusão de uma crítica

### Estrutura do Projeto

```plaintext
Review-Master/
├── .gitignore
├── README.md
├── requirements.txt
└── core/
    ├── manage.py
    ├── core/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── movies/
        ├── .env.template
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── forms.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        ├── utils.py
        ├── views.py
        ├── migrations/
        │   ├── 0001_initial.py
        │   ├── 0002_alter_review_movie_alter_review_rating.py
        │   └── __init__.py
        ├── templates/
        │   ├── add_review.html
        │   ├── edit_review.html
        │   ├── home.html
        │   ├── login.html
        │   ├── movie_detail.html
        │   ├── movie_list.html
        │   └── register.html
        └── templatetags/
            ├── __init__.py
            └── movies_extras.py
