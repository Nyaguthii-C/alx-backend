#!/usr/bin/env python3
"""Creating a basic flask app"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def Index() -> str:
    """render template for default route"""
    return render_template('index.html')
