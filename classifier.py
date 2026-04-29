from embeddings import get_embedding, cosine_sim
from data import INTENT_DATA

intent_embeddings = {}

for intent, examples in INTENT_DATA.items():
    intent_embeddings[intent] = [
        get_embedding(text) for text in examples
    ]


def classify_intent(text: str):
    q_emb = get_embedding(text)

    best_intent = "unknown"
    best_score = 0

    for intent, emb_list in intent_embeddings.items():
        for emb in emb_list:
            score = cosine_sim(q_emb, emb)

            if score > best_score:
                best_score = score
                best_intent = intent

    # CRITICAL FIX: confidence thresholding
    if best_score < 0.45:
        return "unknown", best_score

    return best_intent, best_score