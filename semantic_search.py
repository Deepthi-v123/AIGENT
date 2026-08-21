import requests

def fetch_semantic_scholar(topic, max_results=10):
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": topic,
        "limit": max_results,
        "fields": "title,authors,abstract,year,venue,url,externalIds"
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return []
    
    data = response.json()
    papers = []
    
    for item in data.get("data", []):
        papers.append({
            "title": item.get("title"),
            "authors": [a.get("name") for a in item.get("authors", [])],
            "abstract": item.get("abstract"),
            "year": item.get("year"),
            "venue": item.get("venue"),  # idu publisher/journal name (Elsevier, Springer, etc.)
            "url": item.get("url")
        })
    
    return papers

if __name__ == "__main__":
    topic = "transformer neural networks"
    print(f"Searching Semantic Scholar for: {topic}\n")
    
    papers = fetch_semantic_scholar(topic, max_results=10)
    
    for i, paper in enumerate(papers, 1):
        print(f"{i}. {paper['title']}")
        print(f"   Venue: {paper['venue']}")
        print(f"   Year: {paper['year']}")
        print(f"   Link: {paper['url']}")
        print()