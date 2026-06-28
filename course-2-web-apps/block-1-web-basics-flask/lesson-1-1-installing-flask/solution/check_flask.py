# check_flask.py
# Route Lab — verify Flask is installed in your activated venv

import importlib.metadata
import flask

print("Flask import OK!")
print(f"Flask version: {importlib.metadata.version('flask')}")
