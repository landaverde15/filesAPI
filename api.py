# always run Scripts\activate before starting to work on project
import os
import flask
from flask import request, jsonify, render_template

app = flask.Flask(__name__)

photo_directory = "./photos"
if not os.path.exists(photo_directory):
    os.makedirs(photo_directory)

# this method returns the documentation for this API
@app.route("/")
def greetingToAPI():
    ip_address = flask.request.remote_addr
    # return "Welcome to Erik Landaverde's first API from: " + ip_address
    return render_template('index.html', ip_address=ip_address)

# this method returns a JSON list of all files in server
@app.route("/getAllPhotoInfo")
def getAllPhotoInfo():
    photos = []
    for photo in os.listdir(photo_directory):
        path = os.path.join(photo_directory, photo)
        if os.path.isfile(path):
            photos.append(photo)
    return jsonify(photos)

# this method uploads an image to server
@app.route('/uploadPhoto', methods=['POST'])
def uploadPhoto():
    # save file to variable
    uploaded_photo = request.files['image_file']
    # give file a new name
    file_split = os.path.splitext(uploaded_photo.filename)
    file_extension = file_split[1]
    totalFiles = os.listdir(photo_directory)
    totalFilesLength = len(totalFiles)
    uploaded_photo_name = "photo" + str(totalFilesLength) + file_extension
    uploaded_photo.save(os.path.join(photo_directory, uploaded_photo_name))
    return "Image uploaded onto Erik's server"

# method returns number of total photos in server
@app.route("/getTotalNumberOfPhotos", methods=["GET"])
def getTotalNumberOfPhotos():
    # retrive number of photos in server
    totalFiles = os.listdir(photo_directory)
    totalFilesLength = len(totalFiles)
    return totalFilesLength
    

if __name__ == "__main__":
    app.run(debug=True)