# CBL-SE Canvases

## Engage
- **Big Idea:** Apoio a decisão de visitas turísticas no Rio
- **Essential Question:** Como mostrar e/ou prever os pontos de visitação mais cheios do Rio?
- **Challenge:** Indicar e estimar a quantidade de pessoas em um determinado ponto turístico usando modelos de IA com apoio de dados públicos.

## Investigate
- **Problems/Opportunities:**
  - Obter dados da cidade do Rio de Janeiro para treinar uma IA pode ser complexo
  - Geralmente sempre há um modelo de IA bem conhecido para um problema. Nem sempre é necessário criar novos modelos de previsão

- **Main/Benchmark:** Google Maps, Waze, Skyline webcams

- **Critical success factors:**
  - Subdividir o desenvolvimento do projeto em etapas de forma objetiva
  - Definir tarefas para cada membro do time
  - Ter uma comunicação boa entre os membros do time

- **Stakeholders** *(interessados)*:
  - Moradores da cidade do Rio de Janeiro
  - Turistas e visitantes da cidade

## Act

### Requirements Identification
- **Value proposition:**
  - Monitoramento em tempo real do número de pessoas em lugares específicos da cidade do Rio de Janeiro
  - Realização de estimativas da quantidade de pessoas em pontos estratégicos

- **Platform/Technologies:** Django como *framework fullstack*. Figma para prototipação de telas.

- **Prototype Test Strategy:** Uso do Figma para construção do protótipo de baixa ou média fidelidade. Validação feita pela própria equipe.

- **Requirements**: ver em [requisitos.md](/movrio/docs/requisitos.md)

### Development Approach

- **Indicators:**
  - Aderência às metas de usabilidade: número de interações realizadas pelos usuários no sistema
  - Percentual de precisão das estimativas dos modelos preditivos
  - Feedback de stakeholders (turistas, moradores e órgãos da prefeitura) sobre a eficácia do sistema
  - Frequência de uso do sistema por usuários únicos e usuários retornantes
  - Quantidade de locais salvos pelos usuários autenticados

- **Test Strategy:**
  - Execução de testes unitários para verificar corretude de entradas e saídas de todas as rotas da API
  - Execução de testes de usabilidade para verificar a adequação da interface de usuário aos requisitos levantados e aos padrões de usabilidade

- **Design Patterns**:
  - Disponível em [/movrio/docs/uml_classes.pdf](/movrio/docs/uml_classes.pdf)
  - Singleton
  - Observer
  - TemplateMethod

- **Development Rules:**
  - Usar `snake_case` como convenção para nomear variáveis, classes, métodos ou outros artefatos para o *backend*
  - Usar nomes autoexplicativos, adicionando comentários complementares quando necessário
  - Usar emojis do [gitmoji](gitmoji.com) antes de cada mensagem de commit
  - Realizar reuniões semanais para verificação do andamento do projeto
  
- **Refinement Strategy:**
  - Conduzir entrevistas com usuários sobre a aplicação para recuperar feedbacks
  - Implementar mecanismo de feedback na ferramenta

