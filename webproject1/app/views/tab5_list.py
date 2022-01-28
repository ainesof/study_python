import math
import os.path

from flask import Blueprint, render_template, request, send_file
import traceback, socket
from app.models import query, dateQuery, etcQuery
import pandas as pd
import json
import ftplib
from collections import OrderedDict

bp = Blueprint('tab5', __name__, url_prefix='/')


# -------------------------메인

@bp.route('/main/', methods=["GET","POST"])
def main():
    """win=창, logic=실행 모듈"""
    try:
        recentlydate = dateQuery('tab5_view', 'recently', '', '')
        recentlydate = recentlydate[0][0]
        if request.method=='GET':
            win = 1
            logic = 1
            date1 = recentlydate
        elif request.method=='POST':
            date1 = request.form['datepicker']
            win = int(request.form['win'])
            logic = int(request.form['logic'])

        header, df, selectlist, searchdate = cal('tab5_view',win, logic, date1, '', '', '', '')
        df2 = setComma(df,1)
        """queryData1: 내용, header: 테이블 컬럼, searchdate: 조회기준 날짜, data1:날짜, recentlydate: 최근 데이터 날짜, ip:접속자 IP """
        return render_template('tab5/tab5_view.html', queryData1=df2, header=header, searchdate=searchdate,
                               date1=date1, recentlydate=recentlydate, ip=request.environ.get('HTTP_X_REAL_IP', request.remote_addr), win=win,
                               logic=logic)

    except:
        traceback.print_exc()

@bp.route('/main2/', methods=["GET","POST"])
def main2():
    """win=창, logic=실행 모듈"""
    try:
        recentlydate = dateQuery('tab5_view', 'recently', '', '')
        recentlydate = recentlydate[0][0]
        if request.method=='GET':
            win = 1
            logic = 2
            date1 = recentlydate
        elif request.method=='POST':
            date1 = request.form['datepicker']
            win = int(request.form['win'])
            logic = int(request.form['logic'])

        # tab5_readJson()
        # tab5_createJson()
        header, df, selectlist, searchdate = cal('tab5_view',win, logic, date1, '', '', '', '')
        df2 = setComma(df,1)
        """queryData1: 내용, header: 테이블 컬럼, searchdate: 조회기준 날짜, data1:날짜, recentlydate: 최근 데이터 날짜, ip:접속자 IP """
        return render_template('tab5/tab5_view.html', queryData1=df2, header=header, searchdate=searchdate,
                               date1=date1, recentlydate=recentlydate, ip=request.environ.get('HTTP_X_REAL_IP', request.remote_addr), win=win,
                               logic=logic)
    except:
        traceback.print_exc()

# -----------------------------------

