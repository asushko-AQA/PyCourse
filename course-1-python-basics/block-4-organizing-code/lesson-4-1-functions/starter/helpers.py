# helpers.py
# Adventure Workshop — reusable recipe functions

def draw_banner(text):
    # TODO: Print a line of ===, then text, then another line of ===
    print("===")
    print(text)
    print("===")


def ask_yes_no(question):
    # TODO: Print the question, use input(), return "yes" or "no" (lowercase strings)
    answer = input(f"{question} (yes/no): ").lower().strip()
    if answer in ("y", "yes"):
        return "yes"
    return "no"


def main():
    # TODO: Call draw_banner with "Adventure Workshop"
    draw_banner("Adventure Workshop")

    # TODO: Call ask_yes_no and store the answer
    answer = ask_yes_no("Ready to build helper functions?")
    print(f"You answered: {answer}")


main()
