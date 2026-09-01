# 🏎️ wsBackendFabricaDeSoftware26.2 — API de Gerenciamento de Fórmula 1

API REST desenvolvida em **Django** e **Django REST Framework** para gerenciamento de pilotos e equipes de Fórmula 1, com integração à API pública **OpenF1** para consulta de dados reais do campeonato.

A ideia central do projeto é simples: **você é o dono da sua própria "escuderia digital"**. Em vez de trabalhar apenas com os dados oficiais da F1, a aplicação permite que você **crie seus próprios pilotos e suas próprias equipes**, vincule uns aos outros e gerencie tudo através de uma API REST completa (CRUD), enquanto também pode consultar informações reais de pilotos direto da OpenF1.

---

## 📌 Sobre o Projeto

Este projeto foi desenvolvido como desafio do projeto Fábrica de Software, com foco em praticar conceitos de desenvolvimento **Backend**.

Com a aplicação, é possível:

-  Criar, listar, consultar, atualizar e excluir **pilotos** próprios;
-  Criar, listar, consultar, atualizar e excluir **equipes** próprias;
-  Relacionar cada piloto a uma equipe (uma equipe pode ter vários pilotos);
-  Pesquisar pilotos cadastrados por **nome** ou por **equipe**;
-  Consultar pilotos reais da Fórmula 1 através da **API externa OpenF1**, filtrando por número do piloto;
-  Visualizar e testar todos os endpoints através de uma documentação **Swagger** personalizada.

Ou seja, a aplicação trabalha com duas frentes de dados: as **entidades próprias** (pilotos e equipes que você cadastra no banco) e os **dados externos em tempo real** vindos da OpenF1.

---

##  Tecnologias Utilizadas

- **Python**
- **Django 6.1**
- **Django REST Framework**
- **drf-spectacular** (geração do schema OpenAPI e Swagger)
- **MySQL** (banco de dados relacional)
- **requests** (consumo da API externa OpenF1)
- **OpenF1 API** (fonte de dados externos)

---

## ✅ Pré-requisitos

Antes de rodar o projeto, você precisa ter instalado:

- **Python 3.x**
- **MySQL Server** rodando localmente (ou acessível pela rede)
- **pip** para instalar as dependências

Todas as dependências do projeto estão listadas no arquivo `requirements.txt`, incluindo:

```
asgiref==3.12.1
attrs==26.1.0
certifi==2026.7.22
charset-normalizer==3.5.1
Django==6.1
djangorestframework==3.18.0
drf-spectacular==0.30.0
idna==3.19
inflection==0.5.1
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
mysqlclient==2.2.8
PyYAML==6.0.3
referencing==0.37.0
requests==2.34.2
rpds-py==2026.6.3
sqlparse==0.6.0
tzdata==2026.3
uritemplate==4.2.0
urllib3==2.7.0
```

> ⚠️ O pacote `mysqlclient` exige as bibliotecas de desenvolvimento do MySQL instaladas no sistema operacional para compilar corretamente (no Linux, geralmente `default-libmysqlclient-dev` e `build-essential`).

---

## ▶️ Como Rodar o Projeto

**1. Clone o repositório**

```bash
git clone https://github.com/ndu-xl/wsBackendFabricaDeSoftware26.2.git
cd wsBackendFabricaDeSoftware26.2
```

**2. Crie e ative um ambiente virtual (recomendado)**

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

**3. Instale as dependências**

```bash
pip install -r requirements.txt
```

**4. Configure o banco de dados MySQL**

O projeto está configurado para usar **MySQL**. Crie um banco chamado `f1_database` e ajuste usuário, senha e host no arquivo `projetoFabricaDeSoftware/.env`, e siga o exemplo do `.env.example` , de acordo com o seu ambiente local:

```python
SENHA_DB = 'senha'
HOST_DB = 'host'
PORT_DB =  'porta'
```

**5. Aplique as migrações**

```bash
cd projetoFabricaDeSoftware
python manage.py migrate
```

**6. Rode o servidor**

```bash
python manage.py runserver
```

A aplicação estará disponível em `http://127.0.0.1:8000/`.

---

## 📄 Documentação Swagger Personalizada

O projeto conta com uma documentação **Swagger customizada**, gerada com `drf-spectacular`, contendo título, descrição e tags próprias para cada grupo de endpoints (Pilotos, Equipes e OpenF1).

Após subir o servidor, acesse:

```
http://127.0.0.1:8000/swagger/
```

