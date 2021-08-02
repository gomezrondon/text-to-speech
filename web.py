# https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python?authuser=0
#
# pip install Flask
from flask import Flask, request, send_file
from push_to_bucket import *
from main import *
import os

app = Flask(__name__)

def time():
    import time
    return time.ctime()

@app.route("/time")
def what_time():
    return "the time is: "+time()

@app.route("/process", methods=['POST'])
def process_file():
    json_body = request.get_json()
    bucket = json_body['bucket']
    lang = json_body['lang']

    if lang == "es":
        lang = "es-us"

    inputFile = 'text.txt'
    print(bucket)
    print(lang)
    download_file(bucket, 'python-text.txt', inputFile)
    generate_mp3(inputFile, lang)
    # upload_to_bucket(bucket, 'audio.mp3', 'python-audio.mp3')
    return send_file("/tmp/audio.mp3",as_attachment=True)

@app.route("/listfiles")
def list_files():
    names = []
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        names.append(f)
    return str(names)


# do something

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=8080)