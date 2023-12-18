import flask


app = flask.Flask(__name__, static_folder="dist")


@app.route("/hello")
def hello() -> dict[str, str]:
    return {"message": "Hello World"}


@app.route("/")
def index() -> str | None:
    return flask.send_from_directory(app.static_folder, "index.html")


def create_app(config_filename):
    app = flask.Flask(__name__)
    # app.config.from_pyfile(config_filename)
    # db = SQLAlchemy(app)
