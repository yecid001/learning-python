from flask import Flask, render_template
from database import con, cur
import sqlite3
from flask import g

app=Flask(__name__)

DATABASE= 'market.db'

def get_db():
    db=getattr(g,'_database',None)
    if db is None:
        db = g._database=sqlite3.connect(DATABASE)
    return db
def close_connection(exeption):
    db = getattr(g,'_database',None)
    if db is not None:
        db.close()
@app.route('/')
def index():
    con = get_db()
    cur.execute('SELECT * FROM user')
    data= cur.fetchall()
    return render_template('index.html', None)
if __name__=='__main__':
    app.run(debug=True)
