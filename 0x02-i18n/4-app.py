from flask import Flask, request

app = Flask(__name__)

# Your existing code for translations and setting up the Babel extension

def get_locale():
    if 'locale' in request.args and request.args['locale'] in ['en', 'fr']:
        return request.args['locale']
    return None  # Resort to the default behavior

# Your existing route definitions and other parts of the Flask app

if __name__ == '__main__':
    app.run()

