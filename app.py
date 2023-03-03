from flask import Flask
from flask_cors import CORS
from requests import get, post

app = Flask(__name__)
CORS(app)

BASE_URL = 'https://annauniv.irins.org/profile/'

@app.route('/<id>')
def index(id):
    response = get(BASE_URL  + id)
    return response.text


@app.route('/publications/<id>/<page>')
def publications(id, page):
    data = {
        'current_page': page,
        'expert_id': id,
        'sort_by': 'year',
        'direction': 'desc'
    }
    res = post(BASE_URL + 'get_publication', data=data)
    return res.text


@app.route('/google_citation/<id>')
def citations(id):
    print(id)
    data = {'expert_id': id}
    res = post(BASE_URL + 'getgooglecitation', data=data)
    return res.json()