
# 📊 Projeto: Aplicação de Mapas de Calor para Estimativa de Pessoas

Este projeto consiste no desenvolvimento de uma aplicação web que permite a visualização de mapas de calor indicando a quantidade estimada ou informada de pessoas em pontos turísticos do Rio de Janeiro, como a praia de Copacabana. O sistema é composto por um backend em **Django REST** e um frontend em **React**. A interação principal é através de um mapa que apresenta essas estimativas e que pode ser acessado tanto por usuários anônimos quanto por usuários autenticados.

## Descrição do Sistema

- Ao acessar a aplicação, usuários **não logados** podem visualizar um mapa mostrando a **densidade de pessoas** nos locais monitorados.
- **Usuários logados** têm acesso a um **painel lateral** onde podem ver:
  - Mudanças recentes de atividades nos locais.
  - Avisos relacionados à cidade (como notificações da prefeitura e previsão de chuva).
  - A atividade em **locais salvos** pelo usuário.
- O sistema permite o **login e cadastro** de usuários, sendo necessário apenas **email e senha** para registro.
- **Usuários logados** podem salvar locais de interesse e visualizar informações detalhadas desses locais, como estimativas de lotação e informes importantes (avisos da prefeitura, previsão do tempo, entre outros).
- Usuários também podem **enviar informações** ao sistema sobre a atividade em um local, que serão validadas e processadas antes de serem incorporadas à estimativa do sistema.
- O sistema faz uso de **diferentes modelos de previsão**, que podem ser alimentados por dados de usuários e fontes externas, para gerar estimativas da quantidade de pessoas.
- A visualização do mapa e a interação com o painel de informações são feitas via frontend em **React**, enquanto o **backend Django REST** processa as estimativas e recupera os dados necessários.

---

## ✨ Requisitos Funcionais

- **[RF01]** Visualizar mapa de calor com densidade de pessoas.
- **[RF02]** Interagir com o mapa (zoom e seleção de locais).
- **[RF03]** Atualizar visualização do mapa em tempo real ou intervalos configuráveis.
- **[RF04]** Exibir painel lateral com mudanças de atividade recentes.
- **[RF05]** Exibir painel lateral com avisos da prefeitura e previsões.
- **[RF06]** Exibir painel lateral com locais salvos para usuários logados.
- **[RF07]** Permitir cadastro de novos usuários com email e senha.
- **[RF08]** Permitir login de usuários com email e senha.
- **[RF09]** Autenticar usuários de forma segura.
- **[RF10]** Permitir recuperação de senha de usuários.
- **[RF11]** Permitir que usuários logados salvem locais de interesse. 
- **[RF12]** Exibir atividade de locais salvos no painel lateral para usuários logados.
- **[RF13]** Permitir que usuários removam locais salvos.
- **[RF14]** Permitir envio de informações pelos usuários sobre a atividade em locais.
- **[RF15]** Validar e incorporar informações enviadas pelos usuários.
- **[RF16]** Estimar a quantidade de pessoas usando modelos de previsão.
- **[RF17]** Suportar diferentes modelos de previsão para estimativa de pessoas.
- **[RF18]** Permitir a adição e atualização de novos modelos de previsão.
- **[RF19]** Agregar e processar dados de múltiplas fontes para alimentar modelos.
- **[RF20]** Exibir quantidade estimada de pessoas por dia e hora da semana.
- **[RF21]** Permitir busca por local específico.
- **[RF22]** Exibir informações detalhadas de locais específicos no painel lateral.
- **[RF23]** Exibir previsão de chuva, qualidade da água e segurança por local.
- **[RF24]** Permitir gerenciamento de modelos de previsão no backend.
- **[RF25]** Integrar com APIs externas para dados meteorológicos e governamentais.
- **[RF26]** Exibir informações de APIs externas no painel lateral.
- **[RF27]** Garantir responsividade para dispositivos móveis e desktop.
- **[RF28]** Seguir diretrizes de acessibilidade.
- **[RF29]** Garantir segurança nas comunicações entre frontend e backend.
- **[RF30]** Proteger dados de usuários em conformidade com a LGPD.
- **[RF31]** Suportar escalabilidade para grande volume de usuários e dados.
- **[RF32]** Enviar notificações aos usuários sobre mudanças nos locais salvos.
- **[RF33]** Permitir configuração de preferências de notificação pelos usuários.
- **[RF34]** Fornecer painel administrativo para moderar e gerenciar conteúdo.
- **[RF35]** Exportar dados em formatos como CSV para análises externas.

Obs: os seguintes requisitos são especificamente relacionados a implementação do *backend*: **RF11, RF13, RF14, RF16, RF17, RF18, RF19, RF32, RF33, RF34, RF35**

---

## 🔧 Requisitos Não Funcionais

- **[RNF01]** O sistema deve ser implementado em duas frentes: frontend em React e backend em Django REST.
- **[RNF02]** O sistema deve permitir interação fluida e visualização de mapas de calor.
- **[RNF03]** O backend deve fornecer estimativas de densidade de pessoas em tempo hábil para o frontend.
- **[RNF04]** O sistema deve suportar o consumo de diferentes tipos de mídia para alimentar os modelos de previsão.
- **[RNF05]** O sistema deve ser capaz de agregar dados de múltiplas fontes de forma eficiente.
- **[RNF06]** O sistema deve ser capaz de atualizar as estimativas periodicamente, de acordo com a coleta de novos dados.
- **[RNF07]** O sistema deve ser responsivo para diferentes tipos de dispositivos (móveis e desktops).

---

## 📜 Regras de Negócio

- **[RN01]** Apenas usuários logados podem salvar locais de interesse.
- **[RN02]** Não há restrição sobre o tipo de informações que o usuário pode enviar ao sistema, desde que sejam relacionadas à atividade pública em um local.
- **[RN03]** As informações enviadas pelos usuários devem ser validadas antes de serem incorporadas ao sistema.
- **[RN04]** O sistema deve permitir que os usuários logados vejam a atividade nos locais que salvaram, com base nas estimativas do sistema e em dados enviados por outros usuários.
