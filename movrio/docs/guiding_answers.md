# Registro de perguntas, atividades e recursos
Abaixo estão listadas todas as ***Guiding Questions*** e ***Guiding Activities***. Os ***Guiding Resources*** são listados como referência em cada **GQ** ou **GA** os quais eles estão relacionados.


## *Guiding Questions*
- **GQ01**: Quais são os principais problemas da cidade para os moradores e visitantes do Rio?
  - Segundo pesquisa realizada pelo [Instituto Rio21](https://rio21.org/) e encomendada pelo jornal [Diário do Rio](https://diariodorio.com), o principal fator que preocupou os cariocas entre julho e novembro de 2024 foi o crime e a violência na cidade. Nesse sentido, aplicações que apoiam o visitante ou o morador carioca a inspecionar o local que quer visitar previamente se mostram úteis, principalmente tranquilizando e preparando o turista, seja local ou não, para o ambiente que deseja visitar.
  - A partir de notícias do próprio Diário do Rio, como [esta](https://diariodorio.com/pesquisa-aponta-seguranca-e-conservacao-como-principais-problemas-do-rio/), que divulga os resultados das pesquisas, fica claro que a preocupação do morador carioca já é a mesma há pelo menos 3 anos, indicando o quão significativa é a questão da segurança ao morador da cidade.
  - ***[Resources](#guiding-resources)***: R06.

- **GQ02**: Quais são as regiões da cidade que mais ganham com soluções para cidades inteligentes?
  - Até o momento, as regiões apontadas por notícias como as que já se benefeciam de soluções inteligentes são o Centro, a região portuária (Porto Maravilha) e uma região de Campo Grande, esta última apoiada pela construtura MRV.
  - ***[Resources](#guiding-resources)***: R07, R08, R09

- **GQ03**: Quais projetos de cidades inteligentes já foram desenvolvidos no Rio de Janeiro?
  - Além dos já encontrados em **GQ02**, nota-se também:
    - [**Projeto *Green Light***](https://diariodorio.com/conheca-a-tecnologia-de-ia-que-esta-reduzindo-o-tempo-de-espera-nos-sinais-de-transito-do-rio): em parceria com a Google, utiliza IA e visa otimizar o tempo de semáforos, reduzindo congestinamentos e o tempod e espera dos motoristas trafegando pela cidade
    - [***Senseable Rio Lab***](https://prefeitura.rio/ciencia-e-tecnologia/prefeitura-do-rio-assina-convenio-inedito-na-america-do-sul-para-utilizar-de-inteligencia-artificial-em-projetos-urbanos/): parceira entre MIT e governo municipal para impulsionar o desenvolvimento de soluções inteligentes para a cidade
  - Também existem uma série de outras iniciativas listadas em **R10**.
  - ***[Resources](#guiding-resources)***: R10

- **GQ04**: Como utilizar IA para melhorar algum aspecto da cidade?
  - Observando as soluções pesquisadas em **GQ03** e **GQ02**, as soluções de IA podem ser usadas principalmente para: 
    - Otimizar utilização de espaço e infraestrutura de regiões da cidade; otimizar o trânsito da cidade; 
    - Melhorar o monitoramento de incidentes de segurança; 
    - Auxiliar o desenvolvimento de novas soluções de infraestrutura.
  - Baseando-se nos recursos encontrados, também parece interessante adaptar soluções já realizadas em outras partes do mundo como as listadas em **R11**. Finalmente, destaca-se a utilização de câmeras de segurança para realização de análises em tempo real.
  - ***[Resources](#guiding-resources)***: R11; R12;

- **GQ05**: Quais locais do Rio possuem mais estrutura para receber um projeto desse tipo?
  - Previamente, já foram observadas câmeras de monitoramento em tempo real de fácil acesso através de **R02**, portanto bairros e/ou locais contidos nesse site são interessantes para projetos que utilizem câmeras de monitoramento em tempo real
  - Além disso, bairros e locais que possuem mais infraestrutura certamente abrigarão projetos de cidades inteligentes com maior facilidade, como por exemplo a cidade universitária (UFRJ), que também conta com iniciativas de cidades inteligentes, conforme observado em **R13**.
  - ***[Resources](#guiding-resources)***: R02; R13
  
- **GQ06**: Quais as dificuldades ténicas da implementação desse projeto?
  - Elaborar modelos de previsão adequados, considerando a variedade de dados disponíveis
  - Gerenciar o recebimento e entrega de informações em tempo real aos clientes da aplicação em tempo hábil.
  - ***[Resources](#guiding-resources)***: Nenhum.

- **GQ07**: Como inferir ou prever eventos importantes (trânsito, tiroteio, fesitval...) na cidade através de análise de dados?
  - Uma possibilidade é utilizar dados de telefonia celular para examinar movimentação de pessoas na cidade em dias de grandes eventos.
  - ***[Resources](#guiding-resources)***: R14; R15
  
- **GQ08**: ~~Quais padrões de projeto geralmente adequados para models do DjangoREST?~~
- **GQ09**: Como são aplicados os padrões de projeto no contexto de models do Django?
  - Padrão Observer deve ser implementado utilizando Django Signals
  - Padrão Singleton para acesso a dados não deveria ser utilizado segundo **R17**
  - ***[Resources](#guiding-resources)***: R16, R17


## *Guiding Actvities*
- **GA01**: Pesquisar sobre iniciativas de cidades inteligentes no Rio: executado através de **GQ02**, **GQ03** e **GQ04**.
- **GA02**: Encontrar cases de sucesso de cidades inteligentes: executado através de **GQ02**, **GQ03** e **GQ04**.
- **GA03**: Mapear problemas críticos na cidade: executado através de **GQ01**.
- **GA04**: Levantar dados públicos oferecidos pelo Estado (prefeitura, gov. do estado, federação)
  - Dados diversos estão disponíveis em **R03**

## *Guiding Resources*
- **R01**: https://cor.rio/
  - Site do Centro de Operações do Rio, pode ser útil para recuperar dados públicos sobre turismo, transporte, movimentação e eventos na cidade.
- **R02**: https://www.skylinewebcams.com/en/webcam/brasil/rio-de-janeiro.html
  - Uma das *webcams* na cidade do Rio disponibilizadas pela Skyline WebCams, a princípio podem ser utilizadas gratuitamente mas possuem poucos locais no Rio.
- **R03**: https://www.data.rio/
  - Espécie de Portal da Transparência da cidade, contém diversos conjuntos de dados úteis para previsão de pessoas em locais da cidade.
- **R04**: https://openweathermap.org/
  - Portal de acesso a dados públicos metereológicos
- **R05**: https://refactoring.guru/
  - Referência pra implementação de padrões de projeto orientados a objeto em python
- **R06**: https://drive.google.com/file/d/1WjPxJmBF7L1lk207QKZLXHhpd2k8l2iP/view
  - Pesquisa sobre o perfil do cidadão carioca e visitante da cidade realizada em novembro de 2024 pelo [Instituto Rio21](https://rio21.org/) e encomendada pelo jornal [Diário do Rio](https://diariodorio.com)
- **R07**: https://prefeitura.rio/cidade/com-expansao-do-cor-rio-avanca-no-conceito-de-cidades-inteligentes/
  - Relatório da prefeitura sobre iniciativas de cidades inteligentes no Centro do Rio
- **R08**: https://exame.com/tecnologia/10-acoes-que-tornam-o-porto-maravilha-um-bairro-inteligente
  - Artigo da revista Exame sobre iniciativas de cidades inteligentes na zona portuária do Rio
- **R09**: https://revistaempreende.com.br/mrv-apresenta-sua-primeira-cidade-inteligente-no-rio-de-janeiro-com-foco-em-mobilidade-e-desenvolvimento-urbano/
  - Artigo de divulgação da cidade inteligente construída pela MRV em Campo Grande
- **R10**: https://prefeitura.rio/fazenda/programa-rio-certifica-60-iniciativas-para-uma-cidade-mais-inteligente-e-sustentavel/
  - Divulgação da prefeitura de mais de 60 iniciativas de cidades inteligentes recém certificadas pela mesma
- **R11**: https://www.portaldotransito.com.br/noticias/mobilidade-e-tecnologia/
  - Coleção de ideias que podeM ser interessantes no contexto de cidades inteligentes levantadas em um artigo pelo Portal do Trânsito
- **R12**: https://www.ime.usp.br/~kon/presentations/JAI2016-CidadesInteligentes.pdf
  - Slides de uma aula do curso JAI2016 do IME-USP, que apresenta soluções de cidades inteligentes ao redor do mundo.
- **R13**: https://coppe.ufrj.br/cidades-inteligentes/
  - Artigo de divulgação da COPPE-UFRJ sobre iniciativas de cidades inteligentes no *campus*.
- **RF14**: https://repositorio.fgv.br/server/api/core/bitstreams/bf0a896a-6177-47c9-b901-2ee782fd5f6e/content
  - Dissertação de mestrado da FGV que indica metodologias para análise de dados de telefonia celular para examinar a movimentação na cidade em dias de grandes eventos.
- **RF15**: https://www.academia.edu/124508201/Modelos_De_Previs%C3%A3o_De_Tr%C3%A2nsito_Uma_Contribui%C3%A7%C3%A3o_Para_a_Gest%C3%A3o_P%C3%BAblica_Do_Tr%C3%A1fego_Na_Cidade_De_S%C3%A3o_Paulo
  - Estudo da FEA-SUP sobre modelos de previsão de trânsito.
- **R16**: https://www.youtube.com/watch?v=p4vLpz1D4ow&t=213s
  - Video explicativo do canal *Very Academy* sobre como implementar o padrão Observer utiliando o módulo `signal` do Django. Essa parece ser a forma que melhor cumpre o objetivo de manter a estrutura do projeto coesa com baixo acoplamento.
- **R17**: https://daniel.feldroy.com/posts/when-to-use-mongodb-with-django
  - Artigo de Daniel Feldroy sobre vantagens e desvantagens de usar o Mongo. O artigo discute levemente sobre a decisão de usar ou não usar o ORM do Django para acesso ao Banco de Dados, deixando claro que a melhor opção é sempre utilizar o ORM do Django com um banco relacional, uma vez que essa funcionalidade do *framework* já possui a maioria das facilidades e controles, principalmente de segurança e desempenho, para acesso a dados em um BD (nesse caso, estritamente relacional)
- **R18**: 

## Misc.
- Como renderizar mapas de calor usando a biblioteca do Google: https://developers.google.com/maps/documentation/javascript/heatmaplayer?hl=pt-br (usar como escala a estimativa de pessoas geradas para cada lugar)