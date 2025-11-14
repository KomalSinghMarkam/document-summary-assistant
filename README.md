# Document Summary Assistant

A Flask app that extracts text from PDFs and images (OCR), then produces section-wise summaries using modern language models. Built for clarity, accessibility, and layout fidelity.

## Features
- PDF text extraction (PyMuPDF)
- Image OCR (Tesseract via pytesseract)
- Section-wise summarization
- Simple web UI

## How it works
Upload a document; the app extracts text (PDF parsing or OCR) and generates concise summaries per section.

## Run locally
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
python app.py