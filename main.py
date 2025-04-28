from flask import Flask, render_template
import random

app = Flask(__name__)

def get_random_background():
    backgrounds = [
        'background (2).jpg',
        'background (4).jpeg',
        'background (5).jpeg',
        'background (6).jpeg',
        'background.jpg'
    ]
    return random.choice(backgrounds)

@app.route('/')
def home():
    background = get_random_background()
    return render_template('index.html', background_image=background)

@app.route('/sad')
def sad():
    background = get_random_background()
    return render_template('sad.html', background_image=background)

@app.route('/hug')
def hug():
    background = get_random_background()
    return render_template('hug.html', background_image=background)

@app.route('/miss')
def miss():
    background = get_random_background()
    return render_template('miss.html', background_image=background)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
