from http.server import BaseHTTPRequestHandler, HTTPServer

TEAM = ["Wasan", "norah", "huraa"]

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            message = "Team members: " + ", ".join(TEAM)
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(message.encode())
        else:
            self.send_response(404)
            self.end_headers()

server = HTTPServer(("0.0.0.0", 8000), Server)
print("Server running on port 8000")
server.serve_forever()
