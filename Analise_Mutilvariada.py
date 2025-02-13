# Analise gráfica da distribuição entre Multi Variáveis
import pandas as pd  
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from fpdf import FPDF

df = pd.read_csv(r"C:\Users\embri\OneDrive\Desktop\PDPD - Processos Estocásticos\Dados_coracao.csv", sep=";") 

def create_pdf():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Relatório com Análise Gráfica da Distribuição Entre Multi Variáveis", ln=True, align="C")
    pdf.ln(10)
    
    # Grafico Pairplot
    sns.pairplot(df[['Idade', 'PA', 'Col', 'Açucar']])  # Seleciona as variáveis que você quer ver
    plt.tight_layout()
    plt.tight_layout()
    plt.savefig(f"Gráfico de pairplot.png", format='png')
    plt.close()
    pdf.add_page()
    pdf.image("Gráfico de pairplot.png", x=10, y=30, w=180)

    # Grafico Heatmap
    correlacao = df[['Idade', 'PA', 'Col', 'Açucar']].corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlacao, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Mapa de Calor da Correlação entre as Variáveis')
    plt.tight_layout()
    plt.tight_layout()
    plt.savefig(f"Gráfico Heatmap.png", format='png')
    plt.close()
    pdf.add_page()
    pdf.image("Gráfico Heatmap.png", x=10, y=30, w=180)

    # Grafico 3D
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    x = df['Idade']
    y = df['PA']
    z = df['Col']
    ax.scatter(x, y, z, c='r', marker='o')
    ax.set_title('Gráfico 3D de Idade, PA e Colesterol')
    ax.set_xlabel('Idade')
    ax.set_ylabel('Pressão Arterial')
    ax.set_zlabel('Colesterol')
    plt.tight_layout()
    plt.savefig(f"Gráfico 3D.png", format='png')
    plt.close()
    pdf.add_page()
    pdf.image("Gráfico 3D.png", x=10, y=30, w=180)
  
    pdf.output(r"C:\Users\embri\OneDrive\Desktop\PDPD - Processos Estocásticos\Relatório_Analise_Grafica_Multi.pdf")

create_pdf()