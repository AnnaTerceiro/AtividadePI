import matplotlib.pyplot as plt

def grafico(x, y):
  plt.boxplot(x, y)
  plt.title('SEU TÍTULO')
  plt.xlabel('NOME DO EIXO X')
  plt.ylabel('NOME DO EIXO Y')
  plt.savefig('boxplot.png')
  plt.close()