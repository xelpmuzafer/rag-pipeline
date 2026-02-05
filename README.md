# RAG Pipeline

A minimal Retrieval-Augmented Generation (RAG) pipeline for document Q&A: chunk documents, embed with open-source models, and answer questions using a vector store and an LLM.

## Features

- **Document chunking** — split PDFs and text by size or sentences
- **Embeddings** — optional local embeddings (e.g. sentence-transformers) or API
- **Vector store** — in-memory or persistent FAISS/Chroma for similarity search
- **LLM integration** — plug in OpenAI, Anthropic, or local models for generation

## Requirements

- Python 3.10+
- 8GB+ RAM recommended for local embeddings

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Edit `config.yaml` or set environment variables:

- `EMBEDDING_MODEL` — name of the embedding model
- `CHUNK_SIZE` — characters per chunk
- `TOP_K` — number of chunks to retrieve per query

## Usage

Index documents:

```bash
python pipeline.py index --input ./docs --output ./index
```

Run a Q&A query:

```bash
python pipeline.py query --index ./index --query "What is RAG?"
```

## License

MIT
