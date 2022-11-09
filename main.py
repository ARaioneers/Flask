from flask import Flask, Response ,render_template , url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import pandas as pd
from flask_migrate import Migrate

# WSGI application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# class New_class(db.Model):
#     id = db.column(db.Integer, primary_key = True)
#     content = db.column(db.string(200),nullable=False)
#     completed = db.column(db.integer,default=0)
#     Date_created = db.column(db.DateTime,default=datetime.utcnow)
    
#     def __repr__(self):
#         return '<Task %r>' % self.id
    
    
    

#decorator
@app.route('/')
def User():
    return render_template("index.html")

#Result Checker :
@app.route('/results/<int:score>')
def member(score):
    if score<40:
        return "The person has failed"
    else:
        return "The person has passed"
    
@app.route("/dataframe",methods=['GET','POST'])
def dataframe():
    file = open("New_titanic.xlsx","r")
    data = pd.read_excel('New_titanic.xlsx')
    f = data.to_excel("New_titanic.xlsx")
    return 
    

if __name__=='__main__':
    app.run(debug=True)