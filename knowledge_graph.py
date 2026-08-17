import networkx as nx
import matplotlib.pyplot as plt
from summarizer import summarize_text
from pdf_reader import extract_text

def build_graph(summary_text):
    # Simple keyword-based graph (basic version)
    G = nx.Graph()
    
    # Extract key terms (simple split, real version alli NLP keyword extraction use madbahudu)
    keywords = ["Transformer", "Attention", "Encoder", "Decoder", "Translation", "Training"]
    
    G.add_node("Paper: Attention Is All You Need")
    for kw in keywords:
        if kw.lower() in summary_text.lower():
            G.add_node(kw)
            G.add_edge("Paper: Attention Is All You Need", kw)
    
    return G

def visualize_graph(G):
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=2000, font_size=8, font_weight='bold', edge_color='gray')
    plt.title("AIGENT Knowledge Graph")
    plt.savefig("graph_output.png")
    print("Graph saved as graph_output.png")
    plt.show()

if __name__ == "__main__":
    paper_text = extract_text("sample.pdf")
    summary = summarize_text(paper_text)
    print("Summary:", summary)
    
    graph = build_graph(summary)
    print(f"\nNodes: {list(graph.nodes())}")
    print(f"Edges: {list(graph.edges())}")
    
    visualize_graph(graph)