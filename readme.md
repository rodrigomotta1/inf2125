
# 💻 MOVRIO: Estimador de quantidade de pessoas para apoio a decisão de turistas no Rio

Este projeto consiste no desenvolvimento de uma aplicação web que permite a visualização de mapas de calor indicando a quantidade estimada ou informada de pessoas em pontos turísticos do Rio de Janeiro, como a praia de Copacabana. O sistema se baseia no frameworkd Django. A interação principal é através de um mapa que apresenta essas estimativas e que pode ser acessado tanto por usuários anônimos quanto por usuários autenticados.

## ⚙️ Descrição do Sistema

- Ao acessar a aplicação, usuários **não logados** podem visualizar um mapa mostrando a **quantidade de pessoas** nos locais monitorados.
- **Usuários logados** têm acesso a um **painel lateral** onde podem ver:
  - Mudanças recentes de atividades nos locais.
  - Avisos relacionados à cidade (como notificações da prefeitura e previsão de chuva).
  - A atividade em **locais salvos** pelo usuário.
- O sistema permite o **login e cadastro** de usuários, sendo necessário apenas **email e senha** para registro.
- **Usuários logados** podem salvar locais de interesse e visualizar informações detalhadas desses locais, como estimativas de lotação e informes importantes (avisos da prefeitura, previsão do tempo, entre outros).
- Usuários também podem **enviar informações** ao sistema sobre a atividade em um local, que serão validadas e processadas antes de serem incorporadas à estimativa do sistema.
- O sistema faz uso de **diferentes modelos de previsão**, que podem ser alimentados por dados de usuários e fontes externas, para gerar estimativas da quantidade de pessoas.
- A visualização do mapa e a interação com o painel de informações são feitas via frontend em **React**, enquanto o **backend Django REST** processa as estimativas e recupera os dados necessários.

## Documentação disponível
- [x] [CBL-SE](/movrio/docs/cbl.md) redigido
- [x] [Registro de perguntas, respostas e recursos](/movrio/docs/guiding_answers.md)
- [x] [Reqisitos funcionais, Requisitos não funcionais e Regras de negócio](/movrio/docs/requisitos.md)
- [x] [Diagrama de classes UML](/movrio/docs/diagrama_classes.puml) *(deve ser visualizado através de algum leitor de [PlantUML](https://www.planttext.com/))*
- [x] ~~[Cronograma de desenvolvimento](/movrio/docs/cronograma.md)~~


## 🚀 Setup
### Backend
*(necessita instaslação do **Anaconda** e **python**)*
```bash
conda create --name movrio python=3.10.5
conda activate movrio
pip install -r requirements.txt
python manage.py runserver
```

## Estrutura
**Apps**:
- `visualizer`: responsável pela lógica principal do site, viabilizando a visualização do mapa de calor e controle das entidades envolvidas
- `forecast`: responsável pelas lógicas de implementação e execução dos modelos de previsão e estimadores de quantidade de pessoas dos locais


*Se necessário, acesse o [painel de administração](localhost:8000/admin) usando o usuário `admin` com senha `admin`.*

