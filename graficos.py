import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Nome': ['Alice', 'Joao', 'Charlie', 'David', 'Eva', 'Diego', 'Denize', 'Claudio'],
    'Idade': [25, 30, 35, 40, 45, 60, 22, 24],
    'Profissão': ['Engenheiro', 'Médico', 'Professor', 'Advogado', 'Médico','Engenheiro', 'Estudante','Estudante'],
    'Salário': ['4500', '8000', '5000', '10000', '12000','15000', '1200','1500'],
    'Limite_Credito': ['2500', '4000', '4000', '1000', '10000','2000', '500','250'],
    'Historico_Inadimplencia': ['0', '0', '0', '1', '0','1', '0','1'],
    'Estado_Civil': ['Casamento', 'Casamento', 'Solteiro', 'Solteiro', 'Casamento','Solteiro', 'Solteiro','Solteiro'],
    'Imovel_Proprio': ['0', '0', '0', '1', '1','1', '0','0']
}
df = pd.DataFrame(data)
df.head(5)

#Gráfico de Dispersão (Scatter Plot)
sns.scatterplot(x='Salário', y='Limite_Credito', data=data)
plt.title('Salário vs Limite de credito')
plt.xlabel('Salário')
plt.ylabel('Limite de credito')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Gráfico de Box Plot
sns.boxplot(x='Idade', y='Limite_Credito', data=data)
plt.title('Limite de credito por idade')
plt.xlabel('Idade')
plt.ylabel('Limite de credito')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

#Gráfico de Barras (Bar Plot)
sns.barplot(x='Idade', y='Limite_Credito', data=data, ci=None)

# Ajustando o gráfico
plt.title('Média do Limite de Crédito por Idade')
plt.xlabel('Idade')
plt.ylabel('Média do Limite de Crédito')
plt.grid(True, linestyle='--', alpha=0.7)  # Adicionando grid para visualização

# Exibindo o gráfico
plt.show()
