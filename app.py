from flask import Flask, render_template, request, send_file, after_this_request
import cv2 as cv
import numpy as np
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process_files():
    names = []
    pictures = request.files.getlist('pictures')

    for picture in pictures:
        picture.save(os.path.join('static', picture.filename))
        names.append(picture.filename)

    # Load the first image from the list in grayscale
    image = cv.imread(os.path.join('static', names[0]), 0)
    row, col = image.shape

    # Create an empty image with the same dimensions as the loaded image
    result = np.zeros((row, col), np.uint8)

    # Iterate over each file name in the list of images
    for name in names:
        result_image = cv.imread(os.path.join('static', name), 0)
        result += result_image // len(names)

    # Resize the resulting image to a fixed size of 500x500 pixels
    result = cv.resize(result, (500, 500))

    # Save the resulting image
    result_path = os.path.join('static', 'result.jpg')
    cv.imwrite(result_path, result)

    @after_this_request
    def remove_uploaded_files(response):
        # Remove the uploaded pictures
        for name in names:
            file_path = os.path.join('static', name)
            if os.path.exists(file_path):
                os.remove(file_path)
        return response

    return render_template('result.html', result_path=result_path)


@app.route('/static/result.jpg')
def get_result():
    return send_file('static/result.jpg', mimetype='image/jpeg')


if __name__ == '__main__':
    app.run()