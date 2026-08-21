import arxiv

def fetch_papers(topic, max_results=15):
    client = arxiv.Client()
    search = arxiv.Search(
        query=topic,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    
    papers = []
    for result in client.results(search):
        papers.append({
            "title": result.title,
            "authors": [author.name for author in result.authors],
            "summary": result.summary,
            "published": result.published,
            "pdf_url": result.pdf_url
        })
    
    return papers

if __name__ == "__main__":
    topic = "transformer neural networks"
    print(f"Fetching papers on: {topic}\n")
    
    papers = fetch_papers(topic, max_results=15)
    
    for i, paper in enumerate(papers, 1):
        print(f"{i}. {paper['title']}")
        print(f"   Authors: {', '.join(paper['authors'][:3])}")
        print(f"   Published: {paper['published']}")
        print(f"   PDF: {paper['pdf_url']}")
        print()