import os
import time
from dotenv import load_dotenv
import google.generativeai as genai
from paper_fetcher import fetch_papers

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-3.6-flash")

def detect_gaps(topic, max_results=10):
    papers = fetch_papers(topic, max_results=max_results)
    papers_sorted = sorted(papers, key=lambda p: p['published'])
    
    # Ella papers na titles + abstracts combine madoNa
    combined_text = ""
    for i, paper in enumerate(papers_sorted, 1):
        year = paper['published'].year
        combined_text += f"\nPaper {i} ({year}): {paper['title']}\nAbstract: {paper['summary'][:500]}\n"
    
    prompt = f"""You are a research analyst. Below are {len(papers_sorted)} research papers on the topic "{topic}", sorted from oldest to newest.

{combined_text}

Based on these papers, provide a structured analysis with these exact sections:

Research Trends: (what approaches/methods are commonly explored across these papers)
Research Gaps: (what seems missing, underexplored, or rarely addressed across these papers)
Suggested Directions: (2-3 potential research ideas or directions based on the identified gaps)
"""
    
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    topic = "transformer neural networks"
    print(f"Analyzing trends and gaps for: {topic}\n")
    print("This may take 10-15 seconds...\n")
    
    analysis = detect_gaps(topic, max_results=10)
    print("--- TRENDS & GAPS ANALYSIS ---")
    print(analysis)