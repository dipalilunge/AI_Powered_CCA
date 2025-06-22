import fitz  # PyMuPDF
import markdown

def extract_text(file):
    if file.name.endswith(".pdf"):
        try:
            # Open the PDF file from the uploaded stream
            doc = fitz.open(stream=file.read(), filetype="pdf")
            text = ""
            for page in doc:
                text += page.get_text()
            return text
        except Exception as e:
            return f"Error reading PDF: {str(e)}"

    elif file.name.endswith(".md"):
        try:
            # Decode and convert markdown to HTML (or raw text as needed)
            md_content = file.read().decode("utf-8")
            return md_content  # You can use `markdown.markdown(md_content)` if you want HTML
        except Exception as e:
            return f"Error reading Markdown file: {str(e)}"

    else:
        return "Unsupported file format. Please upload a .pdf or .md file."
