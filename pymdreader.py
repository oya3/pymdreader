from flask import Flask, render_template_string, request, send_from_directory
import markdown2
import glob
import os
import re

app = Flask(__name__, static_url_path='', static_folder=os.path.abspath('.'))

@app.route('/')
def home():
    files = glob.glob("**/*.md", recursive=True)
    files = [f.replace('\\', '/') for f in files if 'venv' not in f]
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
    <title>Markdown Preview</title>
    <style>
        #container {
            display: flex;
        }
        #file-list {
            width: 30%;
            overflow: auto;
            height: 100vh;
            border-right: 1px solid #ccc;
            padding: 10px;
        }
        #file-content {
            width: 70%;
            padding: 10px;
            overflow: auto;
            height: 100vh;
        }
        .file-item {
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div id="container">
        <div id="file-list">
            {% for file in files %}
                <div class="file-item" onclick="loadFile('{{ file }}')">{{ file }}</div>
            {% endfor %}
        </div>
        <div id="file-content"></div>
    </div>
    <script>
        function loadFile(filePath) {
            fetch('/file?path=' + filePath)
                .then(response => response.text())
                .then(data => {
                    document.getElementById('file-content').innerHTML = data;
                });
        }
    </script>
</body>
</html>
    """, files=files)

@app.route('/file')
def file_content():
    path = request.args.get('path')
    with open(path, 'r', encoding='utf-8') as f:
        markdown = f.read()
    html = markdown2.markdown(markdown, extras=["tables"])
    directory = os.path.dirname(path)
    html = re.sub(r'src="([^"]*)"', lambda match: 'src="' + os.path.join(directory, match.group(1)) + '"', html)
    return html

@app.route('/<path:path>')
def static_file(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(port=3000)
