from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return send_from_directory('.', 'New Home.html')

@app.route('/<path:filename>')
def serve_page(filename):
    # Only serve .html files that exist in the directory
    if filename.endswith('.html') and os.path.isfile(filename):
        return send_from_directory('.', filename)
    # Serve static files (css, js, images)
    if os.path.isfile(filename):
        return send_from_directory('.', filename)
    return abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)