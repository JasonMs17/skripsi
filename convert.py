from docling.document_converter import DocumentConverter

file_path = "SKRIPSI_JASON_NATANAEL.docx"

converter = DocumentConverter()
result = converter.convert(file_path)

markdown_text = result.document.export_to_markdown()
print(markdown_text)
with open("output.md", "w", encoding="utf-8") as f:
    f.write(markdown_text)
