from http.server import BaseHTTPRequestHandler, HTTPServer


def greet(name):
    return f"Hello, {name}!"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"SERVICERUNNING\n")


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), Handler)
    print("SERVICERUNNING", flush=True)
    print("Application listening on port 8000", flush=True)
    server.serve_forever()
