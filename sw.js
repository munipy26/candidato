const CACHE_NAME = 'padronapp-v1';
const ASSETS = ['./', './index.html', './padronapp.png', './padronapp1.png'];
self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS)));
});
self.addEventListener('fetch', (e) => {
  e.respondWith(caches.match(e.request).then((res) => res || fetch(e.request)));
});
