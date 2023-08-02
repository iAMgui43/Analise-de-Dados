import pandas as pd
import plotly.express as px


tabela = pd.read_csv("cancelamentos.csv")
tabela = tabela.drop("CustomerID", axis=1)
print(tabela)

tabela = tabela.dropna()
print(tabela.info())

# 4 -> Analise Inicial (Entender como estão os cancelamentos)
print(tabela["cancelou"].value_counts())
# > Comando normalize=True passa os valores em %
# > Utilizando o ".map" e passando o formato correto ele realiza a transformação do número junto com o ".format"
print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

print(tabela["duracao_contrato"].value_counts())
print(tabela["duracao_contrato"].value_counts(normalize=True).map("{:.1%}".format))

# > numeric_only > está instruindo o pandas a considerar apenas as colunas numéricas ao executar a operação
print(tabela.groupby("duracao_contrato").mean(numeric_only=True))
print(tabela.groupby("assinatura").mean(numeric_only=True))

# Observação --> Contrato Mensal sempre cancela

# A linha de códig abaixo ignora os mensais
tabela = tabela[tabela["duracao_contrato"]!="Monthly"]

#Resultado sem os valores mensais cancelamentos caiu de 56,7% para 46,1% queda de 10% em cancelamento
#Solução retirar as assinaturas mensais e tentar converter os clientes para assinatura trimestral ou anual
print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

# 5 -> Analise profunda da Base (Encontrando a causa dos cancelamentos)
# o loop for cria uma variavel coluna onde ela e utilizada o histograma para gerar um gráfico para cada coluna 
# e facilitar a analise

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
    grafico.show()

# Todas as pessoas com mais de 50 anos está cancelando 
# (Precisamos de algo que seja atrativo para essas pessoas se manterem)

coluna = "idade"
grafico = px.histogram(tabela, x=coluna, color="cancelou")
grafico.show()

#Apartir de 5 ligações no call center está tendo cancelamento
#Melhorar o atendimento no call center e proporcinonar uma boa experiência ao cliente 

coluna = "ligacoes_callcenter"
grafico = px.histogram(tabela, x=coluna, color="cancelou")
grafico.show()

#Apartir de 20 dias em atraso os clientes efetuam o cancelamento
#Oferecer alguma recompensa para quando o pagamento for efetuado na data correta isso fará com que o cliente seja pontual
coluna = "dias_atraso"
grafico = px.histogram(tabela, x=coluna, color="cancelou")
grafico.show()

#Clientes que gastam menos de 500 tem alta tendência de efetuar o cancelamento
#Descobrir o que faz ele desistir tão cedo 
coluna = "total_gasto"
grafico = px.histogram(tabela, x=coluna, color="cancelou")
grafico.show()