# helpers.py
# Adventure Workshop — reusable recipe functions

def draw_banner(text):
    # TODO: Replace pass with three print() lines: "===", then text, then "==="
    pass


def ask_yes_no(question):
    answer = input(f"{question} (yes/no): ").lower().strip()
    # TODO: Replace the line below with:
    #       if answer in ("y", "yes"):
    #           return "yes"
    #       return "no"
    return "no"


def main():
    # TODO: Call draw_banner with the text "Adventure Workshop"

    # TODO: Replace "?" with a call: ask_yes_no("Ready to build helper functions?")
    answer = "?"
    print(f"You answered: {answer}")


main()
