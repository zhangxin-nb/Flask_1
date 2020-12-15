from  flask import Flask


def crate_app():
    app = Flask(__name__,instance_relative_config=True)
    from . import auth
    app.register_blueprint(auth.bp)
    return app
