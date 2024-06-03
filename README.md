# Review-Master


# Plataforma de Reviews de Filmes, Séries e Jogos

## Descrição

Este projeto é uma API para uma plataforma de reviews de filmes, séries e jogos. A API é construída utilizando Django no modelo MVT (Model-View-Template) e segue o fluxo de trabalho Git Flow. As principais funcionalidades incluem autenticação de usuários, telas de login, visualização de reviews e criação de novos reviews.

## Funcionalidades

- **Autenticação de Usuários:**
  - Registro de novos usuários
  - Login de usuários existentes
  - Logout

- **Reviews:**
  - Visualização de reviews
  - Criação de novos reviews
  - Edição e exclusão de reviews

## Tecnologias Utilizadas

- Django
- Django Rest Framework
- SQLite (pode ser alterado para outro banco de dados conforme necessidade)
- Git

## Requisitos

- Python 3.x
- Git

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/Ramos-GS/ReviwsApi.git
cd reviws
```

2. Crie um ambiente virtual e ative-o:

```bash
python -m venv .env
```
2. 1. Ative o ambiente virtual
```bash
.env\Scritps\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure o banco de dados e execute as migrações:

```bash
python manage.py migrate
```

5. Crie um superusuário para acessar o admin do Django:

```bash
python manage.py createsuperuser
```

6. Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

## Endpoints

### Autenticação

- `POST /api/auth/register/` - Registro de novos usuários
- `POST /api/auth/login/` - Login de usuários
- `POST /api/auth/logout/` - Logout de usuários

### Reviews

- `GET /api/reviews/` - Lista de reviews
- `POST /api/reviews/` - Criação de novos reviews
- `GET /api/reviews/<id>/` - Detalhe de um review específico
- `PUT /api/reviews/<id>/` - Atualização de um review específico
- `DELETE /api/reviews/<id>/` - Exclusão de um review específico

## Estrutura do Projeto

```plaintext
project-root/
│
├── manage.py
├── Pipfile
├── Pipfile.lock
│
├── reviews/  # Aplicação Django para reviews
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│
├── users/  # Aplicação Django para autenticação de usuários
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│
└── project_name/  # Configurações do projeto Django
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
```

## Contribuição

Este projeto segue o modelo de Git Flow para gerenciamento de branches. Para contribuir, siga os seguintes passos:

1. Crie um fork do projeto
2. Crie uma branch para sua feature ou correção de bug (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Envie para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request
