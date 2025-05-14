from flask import Flask, request, render_template, url_for, flash, redirect
import os
import cv2
import numpy as np
from PIL import Image
import random
import string

app = Flask(__name__)
app.config['INITIAL_FILE_UPLOADS'] = 'static/uploads'
app.config['SECRET_KEY'] = 'my-unique-secret-key-2025'

os.makedirs(app.config['INITIAL_FILE_UPLOADS'], exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", full_filename=None)

    if request.method == "POST":
        if 'image_upload' not in request.files or request.files['image_upload'].filename == '':
            flash("Please upload an image!", "error")
            return redirect(url_for('index'))

        image_upload = request.files['image_upload']
        try:
            image = Image.open(image_upload)
            image_logow = np.array(image.convert('RGB'))
            h_image, w_image, _ = image_logow.shape
        except Exception as e:
            flash("Invalid image file!", "error")
            return redirect(url_for('index'))

        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(10)) + '.png'
        full_filename = 'uploads/' + name
        save_path = os.path.join(app.config['INITIAL_FILE_UPLOADS'], name)

        option = request.form.get('options')
        if option == 'logo_watermark':
            if 'logo_upload' not in request.files or request.files['logo_upload'].filename == '':
                flash("Please upload a logo!", "error")
                return redirect(url_for('index'))

            logo_upload = request.files['logo_upload']
            try:
                logo = Image.open(logo_upload)
                logo = np.array(logo.convert('RGB'))
                h_logo, w_logo, _ = logo.shape
            except Exception as e:
                flash("Invalid logo file!", "error")
                return redirect(url_for('index'))

            center_y = int(h_image / 2)
            center_x = int(w_image / 2)
            top_y = center_y - int(h_logo / 2)
            left_x = center_x - int(w_logo / 2)
            bottom_y = top_y + h_logo
            right_x = left_x + w_logo

            top_y, bottom_y = max(0, top_y), min(h_image, bottom_y)
            left_x, right_x = max(0, left_x), min(w_image, right_x)
            roi = image_logow[top_y:bottom_y, left_x:right_x]
            logo_resized = cv2.resize(logo, (right_x - left_x, bottom_y - top_y))
            result = cv2.addWeighted(roi, 1, logo_resized, 1, 0)
            cv2.line(image_logow, (0, center_y), (left_x, center_y), (0, 0, 255), 1)
            cv2.line(image_logow, (right_x, center_y), (w_image, center_y), (0, 0, 255), 1)
            image_logow[top_y:bottom_y, left_x:right_x] = result

        else:
            text_mark = request.form.get('text_mark', '').strip()
            if not text_mark:
                flash("Please enter text for watermark!", "error")
                return redirect(url_for('index'))

            cv2.putText(image_logow, text=text_mark, org=(w_image - 250, h_image - 20),
                        fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.7, color=(255, 0, 0),
                        thickness=2, lineType=cv2.LINE_4)

        img = Image.fromarray(image_logow, 'RGB')
        img.save(save_path)
        flash("Watermark applied successfully!", "success")
        return render_template('index.html', full_filename=full_filename)

if __name__ == '__main__':
    app.run(debug=True)