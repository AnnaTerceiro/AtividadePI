import matplotlib.pyplot as plt

def grafico(x, y):
  plt.plot(x, y)
  plt.title('SEU TÍTULO')
  plt.xlabel('NOME DO EIXO X')
  plt.ylabel('NOME DO EIXO Y')
  plt.savefig('linha.png')
  plt.close()