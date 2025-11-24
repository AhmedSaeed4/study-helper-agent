import pypdf
import io

def extract_text(pdf_bytes): 
    try:

        pdf_stream = io.BytesIO(pdf_bytes)
        reader = pypdf.PdfReader(pdf_stream)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        cleaned_text = " ".join(text.split()).strip()
        return cleaned_text
    except Exception as e:
        return f"Error extracting PDF text: {e}"