import os
import sys
from app.app import create_app
sys.path.append(os.path.dirname(__name__))


application = create_app()

if __name__ == "__main__":
    app.run(use_reloader=False)
