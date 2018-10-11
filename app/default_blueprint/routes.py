from flask import Blueprint, render_template


default_blueprint = Blueprint('default_blueprint', __name__)


@default_blueprint.route('/')
def index():
    return render_template('index.html', title='Index Page', content='Hello, World!')
