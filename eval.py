from classifier import classify_intent

test_cases = {
    "refund_request": [
        "I want my money back",
        "refund please",
        "return my order"
    ],

    "delay_issue": [
        "my order is late",
        "still waiting for package"
    ],

    "product_issue": [
        "item is broken",
        "received damaged product"
    ],

    "order_status": [
        "track order 123",
        "where is my order"
    ],

    "unknown": [
        "asdfgh",
        "????",
        "blabla random text"
    ]
}


def run_eval():
    correct = 0
    total = 0

    for intent, samples in test_cases.items():
        for s in samples:
            pred, score = classify_intent(s)

            print(f"{s} → {pred} ({score:.2f})")

            if pred == intent:
                correct += 1
            total += 1

    print("\nAccuracy:", correct / total)


if __name__ == "__main__":
    run_eval()