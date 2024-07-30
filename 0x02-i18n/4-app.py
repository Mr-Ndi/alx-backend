#!/usr/bin/env python3

from flask import Flask, render_template, request
from flask_babel import Babel, _
from typing import Optional

app = Flask(__name__)

class Config:
    """Configuration class for Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

babel = Babel(app)

@babel.localeselector
def get_locale() -> Optional[str]:
    """
    Determine the best match with our supported languages.
    
    This function uses request.accept_languages to find the best match
    from the supported languages or locale from URL parameter.
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def homepage():
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run(debug=True)
