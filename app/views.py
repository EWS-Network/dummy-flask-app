""" MAIN VIEWS FOR FLASK APP"""
from . import App

from flask import (
    Flask, jsonify, request, make_response,
    render_template, redirect, flash
)

from . import redis_client

def get_count():
    """
    Function to get the count from Redis
    """
    try:
        r_count = redis_client.get('calls_count')
        if r_count is None:
            count = 0
        else:
            count = int(r_count)
        return count
    except Exception as error:
        print(error)
        return 0


def increase_count():
    """
    Function increasing count from Redis
    """
    count = get_count()
    try:
        redis_client.set('calls_count', (count +1))
    except Exception as error:
        print(error)


@App.route('/', methods=['GET'])
def hello():
    """
    Simple Hello World function
    """
    answer = {}
    answer['reason'] = 'Hello user'
    if redis_client is not None:
        increase_count()
    return make_response(jsonify(answer), 200)


@App.route('/stats/count', methods=['GET'])
def stats_count():
    """
    :return: String defining the status
    """
    answer = {'reason': 'API is running'}
    if redis_client is not None:
        count = get_count()
    else:
        count = -1
    answer['Count'] = count
    if count < 0:
        answer['CountReason']: 'Error getting the statistics from Redis'
    return make_response(jsonify(answer), 200)


@App.route('/stats/reset', methods=['GET'])
def stats_reset():
    """
    :return: 200 when stats are reset in redis
    """
    if redis_client is not None:
        redis_client.set('calls_count', 0)
        answer = {'reason': 'statistics reset'}
    else:
        answer = {'reason': 'no statistics to reset'}
    return make_response(jsonify(answer), 200)


@App.route('/health_check', methods=['GET'])
def healthCheck():
    """
    :return: String defining the status
    """
    answer = {'reason': 'API is running'}
    if redis_client is not None:
        if redis_client.ping():
            answer['RedisService'] = 'Healthy'
            return make_response(jsonify(answer), 200)
        else:
            answer['RedisService'] = 'UnHealthy'
            return make_response(jsonify(answer), 200)

    else:
        answer = {'reason': 'API is running'}
        return make_response(jsonify(answer), 200)
