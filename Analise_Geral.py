import pandas as pd  
from fpdf import FPDF

df = pd.read_csv(r"C:\Users\embri\OneDrive\Desktop\PDPD - Processos Estocásticos\Dados_coracao.csv", sep=";") 

media = df[['Idade', 'PA', 'Col']].mean()
mediana = df[['Idade', 'PA', 'Col']].median()
moda = df[['Idade', 'PA', 'Col']].mode()
desvio_padrao = df[['Idade', 'PA', 'Col']].std()
quartis = df[['Idade', 'PA', 'Col']].quantile([0.25, 0.5, 0.75])
iqr = quartis.loc[0.75] - quartis.loc[0.25]
frequencia_sexo = df['Sexo'].value_counts()
frequencia_acucar = df['Açucar'].value_counts()
frequencia_sexo_percentual = df['Sexo'].value_counts(normalize=True) * 100
frequencia_acucar_percentual = df['Açucar'].value_counts(normalize=True) * 100
tabela_contingencia = pd.crosstab(df['Sexo'], df['Açucar'])
media_por_sexo = df.groupby('Sexo')[['PA', 'Col']].mean()
desvio_por_acucar = df.groupby('Açucar')[['PA', 'Col']].std()

def create_pdf():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Relatório de Estatísticas Descritivas", ln=True, align="C")
    pdf.ln(10)

    # Adicionar as estatísticas ao PDF com formatação
    pdf.set_font("Arial", size=12)

    # Média
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Média:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"Média de Idade, PA e Colesterol:\n{media}\n")
    pdf.ln(5)

    # Mediana
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Mediana:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"Mediana de Idade, PA e Colesterol:\n{mediana}\n")
    pdf.ln(5)

    # Moda
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Moda:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"Moda de Idade, PA e Colesterol:\n{moda}\n")
    pdf.ln(5)

    # Desvio Padrão
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Desvio Padrão:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"Desvio Padrão de Idade, PA e Colesterol:\n{desvio_padrao}\n")
    pdf.ln(5)

    # Quartis
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Quartis:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"Quartis de Idade, PA e Colesterol:\n{quartis}\n")
    pdf.ln(5)

    # Intervalo interquartil (IQR)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Intervalo Interquartil (IQR):", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"IQR de Idade, PA e Colesterol:\n{iqr}\n")
    pdf.ln(5)

    # Frequências de variáveis categóricas
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Frequências:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"Frequência de Sexo:\n{frequencia_sexo}\n")
    pdf.multi_cell(0, 10, txt=f"Frequência de Açúcar:\n{frequencia_acucar}\n")
    pdf.ln(5)

    # Frequência relativa
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Frequência Relativa (percentual):", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"Frequência relativa de Sexo:\n{frequencia_sexo_percentual}\n")
    pdf.multi_cell(0, 10, txt=f"Frequência relativa de Açúcar:\n{frequencia_acucar_percentual}\n")
    pdf.ln(5)

    # Tabela de Contingência
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Tabela de Contingência entre Sexo e Açúcar:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"Tabela de Contingência:\n{tabela_contingencia}\n")
    pdf.ln(5)

    # Média por Sexo
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Média de PA e Colesterol por Sexo:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"Média de PA e Colesterol por Sexo:\n{media_por_sexo}\n")
    pdf.ln(5)

    # Desvio Padrão por Açúcar
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Desvio Padrão de PA e Colesterol por Açúcar:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"Desvio Padrão de PA e Colesterol por Açúcar:\n{desvio_por_acucar}\n")
    pdf.ln(10)

    pdf.output(r"C:\Users\embri\OneDrive\Desktop\PDPD - Processos Estocásticos\Relatorio_Estatisticas_Descritivas_Refinado.pdf")

create_pdf()
