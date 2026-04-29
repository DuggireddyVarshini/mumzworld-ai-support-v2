from classifier import classify_intent
from rag import retrieve_faq
from response import generate_response
from utils import compute_confidence

def run():
    print("Mumzworld AI Support (type exit)")

    while True:
        user = input("\nYou: ")

        if user.lower() == "exit":
            break

        intent, score = classify_intent(user)

        faq_answer, faq_score = retrieve_faq(user)

        response = generate_response(intent)

        confidence = compute_confidence(score, faq_score)

        output = {
            "intent": intent,
            "response_en": response["en"],
            "response_ar": response["ar"],
            "confidence": confidence,
            "faq_used": faq_answer
        }

        print("\nRESPONSE:\n", output)


if __name__ == "__main__":
    run()