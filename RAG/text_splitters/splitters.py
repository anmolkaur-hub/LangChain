import sys
from pathlib import Path
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.documents import Document

# Setup paths relative to script
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"


def print_separator(title: str):
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def inspect_chunks(chunks: list[Document], max_display: int = 3):
    """Utility to print statistical metrics and samples of generated chunks."""
    print(f"\n[+] Total chunks generated: {len(chunks)}")
    if not chunks:
        return

    lengths = [len(c.page_content) for c in chunks]
    print(f"[+] Chunk Lengths -> Min: {min(lengths)} chars | Max: {max(lengths)} chars | Avg: {sum(lengths)/len(lengths):.1f} chars")

    print(f"\n--- Previewing first {min(max_display, len(chunks))} chunks ---")
    for i, chunk in enumerate(chunks[:max_display]):
        print(f"\n[Chunk {i+1}] (Length: {len(chunk.page_content)} chars)")
        print(f"Metadata: {chunk.metadata}")
        preview = chunk.page_content.strip().replace("\n", " ")
        if len(preview) > 160:
            preview = preview[:160] + "..."
        print(f"Content: \"{preview}\"")


def demo_fixed_chunking_on_text():
    print_separator("DEMO 1: Fixed Character Chunking on Contract Text")
    file_path = DATA_DIR / "13_scenarios_billing_and_refunds.txt"

    if not file_path.exists():
        print(f"[!] File not found: {file_path}")
        return

    # 1. Load document using LangChain TextLoader
    loader = TextLoader(str(file_path), encoding="utf-8")
    raw_docs = loader.load()
    print(f"Loaded {len(raw_docs)} document(s) from '{file_path.name}'. Total characters: {len(raw_docs[0].page_content)}")

    # 2. Configure CharacterTextSplitter
    # Splitting on double newline "\n\n" with target size 350 chars and 50 chars overlap
    chunk_size = 350
    chunk_overlap = 50
    separator = "\n\n"

    print(f"\nConfiguring CharacterTextSplitter:")
    print(f"  - separator: {repr(separator)}")
    print(f"  - chunk_size: {chunk_size}")
    print(f"  - chunk_overlap: {chunk_overlap}")

    splitter = CharacterTextSplitter(
        separator=separator,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False,
    )

    # 3. Create chunks
    chunks = splitter.split_documents(raw_docs)
    inspect_chunks(chunks)

    # 4. Demonstrate the Overlap Effect
    if len(chunks) >= 2:
        print("\n--- Overlap Analysis between Chunk 1 & Chunk 2 ---")
        end_chunk1 = chunks[0].page_content[-60:].replace("\n", " ")
        start_chunk2 = chunks[1].page_content[:60].replace("\n", " ")
        print(f"End of Chunk 1  : ...{end_chunk1}")
        print(f"Start of Chunk 2: {start_chunk2}...")


def demo_fixed_chunking_on_pdf():
    print_separator("DEMO 2: Fixed Character Chunking on PDF Document")
    file_path = DATA_DIR / "Digital_India.pdf"

    if not file_path.exists():
        print(f"[!] File not found: {file_path}")
        return

    # 1. Load first 2 pages of PDF using PyPDFLoader
    loader = PyPDFLoader(str(file_path))
    pages = loader.load()
    sample_pages = pages[:2]
    print(f"Loaded {len(sample_pages)} pages from '{file_path.name}' for demonstration.")

    # 2. Split with CharacterTextSplitter
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=500,
        chunk_overlap=80,
        length_function=len,
    )

    chunks = splitter.split_documents(sample_pages)
    inspect_chunks(chunks)

    # Notice how metadata ('page', 'source') is automatically preserved from the original loader
    if chunks:
        print("\n[+] Preserved Metadata in Chunk 1:")
        for k, v in chunks[0].metadata.items():
            print(f"    - {k}: {v}")


if __name__ == "__main__":
    print_separator("LangChain Chunking Strategy 1: Fixed Character Chunking")
    demo_fixed_chunking_on_text()
    demo_fixed_chunking_on_pdf()
    print("\n[Done] Fixed Character Chunking demonstration completed successfully.")
 