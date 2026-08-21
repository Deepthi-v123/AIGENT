import os
from dotenv import load_dotenv
import google.generativeai as genai
from paper_fetcher import fetch_papers
from gap_detector import detect_gaps

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-3.6-flash")

def check_idea(user_idea, topic, papers_sorted):
    combined_text = ""
    for i, paper in enumerate(papers_sorted, 1):
        year = paper['published'].year
        combined_text += f"\nPaper {i} ({year}): {paper['title']}\nAbstract: {paper['summary'][:400]}\n"
    
    prompt = f"""You are an honest research mentor. A student has this research idea:

"{user_idea}"

Here are {len(papers_sorted)} existing papers related to the topic "{topic}":

{combined_text}

Give honest, constructive feedback with these exact sections:

Verdict: (one of: "Already well-explored", "Partially explored", "Genuinely novel")
Explanation: (why you gave this verdict, reference specific papers by number if relevant)
Suggestion: (constructive advice - what angle to add, what to combine, or how to make it more unique/feasible)
"""
    response = model.generate_content(prompt)
    return response.text

def run_aigent_flow(topic, max_results=10):
    papers = fetch_papers(topic, max_results=max_results)
    papers_sorted = sorted(papers, key=lambda p: p['published'])
    
    print(f"\nAnalyzing {len(papers_sorted)} papers on: {topic}")
    print("Generating research trends and gap analysis...\n")
    
    gap_analysis = detect_gaps(topic, max_results=max_results)
    print("--- SUGGESTED RESEARCH DIRECTIONS (based on gaps found) ---")
    print(gap_analysis)
    print("\n" + "=" * 70)
    
    has_idea = input("\nDo you have your own research idea? (yes/no): ").strip().lower()
    
    if has_idea in ["yes", "y"]:
        user_idea = input("Enter your research idea: ")
        print("\nAnalyzing your idea against existing papers...\n")
        feedback = check_idea(user_idea, topic, papers_sorted)
        print("--- IDEA FEEDBACK ---")
        print(feedback)
    else:
        print("\nNo problem! Here are the AI-suggested directions again above — pick one that interests you and start exploring!")

if __name__ == "__main__":
    topic = "transformer neural networks"
    run_aigent_flow(topic, max_results=10)