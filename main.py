# https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python?authuser=0
#
# pip install Flask
from flask import Flask, request, send_file
from push_to_bucket import *
from old_main import *
import os
import json

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
    print(">>>>>"+str(json_body))
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

@app.route("/v2/process", methods=['POST'])
def process_file2():
    json_body = request.get_json()
    print(">>>>>"+str(json_body))
    bucket = json_body['bucket']
    lang = json_body['lang']
    bucket_file = json_body['file']

    if lang == "es":
        lang = "es-us"

    #local name of the file
    inputFile = "text.txt"
    download_file(bucket, bucket_file, inputFile)
    generate_mp3(inputFile, lang)
    hasValue = str(hash(time()))
    hasValue = hasValue[1:11]
    ouputName = 'audio-'+hasValue+'.mp3'
    upload_to_bucket(bucket, 'audio.mp3', ouputName)
    data = {
        "file-name": ouputName
    }
    return json.dumps(data)


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