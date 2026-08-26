
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from radar import analyze

app=FastAPI(title="ETH Entry Radar iOS V0.3.1")
BASE=Path(__file__).parent
app.mount("/static",StaticFiles(directory=BASE/"static"),name="static")

@app.get("/")
def index(): return FileResponse(BASE/"static"/"index.html")
@app.get("/manifest.webmanifest")
def manifest(): return FileResponse(BASE/"static"/"manifest.webmanifest",media_type="application/manifest+json")
@app.get("/service-worker.js")
def sw(): return FileResponse(BASE/"static"/"service-worker.js",media_type="application/javascript")
@app.get("/api/health")
def health(): return {"ok":True,"version":"ios-0.3.1"}
@app.get("/api/radar")
def radar(): return analyze().to_dict()
