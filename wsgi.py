
from waitress import serve
from app import app

if __name__ == "__main__":
    serve(app,port=12514,threads=100)

#if __name__ == "__main__":
#    app.run()