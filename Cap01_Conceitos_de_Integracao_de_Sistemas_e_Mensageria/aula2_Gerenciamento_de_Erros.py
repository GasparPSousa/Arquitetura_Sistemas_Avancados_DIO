""""
=====================================================================================
                            Gerenciamento de Erros
=====================================================================================

- Dead letter queue (Filas de re-tentativas)

- Monitoramento entre eixos

- Rastreamento de Fluxo


============================== Inconsistência de Dados =============================

Exemplo

Web App >>>>>>>>>> Proxy HTTP >>>>>>>>>>> Serviço de Carteira >>>>>>>>>>> Message Broker
                                Adicionar
                                Cartão de Crédito



Web App >>>>>>>>>> Proxy HTTP >>>>>>>>>>> Serviço de Carteira >>>>>>>>>>> Message Broker
                                Adquirir
                                Plano


Message Broker >>>>>>>>>>>>>>>>> Serviço de Cobrança >>>>>>>>>>>>>>> Banco de Dados
                Aquisição                   \
                de                              \
                Plano                                \
                                                         \
                                                        Dead Letter Queue


Imagina que por algum problema na Infraestrutura a Mensagem "Aquisição de Plano"
chegou antes da adição do Cartão de Crédito. Isso pode gerar um certo de erro por
incosistência de dados.

O Serviço de Cobrança não vai saber como fazer determinada operação, não vai saber como proceder.
Nesse gerenciamento de erro, Dead letter queue guarda esse mensagem na fila

Num outro momento, essa mensagem vai tentar ser executada e essa nova mensagem de novo cartão de crédito
vai acabar chegando no Serviço de Cobrança e este vai guardar no seu BD...e na próxima re-tentativa de executar
essa aquisição de plano, ele vai verificar que o cartão de crédito já  foi persistido no BD, então ele
vai poder persistir essa aquisição de plano linkado com aquele cartão de crédito...Aí então proceder com sua lógica
cobrança.



============================ Rastreamento ==========================================

                                                        TrackID
Web App >>>>>>>>>> Proxy HTTP >>>>>>>>>>>> Serviço 1 >>>>>>>>>>>>> Message Broker
                                          Logs Logs Logs
                    TrackID
Message Broker >>>>>>>>>>>>>>  Serviço 2
     \          <<<<<<<<<<<<<<  Logs Logs Logs
        \           TrackID
            \
           Serviço 3
        Logs Logs Logs


Logs Serviços 1 - TrackID
Logs Serviços 2 - TrackID
Logs Serviços 3 - TrackID



"""