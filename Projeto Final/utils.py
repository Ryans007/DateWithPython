import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf
from keras import backend as K
from keras.models import Sequential # type: ignore
from keras.layers import Dense, Dropout # type: ignore

def my_barplot(df, column_names):
    num_columns = len(column_names)
    num_rows = (num_columns + 2) // 3  
    fig, axes = plt.subplots(num_rows, 3, figsize=(18, 5 * num_rows))  
    plt.subplots_adjust(hspace=0.4, wspace=0.4)  

    axes = axes.flatten() if num_rows > 1 else [axes]

    for i, column_name in enumerate(column_names):
        column_groupby = df.groupby(df[column_name]).size()
        barplot = sns.barplot(
            x=column_groupby.index,
            y=column_groupby.values,
            palette=sns.light_palette("navy", reverse=True),  
            ax=axes[i]  
        )

        axes[i].set_title(f'Distribuição de {column_name}', fontsize=14, fontweight='bold')
        axes[i].set_xlabel(column_name, fontsize=12)
        axes[i].set_ylabel('Frequência', fontsize=12)

        axes[i].tick_params(axis='x', rotation=45, labelsize=10)
        axes[i].tick_params(axis='y', labelsize=10)
        
        for p in barplot.patches:
            barplot.annotate(
                format(p.get_height(), ".0f"),  # Formato do número # type: ignore
                (p.get_x() + p.get_width() / 2., p.get_height()),  # Posição # type: ignore
                ha="center", va="center", fontsize=10, color="black", xytext=(0, 5),
                textcoords="offset points"
            )
    for j in range(len(column_names), len(axes)):
        fig.delaxes(axes[j])
    plt.tight_layout()
    plt.show()


def my_barplot_single(df, column_name):
    column_groupby = df.groupby(df[column_name]).size()

    plt.figure(figsize=(10, 6))
    barplot = sns.barplot(
        x=column_groupby.index,
        y=column_groupby.values,
        palette=sns.light_palette("navy", reverse=True)  
    )

    plt.title(f'Distribuição de {column_name}', fontsize=14, fontweight='bold')
    plt.xlabel(column_name, fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)

    for p in barplot.patches:
        barplot.annotate(
            format(p.get_height(), ".0f"),  # Formato do número # type: ignore
            (p.get_x() + p.get_width() / 2., p.get_height()),  # Posição # type: ignore
            ha="center", va="center", fontsize=10, color="black", xytext=(0, 5),
            textcoords="offset points"
        )
    plt.tight_layout()
    plt.show()

def my_numerical_graphics(df, column_name):
  fig, axes = plt.subplots(1, 3, figsize=(18, 5))
  
  sns.boxplot(data=df, x=f'{column_name}', ax=axes[0])
  axes[0].set_title(f'Boxplot de {column_name}')

  sns.histplot(data=df, x=f'{column_name}', kde=True, ax=axes[1])
  axes[1].set_title(f'Histograma de {column_name}')

  sns.scatterplot(data=df, x=range(len(df)), y=f'{column_name}', ax=axes[2])
  axes[2].set_title(f'Scatter Plot de {column_name}')
  axes[2].set_xlabel('Índice')

  plt.tight_layout()
  plt.show()

def my_heatmap(dataframe):
    corr_matrix = dataframe.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Matriz de Correlação das Variáveis', fontsize=16)
    plt.show()

def f1_score(y_true, y_pred):
    y_pred = tf.round(y_pred) 
    
    true_positives = tf.reduce_sum(tf.cast(tf.equal(y_true, 1) & tf.equal(y_pred, 1), tf.float32))
    possible_positives = tf.reduce_sum(tf.cast(tf.equal(y_true, 1), tf.float32))
    predicted_positives = tf.reduce_sum(tf.cast(tf.equal(y_pred, 1), tf.float32))
    
    precision = true_positives / (predicted_positives + K.epsilon())
    recall = true_positives / (possible_positives + K.epsilon())
    
    return 2 * (precision * recall) / (precision + recall + K.epsilon())