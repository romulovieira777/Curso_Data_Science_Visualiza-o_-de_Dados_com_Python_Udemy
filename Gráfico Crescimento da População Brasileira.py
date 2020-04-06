# Crescimento da População Brasileira 1980 até 2016
# DataSUS
import matplotlib.pyplot as plt

dados = open("populacao-brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.plot(x,y)
plt.show()