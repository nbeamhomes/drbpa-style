# PDF Cleanup Web App

This simple Flask application lets you upload a PDF, processes it with `ocrmypdf`, and returns the cleaned PDF for download. It performs deskewing, skips pages that already contain text, and optimizes the output.

## Setup
Install dependencies (Flask and OCRmyPDF). You may need to use a virtual environment.
```bash
pip install flask ocrmypdf
```

## Running
```bash
python app.py
```
The app will be available at `http://localhost:8000`.

## Usage
1. Open the app in a browser.
2. Upload a PDF file.
3. The cleaned PDF downloads automatically if processing succeeds.
