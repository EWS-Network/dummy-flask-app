""" MAIN VIEWS FOR FLASK APP"""
from . import App

from flask import (
    Flask, jsonify, request, make_response,
    render_template, redirect, flash
)


@App.route('/', methods=['GET'])
def hello():
    """
    Simple Hello World function
    """
    answer = {}
    answer['reason'] = 'Hello user'
    return make_response(jsonify(answer), 200)


@App.route('/health_check', methods=['GET'])
def healthCheck():
    """
    :return: String defining the status
    """
    answer = {'reason': 'API is running'}
    return make_response(jsonify(answer), 200)
