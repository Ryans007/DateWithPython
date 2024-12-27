import seaborn as sns
import matplotlib.pyplot as plt

# Função para exibição de Dados Categóricos
def my_barplot(df, column_names):
    # Definir o layout da figura com subplots
    num_columns = len(column_names)
    num_rows = (num_columns + 2) // 3  # Calcula o número de linhas dinamicamente (arredonda para cima)
    fig, axes = plt.subplots(num_rows, 3, figsize=(18, 5 * num_rows))  # Ajusta a altura dinamicamente
    plt.subplots_adjust(hspace=0.4, wspace=0.4)  # Ajusta espaçamento entre subplots

    # Garantir que `axes` seja uma matriz plana para evitar erros de índice
    axes = axes.flatten() if num_rows > 1 else [axes]

    # Loop pelas colunas e criação de gráficos em cada subplot
    for i, column_name in enumerate(column_names):
        # Agrupar os dados por contagem de frequência
        column_groupby = df.groupby(df[column_name]).size()

        # Criar o gráfico de barras no subplot correspondente
        barplot = sns.barplot(
            x=column_groupby.index,
            y=column_groupby.values,
            palette=sns.light_palette("navy", reverse=True),  # Paleta de cores
            ax=axes[i]  # Subplot correspondente
        )

        # Título e rótulos dos eixos
        axes[i].set_title(f'Distribuição de {column_name}', fontsize=14, fontweight='bold')
        axes[i].set_xlabel(column_name, fontsize=12)
        axes[i].set_ylabel('Frequência', fontsize=12)

        # Rotacionar rótulos do eixo x, se necessário
        axes[i].tick_params(axis='x', rotation=45, labelsize=10)
        axes[i].tick_params(axis='y', labelsize=10)

        # Adicionar os valores no topo de cada barra
        for p in barplot.patches:
            barplot.annotate(
                format(p.get_height(), ".0f"),  # Formato do número # type: ignore
                (p.get_x() + p.get_width() / 2., p.get_height()),  # Posição # type: ignore
                ha="center", va="center", fontsize=10, color="black", xytext=(0, 5),
                textcoords="offset points"
            )

    # Ocultar subplots extras (caso o número de colunas seja menor que o número total de subplots)
    for j in range(len(column_names), len(axes)):
        fig.delaxes(axes[j])

    # Ajustar o layout para evitar sobreposição
    plt.tight_layout()

    # Exibir o gráfico
    plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

import seaborn as sns
import matplotlib.pyplot as plt

def my_numerical_graphics(df, column_name):
  # Configuração da figura
  fig, axes = plt.subplots(1, 3, figsize=(18, 5))

  # Boxplot
  sns.boxplot(data=df, x=f'{column_name}', ax=axes[0])
  axes[0].set_title(f'Boxplot de {column_name}')

  # Histograma
  sns.histplot(data=df, x=f'{column_name}', kde=True, ax=axes[1])
  axes[1].set_title(f'Histograma de {column_name}')

  # Scatter plot
  sns.scatterplot(data=df, x=range(len(df)), y=f'{column_name}', ax=axes[2])
  axes[2].set_title(f'Scatter Plot de {column_name}')
  axes[2].set_xlabel('Índice')

  # Exibir a figura
  plt.tight_layout()
  plt.show()
