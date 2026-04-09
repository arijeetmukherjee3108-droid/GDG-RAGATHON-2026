# Statement 2: Lucknow Foodie Guide

## Overview
A context-aware restaurant recommendation engine offering hybrid search capabilities (combining Vector Embeddings for "vibe" and Structured Search for budget/preferences) over a curated local eateries dataset.

## System Architecture
* **Data Preparation:** Hybrid vector-metadata CSV injestion (To be implemented)
* **Embeddings:** (To be implemented)
* **Vector Store & Indexing:** Architecture allowing metadata filtering (To be implemented)
* **Retrieval Workflow:** Semantic Search mapped to Keyword/Attribute filters
* **LLM Synthesizer:** Formats retrieved nodes into conversational recommendations

## Setup Instructions
1. Open terminal and navigate to `Statement-2-Lucknow-Foodie`.
2. Ensure you have activated your python environment and installed core prerequisites at the root level.
3. Configure `OPENAI_API_KEY` (or equivalent) in a new `.env` file based on `.env.example`.
4. (Run instructions to build vector index) -> TBD
5. (Run chatbot local server) -> TBD

## Required Environment Variables
See the `.env.example` file in this directory.

### Creative Features
* Multi-parametric hybrid knowledge integration
* (Other bonus UI/UX implementations will be recorded here)
