# Task Management System

## Descrição

Este é um sistema de gerenciamento de tarefas desenvolvido usando Django e Django REST Framework. Ele fornece uma API RESTful completa para criar, ler, atualizar e excluir tarefas. A API é protegida com autenticação JWT e utiliza PostgreSQL para persistência de dados.

## Funcionalidades

- **Gerenciamento de Tarefas**:
  - Criação, leitura, atualização e exclusão de tarefas.
  - Filtragem e pesquisa de tarefas por título e data de vencimento.

- **Autenticação**:
  - Proteção de endpoints com autenticação JWT.

- **Persistência de Dados**:
  - Armazenamento de tarefas em um banco de dados PostgreSQL.

- **Documentação**:
  - Documentação completa da API usando Swagger.

- **Containers**:
  - Utilização de containers para desenvolvimento e deploy.

## Endpoints da API

### Criar Tarefa

- **Método**: POST
- **URL**: `/tasks`
- **Corpo da Requisição**:
    ```json
    {
      "title": "string",
      "description": "string",
      "due_date": "YYYY-MM-DD"
    }
    ```
- **Resposta**:
    ```json
    {
      "id": "integer",
      "title": "string",
      "description": "string",
      "due_date": "YYYY-MM-DD",
      "created_at": "timestamp",
      "updated_at": "timestamp"
    }
    ```

### Listar Tarefas

- **Método**: GET
- **URL**: `/tasks`
- **Resposta**:
    ```json
    [
      {
        "id": "integer",
        "title": "string",
        "description": "string",
        "due_date": "YYYY-MM-DD",
        "created_at": "timestamp",
        "updated_at": "timestamp"
      }
    ]
    ```

### Detalhar Tarefa

- **Método**: GET
- **URL**: `/tasks/{id}`
- **Resposta**:
    ```json
    {
      "id": "integer",
      "title": "string",
      "description": "string",
      "due_date": "YYYY-MM-DD",
      "created_at": "timestamp",
      "updated_at": "timestamp"
    }
    ```

### Atualizar Tarefa

- **Método**: PUT
- **URL**: `/tasks/{id}`
- **Corpo da Requisição**:
    ```json
    {
      "title": "string",
      "description": "string",
      "due_date": "YYYY-MM-DD"
    }
    ```
- **Resposta**:
    ```json
    {
      "id": "integer",
      "title": "string",
      "description": "string",
      "due_date": "YYYY-MM-DD",
      "created_at": "timestamp",
      "updated_at": "timestamp"
    }
    ```

### Remover Tarefa

- **Método**: DELETE
- **URL**: `/tasks/{id}`
- **Resposta**:
    ```json
    {
      "message": "Task deleted successfully."
    }
    ```

## Configuração do Ambiente

1. **Clone o Repositório**:
    ```bash
    git clone https://github.com/yourusername/task-management-system.git
    cd task-management-system
    ```

2. **Crie e Ative um Ambiente Virtual**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Windows: venv\Scripts\activate
    ```

3. **Instale as Dependências**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o Banco de Dados**:
    - Atualize as configurações do banco de dados no arquivo `settings.py` com as credenciais do PostgreSQL.

5. **Execute as Migrações**:
    ```bash
    python manage.py migrate
    ```

6. **Crie um Superusuário**:
    ```bash
    python manage.py createsuperuser
    ```

7. **Inicie o Servidor**:
    ```bash
    python manage.py runserver
    ```

8. **Acesse a Documentação da API**:
    - Acesse `http://127.0.0.1:8000/swagger/` para visualizar a documentação Swagger.

## Testes

- Execute os testes automatizados para verificar a funcionalidade da API:
    ```bash
    python manage.py test
    ```

## Containerização

O projeto é configurado para uso com Docker-compose. Para construir e executar o container:

1. **Execute o Container**:
    ```bash
    docker-compose up --build -d
    ```

## Tecnologias Utilizadas

- Django
- Django REST Framework
- PostgreSQL
- Django Filters
- JWT Authentication
- Docker
- Swagger (drf_yasg)

