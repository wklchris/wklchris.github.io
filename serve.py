import os
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

def start_local_server(docs_dir):
    bind, port = "localhost", 8000
    doc_url = f"http://{bind}:{port}"

    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=docs_dir, **kwargs)
    
    httpd = HTTPServer((bind, port), Handler)
    thread = threading.Thread(target=httpd.serve_forever)
    thread.start()
    # Open the doc main webpage in the webbrowser
    os.system(f'PowerShell -Command "Start-Process -FilePath {doc_url}"')

    # Press Enter for server shutdown
    _ = input(f'\nHosting server at {bind}:{port}. Press Enter to terminate ...\n\n')
    httpd.shutdown()
    print('---\nLocal server has been terminated.')


# --- Main ---

docs_dir = 'docs'

start_local_server(docs_dir)
