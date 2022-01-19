from app import db
import cx_Oracle

from app import seqrchQuery
import traceback, socket

def query(win,logic,date1,val1,val2,val3):
    try:
        if win is not None:
            cur = connect_hkfund()
            if win == 1 and logic == 1:
                """date1:날짜"""
                sql = seqrchQuery.returnSQL('tab5_view1SearchQuery1').format(date=date1)
            elif win == 1 and logic == 2:
                """date1:날짜"""
                sql = seqrchQuery.returnSQL('tab5_view2SearchQuery1').format(date=date1)
            elif (win == 2 or win == 3) and logic == 1:
                """date1:날짜,val1:본부, val2:수익그룹, val3:NPS여부"""
                sql = seqrchQuery.returnSQL('tab5_group1SearchQuery1').format(date=date1,mg_bu=val1,suik_group=val2,nps=val3)
            elif win == 2 and logic == 2:
                """date1:날짜,val1:본부, val2:항목, val3:NPS여부"""
                sql = seqrchQuery.returnSQL('tab5_group2SearchQuery1').format(date=date1,mg_bu=val1,item=val2,nps=val3)
            elif win == 1 and logic == 99:
                """val1:수익자"""
                sql = seqrchQuery.returnSQL('find_SuikjaSearchQuery').format(suikja=val1)
            elif win == 2 and logic == 99:
                """date1:날짜,val1:수익자"""
                sql = seqrchQuery.returnSQL('tab5_suikjaSearchQuery1').format(date=date1,suikja=val1)
            else:
                print('미구현')
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
            """DB 최근날짜 가져옴"""
            sql = seqrchQuery.returnSQL('tab5_recDateQuery')
        elif module == 'header':
            """조회 쿼리의 기준 날짜조회"""
            if win == 1:
                query = 'tab5_searchDateQuery'
            elif win == 2 or win == 3:
                query = 'tab5_win1searchDateQuery'
            if gubun == 'tab5_suikja':
                print('헤더클릭 안 만듬')
            sql = seqrchQuery.returnSQL(query).format(date=date1)
        # print(sql)
        cur.execute(sql)
        row = cur.fetchall()
        return row
    except:
        traceback.print_exc()

def connect_hkfund():
    """HKfund DB에 접속"""
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