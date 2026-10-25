import os
import sys
import warnings
from typing import List

# 1. Filter out deprecation warnings for clean output
warnings.filterwarnings("ignore", category=DeprecationWarning)

# 2. Set USER_AGENT environment variable to prevent 403 Forbidden errors and LangChain warning
os.environ["USER_AGENT"] = "Mozilla/5.0 (compatible; LangChainWebLoader/1.0; +https://python.langchain.com)"

from langchain_community.document_loaders.web_base import WebBaseLoader
from langchain_core.documents import Document


def load_single_web_page(url: str) -> List[Document]:
    """Load a single webpage into LangChain Document objects."""
    print(f"\n[+] Fetching single webpage: {url}")
    loader = WebBaseLoader(
        web_paths=(url,),
        # Optional: custom request headers or session settings
        requests_kwargs={"timeout": 15},
    )
    docs = loader.load()
    return docs


def load_multiple_web_pages(urls: List[str]) -> List[Document]:
    """Load multiple webpages concurrently using WebBaseLoader."""
    print(f"\n[+] Fetching {len(urls)} web pages...")
    loader = WebBaseLoader(web_paths=tuple(urls))
    docs = loader.load()
    return docs


def stream_web_page_lazy(url: str):
    """Demonstrate memory-efficient lazy loading (returns a generator)."""
    print(f"\n[+] Demonstrating lazy_load() for: {url}")
    loader = WebBaseLoader(web_paths=(url,))
    for i, doc in enumerate(loader.lazy_load(), start=1):
        print(f"  -> Streamed Document {i} (Length: {len(doc.page_content)} chars)")
        print(f"     Title: {doc.metadata.get('title', 'N/A')}")
        print(f"     Source: {doc.metadata.get('source')}")


def main():
    print("=" * 60)
    print("  LangChain WebBaseLoader Execution Demo")
    print("=" * 60)

    target_url = "https://www.columbia.edu/~fdc/sample.html"
    docs = load_single_web_page(target_url)

    print(f"\nLoaded {len(docs)} document(s) from {target_url}")
    for idx, doc in enumerate(docs, start=1):
        print(f"\n--- Document #{idx} ---")
        print(f"Metadata: {doc.metadata}")
        print(f"Content Length: {len(doc.page_content)} characters")
        preview = " ".join(doc.page_content.split()[:40])
        print(f"Preview: {preview}...")

    # Demonstrating lazy loading
    stream_web_page_lazy("https://docs.python.org/3/tutorial/index.html")

    print("\nWebBaseLoader execution finished successfully.")


if __name__ == "__main__":
    main()
 