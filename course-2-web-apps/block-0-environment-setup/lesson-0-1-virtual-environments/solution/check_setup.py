import importlib.metadata


def main():
    try:
        import flask

        print("venv ready")
        print(f"Flask version: {importlib.metadata.version('flask')}")
    except ImportError:
        print("Flask is not installed yet.")
        print("Steps:")
        print("  1. Activate your .venv (see lesson steps)")
        print("  2. Run: pip install flask")
        print("  3. Run this script again")


main()
