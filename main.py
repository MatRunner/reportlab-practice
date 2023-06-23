
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4, inch
from reportlab.pdfgen import canvas
from style.pdf import PERFORMANCE
import json
import numpy

file_name = "test.pdf"

doc = SimpleDocTemplate(file_name, pagesize=(
    A4[0], A4[1]), topMargin=0.1 * inch, bottomMargin=0.1 * inch, leftMargin=0.1 * inch, rightMargin=0.1 * inch)
story = []
# style
normal_style = getSampleStyleSheet()['Heading2']
# normal_style.bold = Tr
# paragraph
paragraph = Paragraph("Hello, World!", normal_style)
story.append(paragraph)
# table
table_style = PERFORMANCE.get()
table_data = []
with open('./raw.json', 'r') as f:
    _data = json.load(f)
    category = []
    value = []
    for key in _data:
        category.append(key)
        value.append(_data[key])
    table_data.append(category)
    table_data.extend(list(map(list, zip(*value))))

table = Table(table_data)
table.setStyle(table_style)
story.append(table)


doc.multiBuild(story)
