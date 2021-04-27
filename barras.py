import matplotlib.pyplot as plt

def grafico(x, y):
  plt.bar(x, y)
  plt.title('SEU TÍTULO')
  plt.xlabel('NOME DO EIXO X')
  plt.ylabel('NOME DO EIXO Y')
  plt.savefig('barras.png')
  plt.close()