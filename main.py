
#https://paulovasconcellos.com.br/15-comandos-de-matplotlib-que-talvez-voc%C3%AA-n%C3%A3o-conhe%C3%A7a-17cf88a75119

####################################################
# Bibliotecas do Sistema
####################################################
import matplotlib.pyplot as plt
import random



####################################################
# Arquivos com funções definidas pelo programador(a)
####################################################
import linha
import barras
import boxplot


#Geração de dados aleatórios para popular os eixos x e y dos grááficos
x = []
y = []
for i in range(20):
  y.append(int (random.random() * 10))
  x.append(i)


#chamada das funções criadas nos outros arquivos para os gráficos
linha.grafico(x, y)
barras.grafico(x, y)
boxplot.grafico(x, y)