import os
import PyPDF2

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a single PDF file.
    Args:
        pdf_path (str): Path to the PDF file.
    Returns:
        str: Extracted text from the PDF.
    """
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() or ""  # Extract text, handle empty pages
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def extract_text_from_folder(folder_path):
    """
    Extract text from all PDF files in a folder.
    Args:
        folder_path (str): Path to the folder containing PDFs.
    Returns:
        dict: Dictionary with file names as keys and extracted text as values.
    """
    extracted_texts = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            print(f"Extracting text from: {filename}")
            text = extract_text_from_pdf(pdf_path)
            extracted_texts[filename] = text
    return extracted_texts

if __name__ == "__main__":
    # Folder containing your PDFs
    folder_path = "../data"
    
    # Extract text from all PDFs in the folder
    extracted_data = extract_text_from_folder(folder_path)
    
    # Save the extracted text to a file
    output_file = "../data/extracted_text.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        for file, text in extracted_data.items():
            f.write(f"--- Text from {file} ---\n{text}\n\n")
    print(f"Text extraction complete! Check {output_file}")
