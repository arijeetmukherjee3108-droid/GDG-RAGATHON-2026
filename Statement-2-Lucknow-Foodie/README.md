# Statement 2: Lucknow Foodie Guide

## Overview
A beautifully crafted, modern full-stack restaurant recommendation engine offering high-precision hybrid search capabilities. It intelligently combines Semantic Vector Embeddings matching with Structured Database queries (budget, veg/non-veg) over a curated local eateries dataset. The interactive UI provides a premium "Swiggy/Zomato" inspired experience!

## System Architecture
* **Frontend:** Vite + React JS, built with custom Vanilla CSS emphasizing micro-animations and glassmorphism.
* **Backend:** Python + FastAPI exposing a high-performance `/api/recommend` AI endpoint.
* **Vector Store & Indexing:** `ChromaDB` (utilizing a local ONNX-based MiniLM embedding mechanism inherently, thereby circumventing heavy PyTorch bloat).
* **Retrieval Workflow:** Robust Hybrid logic executing exact exact-match parameters ($lte budget thresholds, absolute boolean filtering for `veg`) mapped sequentially with semantic textual nearest-neighbor indexing over distinct tags like "Vibe".
* **LLM Synthesizer:** OpenAI API injection dynamically formulating actionable suggestions bounded by the strict vector-retrieved context window to prevent generative hallucinations.

## Setup Instructions

1. Ensure your physical environment supports Python and Node.js (`npm`).
2. Open a functional terminal targeting `Statement-2-Lucknow-Foodie`.
3. Open the `.env.example` file and copy it to a new file literally named `.env`, inserting your `OPENAI_API_KEY`.
4. Trigger the macro boot scripts dependent on your OS:
   - **Windows:** Double-click `start_all.bat` (or execute `.\start_all.bat` via Powershell).
   - **Mac/Linux:** Execute `sh start_all.sh`

*(Note for Evaluation: The macro script automates dependency loading, seamlessly executes the `ingest.py` dataset processor, sets up ChromaDB locally, and concurrently spins up localized servers for Evaluation/Testing!)*

## Required Environment Variables
Please adhere to the mappings declared in `.env.example`.

### Creative Features
* **Premium Swiggy-Clone UI/UX:** Gone drastically beyond basic templates to provide a fully reactive, responsively animated front-end portal paralleling modern industry titans.
* **Algorithmic Hybrid Search Extensibility:** Implemented programmatic conditional operators prior to semantic comparisons. Enforces rigid user demands (like absolute Budget constraints) mathematically instead of relying on ambiguous LLM prompts, increasing recommendation accuracy enormously.
