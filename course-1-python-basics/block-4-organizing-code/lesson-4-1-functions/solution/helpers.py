# helpers.py
# Adventure Workshop — reusable recipe functions

def draw_banner(text):
    print("===")
    print(text)
    print("===")


def ask_yes_no(question):
    answer = input(f"{question} (yes/no): ").lower().strip()
    if answer in ("y", "yes"):
        return "yes"
    return "no"


def main():
    draw_banner("Adventure Workshop")
    answer = ask_yes_no("Ready to build helper functions?")
    print(f"You answered: {answer}")


main()
