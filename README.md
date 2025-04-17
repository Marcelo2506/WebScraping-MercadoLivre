📊 Web Scraping Mercado Livre - Análise de Notebooks
Este projeto realiza uma pesquisa de mercado automatizada sobre notebooks disponíveis no Mercado Livre, utilizando Web Scraping com Scrapy. A partir da coleta de dados, é possível analisar e visualizar tendências de preços, marcas e avaliações por meio de um dashboard interativo feito com Streamlit.

🚀 Funcionalidades
🔍 Coleta automatizada de dados com Scrapy.

🧼 Transformação e limpeza com Pandas.

📊 Dashboard interativo para análise visual com Streamlit.

💾 Armazenamento local em SQLite.

✅ Dados filtrados para eliminar inconsistências e facilitar a análise.

🧠 Informações Coletadas
Para cada notebook extraído do Mercado Livre, são armazenados os seguintes dados:

🖥️ Nome do produto

🏷️ Marca

💵 Valor atual

🪙 Valor antigo (se disponível)

⭐ Avaliação média

🗳️ Quantidade de avaliações

📌 Tecnologias Utilizadas
Scrapy — Web Scraping

Pandas — Análise e manipulação de dados

SQLite — Banco de dados leve

Streamlit — Visualização de dados

📁 Estrutura do Projeto
WebScraping-MercadoLivre/
│
├── scraping/
│   └── mercado_livre_spider.py   # Spider Scrapy
│
├── transform/
│   └── limpar_dados.py           # Limpeza e transformação dos dados
│
├── database/
│   └── notebooks.db              # Base de dados SQLite
│
├── dashboard/
│   └── app.py                    # Aplicativo Streamlit
│
├── data/
│   └── data_raw.json             # Dados brutos coletados
│
└── README.md                     # Documentação do projeto

▶️ Como Rodar o Projeto
Clone o repositório:
git clone https://github.com/Marcelo2506/WebScraping-MercadoLivre.git
cd WebScraping-MercadoLivre

Crie o ambiente virtual e instale as dependências:
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

Execute o Scrapy:
scrapy crawl notebook -o data/data.json

Faça o tratamento dos dados:
python .\Coleta\Transform\main.py

Rode o dashboard:
python .\Coleta\Dashboard\app.py 
run streamlit .\Coleta\Dashboard\app.py

📈 Utilidade
Este projeto é útil para:

👥 Consumidores que desejam comparar preços e avaliações antes de comprar um notebook.

🏪 Lojistas ou marketplaces que querem acompanhar tendências de preços e concorrência.

📊 Analistas de dados interessados em práticas de web scraping e visualização.

🌱 Melhorias Futuras
Agendamento automático de coletas

Exportação para CSV ou integração com AWS

Análise temporal da variação de preços