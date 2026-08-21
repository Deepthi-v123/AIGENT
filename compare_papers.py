from paper_fetcher import fetch_papers
from summarizer import summarize_text
import time

def analyze_papers(topic, max_results=10):
    papers = fetch_papers(topic, max_results=max_results)
    
    # Year-wise sort madoNa - old to current
    papers_sorted = sorted(papers, key=lambda p: p['published'])
    
    print(f"Analyzing {len(papers_sorted)} papers on: {topic}\n")
    print("=" * 70)
    
    results = []
    for i, paper in enumerate(papers_sorted, 1):
        year = paper['published'].year
        print(f"\n📄 Paper {i}: {paper['title']} ({year})")
        print(f"   Authors: {', '.join(paper['authors'][:3])}")
        print()
        
        # Gemini structured summary generate madutte
        structured_summary = summarize_text(paper['summary'], mode="paper")
        print(structured_summary)
        
        time.sleep(4)  # rate limit avoid madoke, 4 seconds wait
        results.append({
            "title": paper['title'],
            "year": year,
            "summary": structured_summary
        })
        print("-" * 70)
    
    return results

if __name__ == "__main__":
    topic = "transformer neural networks"
    results = analyze_papers(topic, max_results=10)