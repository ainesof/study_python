from app import db
import cx_Oracle
from datetime import date, timedelta
from app import seqrchQuery
import traceback, socket

# class Question(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     subject = db.Column(db.String(200), nullable=False)
#     content = db.Column(db.Text(), nullable=False)
#     create_date = db.Column(db.DateTime(), nullable=False)
#
#
# class Answer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     question_id = db.Column(db.Integer, db.ForeignKey('tab5.id', ondelete='CASCADE'))
#     tab5 = db.relationship('Question', backref=db.backref('answer_set'))
#     content = db.Column(db.Text(), nullable=False)
#     create_date = db.Column(db.DateTime(), nullable=False)


def query(win,page,date1,val1,val2,val3):
    try:

        if win is not None:
            cur = connect_hkfund()
            if win==1 and page==1:
                """date:날짜"""
                sql = seqrchQuery.returnSQL('tab5_view1searchQuery2').format(date=date1)
            elif win==1 and page==2:
                sql = seqrchQuery.returnSQL('tab5_view2searchQuery').format(date=date1)
            elif win==2 or win==3:
                """date:날짜,val1:본부, val2:수익그룹, val3:NPS여부"""
                sql=seqrchQuery.returnSQL('tab5_win1searchQuery2').format(date=date1,mg_bu=val1,suik_group=val2,nps=val3)
            # print(sql)
            cur.execute(sql)
            row = cur.fetchall()
            return row
    except:
        traceback.print_exc()

def querydate(date1,win):
    """조회 쿼리의 기준 날짜조회"""
    try:
        """date:날짜"""
        query=''
        if win == 1:
            query ='tab5_searchDateQuery'
        elif win == 2 or win == 3:
            query ='tab5_win1searchDateQuery'
        cur=connect_hkfund()
        sql=seqrchQuery.returnSQL(query).format(date=date1)
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
        print(userinfo)
        conn = cx_Oracle.connect(userinfo['id'], userinfo['pw'], userinfo['connect'])
        cur = conn.cursor()
        return cur
    except:
        traceback.print_exc()
# conn = cx_Oracle.connect("HKCL", "hkcl", "11.10.5.11:1521/hkfund")
# conn = cx_Oracle.connect("system", "1234", "localhost:1521/xe")
# https://wikidocs.net/81051