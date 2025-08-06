from typing import List
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

summarizer = pipeline("summarization")

def summarize_and_extract_keywords(document: str) -> dict:
    summary = summarizer(document, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
    vectorizer = TfidfVectorizer(stop_words='english', max_features=10)
    X = vectorizer.fit_transform([document])
    keywords = vectorizer.get_feature_names_out()
    return {
        "document": summary,
        "keywords": list(keywords)
    }
