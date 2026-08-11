import re

with open('index.html', 'r') as f:
    content = f.read()

# Add manifest link and apple meta tags in <head>
pwa_head = """
    <link rel="manifest" href="manifest.json">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="apple-mobile-web-app-title" content="PADRONAPP">
    <link rel="apple-touch-icon" href="padronapp.png">
"""
content = content.replace('</head>', pwa_head + '</head>')

# Add Service Worker registration script before </body>
sw_script = """
    <script>
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', () => {
                navigator.serviceWorker.register('./sw.js')
                    .then((reg) => console.log('Service Worker registrado', reg))
                    .catch((err) => console.error('Error al registrar Service Worker', err));
            });
        }
    </script>
"""
content = content.replace('</body>', sw_script + '</body>')

with open('index.html', 'w') as f:
    f.write(content)
