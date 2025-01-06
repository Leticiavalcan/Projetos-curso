import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns  # Importar Seaborn para o boxplot


df = pd.read_csv("/content/BASE_SUPERMERCADO (1).csv")
df.head(10)

#Traga a média e a mediana dos preços - coluna Preco_Normal - por categoria de produto.
# Identifique as categorias que parecem ter um valor de média abaixo ou acima da mediana.

# Calcular média e mediana por categoria de produto
preco_estatisticas = df.groupby('Categoria')['Preco_Normal'].agg(['mean', 'median']).reset_index()

# Adicionar uma coluna para identificar se a média está abaixo ou acima da mediana
preco_estatisticas['Media_vs_Mediana'] = preco_estatisticas.apply(
    lambda row: 'Abaixo da Mediana' if row['mean'] < row['median'] else 'Acima da Mediana',
    axis=1
)

# Exibir as estatísticas
print(preco_estatisticas)

#traga o desvio padrão por categoria de produto.
# Qual o comportamento da média e mediana nas categorias com maior desvio? Ocomportamento foi que a media se manteve acima da mediana em ambos valores
#mais altos do desvio padrao

# Calcular o desvio padrão por categoria
desvio_padrao = df.groupby('Categoria')['Preco_Normal'].std().reset_index()

# Exibir o resultado
print("Desvio padrão por categoria:")
print(desvio_padrao)

#Plot um boxplot da distribuição do Preco_Normal para a categoria que você identificou que tem o maior desvio padrão. 
#Como é a distribuição desses dados segundo o boxplot? Você identifica muitos outliers? Embora haja uma diferença nos preços, nao identifiquei muitos outliers

# Identificar a categoria com o maior desvio padrão
categoria_maior_desvio = desvio_padrao.loc[desvio_padrao['Preco_Normal'].idxmax(), 'Categoria']

# Filtrar os dados da categoria com o maior desvio padrão
dados_categoria_maior_desvio = df[df['Categoria'] == categoria_maior_desvio]

# Plotar o boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Categoria', y='Preco_Normal', data=dados_categoria_maior_desvio)
plt.title(f'Boxplot de Preco_Normal para a Categoria: {categoria_maior_desvio}')
plt.show()

# Calcular a média de descontos por categoria
media_descontos = df.groupby('Categoria')['Desconto'].mean().reset_index()

# Plotar o gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(media_descontos['Categoria'], media_descontos['Desconto'], color='skyblue')

# Adicionar título e rótulos
plt.title('Média de Descontos por Categoria', fontsize=16)
plt.xlabel('Categoria', fontsize=12)
plt.ylabel('Média de Desconto', fontsize=12)
plt.xticks(rotation=45, ha='right')  # Rotacionar as categorias para uma melhor visualização

# Exibir o gráfico
plt.tight_layout()  # Ajustar a exibição
plt.show()

#Plote um gráfico de mapa interativo agrupando os dados por categoria, marca e trazendo a média de desconto.

# Calcular a média de desconto por categoria e marca
media_desconto_categoria_marca = df.groupby(['Categoria', 'Marca'])['Desconto'].mean().reset_index()


fig = px.scatter_geo(
    media_desconto_categoria_marca,
    locations="Categoria",  # Se houver localização, pode ser latitude ou coordenadas geográficas
    size="Desconto",  # O tamanho das bolhas pode representar a média do desconto
    color="Marca",  # A cor pode representar a marca
    hover_name="Categoria",  # Informações sobre a categoria ao passar o mouse
    hover_data=["Marca", "Desconto"],  # Mais dados a exibir no hover
    title="Média de Desconto por Categoria e Marca"
)

# Exibir o gráfico
fig.show()