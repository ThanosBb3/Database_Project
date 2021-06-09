import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host=os.getenv("IP", "localhost"), port=int(os.getenv("PORT", 8765)), debug=True)