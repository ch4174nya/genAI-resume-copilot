from sentence_transformers import SentenceTransformer
import faiss

model = SentenceTransformer("all-MiniLM-L6-v2")     # Fast and Small

def chunk_text(text, max_tokens=100):
    lines = text.split("\n")
    chunks = []
    current = ""
    for line in lines:
        if len(current)  + len(line) < max_tokens:
            current += " " + line
        else:
            chunks.append(current.strip())
            current = line
    chunks.append(current.strip())
    return chunks

def embed_chunks(chunks):
    return model.encode(chunks)

def build_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index
