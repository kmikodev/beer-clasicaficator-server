"""
    API REST con Python 3 y SQLite 3
    By Parzibyte: 
    ** https://parzibyte.me/blog **
"""
from flask import Flask, jsonify, request
import beer_controller
from db import create_tables

app = Flask(__name__)


@app.route('/beers', methods=["GET"])
def get_beers():
    beers = beer_controller.get_beers()
    return jsonify(beers)


@app.route("/beer", methods=["POST"])
def insert_beer():
    beer_details = request.get_json()
    name = beer_details["name"]
    comment = beer_details["comment"]
    beer = beer_details["beer"]
    result = beer_controller.insert_beer(name, beer, comment)
    return jsonify({"ok": 'true'})


@app.route("/beer", methods=["PUT"])
def update_beer():
    beer_details = request.get_json()
    id = beer_details["id"]
    name = beer_details["name"]
    beer = beer_details["beer"]
    comment = beer_details["comment"]
    result = beer_controller.update_beer(id, name, beer, comment)
    return jsonify(result)


@app.route("/beer/<id>", methods=["DELETE"])
def delete_beer(id):
    result = beer_controller.delete_beer(id)
    return jsonify(result)


@app.route("/beer/<id>", methods=["GET"])
def get_beer_by_id(id):
    beer = beer_controller.get_by_id(id)
    return jsonify(beer)


if __name__ == "__main__":
    create_tables()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='0.0.0.0', port=80, debug=False)
