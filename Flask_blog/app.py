from flaskblog import create_app
from flask_sqlalchemy import SQLAlchemy
import os


app = create_app()
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result


if __name__ == '__main__':
	app.run(debug=True)




