from flask import Blueprint, render_template,request
import traceback

bp = Blueprint('question', __name__, url_prefix='/')

@bp.route('/list/')
def q():
    try:
        return '다른페이지'
    except:
        traceback.print_exc()

@bp.route('/answer/', methods=["POST"])
def answer():
    try:
        value=request.form['input']
        return value
    except:
        traceback.print_exc()