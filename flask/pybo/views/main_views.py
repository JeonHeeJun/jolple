from flask import Blueprint, render_template
from pybo.models import Question

bp = Blueprint('main',__name__,url_prefix='/');

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    ex_question = Question.query.get(1)
    print(ex_question)
    return 'Pybo index'