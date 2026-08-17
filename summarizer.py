from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from pdf_reader import extract_text

model_name = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def summarize_text(text, max_len=150, min_len=50):
    if len(text) > 4000:
        text = text[:4000]
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs["input_ids"], max_length=max_len, min_length=min_len, do_sample=False)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

if __name__ == "__main__":
    paper_text = extract_text("sample.pdf")
    print("Generating summary... (idu chikka time tagoduthe, model download aagutte first time)")
    summary = summarize_text(paper_text)
    print("\n--- SUMMARY ---")
    print(summary)