@bp.route('/tab5_group/', methods=["POST"])
def tab5_newwindow1():
    """logic1 win1_arg1:본부, win1_arg2:그룹, win1_arg3:날짜, win1_arg4:국민연금 여부"""
    """logic2 win1_arg1:본부, win1_arg2:유형, win1_arg3:날짜, win1_arg4:국민연금 여부"""
    try:
        win = 2
        logic = int(request.form['logic'])
        team = request.form['win1_arg1']
        win1_arg2=request.form['win1_arg2']
        recentlydate = dateQuery('tab5_view', 'recently', '', '')
        recentlydate = recentlydate[0][0]
        if logic==1:
            if win1_arg2 == '0' or request.form['win1_arg4'] == '국민연금':
                group = 'NPS'
            elif win1_arg2 == '1':
                group = '공제회'
            elif win1_arg2 == '2':
                group = '금융일반'
            elif win1_arg2 == '3':
                group = '생보사'
            elif win1_arg2 == '4':
                group = '손보사'
            elif win1_arg2 == '5':
                group = '연기금'
            elif win1_arg2 == '6':
                group = '은행'
            elif win1_arg2 == '7':
                group = '일반법인'
            elif win1_arg2 == '8':
                group = '자산운용'
            elif win1_arg2 == '9':
                group = '저축은행'
            elif win1_arg2 == '10':
                group = '중앙회'
            elif win1_arg2 == '11':
                group = '증권'
            else:
                group = win1_arg2
            date1 = request.form['win1_arg3']
            header, df, selectlist, searchdate = cal('tab5_group',win, logic, date1, team, group, '', request.form['win1_arg4'])
            df2 = setComma(df,1)
            if len(selectlist)==0:
                selectlist['selectlist1']=''
            """queryData1:내용, header:테이블 컬럼, searchdate:조회기준 날짜, recentlydate: 최근 데이터 날짜,
            team:본부, date1:조회일, readonly:고객그룹,  selection:수익자,selected:선택된 수익자, ip:접속자 IP"""
            return render_template('tab5/tab5_group.html', queryData1=df2, header=header, searchdate=searchdate, recentlydate=recentlydate,
                                   team=team, date1=date1, readonly=group, selection=selectlist['selectlist1'], selected=request.form['win1_arg4'],
                                   ip=request.environ.get('HTTP_X_REAL_IP', request.remote_addr), win=win, logic=logic)

        elif logic==2:
            if request.form['win1_arg2'] == '0':
                item = '글로벌'
            elif request.form['win1_arg2'] == '1':
                item = '주식형'
            elif request.form['win1_arg2'] == '2':
                item = '채권형'
            else:
                item = request.form['win1_arg2']
            date1 = request.form['win1_arg3']
            header, df, selectlist, searchdate = cal('tab5_group',win, logic, date1, team, item, '', request.form['win1_arg4'])
            df2 = setComma(df,1)

            """queryData1:내용, header:테이블 컬럼, searchdate:조회기준 날짜, recentlydate: 최근 데이터 날짜,
            team:본부, date1:조회일, readonly:항목, selection:그룹, selected:선택된 그룹, ip:접속자 IP"""
            return render_template('tab5/tab5_group.html', queryData1=df2, header=header, searchdate=searchdate, recentlydate=recentlydate,
                                   team=team, date1=date1, readonly=item,  selection=selectlist['selectlist1'], selected=request.form['win1_arg4'],
                                   ip=request.environ.get('HTTP_X_REAL_IP', request.remote_addr), win=win, logic=logic)
    except:
        traceback.print_exc()


@bp.route('/tab5_items/', methods=["POST"])
def tab5_newwindow2():
    """logic1 arg1:본부, arg2:그룹, arg3:날짜, arg4:유형"""
    """logic2 arg1:본부, arg2:유형, arg3:날짜, arg4:수익자"""
    try:
        win = int(request.form['win'])
        logic = int(request.form['logic'])
        suikja='all'
        selected='all'

        if win == 2:
            NPS = ''
            win = 3
            # team = request.form['win2_arg1']
            selection = request.form['win2_arg2']
            date1 = request.form['win2_arg3']
            readonly = request.form['win2_arg4']
            if selection == 'NPS':
                selection = '연기금'
            if logic == 2:
                suikja = readonly
                group=etcQuery('group',readonly)
                readonly=group[0][0]

        elif win == 3:
            selection = request.form['selection']
            date1 = request.form['datepicker']
            readonly = request.form['readonly']
            suikja = request.form['suikja']

        recentlydate = dateQuery('tab5_view', 'recently', '', '')
        recentlydate=recentlydate[0][0]
        # if group == 'NPS':
        #     NPS = 'NPS'
        header, df, selectlist, searchdate = cal('tab5_items',win, logic, date1, readonly, selection, suikja, '')
        df2 = setComma(df,3)
        # readonly=items

        """queryData1:내용, header:테이블 컬럼, searchdate:조회기준 날짜 date1:조회일, recentlydate: 최근 데이터 날짜,
         readonly: 고정박스 값, selection1,2: 선택가능 값, selected:선택된 항목, team:본부, ip:접속자 IP"""
        return render_template('tab5/tab5_items.html', queryData1=df2, header=header, searchdate=searchdate,
                               date1=date1, recentlydate=recentlydate,readonly=readonly,selection1=selectlist['selectlist1'],
                               selection2=selectlist['selectlist2'], selected=selection, selected2=suikja,
                               ip=request.environ.get('HTTP_X_REAL_IP', request.remote_addr), win=win, logic=logic)

    except:
        traceback.print_exc()


