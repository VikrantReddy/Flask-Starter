from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from app.mod_auth.controllers import mod_auth as auth_module  # noqa

app.register_blueprint(auth_module)

db.create_all()
