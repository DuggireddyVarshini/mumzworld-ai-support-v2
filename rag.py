from embeddings import get_embedding, cosine_sim
from data import FAQ_DATA

faq_embeddings = {k: get_embedding(v) for k, v in FAQ_DATA.items()}

def retrieve_faq(query: str):
    q_emb = get_embedding(query)

    best_key = None
    best_score = 0

    for k, emb in faq_embeddings.items():
        score = cosine_sim(q_emb, emb)
        if score > best_score:
            best_score = score
            best_key = k

    if best_score > 0.35:
        return FAQ_DATA[best_key], best_score

    return None, best_score