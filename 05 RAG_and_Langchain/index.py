from pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings

load_dotenv()

pdf_path = Path(__file__).parent / "nodejs.pdf"

# load this pdf file
loader = PyPDFLoader(file_path=pdf_path)

docs = loader.load() 

# print(docs[0])

# split the document into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)

# 
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=400)

chunks = text_splitter.split_documents(docs)

print(f"Number of chunks: {len(chunks)}")
# print(chunks[0].page_content)

# Embedding model
embedding_model = NVIDIAEmbeddings(
   model="nvidia/nv-embed-v1",
)

# Vector store to store the embeddings with Qdrant 
vector_store = QdrantVectorStore.from_document(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

print("indexing of documents completed...")

