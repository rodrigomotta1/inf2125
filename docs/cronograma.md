# Planejamento de Implementação do Trabalho

**Prazo de Entrega**: 10/12  
**Objetivo**: Desenvolver uma aplicação web que utiliza um backend em Django REST para processar dados e armazenar informações e um frontend em React com Vite para exibir um mapa focado em bairros, com suporte a busca de locais, autocomplete e visualização de mapa de calor.

## Ferramentas Utilizadas
- **Frontend**: React com Vite, shadcn/ui para componentes, Google Maps API (Maps, Places, Geocoding).
- **Backend**: Django REST Framework para a API, PostgreSQL (ou outro banco de dados de escolha) para armazenamento de dados.

## Resumo das Entregas Semanais

1. **Semana 1** (até 12/11): Configuração inicial do frontend e backend, criação de modelos e estrutura básica de API.
2. **Semana 2** (13/11 a 19/11): Implementação de geocodificação e API para locais e pontos de calor no backend.
3. **Semana 3** (20/11 a 26/11): Integração completa entre frontend e backend, API de autenticação e funcionalidade de favoritos.
4. **Semana 4** (27/11 a 03/12): Testes de integração, refinamento da interface e otimização do backend.
5. **Semana 5** (04/12 a 10/12): Documentação, revisão final e preparação para a entrega.


---

## Semana 1 (até 12/11): Configuração Inicial e Estrutura Básica

### Frontend
- **Configurar o ambiente de desenvolvimento**:
  - Configurar o Vite com React.
  - Instalar bibliotecas principais: `@react-google-maps/api`, `axios`, e componentes `shadcn/ui` necessários.
  - Configurar o arquivo `.env` com a chave da API do Google Maps.

- **Implementar a Interface Inicial**:
  - Criar a estrutura básica do projeto com os componentes:
    - `SearchBar` para a barra de busca com autocomplete.
    - `Map` para renderizar o mapa.
    - Sidebar com componentes para "Activity", "Notifications" e "Bookmarks".

### Backend
- **Configuração do Ambiente e Estrutura do Projeto**:
  - Criar o projeto Django e configurar o Django REST Framework.
  - Configurar o banco de dados (recomenda-se **PostgreSQL** para fácil integração e escalabilidade).
  - Criar modelos para armazenar dados dos locais e pontos de calor, incluindo:
    - **Location**: Para armazenar locais específicos, incluindo bairro, coordenadas, e dados adicionais.
    - **HeatPoint**: Para armazenar pontos de calor associados a um local (exemplo: horário, intensidade, etc.).

- **Testar Integração das APIs do Google**:
  - Configurar endpoints iniciais de teste para confirmar que o Django REST está respondendo e que as APIs do Google funcionam.

> **Resultado esperado**: Estrutura básica do frontend, backend configurado com modelos principais e endpoints básicos.

---

## Semana 2 (13/11 a 19/11): Implementação da Lógica de Geocodificação e Mapa de Calor

### Frontend
- **Implementar Geocodificação com a Geocoding API**:
  - Configurar a barra de busca para usar a **Geocoding API** e converter o endereço digitado em coordenadas.
  - Testar a funcionalidade de busca e verificação das coordenadas retornadas.

- **Implementar Visualização Focada no Bairro**:
  - Usar a **Places API** para identificar o bairro do local selecionado e ajustar o mapa para focar nessa área.
  - Adicionar uma camada de visualização do mapa de calor.

### Backend
- **Implementar Endpoints de API para Gerenciar Locais e Pontos de Calor**:
  - **GET /locations**: Endpoint para buscar informações sobre locais armazenados, incluindo detalhes do bairro.
  - **POST /locations**: Endpoint para adicionar novos locais ao banco de dados, caso o local não esteja registrado.
  - **GET /heatpoints**: Endpoint para obter os dados de pontos de calor relacionados a um local específico.
  - **POST /heatpoints**: Endpoint para criar ou atualizar pontos de calor no banco de dados.

- **Desenvolver Lógica de Processamento de Dados**:
  - Implementar uma função para processar as solicitações do frontend e armazenar dados relevantes.
  - Preparar a lógica para gerar dados de mapa de calor com base nos dados históricos de locais, simulando pontos de calor se necessário.

