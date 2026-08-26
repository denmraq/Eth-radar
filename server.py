from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from radar import analyze

app = FastAPI(title="ETH Entry Radar iOS V0.3.5.1")
BASE = Path(__file__).parent
STATIC = BASE / "static"
app.mount("/static", StaticFiles(directory=STATIC), name="static")

@app.get("/")
def index():
    return FileResponse(STATIC / "index.html")

@app.get("/manifest.webmanifest")
def manifest():
    return FileResponse(STATIC / "manifest.webmanifest", media_type="application/manifest+json")

@app.get("/service-worker.js")
def service_worker():
    return FileResponse(STATIC / "service-worker.js", media_type="application/javascript", headers={"Cache-Control": "no-cache"})

@app.get("/api/health")
def health():
    return {"ok": True, "version": "ios-0.3.5.1"}

@app.get("/api/radar")
def radar():
    return analyze().to_dict()
