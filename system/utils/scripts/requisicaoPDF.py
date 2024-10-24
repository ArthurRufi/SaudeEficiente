from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle

def criar_pdf(nome_arquivo, nome_paciente, data, exames_selecionados):
    c = canvas.Canvas(nome_arquivo, pagesize=A4)
    largura, altura = A4
    ajustealtura = 300
    for x in exames_selecionados:
        ajustealtura += 13
        print(exames_selecionados)
        print(ajustealtura)
    

    # Cabeçalho
    c.setFont("Helvetica-Bold", 20)
    c.drawString(100, altura - 30, "Multi Técnica Laboratório Universitário MT")
    c.setFont("Helvetica", 10)
    c.drawString(30, altura - 70, "Endereço: Rua Exemplo, 123 - Cidade - Estado - CEP")
    c.drawString(30, altura - 85, "Telefone: (21) 9999-9999 | Email: contato@laboratorio.com")

    # Informações do paciente
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30, altura - 120, "Nome do Paciente:")
    c.setFont("Helvetica", 10)
    c.drawString(150, altura - 120, nome_paciente)
    
    c.drawString(30, altura - 140, "Data de Solicitação:")
    c.drawString(150, altura - 140, data)

    # Criar uma tabela simples para os exames
    c.setFont("Helvetica-Bold", 20)
    c.drawString(180, altura - 200, "Exames Solicitados:")

    # Criar uma tabela com os exames
    dados_exames = [["Exame", "Selecionado"]]
    for exame in exames_selecionados:
        dados_exames.append([exame, "✔"])

    tabela = Table(dados_exames, colWidths=[300, 50])
    estilo = TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                         ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                         ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                         ("GRID", (0, 0), (-1, -1), 1, colors.black)])
    tabela.setStyle(estilo)

    # Posição da tabela
    tabela.wrapOn(c, largura, altura)
    tabela.drawOn(c, 100, altura - ajustealtura)

    c.setFont("Helvetica", 10)
    c.drawString(130, altura - 800, "Assinatura Medico: ___________________________________________________")
    # Salvar o PDF
    c.save()

# Exemplo de uso
exames = ["adasdaksd", "adasdaksd", "adasdaksd", "adasdaksd", "adasdaksd", "adasdaksd", "adasdaksd", "adasdaksd" ,"adasdaksd", "adasdaksd" ,"adasdaksd", "adasdaksd"  ]
criar_pdf("solicitacao_exame.pdf", "João da Silva", "24/10/2024", exames)
