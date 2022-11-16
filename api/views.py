from api import server
from flask import render_template, request, redirect, jsonify, make_response, send_from_directory, abort
import os
import nude
from PIL import Image

# By default access template folder in root of package
@server.route('/')
def login():
    return "SERVER IS UP & RUNNING."

@server.route('/upload', methods=['POST'])
def upload():

    try:

        if not request.files:
            return make_response(jsonify({"message":"Body can't be empty"}), 400)

        image = request.files['img']

        im = Image.open(image)
        isNude = nude.is_nude(im)
        if isNude:
            return make_response(jsonify({"message":"The picture is NSFW, so unable to upload."}), 400)

        image.seek(0)
        image.save(os.path.join(server.root_path+'/static/img/uploads', image.filename))

        return make_response(jsonify({"message":"Upload Success !"}), 200)

    except:
        return make_response(jsonify({"message":"Internal Server Error"}), 500)


