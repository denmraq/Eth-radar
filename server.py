from __future__ import annotations
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from radar import analyze

app = FastAPI(title='ETH Entry Radar CORE V0.5.1 SCALP')
BASE = Path(__file__).parent
STATIC = BASE / 'static'
app.mount('/static', StaticFiles(directory=STATIC), name='static')

@app.middleware('http')
async def no_cache(request: Request, call_next):
    r = await call_next(request)
    if request.url.path == '/' or request.url.path.startswith('/api/') or request.url.path in {'/service-worker.js','/manifest.webmanifest'}:
        r.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        r.headers['Pragma'] = 'no-cache'
    return r

@app.get('/')
def index():
    return FileResponse(STATIC / 'index.html')

@app.get('/manifest.webmanifest')
def manifest():
    return FileResponse(STATIC / 'manifest.webmanifest', media_type='application/manifest+json')

@app.get('/service-worker.js')
def sw():
    return FileResponse(STATIC / 'service-worker.js', media_type='application/javascript', headers={'Cache-Control':'no-cache'})

@app.get('/api/health')
def health():
    return {'ok': True, 'version': 'core-0.5.1-scalp'}

@app.get('/api/radar')
def radar():
    return analyze().to_dict()
