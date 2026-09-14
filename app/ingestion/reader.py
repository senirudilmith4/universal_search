import os
from typing import Any

import pymupdf


def extract_text_from_pdf(file_path: str) -> dict[str, Any]:
    """
    Extracts text from a PDF file and returns a dictionary containing the extracted text and metadata.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        dict: A dictionary containing the page number and text of the PDF.
    """

    # Open the PDF file using pymupdf
    try:
        with pymupdf.open(file_path, filetype="pdf") as doc:
            # Check if the document is encrypted
            if doc.is_encrypted:
                raise ValueError("The PDF file is encrypted and cannot be processed.")

            # extract metadata
            metadata = doc.metadata
            doc_title = metadata.get("title")
            if not doc_title or not doc_title.strip():
                doc_title = os.path.splitext(os.path.basename(file_path))[0]

            # Extract text
            pages = []
            for page_number, page in enumerate(doc, start=1):
                text_content = page.get_text("text").strip()
                pages.append({"page_number": page_number, "text": text_content})

            # Create a JSON object with the extracted text and metadata
            result = {
                "doc_title": doc_title,
                "file_path": file_path,
                "metadata": metadata,
                "pages": pages,
            }

        return result
    except (FileNotFoundError, PermissionError, OSError) as error:
        print(f"Unable to open PDF '{file_path}': {error}")
        return {}
    except pymupdf.FileDataError as error:
        print(f"Invalid or corrupted PDF '{file_path}': {error}")
        return {}


if __name__ == "__main__":
    file_path = r"D:\OneDrive\Documents\IIT\PersonalWork\universal_search\data\documents\words_only_10pages_sample2.pdf"
    extracted_text = extract_text_from_pdf(file_path)
    print(extracted_text)
