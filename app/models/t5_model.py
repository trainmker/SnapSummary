from transformers import T5ForConditionalGeneration, T5Tokenizer

class T5Summarizer:
    def __init__(self):
        self.tokenizer = T5Tokenizer.from_pretrained("t5-small")
        self.model = T5ForConditionalGeneration.from_pretrained("t5-small")

    def summarize(self, text):
        input_ids = self.tokenizer("summarize: " + text, return_tensors="pt", truncation=True, max_length=512).input_ids
        output_ids = self.model.generate(input_ids, max_length=150, min_length=40, length_penalty=2.0, num_beams=4)
        return self.tokenizer.decode(output_ids[0], skip_special_tokens=True)