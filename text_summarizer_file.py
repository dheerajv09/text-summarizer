from summarizer import Summarizer
from flask import request
from flask import jsonify
from flask import Flask
from flask import send_file
from flask import send_from_directory

from pathlib import Path

import flask

app = Flask(__name__)

def generateSummary(text):

    '''
    text: str # The string body that you want to summarize
    ratio: float # The ratio of sentences that you want for the final summary
    min_length: int # Parameter to specify to remove sentences that are less than 40 characters
    max_length: int # Parameter to specify to remove sentences greater than the max length,
    num_sentences: Number of sentences to use. Overrides ratio if supplied.
    '''

    model = Summarizer()
    result = model(text)
    summary = "".join(result)
    return summary

def load():
    print('* LOADED')

@app.route('/')
def home():
    return 'Hello world'

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    #global response
    text = request.args['text']
    summary = generateSummary(text=text)
    response = {'result' : str(summary)}
    return jsonify(response)


