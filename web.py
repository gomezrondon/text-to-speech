# https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python?authuser=0
#
# pip install Flask
from flask import Flask

app = Flask(__name__)

def time():
    import time
    return time.ctime()

@app.route("/time")
def what_time():
    return "the time is: "+time()


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=8080)