# tweet-analysis

Projeto final do curso de pós graduação em Ciência de Dados e Inteligência de negócios

# Objetivo

O objetivo deste projeto é criar um painel onde é possível analisar, em tempo real, as tendências da rede social Twittter.

É composto por um dashboard, criado com [Dash](https://dash.plotly.com/), onde é possível colocar palavras-chave, e ter uma visão geral do conteúdo sendo compartilhado no twitter, com métricas como quantidade de mensagens, palavras mais compartilhadas e etc.

O processamento das mensagens é feito por meio da lib [Spacy](https://spacy.io/), e inicialmente foca em conteúdo gerado em inglês.

# Configuração do projeto

```bash
pip install -r requirements.txt
```

```bash
- python -m spacy download pt_core_news_sm
```

-----

