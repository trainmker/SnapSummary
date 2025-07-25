from app.models.t5_model import T5Summarizer
from app.models.bart_model import BARTSummarizer

t5_model = T5Summarizer()
bart_model = BARTSummarizer()

def summarize_text(text, model="t5"):
    if len(text.strip()) == 0:
        return "No text found to summarize."
    if model == "bart":
        return bart_model.summarize(text)
    return t5_model.summarize(text)