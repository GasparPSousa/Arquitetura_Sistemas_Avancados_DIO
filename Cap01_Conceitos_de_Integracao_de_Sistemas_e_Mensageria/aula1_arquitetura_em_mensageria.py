"""
===================================================================================
            Aprende o que é e como funciona Arquitetura em Mensageria
===================================================================================


============================= Objetivos da Aula ===================================

1 - O que é Arquitetura em Mensageria

2 - Comunicação Assíncrona entre serviços

3 - Gerenciamento de Erros



============================= Requesitos Básicos ==================================

- Entendimento sobre REST API

- Conhecimento Básico sobre Message Brokers



=========================== O que é Arquitetura em Mensageria ======================

- Explicações sobre o Microserviços #2



======================== Pros e Contras ==========================================

==== Pros =====

- Desacoplamento
- Fácil plug & play
- Comunicação Assíncrona
- Simples Escalabilidade
- Broadcasting
- Permite Event Source


==== Contras ====

- Single Point of Failure
- Dificil Monitoramento


============================= Comunicação Assíncrona entre Serviços ====================

- Comunicação em Cenário Simples

Passo 1

Web App >>>>>>>>>>> Proxy HTTP >>>>>>>>> Serviço 1 >>>>>>>>>>>>>>>>>>> Message Broker


Passo 2

Message Broker >>>>>>  Serviço 2 >>>>>>>> Message Broker


Passo 3

Message Broker >>>>>>>>>> Serviço 3


Esse exemplo parece muito mais uma comunicação liner.



- Comunicação um pouco mais complexa


Passo 1                                  Serviço 1

                                    Msg                 Msg

Passo 2                 Serviço 2                           Serviço 3

                    Msg            Msg                  Msg             Msg

Passo 3     Serviço 4               Serviço 5     Serviço 6                 Serviço 7










"""