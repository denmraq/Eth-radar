const CACHE = 'eth-radar-ios-v037';
const ASSETS = [
  '/manifest.webmanifest',
  '/static/icon-192.png',
  '/static/icon-512.png',
  '/static/apple-touch-icon.png'
];

self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(cache => cache.addAll(ASSETS)));
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);

  // UI and API must always be fresh.
  if (url.pathname === '/' || url.pathname.startsWith('/api/') || url.pathname === '/service-worker.js') {
    event.respondWith(fetch(event.request, {cache: 'no-store'}));
    return;
  }

  // Static app-shell assets may use cache with network fallback.
  event.respondWith(
    caches.match(event.request).then(hit =>
      hit || fetch(event.request).then(resp => {
        if (resp.ok && event.request.method === 'GET') {
          const copy = resp.clone();
          caches.open(CACHE).then(cache => cache.put(event.request, copy));
        }
        return resp;
      })
    )
  );
});
