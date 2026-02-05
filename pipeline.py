"""
RAG Pipeline: index documents and run Q&A.
Usage:
  python pipeline.py index --input ./docs --output ./index
  python pipeline.py query --index ./index --query "Your question"
"""
import argparse


def chunk_text(text: str, chunk_size: int = 512) -> list[str]:
    """Split text into overlapping chunks (stub)."""
    return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size - 64)]


def index_docs(input_dir: str, output_dir: str) -> None:
    """Index documents into a vector store (stub)."""
    print(f"Indexing {input_dir} -> {output_dir} (stub)")


def query(index_dir: str, query_text: str, top_k: int = 5) -> str:
    """Retrieve and generate answer (stub)."""
    print(f"Query: {query_text}, top_k={top_k}")
    return "RAG answer stub. Wire embeddings + LLM."


def main():
    p = argparse.ArgumentParser(description="RAG Pipeline")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("index").add_argument("--input").add_argument("--output")
    q = sub.add_parser("query")
    q.add_argument("--index")
    q.add_argument("--query")
    args = p.parse_args()
    if args.cmd == "index":
        index_docs(args.input or "./docs", args.output or "./index")
    elif args.cmd == "query":
        print(query(args.index or "./index", args.query or ""))


if __name__ == "__main__":
    main()
