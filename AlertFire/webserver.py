# -*- coding: utf-8 -*-

import os

from flask import Flask, render_template, redirect, url_for, request

UPLOAD_FOLDER = '/static/images/detection'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

setTemp = 100
lastDangerous = 0


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/templates/main.html')
def secondIndex():
    return redirect(url_for('index'))


@app.route('/templates/admin.html')
def admin():
    return render_template('admin.html')


@app.route('/templates/dangerous.html', methods=['POST', 'GET'])
def originalDangerous():
    if request.method == 'POST':
        result = request.form
        if lastDangerous == 0:
            return render_template('dangerous.html',result=result)

        elif lastDangerous == 1:
            return render_template('dangerous1.html',result=result)

        elif lastDangerous == 2:
            return render_template('dangerous2.html',result=result)


@app.route('/templates/dangerous1.html')
def firstDangerous():
    return render_template('dangerous.html')


@app.route('/templates/dangerous2.html')
def secondDangerous():
    return render_template('dangerous2.html')


@app.route('/templates/newFiles.html')
def newFiles():
    return render_template('newFiles.html')


# @app.route('/templates/dangerous/<int:max_t>')
# def maxTemp(max_t):
#     global setTemp
#     setTemp = max_t
#     return render_template(url_for('O'))
#
#
# @app.route('/maxtemp')
# def returnTemp():
#     return {'maxtemp': setTemp}
#
# @app.route('/static/images/detection')


# @app.route('/now-images', methods=['GET', 'POST'])
# def upload_images():
#     if request.method == 'POST':
#         file = request.files['file']
#         if file:
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
