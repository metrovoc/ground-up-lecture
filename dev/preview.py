"""Serve the style specimen, rebuilt from assets/template.html on every request."""

import http.server
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        template = (ROOT / "assets/template.html").read_text()
        body = (ROOT / "dev/specimen.html").read_text()
        head, rest = template.rsplit("<main>", 1)
        page = head + "<main>\n" + body + "\n</main>" + rest.rsplit("</main>", 1)[1]
        data = page.replace("<title>Lecture title</title>", "<title>Style specimen</title>").encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)


print(f"Specimen at http://localhost:{PORT}")
http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
