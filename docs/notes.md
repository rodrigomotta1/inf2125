# Projeto
A ideia do projeto é fornecer uma espaço para estimar a quantidade de pessoas em algum ponto turístico do rio antes de ir ao local, dando a possibilidade ao turista da cidade de se planejar antes de visitar algum local do rio, como a praia de copacabana.

- **Big Idea:** Gerador de indicadores de quantidade de pessoas em pontos específicos do Rio
- **Essential Question:** Como mostrar e/ou prever os pontos de visitação mais cheios do Rio?
- **Challenge:** Indicar e estimar a quantidade de pessoas em um determinado ponto turístico usando modelos de IA com apoio de dados públicos.


# Apresentação 1
**Pontos principais:**
- Não é necessário mostrar cada etapa do CBL Canvas na apresentação (pode usar algumas partes apenas, pra elucidar a apresentação)
- Fundamentação: mencionar e comentar sobre soluções parecidas com a sua
- Protótipo deveria vir antes do Diagrama de Classes, ajuda a entender mais facilmente o que quer ser visto em cada tela
- Motivação, Problema, 
- 8 funcionalidades (3 pontos de variação no código e o resto fixo)


# Arquitetura
- **Backend:** Django REST
- **Frontend:** React Vite com componentes do shadcn.ui (TBD)

# Repositório
- Utilizar emojis do gitmoji.com antes de cada mensagem de commit para facilitar entendimento
- Identação com 4 espaços
- O código deve ter nomes autoexplicativos (comentar apropriadamente o código caso contrário)
- Manter convenção de nomes de variáveis, classes, funções... para cada linguagem

# Funcionalidades
1. Buscar locais por nome recuperando coordenadas do GPS a partir disso
2. Salvar locais pra visualização
3. Indicar a partir de mapas de calor a intensidade de fluxo de pessoas no local
4. Permitir que usuários se cadastrem no site
5. Permitir que usuários indiquem a situação do local enquanto estiverem por ali (as inidicações aparecem e desaparecem baseado na quantidade de pessoas que estiverem indicando, como no Waze)
6. Permitir configuração de parâmetros de previsão (frequência de previsão, modelo, ...)
7. Exibir metadados de cada local providos pela prefeitura  numa sidebar ao buscar pelo local (previsão de chuva, avisos da defesa civil, qualidade do ar, da água, operações policiais, eventos, mostrar previsões do app por dia e hora / quantidade de pessoas, como no Google Maps)
8. Permitir que usuários reportem bugs e inconsistências nas previsões e visualizações do sistema
9. Permitir que usuários façam upload de fotos dos locais com horário e localização precisa, para alimentar o modelo enquanto ele é usado.
10. Permitir visualização em inglês, espanhol e português

# 
