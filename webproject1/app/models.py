from app import db
import cx_Oracle

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

def query(sql):
    conn = cx_Oracle.connect("system", "1234", "localhost:1521/xe")
    cur = conn.cursor()
    cur.execute(sql)
    row = cur.fetchall()
    return row

# conn = cx_Oracle.connect("HKCL", "hkcl", "11.10.5.11:1521/hkfund")
# conn = cx_Oracle.connect("system", "1234", "localhost:1521/xe")
# https://wikidocs.net/81051