@bp.route('/find_suikja/', methods=["GET","POST"])
def find_suikjaPopup():
    """수익자 찾는 팝업"""
    try:
        logic = 99
        win = 1
        if request.method=='GET':
            """윈도우 오픈시"""
            suikja=''
        elif request.method=='POST':
            """글자 검색시"""
            win = int(request.form['win'])
            logic = int(request.form['logic'])
            suikja = request.form['suikja']

        df = pd.DataFrame(query(win, logic, '', suikja, '', ''))
        df = df.values.tolist()
        return render_template('tab5/find_suikja.html',queryData1=df,date1='',suikja=suikja,win=win,logic=logic)

    except:
        traceback.print_exc()

@bp.route('/find_suikja2/', methods=["GET","POST"])
def find_suikjaPopup2():
    """수익자정보 창에서 고객명 검색 유입"""
    try:
        logic = 99
        win = 1
        date1 = request.form['arg1']
        df = pd.DataFrame(query(win, logic, '', '', '', ''))
        df = df.values.tolist()
        return render_template('tab5/find_suikja.html',queryData1=df,date1=date1,win=win,logic=logic)

    except:
        traceback.print_exc()


@bp.route('/tab5_suikja/', methods=["GET","POST"])
def tab5_newwindow_suikja():
    """수익자 정보 다이렉트 검색"""
    try:
        suikja=''
        date1=''
        items=''
        selected=''
        win=int(request.form['win'])
        recentlydate = dateQuery('tab5_view', 'recently', '', '')
        recentlydate = recentlydate[0][0]

        if win == 1:
            """팝업으로 들어올시"""
            win = 2
            date1 = request.form['date1']
            suikja = request.form['find_arg1']
            if date1=='':
                date1 = recentlydate
        elif win == 2:
            """내부 검색"""
            date1 = request.form['datepicker']
            suikja = request.form['find']
            items = request.form['items']

        logic = int(request.form['logic'])
        header, df, selectlist, searchdate = cal('tab5_suikja',win, logic, date1, suikja, items, '', '')
        df2 = setComma(df,2)

        """queryData1:내용, header:테이블 컬럼, searchdate:조회기준 날짜 date1:조회일, recentlydate: 최근 데이터 날짜
        ,suikja:검색고객,items:상품유형, selected:선택된 유형,ip:접속자 IP"""
        return render_template('tab5/tab5_suikja.html', queryData1=df2, header=header, searchdate=searchdate,
                               date1=date1, recentlydate=recentlydate, suikja=suikja, items=selectlist['selectlist1'], selected=items,
                               ip=request.environ.get('HTTP_X_REAL_IP', request.remote_addr),win=win, logic=logic)

    except:
        traceback.print_exc()


@bp.route('/layout/')
def layout():
    """사이트 흐름도 보여줌"""
    try:
        recentlydate = dateQuery('tab5_view', 'recently', '', '')
        df = dateQuery('layout', 'parity', '', recentlydate[0][0])
        df.columns=["No","index","suik_set_money","parity"]
        df = df.values.tolist()

        return render_template('tab5/layout.html', queryData1=df)

    except:
        traceback.print_exc()

@bp.route('/jsontest2/', methods=['POST'])
def callAjax2():
    """버튼 클릭시 refresh"""
    try:
        # arr=request.form['sendMSG']
        recentlydate = dateQuery('tab5_view', 'recently', '', '')
        df = dateQuery('layout', 'parity', '', recentlydate[0][0])
        df.columns=["No","index","suik_set_money","parity"]
        value = df.values.tolist()

        return json.dumps(value)

    except:
        traceback.print_exc()

