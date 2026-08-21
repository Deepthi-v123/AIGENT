import os
from dotenv import load_dotenv
import google.generativeai as genai
from pdf_reader import extract_text

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-3.6-flash")

def summarize_text(text, mode="paper"):
    if mode == "paper":
        prompt = f"""Analyze this research paper abstract and provide a structured summary with these exact sections:

Existing Problem: (what problem/limitation existed before this paper)
Proposed Solution: (what this paper proposes/introduces)
Key Result: (main outcome or finding)

Abstract: {text[:3000]}
"""
    else:
        prompt = f"Summarize this text concisely:\n\n{text[:3000]}"
    
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    paper_text = extract_text("sample.pdf")
    print(f"Extracted text length: {len(paper_text)}")  # idu add madi
    print("Generating structured summary with Gemini...\n")
    summary = summarize_text(paper_text, mode="paper")
    print("--- STRUCTURED SUMMARY ---")
    print(summary)