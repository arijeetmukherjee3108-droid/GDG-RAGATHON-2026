@echo off
echo ========================================================
echo Starting Lucknow Foodie Backend and Frontend
echo ========================================================

echo Loading Backend...
start cmd /k "cd backend && pip install -r requirements.txt && python ingest.py && uvicorn app:app --reload"

echo Loading Frontend...
start cmd /k "cd frontend && npm install && npm run dev"

echo Both services are booting up in separate windows! 
echo Keep an eye on them. The frontend will usually run at http://localhost:5173
echo ========================================================
