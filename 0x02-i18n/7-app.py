#!/usr/bin/env python3

from flask import Flask, render_template, request, g
from flask_babel import Babel, _, format_datetime
import pytz
from datetime import datetime

app = Flask(__name__)

class Config:
    """Configuration class for Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user() -> Optional[dict]:
    """Retrieve user by ID."""
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None

@app.before_request
def before_request():
    """Set user as a global on flask.g.user."""
    g.user = get_user()

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
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone() -> str:
    """Determine the appropriate timezone."""
    try:
        tzname = request.args.get('timezone')
        if tzname:
            return pytz.timezone(tzname).zone
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    if g.user:
        try:
            return pytz.timezone(g.user['timezone']).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']

@app.route('/')
def homepage():
    current_time = format_datetime(datetime.now())
    return render_template('7-index.html', current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
