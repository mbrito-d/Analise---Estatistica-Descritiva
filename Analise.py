# Analise gráfica da distribuição de Variáveis Individuais
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
    pdf.cell(200, 10, txt="Relatório com Análise Gráfica da Distribuição de Variáveis Individuais", ln=True, align="C")
    pdf.ln(10)
    
    # Histogramas:
    #Idade
    plt.figure(figsize=(16, 9))
    palette = sns.color_palette('magma', as_cmap=True)
    n, bins, patches = plt.hist(df['Idade'], bins=10, edgecolor='black')
    # Atribuindo uma cor para cada barra do histograma
    for i in range(len(patches)):
        color = palette(i / len(patches))  # Distribuindo as cores pela paleta
        patches[i].set_facecolor(color)
    plt.title('Distribuição da Idade')
    plt.xlabel('Idade')
    plt.ylabel('Frequência')
    plt.tight_layout()
    plt.savefig(f"Histograma - Distribuição da Idade.png", format='png')
    plt.close()
    pdf.add_page()
    pdf.image("Histograma - Distribuição da Idade.png", x=10, y=30, w=180)
    # Colesterol
    plt.figure(figsize=(16, 9))
    palette = sns.color_palette('rocket', as_cmap=True)
    n, bins, patches = plt.hist(df['Col'], bins=10, edgecolor='black')
    for i in range(len(patches)):
        color = palette(i / len(patches))
        patches[i].set_facecolor(color)
    plt.title('Distribuição do Colesterol')
    plt.xlabel('Colesterol')
    plt.ylabel('Frequência')
    plt.tight_layout()
    plt.savefig(f"Histograma - Distribuição do Colesterol.png", format='png')
    plt.close()
    pdf.add_page()
    pdf.image("Histograma - Distribuição do Colesterol.png", x=10, y=30, w=180)
    # Pressão Arterial
    plt.figure(figsize=(16, 9))
    palette = sns.color_palette('viridis', as_cmap=True)
    n, bins, patches = plt.hist(df['PA'], bins=10, edgecolor='black') 
    for i in range(len(patches)):
        color = palette(i / len(patches))
        patches[i].set_facecolor(color)
    plt.title('Distribuição da Pressão Arterial')
    plt.xlabel('Pressão Arterial')
    plt.ylabel('Frequência')
    plt.tight_layout()
    plt.savefig(f"Histograma - Distribuição da PA.png", format='png')
    plt.close()
    pdf.add_page()
    pdf.image("Histograma - Distribuição da PA.png", x=10, y=30, w=180)

    #Boxplot:
    #Pressão Arterial por sexo
    plt.figure(figsize=(16, 9))
    sns.boxplot(x='Sexo', y='PA', data=df, hue = 'Sexo', palette='gnuplot2', legend= False)
    plt.title('Boxplot da Pressão Arterial por Sexo')
    plt.tight_layout()
    plt.savefig(f"Boxplot - PA relação a sexo.png", format='png')
    plt.close()
    pdf.add_page()
    pdf.image("Boxplot - PA relação a sexo.png", x=10, y=30, w=180)
    #Pressão Arterial por idade
    plt.figure(figsize=(16, 9))
    sns.boxplot(x='Idade', y='PA', data=df, hue = 'Idade', palette='rocket', legend= False)
    plt.title('Boxplot da Pressão Arterial por Idade')
    plt.tight_layout()
    plt.savefig(f"Boxplot - PA relação a Idade.png", format='png')
    plt.close()
    pdf.add_page()
    pdf.image("Boxplot - PA relação a Idade.png", x=10, y=30, w=180)
    #Colesterol em relação ao sexo  
    plt.figure(figsize=(16, 9))
    sns.boxplot(x='Sexo', y='Col', data=df, hue = 'Sexo', palette='gnuplot2', legend=False)
    plt.title('Boxplot da Colesterol por Sexo')
    plt.tight_layout()
    plt.savefig(f"Boxplot - COL relação a sexo.png", format='png')
    plt.close()
    pdf.add_page()
    pdf.image("Boxplot - COL relação a sexo.png", x=10, y=30, w=180)
    #Colesterol em relação a idade
    plt.figure(figsize=(16, 9))
    sns.boxplot(x='Idade', y='Col', data=df, hue = 'Idade', palette='rocket_r', legend= False)
    plt.title('Boxplot da Colesterol por Idade')
    plt.tight_layout()
    plt.savefig(f"Boxplot - COL relação a Idade.png", format='png')
    plt.close()
    pdf.add_page()
    pdf.image("Boxplot - COL relação a Idade.png", x=10, y=30, w=180)

    #Grafico em Barra:
    #Sexo
    plt.figure(figsize=(16, 9))
    sexo_counts = df['Sexo'].value_counts()
    cores = ['turquoise', 'mediumorchid']
    sexo_counts.plot(kind='bar', color=cores)
    plt.title('Sexo')
    plt.xlabel('Sexo')
    plt.ylabel('Quantidade')
    plt.tight_layout()
    plt.savefig(f"Barra - Sexo.png", format='png')
    plt.close()
    pdf.add_page()
    pdf.image("Barra - Sexo.png", x=10, y=30, w=180)
    #Açucar
    plt.figure(figsize=(16, 9))
    acucar_counts = df['Açucar'].value_counts()
    cores = ['saddlebrown', 'crimson']
    acucar_counts.plot(kind='bar', color=cores)
    plt.title('Açucar')
    plt.xlabel('Açucar')
    plt.ylabel('Quantidade')
    plt.tight_layout()
    plt.savefig(f"Barra - Açucar.png", format='png')
    plt.close()
    pdf.add_page()
    pdf.image("Barra - Açucar.png", x=10, y=30, w=180)

    #Pie Chart:
    #Açucar
    plt.figure(figsize=(16, 9))
    df['Açucar'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['darkmagenta', 'mediumvioletred'])
    plt.title('Proporção de Açúcar')
    plt.ylabel('')  # Remove o rótulo do eixo y
    plt.tight_layout()
    plt.savefig(f"Pie Chart - Açucar.png", format='png')
    plt.close()
    pdf.add_page()
    pdf.image("Pie Chart - Açucar.png", x=10, y=30, w=180)
    #Sexo
    plt.figure(figsize=(16, 9))
    df['Sexo'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['aqua', 'springgreen'])
    plt.title('Sexo')
    plt.ylabel('')  # Remove o rótulo do eixo y
    plt.tight_layout()
    plt.savefig(f"Pie Chart - Sexo.png", format='png')
    plt.close()
    pdf.add_page()
    pdf.image("Pie Chart - Sexo.png", x=10, y=30, w=180)

    pdf.output(r"C:\Users\embri\OneDrive\Desktop\PDPD - Processos Estocásticos\Relatório_Analise_Grafica.pdf")

create_pdf()