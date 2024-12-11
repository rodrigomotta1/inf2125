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
  - Ter uma comunicação boa entre os membros dot ime

- **Stakeholders** *(interessados)*:
  - Moradores da cidade do Rio de Janeiro
  - Turistas e visitantes da cidade

## Act

### Requirements Identification
- **Value proposition:**
  - Monitoramento em tempo real do número de pessoas em lugares específicos da cidade do Rio de Janeiro
  - Realização de estimativas da quantidade de pessoas em pontos estratégicos

- **Platform/Technologies:** Django RESTful API *(python/backend)* e React *(frontend)*. Figma para prototipação

- **Prototype Test Strategy:** Uso do Figma para construção do protótipo de baixa ou média fidelidade

- **Requirements**: ver em [requisitos.md](/docs/requisitos.md)

### Development Approach

- **Indicators:**

- **Test Strategy:**

- **Design Patterns** *(ver classes em [diagrama_classes.puml](/docs/diagrama_classes.puml))*:
  - TemplateMethod
  - FactoryMethod

- **Development Rules:**
  - Usar `snake_case` como convenção para nomear variáveis, classes, métodos ou outros artefatos para o *backend*
  - Usar nomes autoexplicativos, adicionando comentários complementares quando necessário
  - Usar emojis do [gitmoji](gitmoji.com) antes de cada mensagem de commit
  - Realizar reuniões semanais para verificação do andamento do projeto
  
- **Refinement Strategy:**

