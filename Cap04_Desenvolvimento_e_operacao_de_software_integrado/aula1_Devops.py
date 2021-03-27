"""
===============================================================================
                Desenvolvimento e Operação de Software Integrado
===============================================================================


========================= Objetivos da Aula ==================================

1 - Devops - Conceitos e Práticas
2 - Continuous Integration
3 - Continuous Inspection


========================= Requisitos Básicos =================================

- Conhecimentos de Infraestrutura
- Conhecimentos de Testes
- Versionamento com Git
- Scripts(bash, power shell, etc)



========================== Parte 1: DevOps ===================================

Antigamente tínhamos áreas totalmente separadas e cada uma tinha sua responsabilidade.

- Development
- Quality Assurance(QA)
- IT Operations

Por serem áreas isoladas, cada uma tinha suas próprias metas e não gostavam de assumir
a responsabilidade do outro time.

Isso criava muitos bloqueios e tornava o processo extremamente lento.


O Devops veio para ajudar a gente com várias conceitos e práticas de automatização
para que agente consiga integrar melhor esses times e mudar o mindset dessa galera.
Com as áres mais integradas nós conseguimos atingir um cultura de colaboração e também
uma entrega mais rápida de valor ao nosso cliente garantindo uma qualidade superior
do nosso produto e software de confiança.


" DEVOPS é um termo criado para definir o CONJUNTOS DE PRÁTICAS que INTEGRAM E AUTOMATIZAM
os PROCESSOS entre as equipes de DESENVOLVIMENTO, OPERAÇÕES e de APOIO(como o QA) para a
PRODUÇÃO RÁPIDA e CONFIÁVEL de SOFTWARE."



" O conceito de DEVOPS baseia-se em criar uma CULTURA DE COLABORAÇÃO ENTRE AS EQUIPES que
sempre trabalharam separadas.
  DEVOPS é uma MUDANÇA DE MENTALIDADE, UMA CULTURA, UM MOVIMENTO, UMA FILOSOFIA."




============================= Framework CALMS =======================================

Serve para suportar se agente realmente está conseguindo aplicar o DevOps ou não.

Ele é definido em 5 Pilares.


Cuture      Automation      Lean        Measurement         Sharing




============================ Culture =============================================

É o pilar mais forte de todos, nada acontece sem ele.

Todas FERRAMENTAS E AUTOMAÇÕES SÃO INÚTEIS se não forem acompanhadas pela VERDADEIRA
DISPOSIÇÃO da área de DESENVOVIMENTO e OPERAÇÕES em TRABALHAR JUNTOS.

Porque DevOps não resolve problemas de ferramentas.
RESOLVE PROBLEMAS HUMANOS.


=========================== Automation ==========================================

Automação ELIMINA O TRABALHO MANUAL repetitivo, produz processo repetíveis e cria
SISTEMAS CONFIÁVEIS.

Automatizar gera VELOCIDADE NA ENTREGA e tornam os envolvidos MAIS PRODUTIVOS.

Normalmente, COMPILAÇÃO, TESTE, IMPLEMENTAÇÃO E PROVISIONAMENTO automatizados são
O PONTO DE PARTIDA típico para equipes que ainda não tem isso implementado.


============================ LEAN ==============================================

Precisamos focar nas ENTREGAS DE VALOR AO CLIENTE. Precisamos ser OBJETIVOS E ENXUTOS.

Precisamos conhecer as nossas LIMITAÇÕES e os GARGALOS DO PROCESSO.

Precisamos ser LEAN.


A mentalidade DevOps vê oportunidades de MELHORIA CONTÍNUA em toda parte. Identificando
as LIMITAÇÕES, podemos OTIMIZAR O FLUXO, entregando MAIS VELOCIDADE e MAIOR EFICIÊNCIA.


================================ Measurement ====================================

DevOps é CÍCLICO E INFINITO. Mensurar e obter MÉTRICAS é o ponto de partida para
NOVAS MELHORIAS, seja para o PROCESSO DE DESENVOLVIMENTO, o SOFTWARE PRODUZIDO ou
as REGRAS DE NEGÓCIO.

Além de gerar CONHECIMENTO, MÉTRICAS criam PREVISIBILIDADE sobre POSSÍVEIS INCIDENTES
que possam vir a surgir.

Assim, temos INSUMOS suficientes para ANALISAR FALHAS e gerar MELHORIAS CONSTANTEMENTE.

Essas métricas podem ser baseadas em feedbacks de clientes, teste A/B, logs ou qualquer
outro tipo de métricas que a gente consiga tirar do nosso software em produção.



================================= Sharing ==========================================

O COMPARTILHAMENTO DE INFORMAÇÕES, além de ser SAUDÁVEL, auxilia na DESCENTRALIZAÇÃO
DE CONHECIMENTO em pessoas do time, evitando que os PROCESSOS se tornem DEPENDENTES.

COMPARTILHAR CONHECIMENTO ajuda na criação de TIMES GENÉRICOS, com conhecimento básicos
em diversos ASSUNTOS DO NEGÓCIO e TECNOLOGIAS.

Assim o time se torna AUTOSSUSTENTÁVEL



========================== Os Três Caminhos =====================================

Flow
Feedback
Learnig



===== FLOW =====

A OTIMIZAÇÃO DO FLUXO visa ELIMINAR desperdícios, GARGALOS NO PROCESSO,
transferência de responsabilidades e tempo de espera. Esse CAMINHO é trilhado
ENTRE A DEMANDA E A ENTREGA em produção.

A CHAVE para este caminho é a aplicação de METODOLOGIA ÁGEIS e a AUTOMATIZAÇÃO dos
processos de DESENVOLVIMENTO À RELEASE, como a INTEGRAÇÃO CONTÍNUA e/ou ENTREGA CONTÍNUA.


===== FEEDBACK =====

Ciclos rápidos de FEEDBACKS VISAM RESOLVER PROBLEMAS O QUANTO ANTES, testando tudo, ALERTANDO
EM QUALQUER FALHA, considerando TODAS AS MÉTRICAS coletadas no ambiente produtivo sobre o
VALOR ENTREGADO.

O MONITORAMENTE é a chave, ajudando a GERAR INFORMAÇÕES RELEVANTES CONSTANTEMENTE. Com
feedbacks rápidos, o NEGÓCIO CONSEGUE FALHAR RÁPIDO e LOGO RETOMAR O RUMO, caso necessário.


===== LEARNING =====

O APRENDIZADO CONTÍNUO visa GERAR CONHECIMENTO através de experimentação. HIPÓTESES
são MELHORES do que uma CERTEZA imediata. Este caminho é fruto de PROCESSO CIENTÍFICO e
produz SEGURANÇA PSICOLÓGICA.

A chave é o TRABALHO DINÂMICO, com times realizando EXPERIMENTOS em seu trabalho diário para
GERAR NOVAS MELHORIAS.
ELIMINE a CULTURA DA CULPA e AUMENTE a COLABORAÇÂO e o COMPARTILHAMENTO DE CONHECIMENTO.




================================ Entregando o Software ==================================

===== Plan =====

Microsoft Teams
Draw.io
Balsamiq
roadmunk
Confluence
Jira

===== Code =====

IDEs
VS Code
GitHub
Git
Sublime Text

===== Build =====

Container
Docker
Nuget
npm
crio-o
.NET CLI
MSBuild

===== Test =====

Unit.net
loader.io
JMeter
Selenium
Runscope
POSTMAN
sonarqube

===== RELEASE =====

Disponibilizar para o cliente


===== DEPLOY =====

Azure Pipelines
circleci
AppVeyor
GitLab CI
Travis CI[
Jenkins


===== OPERATE =====

Kubernetes
Rancher
Microsoft Azure
puppet
Terraform
CHEF
OPENSHIFT
AWS

===== MONITOR =====

Datadog
Prometheus
AppMetrics
Rollbar
Zabbix
New Relic
Pushover
Seq
Monitis




============================= Livro Recomendado ===============================

Manual do DevOps (The DevOps Handbook)

Como obter agilidade, confiabilidade e segurança em Organizações Tecnológicas

Gene Kim, John Wiils, Jez Humble
2016





"""