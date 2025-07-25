from transformers import BartForConditionalGeneration, BartTokenizer

class BARTSummarizer:
    def __init__(self):
        self.tokenizer = BartTokenizer.from_pretrained("facebook/bart-base")
        self.model = BartForConditionalGeneration.from_pretrained("facebook/bart-base")

    def summarize(self, text):
        input_ids = self.tokenizer.encode(text, return_tensors="pt", truncation=True, max_length=1024)
        output_ids = self.model.generate(input_ids, max_length=150, min_length=40, length_penalty=2.0, num_beams=4)
        return self.tokenizer.decode(output_ids[0], skip_special_tokens=True)