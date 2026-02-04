# Star Wars API - Case Técnico PowerOfData

API REST em Python que consome a API SWAPI (Star Wars API) e disponibiliza dados sobre filmes, personagens, planetas e naves da saga Star Wars.

---

## Sobre o Projeto

Este projeto foi desenvolvido como parte do processo seletivo para Desenvolvedor Back End Python na PowerOfData.

**Objetivo:** Criar uma API que permita consultar e filtrar informações do universo Star Wars de forma organizada.

---

## Tecnologias Utilizadas

- Python 3.14
- Flask (framework web)
- Requests (cliente HTTP)
- Pytest (testes)
- SWAPI (fonte de dados)

---

## Estrutura do Projeto

starwars-api/
- docs/
    - arquitetura.md (Documentação técnica)

    -> src/

        - main.py (Endpoints da API)

        - swapi_client.py (Cliente para consumir SWAPI)

        - utils.py (Funções auxiliares)

    -> tests/

        - test_api.py (Testes automatizados)

    -> .gitignore    

    -> README.md
    
    -> requirements.txt

---

## Como Rodar o Projeto (Terminal)

### 1. Clonar o repositório
- git clone https://github.com/andre-zana/starwars-api.git
- cd starwars-api

### 2. Criar ambiente virtual
- python -m venv venv
- .\\venv\\Scripts\\activate # Windows

### 3. Instalar dependências
- pip install -r requirements.txt

### 4. Rodar a aplicação
- cd src
- python main.py

A API vai estar rodando em \http://localhost:8080\

---

## Endpoints Disponíveis

### Raiz

- GET /

Retorna informações básicas da API e lista de endpoints

### Filmes

- GET /api/films
- GET /api/films/{id}

Parâmetros: \search\, \sort_by\, \order\

### Personagens

- GET /api/people
- GET /api/people/{id}
Parâmetros: \search\, \sort_by\, \order\

### Planetas

- GET /api/planets
- GET /api/planets/{id}

### Naves

- GET /api/starships
- GET /api/starships/{id}

---

## Testes (terminal)

Para rodar os testes:
- pytest tests/ -v

Resultado: 13 testes realizados com sucesso!

---

## Funcionalidades Implementadas

- Consumo da API SWAPI
- Endpoints REST completos
- Filtros por busca textual
- Ordenação de resultados
- Dados formatados e limpos
- Cache para melhorar performance
- Testes automatizados
- Tratamento de erros
- Código organizado e documentado

---

## Arquitetura

O projeto foi estruturado pensando em deploy no Google Cloud Platform:
- Cliente → API Gateway → Cloud Function → SWAPI

Documentação completa em \docs/arquitetura.md\

---

## Deploy (preparado para GCP)

O projeto está pronto para ser deployado como Cloud Function:
- gcloud functions deploy starwars-api
- --runtime python314
- --trigger-http
- --entry-point starwars_api

---

## O Que Aprendi

Durante o desenvolvimento deste projeto:

- Como consumir APIs externas com Python
- Estruturação de APIs REST com Flask
- Implementação de cache para otimização
- Testes automatizados com pytest
- Preparação de código para cloud

---

## 🎯 Critérios Atendidos

| Requisito           | Status |
| ------------------- | ------ |
| Utilizar Python     | ✅     |
| Consumir SWAPI      | ✅     |
| Criar endpoints     | ✅     |
| Implementar filtros | ✅     |
| Testes unitários    | ✅     |
| Documentação        | ✅     |
| Estrutura GCP       | ✅     |

---

## Autor

André Zana - Desenvolvido para o processo seletivo PowerOfData - 2026
