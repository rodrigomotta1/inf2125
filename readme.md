# Projeto
A ideia do projeto é fornecer uma espaço para estimar a quantidade de pessoas em algum ponto turístico do rio antes de ir ao local, dando a possibilidade ao turista da cidade de se planejar antes de visitar algum local do rio, como a praia de copacabana.

- **Big Idea:** Cidades Inteligentes: Rio de Janeiro
- **Essential Question:** Como impactar positivamente as pessoas da cidade do Rio de Janeiro
- **Challenge:** Desenvolver alguma solução com IA que traga benefícios aos frequentadores e/ou moradores da cidade do Rio.

# Apresentação 1
**Pontos principais:**
- Não é necessário mostrar cada etapa do CBL Canvas na apresentação (pode usar algumas partes apenas, pra elucidar a apresentação)
- Fundamentação: mencionar e comentar sobre soluções parecidas com a sua
- Protótipo deveria vir antes do Diagrama de Classes, ajuda a entender mais facilmente o que quer ser visto em cada tela
- Motivação, Problema, 
- 8 funcionalidades (3 pontos de variação no código e o resto fixo (?))


# Arquitetura
- **Backend:** Django REST
- **Frontend:** Vite com componentes do shadcn.ui

# Repositório
- Utilizar emojis do gitmoji.com antes de cada mensagem de commit para facilitar entendimento (?)

# Funcionalidades
1. Buscar locais por nome recuperando coordenadas do GPS a partir disso
2. Salvar locais pra visualização
3. Indicar a partir de mapas de calor a intensidade de fluxo de pessoas no local
4. Permitir que usuários se cadastrem no site
5. Permitir que usuários indiquem a situação do local enquanto estiverem por ali (as inidicações aparecem e desaparecem baseado na quantidade de pessoas que estiverem indicando) -> ideia Waze
6. Permitir configuração de parâmetros de previsão (frequência de previsão, modelo, ...)
7. Exibir metadados de cada local providos pela prefeitura  numa sidebar ao buscar pelo local (previsão de chuva, avisos da defesa civil, qualidade do ar, da agua, operações policiais, eventos, mostrar previsões do app por dia e hora / quantidade de pessoas -- como no google...) -> Flightradar24
8. Permitir que usuários reportem bugs e inconsistências nas previsões e visualizações do sistema
9. Permitir que usuários façam upload de fotos dos locais com horário e localização precisa, para alimentar o modelo enquanto ele é usado.
10. Permitir visualização em inglês, espanhol (?) e português

# 
