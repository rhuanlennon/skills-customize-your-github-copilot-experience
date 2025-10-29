# 🚀 API REST com FastAPI

Desenvolva uma API REST moderna e eficiente usando o framework FastAPI do Python.

## O que você vai construir

Uma API REST para gerenciar uma biblioteca de livros, incluindo operações CRUD (Create, Read, Update, Delete), validação de dados, documentação automática e testes.

### Competências praticadas

- Desenvolvimento de APIs REST com FastAPI
- Modelagem de dados com Pydantic
- Documentação automática com Swagger/OpenAPI
- Testes de API com TestClient
- Manipulação de requisições HTTP
- Validação de dados e tratamento de erros

## Objetivos de aprendizagem

Ao final dessa tarefa você deverá ser capaz de:

- Criar endpoints REST seguindo as melhores práticas
- Implementar validação de dados usando Pydantic
- Documentar APIs automaticamente com OpenAPI
- Escrever testes para endpoints da API
- Tratar erros e exceções de forma adequada

## Pré-requisitos

- Python 3.8+
- Conhecimentos básicos de HTTP e REST
- Familiaridade com funções e classes Python

## Requisitos obrigatórios (Must Haves)

Sua API deve implementar:

- Modelo `Book` com campos: id, título, autor, ano, isbn
- Endpoints CRUD completos:
  - GET /books - listar todos os livros
  - GET /books/{id} - obter um livro específico
  - POST /books - adicionar novo livro
  - PUT /books/{id} - atualizar livro existente
  - DELETE /books/{id} - remover livro
- Validação de dados com Pydantic
- Respostas com status codes apropriados
- Documentação automática acessível em /docs

## Requisitos opcionais (Stretch Goals)

- Implementar paginação na listagem de livros
- Adicionar filtros de busca (por autor, ano, etc)
- Implementar autenticação básica
- Adicionar rate limiting
- Criar mais testes usando TestClient

## Estrutura de arquivos

```
fastapi-rest-api/
├── README.md           # este arquivo
├── starter-code.py     # estrutura inicial da API
└── test_api.py        # testes básicos
```

## Como executar (local)

1. Instale as dependências:

```bash
pip install fastapi uvicorn pytest
```

2. Execute o servidor:

```bash
uvicorn starter-code:app --reload
```

3. Acesse a documentação em: http://localhost:8000/docs

Para executar os testes:

```bash
pytest test_api.py -v
```

## Critérios de avaliação (rubrica)

Para a entrega ser considerada completa, verifique:

- (✅) Todos os endpoints CRUD funcionam corretamente
- (✅) Validação de dados está implementada
- (✅) Documentação OpenAPI está disponível e correta
- (✅) Testes passam com sucesso

Para nota extra, implemente ao menos um dos requisitos opcionais.

## Como submeter

1. Confirme que seu código está na pasta `assignments/fastapi-rest-api`
2. Verifique se os testes passam
3. Faça commit seguindo o padrão Conventional Commits:

```bash
git add .
git commit -m "feat(fastapi-rest-api): implementar API REST de biblioteca"
```

## Dicas e casos de borda

- Valide ISBN usando regex ou algoritmo de verificação
- Trate tentativas de acessar/modificar IDs inexistentes
- Normalize dados de entrada (ex: remover espaços extras)
- Use status codes HTTP apropriados para cada situação
- Documente parâmetros e respostas com exemplos

Boa codificação! 📚✨