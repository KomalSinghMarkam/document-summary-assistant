from flask import Flask, render_template, request
from utils.extract_text import extract_text
from utils.section_breakdown import summarize_sections
import os

app = Flask(__name__)

# Folder to store uploaded files
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # Render the upload form
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_document():
    # Get the uploaded file (PDF or image)
    file = request.files['document']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Extract text (PDF parsing or OCR for images)
    full_text = extract_text(filepath)

    # Generate section-wise summaries
    section_summaries = summarize_sections(full_text)

    # Pass both raw text and summaries to the template
    return render_template(
        'summary.html',
        raw_text=full_text,
        sections=section_summaries
    )

if __name__ == '__main__':
    app.run(debug=True)