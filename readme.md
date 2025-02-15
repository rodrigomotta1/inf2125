
# 💻 MOVRIO: Estimador de quantidade de pessoas para apoio a decisão de turistas no Rio

Este projeto consiste no desenvolvimento de uma aplicação web que permite a visualização de mapas de calor indicando a quantidade estimada ou informada de pessoas em pontos turísticos do Rio de Janeiro, como a praia de Copacabana. O sistema se baseia no frameworkd Django. A interação principal é através de um mapa que apresenta essas estimativas e que pode ser acessado tanto por usuários anônimos quanto por usuários autenticados.

## ⚙️ Descrição do Sistema

- Ao acessar a aplicação, usuários **não logados** podem visualizar um mapa mostrando a **quantidade de pessoas** nos locais monitorados.
- **Usuários logados** têm acesso a um **painel lateral** onde podem ver:
  - Mudanças recentes de atividades nos locais.
  - Avisos relacionados à cidade, como notificações da prefeitura.
  - A atividade em **locais salvos** pelo usuário.
- O sistema permite o **login e cadastro** de usuários, sendo necessário apenas **email e senha** para registro.
- **Usuários logados** podem salvar locais de interesse e visualizar informações detalhadas desses locais, como estimativas de lotação e informes importantes.
- Usuários também podem **enviar informações** ao sistema sobre a atividade em um local, que serão validadas e processadas antes de serem incorporadas à estimativa do sistema.
- O sistema faz uso de **diferentes modelos de previsão**, que podem ser alimentados por dados de usuários e fontes externas, para gerar estimativas da quantidade de pessoas.

## Documentação disponível
- [x] [CBL-SE](/docs/cbl.md) redigido
- [x] [Registro de perguntas, respostas e recursos](/docs/guiding_answers.md)
- [x] [Reqisitos funcionais, Requisitos não funcionais e Regras de negócio](/docs/requisitos.md)
- [x] [Diagrama de classes UML](/docs/uml_classes.pdf)
- [x] ~~[Cronograma de desenvolvimento](/#)~~


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
**Módulos**:
- `visualizer` *(app)*: responsável pela lógica principal do site, viabilizando a visualização do mapa de calor e controle das entidades envolvidas
- `movrio.forecast`: responsável pelas lógicas de implementação e execução dos modelos de previsão e estimadores de quantidade de pessoas dos locais


*Se necessário, acesse o [painel de administração](localhost:8000/admin) usando o usuário `admin` com senha `admin`.*

