from app import db
import cx_Oracle
from datetime import date, timedelta
from app import seqrchQuery
import traceback

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


def query(page,date1,val1,val2,val3):
    try:
        """sql연산"""
        if page==1:
            cur=connect_hkfund()
            sql=seqrchQuery.returnSQL('tab5_searchQuery').format(date=date1)
            cur.execute(sql)
            print(sql)
            row = cur.fetchall()
        elif page==2:
            """val1=본부, val2=수익그룹, val3=NPS여부"""
            cur=connect_hkfund()
            sql=seqrchQuery.returnSQL('tab5_win1searchQuery').format(date=date1,mg_bu=val1,suik_group=val2,nps=val3)
            print(sql)
            cur.execute(sql)
            row = cur.fetchall()
        return row
    except:
        traceback.print_exc()

def connect_hkfund():
    """HKfund DB에 접속"""
    try:
        conn = cx_Oracle.connect("system", "1234", "localhost:1521/xe")
        cur = conn.cursor()
        return cur
    except:
        traceback.print_exc()
# conn = cx_Oracle.connect("HKCL", "hkcl", "11.10.5.11:1521/hkfund")
# conn = cx_Oracle.connect("system", "1234", "localhost:1521/xe")
# https://wikidocs.net/81051