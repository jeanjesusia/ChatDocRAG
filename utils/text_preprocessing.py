import os
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def create_chunks(file):
    """
    Return the given document in chunks, converting bytes into a tempfile
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
        temp_file.write(file.read()) # write binary file in disk
        temp_file_path = temp_file.name # document path

    loader = PyPDFLoader(temp_file_path)
    docs = loader.load()

    # Remove created tempfile
    os.remove(temp_file_path)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap = 400
    )

    chunks = text_splitter.split_documents(docs)

    return chunks


def process_pdf(uploaded_files):
    """
    Processes each uploaded PDF and splits them into chunks.
    Args:
        uploaded_files (list): List of uploaded PDF files.
    """
    all_chunks = []

    for uploaded_file in uploaded_files:
        chunks = create_chunks(uploaded_file)
        all_chunks.extend(chunks)
    
    return all_chunks