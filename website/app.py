from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_gtts import gtts

from PIL import Image

import base64
import os
import io
from generate_caption import generate_caption


app = Flask(__name__)
app_gtts = gtts(app)
photos = UploadSet('photos', IMAGES)

# path for saving uploaded images
app.config['UPLOADED_PHOTOS_DEST'] = './static/img'
configure_uploads(app, photos)

# professionals have standards :p
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('upload.html')

# the main route for upload and prediction
@app.route('/caption', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        # save the image

        filename = photos.save(request.files['photo'])
        # load the image
        img_path = './static/img/' + filename
        initial_caption = generate_caption(filename,img_path)
        caption=' '.join(initial_caption.split(' ')[1:-1])
        #caption = generate_caption(filename)
        im = Image.open(img_path)
        data = io.BytesIO()
        #First save image as in-memory.
        im.save(data, "JPEG")
        #Then encode the saved image file.
        encoded_img_data = base64.b64encode(data.getvalue())
        #delete image after it is captioned
        os.remove(img_path)
        #app_gtts.say(text=caption)
        #text_to_speech(caption)
        return render_template("caption.html", img_data=encoded_img_data.decode('utf-8'), caption=caption, sayit= app_gtts.say)

    # web page to show before the POST request containing the image
    return render_template('upload.html')

@app.route('/caption-api', methods=['POST'])
def caption():
    # save the image
    filename = photos.save(request.files['photo'])
    # load the image
    img_path = './static/img/' + filename
    initial_caption = generate_caption(filename,img_path)
    caption=' '.join(initial_caption.split(' ')[1:-1])
    os.remove(img_path)
    # the answer which will be rendered back to the user
    return jsonify({'caption': caption})
    # web page to show before the POST request containing the image

#@app.route('/favicon.ico', methods=['GET'])
#def favicon():
#    return send_from_directory('static/logo', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    #app.run(host='0.0.0.0', debug=True)
    app.run(host='0.0.0.0')
    
