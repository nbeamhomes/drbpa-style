from flask import Flask, request, send_file, render_template_string
import os
import tempfile
import subprocess

app = Flask(__name__)

UPLOAD_FORM = """
<!doctype html>
<title>PDF Cleanup</title>
<h1>Upload PDF to Clean</h1>
<form method=post enctype=multipart/form-data action="/upload">
  <input type=file name=pdf_file accept="application/pdf">
  <input type=submit value=Upload>
</form>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(UPLOAD_FORM)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get('pdf_file')
    if not file:
        return "No file uploaded", 400
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, 'input.pdf')
        output_path = os.path.join(tmpdir, 'output.pdf')
        file.save(input_path)
        try:
            subprocess.run([
                'ocrmypdf', '--deskew', '--skip-text', '--optimize', '3',
                input_path, output_path
            ], check=True)
        except subprocess.CalledProcessError as e:
            return f"Error running ocrmypdf: {e}", 500
        return send_file(output_path, as_attachment=True, download_name='cleaned.pdf')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
