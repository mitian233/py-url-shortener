from flask import Flask, abort, render_template, request, redirect
import pymongo
import os
from dotenv import load_dotenv
import main as main

load_dotenv()

app = Flask(__name__)

client = pymongo.MongoClient(os.getenv('MONGO_URL'))
db = client[os.getenv('MONGO_DB')]
collection = db[os.getenv('MONGO_COLLECTION')]
url_length = int(os.getenv('URL_LENGTH'))
site_url = os.getenv('SITE_URL')

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/shorten', methods=['GET', 'POST'])
def shorten():
    if request.method == 'POST':
        orig_url = request.form['origurl']
        if request.form['shortened_url'] == '':
            shorten = main.create_shortened_url(orig_url)
        else:
            shorten = main.create_shortened_url(orig_url, defined_shortened_url = request.form['shortened_url'])
        return render_template('shorten.html', site_url = site_url, shorten = shorten)

@app.route('/<shortened_url>')
# if not exist return 404
def redirect_to_original_url(shortened_url):
    url = main.get_original_url(shortened_url)
    if url is None:
        return abort(404)
    else:
        return redirect(url)

if __name__ == '__main__':
    app.run()
