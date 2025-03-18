from fpdf import FPDF
from datetime import datetime

# VARIÁVEIS
value = float(input("Digite o valor do serviço: "))
value_formated = f'R$ {value:.2f}'
client = input("Digite o nome do cliente: ")
description = input("Digite a descrição do serviço: ")

# DATA
months = [
    'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
    'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
]

date = datetime.today()
month = months[date.month - 1]
current_date = date.strftime('%d/%m/%Y')
current_format = f'Uberaba, {date.strftime(f'%d de {month} de %Y')}'

# LAYOUT
pdf = FPDF(orientation="L", unit="mm", format=(315, 800))
pdf.add_page()
pdf.set_font("Arial", size=36)

# IMAGEM DE FUNDO
pdf.image("img/recibo.png", x=0, y=0)

# ADICIONANDO O VALOR DO SERVIÇO NO RECIBO
pdf.set_xy(30, 60)
pdf.set_font("Arial", size=36)
pdf.cell(0, 10, value_formated)

# ADICIONANDO O NOME DO CLIENTE
pdf.set_xy(30, 125)
pdf.set_font("Arial", size=36)
pdf.cell(0, 10, client)

# DESCRIÇÃO COM QUEBRA AUTOMÁTICA DE LINHA
pdf.set_xy(30, 180)
pdf.set_font("Arial", size=24)
pdf.multi_cell(300, 10, description)

# DATA DO RECIBO
pdf.set_xy(30, 294)
pdf.set_font("Arial", size=36)
pdf.cell(0, 0, current_date)

# DATA NO FORMATO POR EXTENSO
pdf.set_xy(260, 205)
pdf.set_font("Arial", size=36)
pdf.cell(0, 0, current_format)

pdf.set_xy(600, 40)
pdf.set_font("Arial", size=48)
pdf.set_text_color(95, 130, 164)
pdf.cell(0, 10, value_formated)

# GERANDO O PDF
pdf.output("dados/recibo.pdf")
