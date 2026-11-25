import importlib.metadata


def main():
    try:
        import flask

        # TODO: print "venv ready"
        # TODO: print the Flask version with importlib.metadata.version("flask")
    except ImportError:
        print("Flask is not installed yet.")
        # TODO: print three setup steps:
        #   1. Activate your .venv
        #   2. Run: pip install flask
        #   3. Run this script again


main()
