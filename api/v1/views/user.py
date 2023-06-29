#!/usr/bin/python3

from flask import abort, jsonify, make_response, request

from api.v1.views import api
from models.base_model import BaseModel, db
from models.user import User

@api.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """
    Retrieves all users from the database
    """
    users = User.query.all()
    user_list = []
    for user in users:
        user_data = user.to_dict()
        user_list.append(user_data)
    return jsonify(user_list)

@api.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_one_user(user_id):
    """
    Retrieve one user from the database using
    the provided user_id
    """
    user = User.query.get(user_id)
    if user:
        user_data = user.to_dict()
        return jsonify(user_data)
    abort(404)

@api.route('/users', methods=['POST'], strict_slashes=False)
def post_new_user():
    """
    posts a new user to the database
    """
    form = request.get_json()
    if not form:
        return jsonify({"error": "Not a JSON"})
    if "email" not in form:
        return jsonify({"error": "Missing email"})
    user = User()
    for key, value in form.items():
        setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict()), 201
    user.close()