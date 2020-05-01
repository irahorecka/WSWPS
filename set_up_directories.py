from docx import Document

def write_docx(parent_dir_name, header):
    document = Document()
    document.add_heading(header)
    document.save(f"{parent_dir_name}.docx")

def get_header(file_key):
    headers = {
        'quote': 'Quote'
        'origin': 'Quote Origin'
    }
