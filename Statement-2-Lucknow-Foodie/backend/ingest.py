import os
import pandas as pd
import chromadb
from pathlib import Path

# Setup paths
backend_dir = Path(__file__).parent.absolute()
dataset_path = backend_dir.parent / "dataset" / "restaurants.csv"
db_dir = backend_dir / "chroma_db"

print(f"Initializing ChromaDB at {db_dir}")
# We use ChromaDB persistent client which saves embeddings to disk.
client = chromadb.PersistentClient(path=str(db_dir))

# Create or load the collection. Note: Chroma's default embedding function 
# automatically downloads a lightweight ONNX all-MiniLM-L6-v2 embedding model 
# ensuring you don't need heavy PyTorch dependencies!
collection = client.get_or_create_collection(name="lucknow_restaurants")

def ingest_data():
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset not found at {dataset_path}")
        return
        
    print(f"Loading dataset from {dataset_path}")
    df = pd.read_csv(dataset_path)
    
    ids = []
    documents = []
    metadatas = []
    
    for idx, row in df.iterrows():
        # The document text is what the vector semantic search actually embeds
        # We merge vibe, reviews, and distinct attributes so similarity queries grab the right context
        doc_text = f"A {row['vibe']} place known for {row['special_dishes']}. People say: {row['reviews']}."
        
        # Metadatas are strictly typed variables we use to explicitly filter (e.g. max price, must be veg)
        metadata = {
            "name": str(row["name"]),
            "location": str(row["location"]),
            "area": str(row["area"]),
            "price_range": int(row["price_range"]),
            "veg": str(row["veg"]).lower() == 'true',
            "rating": float(row["rating"])
        }
        
        ids.append(f"rest_{idx}")
        documents.append(doc_text)
        metadatas.append(metadata)
        
    print(f"Uploading {len(documents)} restaurants to ChromaDB into batches...")
    
    # Process in batches to ensure stable execution
    batch_size = 100
    for i in range(0, len(documents), batch_size):
        end_idx = min(i + batch_size, len(documents))
        collection.upsert(
            ids=ids[i:end_idx],
            documents=documents[i:end_idx],
            metadatas=metadatas[i:end_idx]
        )
        print(f"Processed subset {i} to {end_idx}")

    print("Ingestion completely finished! Your vector DB is ready for queries.")

if __name__ == "__main__":
    # Test if DB already has records
    existing_count = collection.count()
    if existing_count > 0:
        print(f"There are already {existing_count} records in the collection.")
        print("Re-running ingestion to overwrite or append fresh data...")
    ingest_data()
