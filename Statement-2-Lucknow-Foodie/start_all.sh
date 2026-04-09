#!/bin/bash
echo "========================================================"
echo "Starting Lucknow Foodie Backend and Frontend"
echo "========================================================"

# Start backend in background
echo "Loading Backend pipeline..."
(cd backend && pip install -r requirements.txt && python ingest.py && uvicorn app:app --reload) &

# Start frontend in background
echo "Loading Frontend pipeline..."
(cd frontend && npm install && npm run dev) &

echo "Services started in the background! Terminate this script using Ctrl+C to kill both."
wait
