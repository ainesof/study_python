from app import db
import cx_Oracle
import pandas as pd

from app import searchQuery
import traceback, socket

def query(win,logic,date1,val1,val2,val3):
    """메인 쿼리"""
    try:
        if win is not None:
            cur = connect_hkfund()
            if win == 1 and logic == 1:
                """date1:날짜"""
                view1table1 = searchQuery.returnSQL('tab5_view1Table1')
                view1table2 = searchQuery.returnSQL('tab5_view1Table2')
                sql = searchQuery.returnSQL('tab5_viewCommonSearchQuery').format(table1=view1table1, table2=view1table2, val='suik_group', date=date1)
            elif win == 1 and logic == 2:
                """date1:날짜"""
                view2table = searchQuery.returnSQL('tab5_view2Table')
                sql = searchQuery.returnSQL('tab5_viewCommonSearchQuery').format(table1=view2table, table2=view2table, val='SUIK_FUND_TYPE', date=date1)
            elif win == 2 and logic == 1:
                """date1:날짜,val1:본부, val2:수익그룹, val3:PN_NPS"""
                sql = searchQuery.returnSQL('tab5_groupCommonSearchQuery').format(date=date1, mg_bu=val1, val='SUIK_FUND_TYPE',val2='suik_group',select=val2,nps=val3)
            elif win == 2 and logic == 2:
                """date1:날짜,val1:본부, val2:항목, val3:PN_NPS"""
                sql = searchQuery.returnSQL('tab5_groupCommonSearchQuery').format(date=date1, mg_bu=val1, val='suik_group',val2='SUIK_FUND_TYPE',select=val2,nps=val3)
            elif win == 3 and logic == 1:
                """date1:날짜"""
                sql = searchQuery.returnSQL('tab5_itemCommonSearchQuery').format(date=date1)
            elif win == 3 and logic == 2:
                """date1:날짜"""
                sql = searchQuery.returnSQL('tab5_itemCommonSearchQuery').format(date=date1)
            elif win == 1 and logic == 99:
                """val1:수익자"""
                sql = searchQuery.returnSQL('find_SuikjaSearchQuery').format(suikja=val1)
            elif win == 2 and logic == 99:
                """date1:날짜,val1:수익자"""
                if val1=='전체':
                    suikja=''
                else:
                    suikja=val1
                sql = searchQuery.returnSQL('tab5_suikjaSearchQuery1').format(date=date1,suikja=suikja)
            else:
                print('미구현')
                print(win,logic,date1,val1,val2,val3)
            # print(sql)
            cur.execute(sql)
            row = cur.fetchall()
            return row
    except:
        traceback.print_exc()

def dateQuery(gubun,module,win,date1):
    """날짜 관련 쿼리"""
    try:
        sql=''
        cur = connect_hkfund()
        if module == 'recently':
            """DB 최근자료 날짜 가져옴"""
            sql = searchQuery.returnSQL('tab5_recentlyDateSearchQuery')
        elif module == 'header':
            """조회 쿼리의 기준별 일자 조회"""
            query = 'tab5_headerDateSearchQuery'
            sql = searchQuery.returnSQL(query).format(date=date1)
        elif module == 'parity':
            """조회값 하나펀드 자료테이블과 비교"""
            query = 'tableParityCheck'
            sql = searchQuery.returnSQL(query).format(date=date1)
        # print(sql)
        cur.execute(sql)
        row = cur.fetchall()
        df=pd.DataFrame(row)

        if module == 'header':
            df.columns = ['null', 'str', 'today', 'lastmonth', 'lastquater', 'lastyear', 'last2year']
            if gubun == 'tab5_suikja':
                df=df[['str','null','today','today','lastmonth','lastquater','lastyear','last2year','lastmonth','lastquater',
                       'lastyear','last2year']]
            elif win == 1:
                df=df[['str','today','today','lastmonth','lastquater','lastyear','today','lastmonth','lastquater','lastyear']]
            elif win == 2:
                df = df[['str', 'today', 'today', 'lastmonth', 'lastquater', 'lastyear', 'last2year', 'lastmonth', 'lastquater',
                     'lastyear', 'last2year']]
            elif win == 3:
                df = df[['str', 'null', 'today', 'lastmonth', 'lastquater', 'lastyear', 'last2year', 'lastmonth', 'lastquater',
                     'lastyear', 'last2year']]
        return df
    except:
        traceback.print_exc()

def etcQuery(module,val1):
    """기타 쿼리들"""
    try:
        sql=''
        cur = connect_hkfund()
        if module == 'group':
            """DB 최근자료 날짜 가져옴"""
            query = 'findGroup'
            sql = searchQuery.returnSQL(query).format(suikja=val1)
        # print(sql)
        cur.execute(sql)
        row = cur.fetchall()
        df = pd.DataFrame(row)
        return df
    except:
        traceback.print_exc()

def connect_hkfund():
    """오라클 DB에 접속"""
    try:
        conn={}
        server = [{'id': 'system', 'pw': '1234', 'connect': 'localhost:1521/xe'},
                  {'id': 'HKCL', 'pw': 'hkcl', 'connect': '11.10.5.11:1521/hkfund'}]
        userinfo = {}
        ip=str(socket.gethostbyname(socket.gethostname()))
        if ip[0:2] == '19':
            userinfo.update(server[0])
        elif ip[0:2] == '11':
            userinfo.update(server[1])
        else:
            print(socket.gethostbyname(socket.gethostname()))
        conn = cx_Oracle.connect(userinfo['id'], userinfo['pw'], userinfo['connect'])
        cur = conn.cursor()
        return cur
    except:
        traceback.print_exc()
# conn = cx_Oracle.connect("HKCL", "hkcl", "11.10.5.11:1521/hkfund")
# conn = cx_Oracle.connect("system", "1234", "localhost:1521/xe")
# https://wikidocs.net/81051