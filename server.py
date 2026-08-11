import http.server
import socketserver
import json
import os

PORT = 8000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.end_headers()

    def do_POST(self):
        if self.path == '/registrar':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                cedula = data.get('cedula', '').strip()
                whatsapp = data.get('whatsapp', '').strip()

                if cedula and whatsapp:
                    # Append to datos.csv
                    # Column A is 'cedula', Column B is 'nro'. Delimiter is ','
                    # Header is: cedula,nro,,,
                    with open('datos.csv', 'a', encoding='utf-8') as f:
                        f.write(f"{cedula},{whatsapp},,,\n")

                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    response = {"status": "success", "message": "WhatsApp registrado con éxito"}
                    self.wfile.write(json.dumps(response).encode('utf-8'))
                    return
            except Exception as e:
                print("Error registering:", e)

            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {"status": "error", "message": "Datos inválidos"}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            super().do_POST()

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"Serving HTTP on port {PORT}...")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
