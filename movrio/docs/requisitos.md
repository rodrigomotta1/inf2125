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
- **[RF24]** ~~Permitir gerenciamento de modelos de previsão no backend.~~
- **[RF25]** Integrar com APIs externas para dados meteorológicos e governamentais.
- **[RF26]** Exibir informações de APIs externas no painel lateral.
- **[RF27]** ~~Garantir responsividade para dispositivos móveis e desktop.~~
- **[RF28]** Seguir diretrizes de acessibilidade.
- **[RF29]** ~~Garantir segurança nas comunicações entre frontend e backend.~~
- **[RF30]** ~~Proteger dados de usuários em conformidade com a LGPD.~~
- **[RF31]** ~~Suportar escalabilidade para grande volume de usuários e dados.~~
- **[RF32]** Enviar notificações aos usuários sobre mudanças nos locais salvos.
- **[RF33]** Permitir configuração de preferências de notificação pelos usuários.
- **[RF34]** Fornecer painel administrativo para moderar e gerenciar conteúdo.
- **[RF35]** Exportar dados em formatos como CSV para análises externas.

---

## 🔧 Requisitos Não Funcionais

- **[RNF01]** ~~O sistema deve ser implementado em duas frentes: frontend em React e backend em Django REST.~~
- **[RNF02]** O sistema deve permitir interação fluida e visualização de mapas de calor.
- **[RNF03]** ~~O backend deve fornecer estimativas de densidade de pessoas em tempo hábil para o frontend.~~
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