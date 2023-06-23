
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4,inch

file_name = "test.pdf"

doc=SimpleDocTemplate(file_name,pagesize=(A4[0],A4[1]),topMargin = 0.1 * inch,bottomMargin =  0.1 * inch,leftMargin=0.1 * inch,rightMargin=0.1 * inch)
story = []
paragraph_style = getSampleStyleSheet()['BodyText']
paragraph = Paragraph("Hello, World!",paragraph_style)
story.append(paragraph)
doc.build(story)