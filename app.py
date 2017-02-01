#! /usr/bin/env python2
from os import environ as env

from flask import Flask, request, jsonify
import geocoder

app = Flask(__name__)

@app.route('/geocoder/google')
def google_geocode(address=None):
    address = request.args.get('address')
    g = geocoder.google(address)
    return jsonify(g.latlng)

if __name__ == '__main__':
    DEBUG = False if env['STAGE'] == 'prod' else True
    app.run('localhost', port=5004, debug=True)
