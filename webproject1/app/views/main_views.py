from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
import traceback

bp = Blueprint('main', __name__, url_prefix='/')
err= Blueprint('errors',__name__)

@bp.route('/')
def find_page():
    """main페이지로 보냄"""
    return redirect(url_for('tab5.main'))

@err.app_errorhandler(404)
def page_not_found(e):
    """404 에러처리"""
    return render_template('tab5/error_page.html'),404