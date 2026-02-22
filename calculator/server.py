
import http.server
import socketserver
import os

PORT = 8000

# SimpleHTTPRequestHandler serves files relative to the current working directory.
# If a directory is requested (e.g., '/'), it will list its contents automatically.
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server started at http://localhost:{PORT}")
    print(f"Serving files from: {os.getcwd()}")
    httpd.serve_forever()
