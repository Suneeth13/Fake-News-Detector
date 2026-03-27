from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import sys
import os

# Add project root to sys.path to import ml modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ml.predict_gemini import predict_with_gemini

app = FastAPI(title="TruthLens AI - Gemini Powered")

# Serve frontend files
# app.mount("/static", StaticFiles(directory="frontend"), name="static")

class NewsContent(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
async def get_index():
    if not os.path.exists("frontend/index.html"):
         return HTMLResponse(content="<h1>Frontend files missing</h1>", status_code=404)
    with open("frontend/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/predict")
async def predict(content: NewsContent):
    if not content.text.strip():
        raise HTTPException(status_code=400, detail="Text content cannot be empty")
    
    try:
        prediction = predict_with_gemini(content.text)
        return prediction
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

# Add other routes for static files (CSS, JS)
@app.get("/styles.css")
async def get_css():
    with open("frontend/styles.css", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read(), media_type="text/css")

@app.get("/script.js")
async def get_js():
    with open("frontend/script.js", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read(), media_type="application/javascript")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
