
from reportlab.pdfgen import canvas

def export_to_pdf(content, filename):
    path = f"outputs/{filename}.pdf"
    c = canvas.Canvas(path)
    c.drawString(100, 800, content[:1000])
    c.save()
    return path
