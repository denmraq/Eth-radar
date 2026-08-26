ETH Entry Radar iOS V0.3.5.1 — FULL FIXED

GitHub structure must be exactly:

Eth-radar/
  radar.py
  server.py
  requirements.txt
  render.yaml
  Dockerfile
  Procfile
  README_INSTALL.txt
  static/
    index.html
    manifest.webmanifest
    service-worker.js
    icon-192.png
    icon-512.png
    apple-touch-icon.png

Render:
- Runtime: Python 3
- Region: Frankfurt (EU Central)
- Build Command: pip install -r requirements.txt
- Start Command: uvicorn server:app --host 0.0.0.0 --port $PORT

Important: service-worker.js MUST remain inside static/.
The server exposes it at /service-worker.js for iPhone PWA registration.
