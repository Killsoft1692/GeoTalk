from flask_api import FlaskAPI, status

app = FlaskAPI(__name__)

from views import *

if __name__ == "__main__":
    app.run(debug=True)
