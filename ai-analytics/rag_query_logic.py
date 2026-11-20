# AI and RAG query logic for water conservation
from typing import List, Dict


KNOWLEDGE_BASE: List[Dict[str, str]] = [
    {
        "topic": "auto_shutoff",
        "text": "Automatic shutoff or proximity-controlled public taps reduce accidental open-tap wastage in shared areas.",
    },
    {
        "topic": "leak_detection",
        "text": "Sudden drops or continuous low-volume flow during off-hours can indicate a valve fault or pipeline leak.",
    },
    {
        "topic": "sdg_6",
        "text": "UN SDG 6 emphasizes sustainable water management, efficiency, and reducing losses across distribution points.",
    },
]


def retrieve_relevant_notes(query: str, top_k: int = 2) -> List[str]:
    query_terms = {word.lower().strip(".,?!") for word in query.split()}
    scored = []
    for item in KNOWLEDGE_BASE:
        doc_terms = set(item["text"].lower().split()) | set(item["topic"].lower().split("_"))
        score = len(query_terms & doc_terms)
        scored.append((score, item["text"]))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [text for score, text in scored[:top_k] if score > 0] or [KNOWLEDGE_BASE[0]["text"]]


def answer_conservation_query(query: str, total_saved_liters: float = 12.5) -> str:
    context = retrieve_relevant_notes(query)
    grounded_context = " | ".join(context)
    return (
        f"Query: {query}\n"
        f"Current Simulated Savings: {total_saved_liters:.2f} L\n"
        f"Retrieved Guidance: {grounded_context}"
    )


if __name__ == "__main__":
    print(answer_conservation_query("How does auto shutoff help with water conservation and SDG 6?"))
