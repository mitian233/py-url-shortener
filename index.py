from flask import Flask, abort, render_template, request, redirect
import os
from dotenv import load_dotenv
import main as main
import json

load_dotenv()
site_url = os.getenv('SITE_URL')
site_url = main.format_url(site_url)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False  # json出力のソートを無効化


# CORS対策
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    resp.headers['Access-Control-Allow-Methods'] = 'GET'
    return resp


app.after_request(after_request)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/shorten', methods=['POST'])
def shorten():
    if request.method == 'POST':
        orig_url = main.format_url(request.form['origurl'])
        if request.form['shortened_url'] == '':
            shorten = main.create_shortened_url(orig_url)
        else:
            shorten = main.create_shortened_url(orig_url, defined_shortened_url=request.form['shortened_url'])
        return render_template('shorten.html', site_url=site_url, shorten=shorten)


@app.route('/<shortened_url>')
def redirect_to_original_url(shortened_url):
    url = main.get_original_url(shortened_url)
    if url is None:
        return abort(404)  # 短縮URLが存在しない場合は404を返す
    else:
        return redirect(url)


# API
@app.route('/api/shorten', methods=['GET'])
def api_shorten():
    orig_url = main.format_url(request.args.get('url', ''))
    shorten_url = request.args.get('shorten', '')
    if orig_url == '':
        return json.dumps({'status': 'error', 'shortened_url': '', 'path': '', 'message': 'url is empty'})
    else:
        if shorten_url != '':
            shorten = main.create_shortened_url(orig_url)
        else:
            shorten = main.create_shortened_url(orig_url, defined_shortened_url=shorten_url)
        genurl = site_url + shorten
        return json.dumps({'status': 'OK', 'shortened_url': site_url + shorten, 'path': shorten, 'message': ''})


@app.route('/api/jumpto', methods=['GET'])
def api_jumpto():
    shortened_url = request.args.get('shortened_url', '')
    if shortened_url == '':
        return json.dumps({'status': 'error', 'original_url': '', 'message': 'shortened_url is empty'})
    else:
        original = main.get_original_url(shortened_url)
        return json.dumps({'status': 'OK', 'original_url': original, 'message': ''})


if __name__ == '__main__':
    app.run()