Por lá é possível visualizar e testar todos os endpoints da API diretamente pelo navegador, já organizados por categoria.

---

## 🔗 Endpoints Disponíveis

###  Pilotos (`/pilotos/`)

CRUD completo dos pilotos cadastrados no seu próprio banco de dados.

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/pilotos/` | Lista todos os pilotos cadastrados |
| `GET` | `/pilotos/{id}/` | Consulta um piloto específico pelo ID |
| `POST` | `/pilotos/` | Cadastra um novo piloto |
| `PUT` | `/pilotos/{id}/` | Atualiza completamente um piloto |
| `PATCH` | `/pilotos/{id}/` | Atualiza parcialmente um piloto |
| `DELETE` | `/pilotos/{id}/` | Remove um piloto |

**Filtros de pesquisa disponíveis:**

- Pesquisar por **nome**:
  ```
  GET /pilotos/?nome=[nome]
  ```
- Pesquisar por **equipe** (ID da equipe):
  ```
  GET /pilotos/?equipe=[equipe]
  ```

Exemplo de corpo para cadastro (`POST /pilotos/`):

```json
{
  "nome": "Lewis Hamilton",
  "numero": 44,
  "equipe": 1
}
```

---

###  Equipes (`/equipe/`)

CRUD completo das equipes cadastradas.

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/equipe/` | Lista todas as equipes cadastradas |
| `GET` | `/equipe/{id}/` | Consulta uma equipe específica pelo ID |
| `POST` | `/equipe/` | Cadastra uma nova equipe |
| `PUT` | `/equipe/{id}/` | Atualiza completamente uma equipe |
| `PATCH` | `/equipe/{id}/` | Atualiza parcialmente uma equipe |
| `DELETE` | `/equipe/{id}/` | Remove uma equipe |

Exemplo de corpo para cadastro (`POST /equipe/`):

```json
{
  "nome": "Ferrari",
  "pais": "Itália"
}
```

---

###  OpenF1 — Dados Externos da Fórmula 1 (`/openf1/pilotos/`)

Endpoint que consome a **API pública OpenF1** para trazer dados reais de pilotos da temporada mais recente da Fórmula 1.

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/openf1/pilotos/` | Lista os pilotos da sessão mais recente da F1, consultados em tempo real na OpenF1 |

**Filtro de pesquisa disponível:**

- Pesquisar piloto pelo **número**:
  ```
  GET /openf1/pilotos/?numero=[numero]
  ```

Exemplo de resposta:

```json
[
  {
    "nome": "Max Verstappen",
    "numero": 1,
    "equipe": "Red Bull Racing"
  }
]
```

---

## 🛡️ Tratamento de Erros

O endpoint que consome a API externa (`/openf1/pilotos/`) possui **tratamento de erros dedicado** para lidar com falhas de comunicação com a OpenF1, retornando mensagens claras e códigos HTTP apropriados:

| Situação | Código HTTP | Mensagem |
|----------|-------------|----------|
| Tempo de resposta excedido | `504 Gateway Timeout` | "A openF1 demorou muito para responder" |
| Falha de conexão | `503 Service Unavailable` | "Não foi possível conectar à openF1" |
| Outros erros de requisição | `500 Internal Server Error` | "Não foi possível acessar a API Open F1" |

Isso garante que, mesmo se a API externa estiver fora do ar ou instável, a aplicação continue respondendo de forma controlada, sem quebrar.

---

## 📁 Estrutura Principal do Projeto

```
projetoFabricaDeSoftware/
├── manage.py
├── projetoFabricaDeSoftware/      # Configurações do projeto (settings, urls, wsgi/asgi)
└── f1_manage/                     # App principal
    ├── models.py                  # Models: Piloto e Equipe
    ├── views.py                   # View de integração com a OpenF1
    ├── urls.py                    # Rota /openf1/pilotos/
    └── api/
        ├── serializers.py         # Serializers de Piloto e Equipe
        └── viewsets.py            # ViewSets (CRUD) de Piloto e Equipe
```

---

## 🎯 Objetivo Educacional

O foco principal do projeto é praticar a criação de uma API REST com **Django**, trabalhando com:

- Banco de dados relacional (MySQL);
- Relacionamento entre entidades (`ForeignKey` entre Piloto e Equipe);
- Operações CRUD completas via `ModelViewSet`;
- Filtros de pesquisa customizados via query params;
- Consumo de APIs externas com tratamento de erros;
- Documentação automática de API com Swagger/OpenAPI.