> **Resultado esperado**: Geocodificação funcional no frontend, API do backend para locais e pontos de calor configurada e testada.

---

## Semana 3 (20/11 a 26/11): Finalização da Interface e Funcionalidades Secundárias

### Frontend
- **Aprimorar a Interface do Usuário**:
  - Ajustar o layout com **shadcn/ui** para melhorar a usabilidade da barra de busca, sidebar e mapa.
  - Estilizar os botões de autenticação ("Sign In" e "Register").

- **Integrar Frontend com o Backend**:
  - Configurar o frontend para fazer requisições à API do Django REST e carregar os dados dos locais e pontos de calor.
  - Implementar a funcionalidade de salvar locais na seção "Bookmarks" (salvar nos favoritos, enviando dados ao backend).
  
- **Testar Funcionalidade de Mapa de Calor**:
  - Configurar o **HeatmapLayer** para exibir pontos de calor dinâmicos com base nos dados do backend.

### Backend
- **Implementar Endpoints para Autenticação e Registro de Usuários**:
  - **POST /register**: Endpoint para registro de novos usuários.
  - **POST /login**: Endpoint para login e geração de token de autenticação.
  - Configurar autenticação via **Token ou JWT** para proteger os endpoints sensíveis (como salvamento de locais).

- **Criar Funcionalidade para Armazenar Favoritos (Bookmarks)**:
  - **POST /bookmarks**: Endpoint para adicionar locais aos favoritos do usuário.
  - **GET /bookmarks**: Endpoint para buscar os favoritos do usuário logado.

- **Testar Integração do Backend com o Frontend**:
  - Testar a comunicação entre frontend e backend para buscar dados de locais e pontos de calor.
  - Validar o processo de salvamento e recuperação dos favoritos.

> **Resultado esperado**: Interface aprimorada, frontend integrado com o backend, API de autenticação e funcionalidade de favoritos implementadas.

---

## Semana 4 (27/11 a 03/12): Testes, Validação e Ajustes Finais

### Frontend
- **Testar Funcionalidade de Busca e Visualização de Dados**:
  - Testar o autocomplete da barra de busca, mapa de calor e funcionalidade de favoritos.
  - Validar o processo de autenticação (login/registro) e verificar se os dados de favoritos são carregados corretamente.

- **Ajustes de Interface e Experiência do Usuário**:
  - Refinar a experiência do usuário, ajustando a aparência da sidebar, layout da página e responsividade.
  - Ajustar a sidebar de acordo com o design original (anexo), se necessário.

### Backend
- **Testes e Validação de Funcionalidades**:
  - Testar todos os endpoints de API para garantir que as funcionalidades principais estão funcionando como esperado.
  - Validar o armazenamento e recuperação de dados de locais, favoritos e pontos de calor.

- **Otimizar o Backend para Desempenho e Segurança**:
  - Revisar as configurações de segurança, especialmente nas rotas autenticadas.
  - Otimizar consultas ao banco de dados para melhorar a performance.

> **Resultado esperado**: Funcionalidades completamente testadas e integradas, interface refinada e backend otimizado.

---

## Semana 5 (04/12 a 10/12): Documentação, Revisão e Preparação para a Entrega

### Frontend e Backend
- **Documentação Completa do Projeto**:
  - Documentar a estrutura do código, principais funções e como configurar e rodar o sistema.
  - Incluir exemplos de requisições à API no README para facilitar a compreensão do uso.

- **Preparação para a Apresentação do Projeto**:
  - Preparar uma apresentação ou demonstração para mostrar as funcionalidades do sistema, com foco na integração entre frontend e backend.
  - Organizar a apresentação em tópicos que demonstrem o uso das APIs (Google Maps, Places e Geocoding), a estrutura da aplicação e a lógica do backend.

- **Últimos Ajustes e Backup do Projeto**:
  - Realizar um backup do projeto e verificar se o repositório está atualizado.
  - Realizar uma última revisão geral para garantir que o sistema está funcional e pronto para entrega.

> **Resultado esperado**: Projeto finalizado, documentado e preparado para a entrega, com uma apresentação clara e organizada das funcionalidades principais.

---