import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def build_network():

    df = pd.read_csv("data/tenders.csv")

    G = nx.Graph()

    for _, row in df.iterrows():

        company = row["company"]
        department = row["department"]

        G.add_node(company, type="company")
        G.add_node(department, type="department")

        G.add_edge(company, department)

    plt.figure(figsize=(8,6))

    nx.draw(
        G,
        with_labels=True,
        node_color="lightblue",
        node_size=2000,
        font_size=10
    )

    plt.savefig("static/graph.png")

    plt.close()


def find_suspicious_nodes():

    df = pd.read_csv("data/tenders.csv")

    G = nx.Graph()

    for _, row in df.iterrows():
        G.add_edge(row["company"], row["department"])

    centrality = nx.degree_centrality(G)

    suspicious = []

    for node, score in centrality.items():
        if score > 0.5:
            suspicious.append((node, round(score,2)))

    return suspicious