"""Simple shopping server using only the Python standard library.

Run: python3 server.py [port]
Default port: 8000
"""

from __future__ import annotations

import json
import sys
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse


PRODUCTS = [
    {
        "id": 1,
        "name": "Mechanical Keyboard",
        "price_eur": 129.00,
        "stock": 12,
        "url": "https://example.com/products/mechanical-keyboard",
        "image": "https://picsum.photos/seed/keyboard/400/300",
        "description": "Tactile switches, hot-swappable, RGB backlight.",
    },
    {
        "id": 2,
        "name": "Wireless Mouse",
        "price_eur": 49.90,
        "stock": 0,
        "url": "https://example.com/products/wireless-mouse",
        "image": "https://picsum.photos/seed/mouse/400/300",
        "description": "Ergonomic, 70-hour battery, USB-C charging.",
    },
    {
        "id": 3,
        "name": "27\" 4K Monitor",
        "price_eur": 379.00,
        "stock": 4,
        "url": "https://example.com/products/4k-monitor",
        "image": "https://picsum.photos/seed/monitor/400/300",
        "description": "IPS panel, 60 Hz, USB-C 65 W power delivery.",
    },
    {
        "id": 4,
        "name": "Noise-Cancelling Headphones",
        "price_eur": 219.00,
        "stock": 7,
        "url": "https://example.com/products/headphones",
        "image": "https://picsum.photos/seed/headphones/400/300",
        "description": "Over-ear, 30-hour battery, multipoint Bluetooth.",
    },
    {
        "id": 5,
        "name": "USB-C Hub (8-in-1)",
        "price_eur": 39.95,
        "stock": 23,
        "url": "https://example.com/products/usb-c-hub",
        "image": "https://picsum.photos/seed/hub/400/300",
        "description": "HDMI 4K, SD/microSD, 100 W passthrough.",
    },
    {
        "id": 6,
        "name": "Standing Desk Mat",
        "price_eur": 59.00,
        "stock": 1,
        "url": "https://example.com/products/desk-mat",
        "image": "https://picsum.photos/seed/mat/400/300",
        "description": "Anti-fatigue, non-slip, 76 x 51 cm.",
    },
]


def availability_label(stock: int) -> tuple[str, str]:
    if stock == 0:
        return ("Out of stock", "out")
    if stock <= 3:
        return (f"Only {stock} left", "low")
    return ("In stock", "ok")


