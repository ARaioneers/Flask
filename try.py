from flask import Flask , render_template
from flask import Response
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
import openpyxl

app = Flask(__name__)
    
@app.route('/',methods=['GET'])
def User():
    return render_template("index.html")

@app.route("/dataframe", methods=['GET','POST'])
def dataframe():
    file = open("New_titanic.xlsx","r")
    data = pd.read_excel('New_titanic.xlsx')
    df = pd.DataFrame(data)
    for index, rows in df.iterrows():
        print()
         
    return Response(data.to_json(),status=20)

    
if __name__=="__main__":
    app.run(debug=True)

