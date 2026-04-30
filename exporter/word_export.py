
from docx import Document
import os

def export_to_word(content, filename):
    doc = Document()
    doc.add_paragraph(content)

    path = f"outputs/{filename}.docx"
    doc.save(path)
    return path
