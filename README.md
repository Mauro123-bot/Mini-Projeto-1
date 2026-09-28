# Raspagem de Pesquisas Eleitorais

Este é um mini projeto em Python.

## Objetivo do Projeto

O script extrai dados como:
- Nome do instituto de pesquisa
- Data de realização ou divulgação
- Intenções de voto de cada candidato
- Margem de erro e nível de confiança

Os dados coletados são organizados.

## Tecnologias Utilizadas

- **Python:** Linguagem principal do projeto.
- **Ambiente Virtual (venv):** Utilizado para isolar as dependências e manter o projeto organizado.
- **Requests:** Para fazer requisições HTTP e acessar o código dos sites.
- **BeautifulSoup4:** Para analisar e extrair dados de páginas HTML estáticas.
- **Selenium:** Para automação e raspagem de dados em sites dinâmicos que exigem interações (cliques/filtros).
- **Git & GitHub:** Para controle de versão e hospedagem do código.

## 📅 Diário de Bordo

### Dia 1: Preparação do Ambiente (Ontem)
- Criação e estruturação inicial do repositório no GitHub.
- Clonagem do projeto para a máquina local via Git.
- Configuração de um ambiente virtual isolado (venv) para gerenciamento seguro de dependências.
- Instalação dos módulos requests, beautifulsoup4 e selenium.
- Geração e publicação do arquivo requirements.txt com os requisitos solicitados.

### Dia 2: Desenvolvimento do Robô (Hoje)
- *Implementação do Selenium:* Configuração do navegador automatizado para interagir com o portal oficial do PesqEle do Tribunal Superior Eleitoral (TSE).
- *Automação de Cliques:* Criação da lógica para o robô localizar de forma inteligente o menu de pesquisas registradas e simular o clique humano para transição de página.
- *Filtro Inteligente de Dados:* Uso do BeautifulSoup para varrer o código HTML capturado, filtrando termos institucionais irrelevantes e isolando apenas opções úteis de consultas de pesquisas.
- *Estruturação em Tabela:* Organização visual dos dados filtrados diretamente no console do terminal.
- *Exportação de Dados:* Integração