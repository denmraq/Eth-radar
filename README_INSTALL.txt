ETH ENTRY RADAR V0.3.7.2 — COMPLETE PACKAGE

ЗАГРУЗКА В GITHUB
1. Файлы radar.py, server.py, requirements.txt, render.yaml, Dockerfile, Procfile и остальные корневые файлы загружать в КОРЕНЬ репозитория.
2. Папку static сохранить именно как папку.
3. В static должны находиться:
   index.html
   service-worker.js
   manifest.webmanifest
   icon-192.png
   icon-512.png
   apple-touch-icon.png

RENDER
Region: Frankfurt (EU Central)
Build: pip install -r requirements.txt
Start: uvicorn server:app --host 0.0.0.0 --port $PORT

IPHONE
Safari -> открыть URL -> Поделиться -> На экран Домой -> Добавить.
