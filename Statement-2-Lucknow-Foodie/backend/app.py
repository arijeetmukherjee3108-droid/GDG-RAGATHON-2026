import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import chromadb
from dotenv import load_dotenv
import openai

# Load environment variables (like OPENAI_API_KEY)
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

app = FastAPI(title="Lucknow Foodie RAG API")

# Essential CORSMiddleware to allow our React Vite app to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect to the local ChromaDB vector store
db_dir = os.path.join(os.path.dirname(__file__), "chroma_db")
client = chromadb.PersistentClient(path=db_dir)

try:
    collection = client.get_collection(name="lucknow_restaurants")
except Exception:
    # Fallback to creating it just in case someone hits the API before ingestion
    collection = client.get_or_create_collection(name="lucknow_restaurants")

class QueryRequest(BaseModel):
    query: str
    budget: int = None
    veg_only: bool = False

@app.post("/api/recommend")
async def get_recommendation(req: QueryRequest):
    # 1. Prepare Metadata Filters for Hybrid Search
    where_filter = {}
    if req.veg_only:
        # Chroma expects exact boolean matches here based on our ingest.py
        where_filter["veg"] = True
    if req.budget is not None and req.budget > 0:
        # Price must be less than or equal to budget
        where_filter["price_range"] = {"$lte": req.budget}
        
    try:
        # 2. Semantic Search using the built-in embedding
        results = collection.query(
            query_texts=[req.query],
            n_results=5,
            where=where_filter if where_filter else None
        )
        
        # 3. Handle Empty Results
        if not results['documents'] or not results['documents'][0]:
            return {
                "recommendation": "Sorry, I couldn't find any restaurants matching your specific vibe and budget. Try loosening your filters!", 
                "raw_results": []
            }
            
        matched_docs = results['documents'][0]
        matched_meta = results['metadatas'][0]
        
        # Compile retrieved chunks
        context_blocks = []
        for doc, meta in zip(matched_docs, matched_meta):
            veg_label = "🟩 Veg" if meta['veg'] else "🟥 Non-Veg"
            context_blocks.append(
                f"- **{meta['name']}** ({meta['area']}) | Price: ₹{meta['price_range']} | {veg_label} | Rating: {meta['rating']}\n  Details: {doc}"
            )
            
        context_str = "\n".join(context_blocks)
        
        # 4. LLM Response Synthesis (RAG)
        api_key = os.environ.get("OPENAI_API_KEY")
        if api_key and api_key != "your_openai_api_key_here":
            client_llm = openai.Client(api_key=api_key)
            prompt = f"""
            You are a helpful and enthusiastic foodie assistant for students at IIIT Lucknow.
            A user asked: "{req.query}"
            
            Based EXACTLY on the following local search results:
            {context_str}
            
            Provide a warm, personalized recommendation identifying the best fit for them. 
            Keep it strictly confined to the options provided above. Do not hallucinate restaurants.
            """
            
            completion = client_llm.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            final_recc = completion.choices[0].message.content
        else:
            # Fallback response if no API key is set
            final_recc = f"**I found the following matches based on your vibe:**\n\n{context_str}\n\n*(Note for Devs: Add your OPENAI_API_KEY to .env to unlock conversational AI generation!)*"

        return {
            "recommendation": final_recc,
            "raw_results": matched_meta
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
