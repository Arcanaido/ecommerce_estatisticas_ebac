import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('ecommerce_estatistica.csv')
print(df['Marca'].value_counts())
print('Quantidade de valores null: \n',df.isnull().sum())

notas = df['Nota_MinMax']

# Histograma da Distribuição de Notas
plt.hist(notas, bins=5, color='#87CEEB', edgecolor='#000000')
plt.title('Distribuição das Notas')
plt.xlabel('Notas')
plt.xticks(ticks=range(0,  int(notas.max()) + 1, 1))
plt.ylabel('Quantidade')
plt.grid(True)
plt.show()

# Gráfico de Dispersão notas vs N_Avaliações
n_avaliacao = df['N_Avaliações_MinMax']

plt.scatter(notas, n_avaliacao, color='#32CD32', alpha=0.6, s=30)
plt.title('Notas vs Número de Avaliações')
plt.xlabel('Número de Avaliações')
plt.ylabel('Nota Média')
plt.grid(True)
plt.show()

# Heatmap - Correlação entre Notas, Aval, Descontos, Qtd_Vendidos e Preços
colunas = ['Nota', 'N_Avaliações', 'Desconto', 'Preço']
corr = df[colunas].corr()
plt.subplot(2, 2, 3)
plt.figure(figsize = (10, 6))
sns.heatmap(corr, annot = True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de Calor - Correlação entre Variáveis Numéricas')
plt.show()

# Gráfico de Barra
contagem_genero = df['Gênero'].value_counts()

plt.figure(figsize = (10, 6))
contagem_genero.plot(kind='bar', color='#9400D3', edgecolor='#A9A9A9')
plt.title('Distribuição por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Gráfico de Pizza

df['Faixa_Desconto'] = df['Desconto'].map(lambda x:
                                          '0-20%' if x <= 20 else
                                          '21-40%' if x <= 40 else
                                          '41-60%' if x <= 60 else
                                          '61-80%' if x <= 80 else
                                          '81-100%')

contagem = df['Faixa_Desconto'].value_counts().sort_index()

plt.figure(figsize = (10, 6))
plt.pie(contagem, labels=contagem.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Set2.colors)
plt.title('Distribuição por Faixas de Desconto')
plt.legend(title='Faixa de Desconto')
plt.tight_layout()
plt.show()

# Gráfico de Densidade

plt.figure(figsize = (10, 6))
sns.kdeplot(df['Preço'], fill=True, color='#FA8072')
plt.title('Distribuição de Densidade de Preço')
plt.xlabel('Preço')
plt.ylabel('Densidade')
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico Regressão

plt.figure(figsize = (10, 6))
sns.regplot(x='Nota', y='N_Avaliações', data=df, scatter_kws={'color': '#6495ED'}, line_kws={'color': '#FF0000'})
plt.title('Relação entre Nota e Número de Avaliações')
plt.xlabel('Nota')
plt.ylabel('Número de Avaliações')
plt.grid(True)
plt.show()