def cal(gubun,win, logic, date1, val1, val2, val3, val4):
    """logic:페이지구분, date1:날짜"""
    try:
        selectlist = {}
        df2 = dateQuery(gubun,'header',win,date1)
        searchdate = df2.values.tolist()

        if gubun == 'tab5_view' and win == 1:
            if logic == 1:
                header = ['고객그룹', '설정액 합', '설정액', '전월말대비', '전분기말대비', '전년말대비', '설정액',
                          '전월말대비', '전분기말대비', '전년말대비']
            if logic == 2:
                header = ['유형', '설정액 합', '설정액', '전월말대비', '전분기말대비', '전년말대비', '설정액',
                          '전월말대비', '전분기말대비', '전년말대비']
            df = pd.DataFrame(query(win, logic, date1, '', '', ''))
            df = df.values.tolist()
            if len(df) == 0:
                df = ['', 0, 0, 0, 0, 0, 0, 0, 0, 0]
            changeWon(df,1)


        elif gubun == 'tab5_group' and win == 2:
            """logic 1 val1:본부, val2:수익그룹, val4: 수익자명(재검색용)"""
            """logic 2 val1:본부, val2:항목, val4: 고객그룹(재검색용)"""

            header = ['NULL', '설정액', '순자산', '전월말대비', '전분기말대비', '전년말대비', '전전년말대비', '전월말',
                      '전분기말', '전년말', '전전년말']

            if val2 == 'NPS':
                val2 = '연기금'
                val3 = 'PN_NPS'
            else:
                val3 = ''
            df = pd.DataFrame(query(win, logic, date1, val1, val2, val3))
            if len(df.index) == 0:
                df = [['값 없음', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            else:
                df.columns = ['SUIK_NAME', 'NULL', 'SUIK_SET_MONEY', 'SUIK_NET_MONEY',
                              'SUIK_NET_MONEYSUM', 'SUIK_NET_MONEYSUM2',
                              'SUIK_NET_MONEYSUM3', 'SUIK_NET_MONEYSUM4',
                              'SUIK_SET_MONEY1', 'SUIK_SET_MONEY2', 'SUIK_SET_MONEY3', 'SUIK_SET_MONEY4']
                valsum = ['합계', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                gubunja=[{"header" : "유형","column":"INTE_FUND_TYPE","gubun3":"SUIK_NAME","grouping":"INTE_FUND_TYPE"},
                         {"header" : "고객그룹","column":"suik_group","gubun3":"suik_group","grouping":"SUIK_NAME"}]
                i=logic-1

                header[0] = gubunja[i]['header']
                df.rename(columns={"NULL": gubunja[i]['column']}, inplace=True)
                selectlist['selectlist1'] = (df[gubunja[i]['gubun3']].drop_duplicates().values.tolist())
                if val4 != 'all' and val4 != '':
                    where = val4
                    df = df.query(gubunja[i]['gubun3']+"==@where")
                df = df.groupby(df[gubunja[i]['grouping']]).sum()
                df = df.reset_index()
                df = df.values.tolist()

                if df:
                    for i in range(1, len(df[0])):
                        for j in range(len(df)):
                            valsum[i] += math.floor(df[j][i])
                    df.append(valsum)
                    changeWon(df,1)
                else:
                    df = [['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


        elif gubun == 'tab5_items':
            """val1:고정박스값, val2:선택가능값, val3:선택된 수익자"""
            header = ['수익자명','펀드번호','펀드명','설정액', '전월말대비', '전분기말대비', '전년말대비', '전전년말대비', '전월말',
                      '전분기말', '전년말', '전전년말']
            NPS = ''
            querycolumn = val1

            if val2 == 'NPS':
                val2 = '연기금'
                NPS = '='
            else:
                NPS = '<>'
            df = pd.DataFrame(query(win, logic, date1, val1, val2, NPS))
            if len(df.index) == 0:
                df = [['값 없음', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            else:
                columns=['SUIK_NAME','SUIK_GROUP', 'INTE_FUND_TYPE','FUND_CD', 'SUIK_SET_MONEY', 'SUIK_NET_MONEY',
                              'SUIK_NET_MONEYSUM', 'SUIK_NET_MONEYSUM2',
                              'SUIK_NET_MONEYSUM3', 'SUIK_NET_MONEYSUM4',
                              'SUIK_SET_MONEY1', 'SUIK_SET_MONEY2', 'SUIK_SET_MONEY3', 'SUIK_SET_MONEY4']
                gubunja=[{"readonly" : "INTE_FUND_TYPE", "selection" : "SUIK_GROUP"},
                         {"readonly" : "SUIK_GROUP", "selection" : "INTE_FUND_TYPE"}]
                i=logic-1
                """logic 1 고정박스값:유형, 선택가능값:그룹"""
                """logic 2 고정박스값:그룹, 선택가능값:유형"""
                df.columns = columns
                df = df.query(gubunja[i]['readonly']+"==@querycolumn")
                columns.remove(gubunja[i]['readonly'])
                df=df[columns]
                selectlist['selectlist1'] = df[gubunja[i]['selection']].drop_duplicates().values.tolist()
                if val2!='all' and val2!='':
                    df = df.query(gubunja[i]['selection']+"==@val2")
                selectlist['selectlist2']=df['SUIK_NAME'].drop_duplicates().values.tolist()
                if val3!='all' and val3!='':
                    df = df.query("SUIK_NAME==@val3")
                del columns[1:2] # 공간부족으로 제거
                df = df[columns]  
                valsum = ['합계', str(len(df.index))+'개', '', 0, 0, 0, 0, 0, 0, 0, 0, 0]
                df = df.values.tolist()

                if df:
                    for i in range(3, len(df[0])):
                        for j in range(len(df)):
                            valsum[i] += math.floor(df[j][i])
                    df.append(valsum)
                    changeWon(df, 3)
                else:
                    df = [['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
                # 순자산 표시, 차액 표시 스위칭 용도, 쿼리에 최종 뺄셈 연산 지워야함
                # valcal = 0
                # for i in range(0, len(df)):
                #     for j in range(len(df[0])):
                #         if j == 2:
                #             valcal = df[i][j]
                #         if j > 2 and j < 7:
                #             df[i][j] = valcal - df[i][j]
                # print(df)

        elif gubun == 'tab5_suikja':
            """date1:날짜, val1:수익자, val2:유형"""
            header = ['펀드코드', '펀드명', '설정액', '순자산', '전월말대비', '전분기말대비', '전년말대비', '전전년말대비', '전월말',
                      '전분기말', '전년말', '전전년말']
            df = pd.DataFrame(query(win, logic, date1, val1, '', ''))

            if len(df.index) == 0:
                df = [['값 없음', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            else:
                df.columns=['fund_cd', 'fund_nm', 'SUIK_FUND_TYPE', 'suik_set_money', 'SUIK_NET_MONEY', 'SUIK_NET_MONEY1',
                            'SUIK_NET_MONEY2','SUIK_NET_MONEY3','SUIK_NET_MONEY4','suik_set_money1','suik_set_money2',
                            'suik_set_money3','suik_set_money4']
                selectlist['selectlist1'] = (df['SUIK_FUND_TYPE'].drop_duplicates().values.tolist())

                if val2 != 'all' and val2 != '':
                    where = val2
                    df = df.query("SUIK_FUND_TYPE==@where")
                df = df[['fund_cd', 'fund_nm', 'suik_set_money', 'SUIK_NET_MONEY', 'SUIK_NET_MONEY1',
                        'SUIK_NET_MONEY2','SUIK_NET_MONEY3','SUIK_NET_MONEY4','suik_set_money1','suik_set_money2',
                        'suik_set_money3','suik_set_money4']]
                valsum = ['합계', str(len(df.index))+'개', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                # df = df.groupby(df['SUIK_FUND_TYPE']).sum()
                df = df.values.tolist()
                for i in range(2, len(df[0])):
                    for j in range(len(df)):
                        valsum[i] += math.floor(df[j][i])
                df.append(valsum)
                changeWon(df,2)

        return header, df, selectlist, searchdate
    except:
        traceback.print_exc()

@bp.route('/file_down/', methods=['GET', 'POST'])
def file_down():
    '''최근버전은 main, 그 외는 풀네임으로 찾음'''
    try:
        fileType = request.form['arg1']
        name = request.form['arg2']
        if fileType == 'file_py_recently':
            name = 'main.exe'
        elif fileType == 'file_py':
            name = 'main' + name.replace('/', '')[2:] + '.exe'
        fileName = f'static/file/' + name

        return send_file(fileName,
                         mimetype='application/octet-stream',
                         attachment_filename=name,
                         as_attachment=True
                         )
    except:
        traceback.print_exc()



@bp.route('/download/')
def download():
    return render_template('tab5/download.html')


# --------단순 메소드

def changeWon(df,start):
    """단위 억으로 변경 df: 변경할 데이터프레임, start: 변환할 column 시작값"""

    def is_digit(str):
        try:
            tmp = float(str)
            return True
        except ValueError:
            return False

    for i in range(len(df)):
        for j in range(start, len(df[0])):
            # print(df[i][j])
            if is_digit(df[i][j])==True:
                # if (str(type(df[i][j])).find('int') or str(type(df[i][j])).find('float')):
                    df[i][j] = math.floor(int(df[i][j]) / 100000000)

def setComma(df,start):
    """df: 변경할 데이터프레임, start: 변환할 column 시작값"""
    df2 = df.copy()
    for i in range(len(df)):
        for j in range(start, len(df[0])):
            if j > 0:
                df2[i][j] = format(df[i][j], ',')
    return df2


def tab5_createJson():
    """JSON파일 생성"""
    if os.path.isfile(f"app\static\\setting\\userimsi.json") == False:
        file_data = OrderedDict()
        file_data['ip'] = socket.gethostbyname(socket.gethostname())
        file_data['info1'] = '2'
        file_data['info2'] = '3'
        with open('app\static\\setting\\userimsi.json', 'w', encoding="utf-8") as makefile:
            json.dump(file_data, makefile, ensure_ascii=False, indent='\t')


def tab5_readJson():
    """JSON파일 읽기"""
    if os.path.isfile(f"app\static\\file\\setting\\userimsi.json"):
        with open(f'app\static\\file\\setting\\userimsi.json', 'r', encoding='utf-8') as readfile:
            content = json.load(readfile)
            # print(content)
            # print(content['ip'])

def getfile():
    try:
        user={'id':'heungkuk', 'password': 'gmdrnr!@'}
        ftp=ftplib.FTP()
        ftp.connect('211.62.79.4',21)
        ftp.login(user['id'],user['password'])
        ftp.cwd('/heungkuk')
    # https: // itcenter.yju.ac.kr / xe_board_tech_python / 8416



    except:
        traceback.print_exc()


# --------------------안씀



# 연습용 ajax
@bp.route('/jsontest/', methods=['POST'])
def callAjax():
    value = request.form['SensorID']
    value2 = request.form['tt']
    print(value,value2)
    tab5_createJson()
    return value2


@bp.route('/set_info')
def set_info():
    '''들어오는 IP 기준으로 설정정보 가져옴'''
    try:
        return render_template('tab5/download.html')
    except:
        traceback.print_exc()


@bp.route('/main/<int:question_id>/')
def detail(question_id):
    """변수 받음"""
    try:
        return render_template('tab5/tab5_view.html', queryData1='', link1='http://127.0.0.1:5000/main',
                               val1=question_id)
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

# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조
# --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org
# flask run
# flask run --host=0.0.0.0
# 포트까지 입력하면 다른PC에서 직접 접근 가능하나 외부망을 타고가진 않음 DLP검출 안됨
# 현재 시점 리비전과 최종 리비전이 같아야 migrate가 됨 https://programmer-ririhan.tistory.com/222
# https://wikidocs.net/81046
# https://coderap.tistory.com/447