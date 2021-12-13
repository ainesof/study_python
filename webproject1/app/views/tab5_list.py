from flask import Blueprint, render_template,request
import traceback
from app.models import query
from datetime import date, timedelta
import pandas as pd

bp = Blueprint('tab5', __name__, url_prefix='/')


@bp.route('/main/')
def main():
    """시작시 조회"""
    try:
        date1 = date.today() - timedelta(2)
        header, df, val = cal(1,date1,'','','','')
        return render_template('tab5/tab5_view.html', queryData1=df,header=header,date1=date1,val1='')
    except:
        traceback.print_exc()

@bp.route('/main/', methods=["POST"])
def tab5_search():
    """submit 값 받아서 출력"""
    try:
        date1=request.form['input']
        header, df, val = cal(1,date1,'','','','')
        return render_template('tab5/tab5_view.html', queryData1=df,header=header,date1=date1,val1='')
    except:
        traceback.print_exc()

@bp.route('/tab5_group/', methods=["POST"])
def tab5_newwindow1():
    try:
        group=''
        NPS=''
        team = request.form['arg1']
        if request.form['arg2']=='0' or request.form['arg4']=='국민연금':
            group='NPS'
            NPS='NPS'
        elif request.form['arg2'] == '1':             group='공제회'
        elif request.form['arg2'] == '2':             group='금융일반'
        elif request.form['arg2'] == '3':             group='생보사'
        elif request.form['arg2'] == '4':             group='손보사'
        elif request.form['arg2'] == '5':             group='연기금'
        elif request.form['arg2'] == '6':             group='은행'
        elif request.form['arg2'] == '7':             group='자산운용'
        elif request.form['arg2'] == '8':             group='저축은행'
        elif request.form['arg2'] == '9':             group='중앙회'
        elif request.form['arg2'] == '10':            group='증권'
        else:                                         group=request.form['arg2']
        date1 = request.form['arg3']
        header, df, val = cal(2,date1,team,group,NPS,request.form['arg4'])
        return render_template('tab5/tab5_group.html', queryData1=df, header=header, date1=date1, group=group, team=team, items=val, selected=request.form['arg4'])

    except:
        traceback.print_exc()

def cal(page,date1,val1,val2,val3,val4):
    """page=페이지구분, date1=날짜"""
    try:
        val=''
        if page==1:
            header = ['고객그룹', '설정액 합', '설정액', '전월말대비', '전분기말대비', '전년말대비', '설정액', '전월말대비', '전분기말대비', '전년말대비']
            df = pd.DataFrame(query(1,date1,'','',''))
            df = df.values.tolist()
        elif page==2:
            """val1=본부, val2=수익그룹, val3=NPS여부"""
            header = ['유형', '설정액', '순자산', '전월말대비', '전분기말대비', '전년말대비', '전전년말대비', '전월말', '전분기말', '전년말', '전전년말']
            if val3 == 'NPS':
                val2 = '연기금'
                val3 = '='
            else:
                val3 = '<>'
            df = pd.DataFrame(query(2,date1,val1,val2,val3))
            if df.empty:
                df=['',0,0,0,0,0,0,0,0,0,0]
            else:
                df.columns = ['SUIK_NAME', 'INTE_FUND_TYPE', 'SUIK_SET_MONEY', 'SUIK_NET_MONEY',
                              'SUIK_NET_MONEYSUM', 'SUIK_NET_MONEYSUM2',
                              'SUIK_NET_MONEYSUM3', 'SUIK_NET_MONEYSUM4',
                              'SUIK_SET_MONEY1', 'SUIK_SET_MONEY2', 'SUIK_SET_MONEY3', 'SUIK_SET_MONEY4']
                val = (df['SUIK_NAME'].drop_duplicates().values.tolist())
                if val4 != 'all' and val4 != '':
                    suik_name=val4
                    df = df.query("SUIK_NAME==@suik_name")
                df = df.groupby(df['INTE_FUND_TYPE']).sum()
                df = df.reset_index()
                df = df.values.tolist()
                valsum=['합계',0,0,0,0,0,0,0,0,0,0]
                for i in range(1, len(df[0])):
                    for j in range(len(df)):
                        valsum[i]+=df[j][i]
                df.append(valsum)
                for i in range(len(df)): # s부동소수점 문제 해결용
                    for j in range(1,len(df[0])-1):
                        if df[i][j]:
                            df[i][j]=round(float(df[i][j]),2)

        return header,df, val
    except:
        traceback.print_exc()




@bp.route('/main/<int:question_id>/')
def detail(question_id):
    """변수 받음"""
    try:
        return render_template('tab5/tab5_view.html',queryData1='',link1='http://127.0.0.1:5000/main',val1=question_id)
    except:
        traceback.print_exc()



@bp.route('/list/')
def q():
    try:
        return '다른페이지'
    except:
        traceback.print_exc()

# https://wikidocs.net/book/4542
# Method Not Allowed 값 넘기는데서 get, post 방식이 안 맞는거