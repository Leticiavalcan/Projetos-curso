import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Projeto
# Leia o arquivo ‘ecommerce_estatistica.csv’ dentro de um dataframe .

# Faça uma análise detalhada dos dados, descubra quais dados gostaria de destacar e crie os seguintes gráficos:

# Gráfico de Histograma

# Gráfico de dispersão

# Mapa de calor

# Gráfico de barra

# Gráfico de pizza

# Gráfico de densidade

# Gráfico de Regressão



# Carregar o arquivo CSV
file_path = r"C:\Users\leticiacavalcante\Downloads\ecommerce_preparados.csv"  # Atualize o caminho conforme necessário
df = pd.read_csv(file_path)

# Tratamento inicial de dados
df_clean = df.drop(columns=['Unnamed: 0', 'Review1', 'Review2', 'Review3'])  # Remover colunas irrelevantes
df_clean['Qtd_Vendidos'] = pd.to_numeric(df_clean['Qtd_Vendidos'], errors='coerce')  # Converter para numérico

# Preencher valores ausentes em variáveis numéricas com a mediana
numerical_columns = ['Nota', 'N_Avaliações', 'Desconto', 'Qtd_Vendidos', 'Preço']
for col in numerical_columns:
    df_clean[col].fillna(df_clean[col].median(), inplace=True)

# Preencher valores ausentes em variáveis categóricas com "Não especificado"
categorical_columns = ['Material', 'Gênero']
for col in categorical_columns:
    df_clean[col].fillna('Não especificado', inplace=True)

# Configuração de estilo para gráficos
sns.set_theme(style="whitegrid")  # Configura o estilo diretamente com o Seaborn

# Gráficos
# 1. Histograma da distribuição de preços
plt.figure(figsize=(10, 6))
sns.histplot(df_clean['Preço'], bins=30, kde=True, color='blue')
plt.title('Distribuição de Preços', fontsize=16)
plt.xlabel('Preço', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 2. Gráfico de dispersão (Nota vs. Preço)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_clean, x='Preço', y='Nota', alpha=0.7)
plt.title('Dispersão: Nota vs. Preço', fontsize=16)
plt.xlabel('Preço', fontsize=12)
plt.ylabel('Nota', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 3. Mapa de calor das correlações
numerical_data = df_clean.select_dtypes(include=['float64', 'int64'])  # Apenas variáveis numéricas
plt.figure(figsize=(12, 8))
sns.heatmap(numerical_data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de Calor das Correlações', fontsize=16)
plt.show()

# 4. Gráfico de barra (Frequência de marcas)
marca_counts = df_clean['Marca'].value_counts()[:10]  # Top 10 marcas
plt.figure(figsize=(12, 6))
sns.barplot(x=marca_counts.index, y=marca_counts.values, palette='viridis')
plt.title('Top 10 Marcas Mais Frequentes', fontsize=16)
plt.xlabel('Marca', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.xticks(rotation=45)
plt.show()

# 5. Gráfico de pizza (Distribuição dos gêneros)
genero_counts = df_clean['Gênero'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(genero_counts, labels=genero_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Distribuição dos Gêneros', fontsize=16)
plt.show()

# 6. Gráfico de densidade (Distribuição de preços)
plt.figure(figsize=(10, 6))
sns.kdeplot(df_clean['Preço'], shade=True, color='green')
plt.title('Densidade de Preços', fontsize=16)
plt.xlabel('Preço', fontsize=12)
plt.ylabel('Densidade', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 7. Gráfico de regressão (Preço vs. Nota)
plt.figure(figsize=(10, 6))
sns.regplot(data=df_clean, x='Preço', y='Nota', scatter_kws={'alpha':0.6}, line_kws={'color': 'red'})
plt.title('Regressão: Preço vs. Nota', fontsize=16)
plt.xlabel('Preço', fontsize=12)
plt.ylabel('Nota', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()