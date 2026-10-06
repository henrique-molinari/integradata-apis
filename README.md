# IntegraData - Integração de Dados com APIs REST

**Aluno:** Henrique Molinari
**RA:** 25001176

## Sobre o projeto

Projeto da disciplina de Integração de Dados. A empresa fictícia **LojaTech** tem suas informações espalhadas em sistemas diferentes, e o objetivo foi construir uma sequência de APIs REST em Python (Flask) que consulta cada fonte, consolida os dados de um cliente em um banco NoSQL e gera um relatório em Excel.

## O que foi desenvolvido

Seis APIs, cada uma em uma porta:

| API | Arquivo | Porta | Banco / Destino | Endpoint |
|---|---|---|---|---|
| Consulta de clientes | `api_cliente.py` | 5001 | SQLite (`clientes.db`) | `GET /cliente/<codigo>` |
| Consulta de compras | `api_compras.py` | 5002 | PostgreSQL (Neon) | `GET /compras/<cliente>` |
| Consulta financeira | `api_financeiro.py` | 5003 | Firebase Realtime Database | `GET /financeiro/<codigo>` |
| Consolidação | `api_consolidar.py` | 5004 | MongoDB Atlas | `GET /consolidar/<codigo>` |
| Dados consolidados | `api_consolidados.py` | 5005 | MongoDB Atlas | `GET /consolidados` |
| Exportação | `api_exportar.py` | 5006 | Excel (`clientes_consolidados.xlsx`) | `GET /exportar` |

### Fluxo

```
SQLite (cliente) ─┐
PostgreSQL (compras) ─┼─> API de consolidação ─> MongoDB ─> API de consulta
Firebase (financeiro) ─┘                                  └─> Exportação para Excel
```

Também foram criados:

- `startall.bat`: sobe as seis APIs de uma vez.
- `criar_clientes_db.py`: cria o `clientes.db` com dados de exemplo.
- `firebase-dados.json`: dados financeiros para importar no Firebase.
- `insomnia_integradata.json`: coleção do Insomnia com todos os testes e a documentação de cada requisição.
- `config.example.py`: modelo para as credenciais dos bancos.

## Como executar

1. Instale as dependências:

   ```
   pip install -r requirements.txt
   ```

2. Configure as credenciais: copie `config.example.py` para `config.py` e preencha a string do MongoDB Atlas e os dados de conexão do Neon.
3. Coloque o `firebase-key.json` (chave de conta de serviço do Firebase) na pasta do projeto e ajuste a `databaseURL` em `api_financeiro.py`.
4. Garanta o `clientes.db` na pasta (ou rode `python criar_clientes_db.py`).
5. Rode `startall.bat`.
6. Teste na ordem: `/cliente/1`, `/compras/1`, `/financeiro/1`, `/consolidar/1`, `/consolidados` e `/exportar`.

Os arquivos `config.py` e `firebase-key.json` contêm credenciais e não são versionados.

## Tecnologias

Python, Flask, SQLite, PostgreSQL (Neon), Firebase Realtime Database, MongoDB Atlas, pandas, openpyxl e Insomnia.
