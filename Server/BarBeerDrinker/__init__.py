from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request
import json

from BarBeerDrinker import database

app = Flask(__name__)

@app.route('/api/bar', methods=["GET"])
def get_bars():
    return jsonify(database.get_bars())


@app.route("/api/bar/<barId>", methods=["GET"])
def find_bar(barId):
    try:
        if barId is None:
            raise ValueError("Bar is not specified.")
        bar = database.find_bar(barId)
        if bar is None:
            return make_response("No bar found with the given name.", 404)
        return jsonify(bar)
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)


@app.route("/api/beers_cheaper_than", methods=["POST"])
def find_beers_cheaper_than():
    body = json.loads(request.data)
    max_price = body['maxPrice']
    return jsonify(database.filter_beers(max_price))


@app.route('/api/menu/<barId>', methods=['GET'])
def get_menu(barId):
    try:
        if barId is None:
            raise ValueError('Bar is not specified.')
        bar = database.find_bar(barId)
        if bar is None:
            return make_response("No bar found with the given id.", 404)
        return jsonify(database.get_bar_menu(barId))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)


@app.route("/api/bar-cities", methods=["GET"])
def get_bar_cities():
    try:
        return jsonify(database.get_bar_cities())
    except Exception as e:
        return make_response(str(e), 500)


@app.route("/api/items", methods=["GET"])
def get_beers():
    print("Getting beers")
    try:
        return jsonify(database.get_beers())
    except Exception as e:
        return make_response(str(e), 500)


@app.route("/api/beer-manufacturer", methods=["GET"])
def get_beer_manufacturers():
    print("abcd")
    try:
        return jsonify(database.get_beer_manufacturers(None))
    except Exception as e:
        print("Exception")
        return make_response(str(e), 500)


@app.route("/api/beer-manufacturer/<itemId>", methods=["GET"])
def get_manufacturers_making(beer):
    print("This one")
    try:
        return jsonify(database.get_beer_manufacturers(itemId))
    except Exception as e:
        return make_response(str(e), 500)


@app.route("/api/likes", methods=["GET"])
def get_likes():
    try:
        drinker = request.args.get("drinker")
        if drinker is None:
            raise ValueError("Drinker is not specified.")
        return jsonify(database.get_likes(drinker))
    except Exception as e:
        return make_response(str(e), 500)


@app.route("/api/drinker", methods=["GET"])
def get_drinkers():
    try:
        return jsonify(database.get_drinkers())
    except Exception as e:
        return make_response(str(e), 500)


@app.route("/api/drinker/<name>", methods=["GET"])
def get_drinker(name):
    try:
        if name is None:
            raise ValueError("Drinker is not specified.")
        return jsonify(database.get_drinker_info(name))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)


@app.route('/api/bars-selling/<items>', methods=['GET'])
def find_bars_selling(beer):
    print("This..")
    try:
        if beer is None:
            raise ValueError('Beer not specified')
        return jsonify(database.get_bars_selling(beer))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)


@app.route('/api/frequents-data', methods=['GET'])
def get_bar_frequent_counts():
    try:
        return jsonify(database.get_bar_frequent_counts())
    except Exception as e:
        return make_response(str(e), 500)