def render_index() -> bytes:
    cards = []
    for p in PRODUCTS:
        label, css = availability_label(p["stock"])
        disabled = "disabled" if p["stock"] == 0 else ""
        cards.append(
            f"""
        <article class="card">
          <img src="{p['image']}" alt="{p['name']}" loading="lazy">
          <div class="body">
            <h2>{p['name']}</h2>
            <p class="desc">{p['description']}</p>
            <div class="row">
              <span class="price">€{p['price_eur']:.2f}</span>
              <span class="badge {css}">{label}</span>
            </div>
            <a class="btn {disabled}" href="{p['url']}" target="_blank" rel="noopener">
              {'View product' if p['stock'] else 'Notify me'} &rarr;
            </a>
          </div>
        </article>"""
        )

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Claude Shop</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    :root {{ color-scheme: light dark; }}
    * {{ box-sizing: border-box; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      margin: 0;
      background: #f5f5f7;
      color: #1d1d1f;
    }}
    @media (prefers-color-scheme: dark) {{
      body {{ background: #111; color: #eee; }}
      .card {{ background: #1c1c1e; }}
    }}
    header {{
      padding: 2rem 1.5rem;
      background: linear-gradient(135deg, #6366f1, #8b5cf6);
      color: white;
    }}
    header h1 {{ margin: 0 0 .25rem; font-size: 1.75rem; }}
    header p {{ margin: 0; opacity: .9; }}
    main {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 1.5rem;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 1rem;
    }}
    .card {{
      background: white;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 1px 3px rgba(0,0,0,.08);
      display: flex;
      flex-direction: column;
    }}
    .card img {{ width: 100%; height: 180px; object-fit: cover; }}
    .card .body {{ padding: 1rem; display: flex; flex-direction: column; gap: .5rem; flex: 1; }}
    .card h2 {{ margin: 0; font-size: 1.05rem; }}
    .desc {{ margin: 0; font-size: .9rem; opacity: .75; flex: 1; }}
    .row {{ display: flex; justify-content: space-between; align-items: center; }}
    .price {{ font-weight: 600; font-size: 1.1rem; }}
    .badge {{
      font-size: .75rem;
      padding: .2rem .55rem;
      border-radius: 999px;
      font-weight: 500;
    }}
    .badge.ok {{ background: #d1fae5; color: #065f46; }}
    .badge.low {{ background: #fef3c7; color: #92400e; }}
    .badge.out {{ background: #fee2e2; color: #991b1b; }}
    .btn {{
      display: inline-block;
      text-align: center;
      padding: .55rem .9rem;
      background: #6366f1;
      color: white;
      text-decoration: none;
      border-radius: 8px;
      font-weight: 500;
      font-size: .9rem;
    }}
    .btn:hover {{ background: #4f46e5; }}
    .btn.disabled {{ background: #9ca3af; pointer-events: none; }}
    footer {{ text-align: center; padding: 2rem; opacity: .6; font-size: .85rem; }}
  </style>
</head>
<body>
  <header>
    <h1>Claude Shop</h1>
    <p>{len(PRODUCTS)} products &middot; JSON API at <code>/api/products</code></p>
  </header>
  <main>{''.join(cards)}</main>
  <footer>Stdlib-only demo &middot; in-memory data</footer>
</body>
</html>"""
    return html.encode("utf-8")


class ShopHandler(BaseHTTPRequestHandler):
    def _send(self, status: int, body: bytes, content_type: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def _send_json(self, status: int, payload: object) -> None:
        self._send(status, json.dumps(payload, indent=2).encode("utf-8"), "application/json")

    def do_GET(self) -> None:
        path = urlparse(self.path).path

        if path in ("/", "/index.html"):
            self._send(HTTPStatus.OK, render_index(), "text/html; charset=utf-8")
            return

        if path == "/api/products":
            enriched = []
            for p in PRODUCTS:
                label, _ = availability_label(p["stock"])
                enriched.append({**p, "availability": label, "available": p["stock"] > 0})
            self._send_json(HTTPStatus.OK, enriched)
            return

        if path.startswith("/api/products/"):
            try:
                pid = int(path.rsplit("/", 1)[-1])
            except ValueError:
                self._send_json(HTTPStatus.BAD_REQUEST, {"error": "invalid id"})
                return
            for p in PRODUCTS:
                if p["id"] == pid:
                    label, _ = availability_label(p["stock"])
                    self._send_json(
                        HTTPStatus.OK,
                        {**p, "availability": label, "available": p["stock"] > 0},
                    )
                    return
            self._send_json(HTTPStatus.NOT_FOUND, {"error": "not found"})
            return

        if path == "/health":
            self._send_json(HTTPStatus.OK, {"status": "ok", "products": len(PRODUCTS)})
            return

        self._send_json(HTTPStatus.NOT_FOUND, {"error": "not found", "path": path})

    def log_message(self, format: str, *args) -> None:  # quieter logs
        sys.stderr.write(f"[{self.log_date_time_string()}] {format % args}\n")


def main() -> None:
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    server = ThreadingHTTPServer(("0.0.0.0", port), ShopHandler)
    print(f"Claude Shop running at http://localhost:{port}/")
    print(f"  HTML  http://localhost:{port}/")
    print(f"  JSON  http://localhost:{port}/api/products")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.server_close()


if __name__ == "__main__":
    main()
