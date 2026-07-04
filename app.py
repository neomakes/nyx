#!/usr/bin/env python3
"""Serve the Nyx public demo without external dependencies."""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json
import os
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent
HOST = os.environ.get("NYX_HOST", "0.0.0.0")
PORT = int(os.environ.get("NYX_PORT", "8080"))


class NyxHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/":
            self.path = "/demo/index.html"
            return super().do_GET()
        if path == "/api/scenarios":
            return self._json(self._load_scenarios())
        return super().do_GET()

    def _json(self, payload):
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _load_scenarios(self):
        scenario_dir = ROOT / "demo" / "sample_scenarios"
        scenarios = []
        for file_path in sorted(scenario_dir.glob("*.json")):
            with file_path.open("r", encoding="utf-8") as handle:
                scenarios.append(json.load(handle))
        return {"brand": "Nyx", "scenarios": scenarios}


def main():
    server = ThreadingHTTPServer((HOST, PORT), NyxHandler)
    print(f"Nyx demo running at http://localhost:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    main()

