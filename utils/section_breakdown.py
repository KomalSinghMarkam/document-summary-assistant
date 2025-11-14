import re
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def split_into_sections(text):
    pattern = r"(?:^|\n)([A-Z][A-Za-z0-9 ,\-]{3,}):\s*\n"
    matches = list(re.finditer(pattern, text))
    
    sections = {}
    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        section_title = match.group(1).strip()
        section_text = text[start:end].strip()
        sections[section_title] = section_text
    return sections

def summarize_sections(text):
    sections = split_into_sections(text)
    summarized = {}
    for title, content in sections.items():
        if len(content) < 100:
            summarized[title] = content
        else:
            summary = summarizer(content[:1000])[0]['summary_text']
            summarized[title] = summary
    return summarized