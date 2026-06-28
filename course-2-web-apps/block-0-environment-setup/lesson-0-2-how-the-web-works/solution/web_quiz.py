def main():
    print("=== Web Workshop Quiz ===")
    print()

    questions = [
        ("What app on your computer opens pages and sends requests?", "browser"),
        ("What waits for requests and sends back pages or data?", "server"),
        ("What is the web address you type, like https://example.com?", "url"),
    ]

    score = 0
    for question, answer in questions:
        guess = input(f"{question} ").lower().strip()
        if guess == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Not quite — the answer is: {answer}")

    print()
    print(f"Score: {score}/{len(questions)}")
    print()
    print("=== Request / Response Demo ===")
    print("Browser: GET https://example.com/hello")
    print("Server:  Received request for /hello")
    print("Server:  Sending response (200 OK)")
    print("Browser: Displaying the page to you")


main()
