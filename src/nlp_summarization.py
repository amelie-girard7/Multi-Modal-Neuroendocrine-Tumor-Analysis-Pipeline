# nlp_summarization.py
from transformers import pipeline

# Load once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_report(text):
    """
    Generate a concise summary of a radiology report.
    """
    result = summarizer(text, max_length=60, min_length=10, do_sample=False)
    return result[0]['summary_text']
