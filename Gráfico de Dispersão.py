# Visualização de Dados em Python
import matplotlib.pyplot as plt

x1 = [1,3,5,7,9]
y1 = [2,3,7,1,0]
z = [200,250,400,330,100]

titulo = "Scatterplot: gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo y"

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x1,y1, color = "#000099", linestyle = "-")
plt.scatter(x1,y1, label = "Meus pontos", color = "k", marker = ".", s = z)
plt.legend()
plt.show()

#plt.savefig("figura1.png")#para salvar o gráfico


# Biblioteca de Configuração de Gráficos no Python
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html