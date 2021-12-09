from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
import traceback
from app.models import query
import pandas as pd

bp = Blueprint('main', __name__, url_prefix='/')

err= Blueprint('errors',__name__)

@bp.route('/')
def hello_pybo():
    """SQL조회"""
    try:
        df=pd.DataFrame(query('select * from SUIKJA_INFO where rownum<=2'))
        df=df.values.tolist()
        return render_template('question/question_list.html',queryData1=df[0],queryData2=df[1],link1='http://127.0.0.1:5000/main', val1='')

    except:
        traceback.print_exc()


@bp.route('/<int:question_id>/')
def detail(question_id):
    """변수 받음"""
    try:
        return render_template('question/question_list.html',queryData1='',queryData2='',link1='http://127.0.0.1:5000/main',val1=question_id)
    except:
        traceback.print_exc()

@bp.route('/main/')
def find_page():
    """다른 페이지를 재검색"""
    return redirect(url_for('question.q'))

@err.app_errorhandler(404)
def page_not_found(e):
    """404 에러처리"""
    return render_template('question/error_page.html'),404