# Analise gráfica da distribuição entre Duas Variáveis
import pandas as pd  
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from fpdf import FPDF

df = pd.read_csv(r"C:\Users\embri\OneDrive\Desktop\PDPD - Processos Estocásticos\Dados_coracao.csv", sep=";") 

def create_pdf():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Relatório com Análise Gráfica da Distribuição Entre Duas Variáveis", ln=True, align="C")
    pdf.ln(10)
    
    # Grafico Scatter:
    
    # Scatter Plot: Relação entre Idade e PA
    plt.figure(figsize=(16, 9))
    sns.scatterplot(x='Idade', y='PA', data=df, hue = 'Idade', palette='magma', legend=False)
    plt.title('Relação entre Idade e Pressão Arterial')
    plt.xlabel('Idade')
    plt.ylabel('Pressão Arterial')
    plt.tight_layout()
    plt.savefig(f"Scatter Plot - Relação entre Idade e PA.png", format='png')
    plt.close()
    pdf.add_page()
    pdf.image("Scatter Plot - Relação entre Idade e PA.png", x=10, y=30, w=180)
    # Scatter Plot: Relação entre Idade e Col
    plt.figure(figsize=(16, 9))
    sns.scatterplot(x='Idade', y='Col', data=df, hue = 'Idade', palette='magma', legend=False)
    plt.title('Relação entre Idade e Colesterol')
    plt.xlabel('Idade')
    plt.ylabel('Colesterol')
    plt.tight_layout()
    plt.savefig(f"Scatter Plot - Relação entre Idade e Colesterol.png", format='png')
    plt.close()
    pdf.add_page()
    pdf.image("Scatter Plot - Relação entre Idade e Colesterol.png", x=10, y=30, w=180)
    # Scatter Plot: Relação entre Col e PA
    plt.figure(figsize=(16, 9))
    sns.scatterplot(x='Col', y='PA', data=df, hue = 'Col', palette='rocket', legend=False)
    plt.title('Relação entre Colesterol e Pressão Arterial')
    plt.xlabel('Colesterol')
    plt.ylabel('Pressão Arterial')
    plt.tight_layout()
    
    # Grafico Boxplot:
   
    # Boxplot comparativo: Pressão Arterial por Sexo
    plt.figure(figsize=(16, 9))
    sns.boxplot(x='Sexo', y='PA', data=df, hue= 'Sexo', palette='gnuplot2', legend= False)
    plt.title('Pressão Arterial por Sexo')
    plt.xlabel('Sexo')
    plt.ylabel('Pressão Arterial')
    plt.tight_layout()
    plt.savefig(f"Boxplot comparativo: Pressão Arterial por Sexo.png", format='png')
    plt.close()
    pdf.add_page()
    pdf.image("Boxplot comparativo: Pressão Arterial por Sexo.png", x=10, y=30, w=180)
    # Boxplot comparativo: Colesterol por Sexo
    plt.figure(figsize=(16, 9))
    sns.boxplot(x='Sexo', y='Col', data=df, hue= 'Sexo', palette='rocket_r', legend= False)
    plt.title('Colesterol por Sexo')
    plt.xlabel('Sexo')
    plt.ylabel('Colesterol')
    plt.tight_layout()
    plt.savefig(f"Boxplot comparativo: Colesterol por Sexo.png", format='png')
    plt.close()
    pdf.add_page()
    pdf.image("Boxplot comparativo: Colesterol por Sexo.png", x=10, y=30, w=180)
    
    # Grafico Violin:
    
    # Violin Plot comparativo: Pressão Arterial por Idade
    plt.figure(figsize=(16, 9))
    sns.violinplot(x='Idade', y='PA', data=df, hue = 'Idade', palette='viridis', legend=False)
    plt.title('Distribuição da Pressão Arterial por Idade')
    plt.xlabel('Idade')
    plt.ylabel('Pressão Arterial')
    plt.tight_layout()
    plt.savefig(f"Violin Plot comparativo: Pressão Arterial por Idade.png", format='png')
    plt.close()
    pdf.add_page()
    pdf.image("Violin Plot comparativo: Pressão Arterial por Idade.png", x=10, y=30, w=180)
    # Violin Plot comparativo: Colesterol por Idade
    plt.figure(figsize=(16, 9))
    sns.violinplot(x='Idade', y='Col', data=df, hue = 'Idade', palette='viridis', legend=False)
    plt.title('Distribuição da Colesterol por Idade')
    plt.xlabel('Idade')
    plt.ylabel('Colesterol')
    plt.tight_layout()
    plt.savefig(f"Violin Plot comparativo: Colesterol por Idade.png", format='png')
    plt.close()
    pdf.add_page()
    pdf.image("Violin Plot comparativo: Colesterol por Idade.png", x=10, y=30, w=180)
    
    # Grafico de barras:
    
    # Gráfico de barras com as médias de PA por Sexo
    plt.figure(figsize=(16, 9))
    media_sexo = df.groupby('Sexo')[['PA', 'Col']].mean()
    media_sexo.plot(kind='bar', color=['turquoise', 'mediumorchid'])
    plt.title('Média da Pressão Arterial e Colesterol por Sexo')
    plt.xlabel('Sexo')
    plt.ylabel('Média da Pressão Arterial e Colesterol')
    plt.tight_layout()
    plt.savefig(f"Gráfico de barras com as médias de PA e Col por Sexo.png", format='png')
    plt.close()
    pdf.add_page()
    pdf.image("Gráfico de barras com as médias de PA e Col por Sexo.png", x=10, y=30, w=180)
    # Gráfico de barras com as médias de PA e Col por Açucar
    plt.figure(figsize=(16, 9))
    media_sexo = df.groupby('Açucar')[['PA', 'Col']].mean()
    media_sexo.plot(kind='bar', color=['saddlebrown', 'crimson'])
    plt.title('Média da Pressão Arterial e Colesterol por Açucar')
    plt.xlabel('Açucar')
    plt.ylabel('Média da Pressão Arterial e Colesterol')
    plt.tight_layout()
    plt.savefig(f"Gráfico de barras com as médias de PA e Col por Açucar.png", format='png')
    plt.close()
    pdf.add_page()
    pdf.image("Gráfico de barras com as médias de PA e Col por Açucar.png", x=10, y=30, w=180)
    
    pdf.output(r"C:\Users\embri\OneDrive\Desktop\PDPD - Processos Estocásticos\Relatório_Analise_Grafica_Duas.pdf")

create_pdf()