from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_chunk=1000):
    chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]
    return "\n\n".join(summarizer(chunk)[0]['summary_text'] for chunk in chunks)