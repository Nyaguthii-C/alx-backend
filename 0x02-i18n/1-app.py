#!/usr/bin/env python3
"""Basic Babel setup"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
# instatiate babel object
babel = Babel(app)


class Config(object):
    """set babel configuration values"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/", methods=['GET'])
def Index() -> str:
    """render template for default route"""
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
